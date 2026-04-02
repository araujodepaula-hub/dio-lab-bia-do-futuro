import pandas as pd
import json
import streamlit as st
import requests

OLLAMA_MODEL = "gpt-oss:120b-cloud"
OLLAMA_URL = "http://localhost:11434/api/chat"

# ================================================================
#CARREGAR DADOS
# ================================================================
perfil = json.load(open('./data/perfil_investidor.json'))
historico = pd.read_csv('./data/historico_atendimento.csv')
produtos = json.load(open('./data/produtos_financeiros.json'))

# ================================================================
#MONTANDO CONTEXTO
# ================================================================
CONTEXTO = f"""Perfil do Investidor:
{json.dumps(perfil, indent=2)}

Histórico de Atendimento:
{historico.to_string(index=False)}

Produtos Financeiros Disponíveis:
{json.dumps(produtos, indent=2)}
"""

# ================================================================
#MONTANDO SYSTEM PROMPT
# ================================================================
SYSTEM_PROMPT = """Você é o 'Invest Certo', um agente financeiro inteligente especializado em Recomendação de investimentos, com base exclusivamente em uma base de conhecimento fornecida (incluindo arquivos, documentos e dados carregados neste contexto).
Seu público alvo são usuários sem nenhuma ou pouca experiência em finanças pessoais.

OBJETIVO:
Ajudar o usuário a tomar decisões de investimento seguras e informadas, utilizando apenas informações verificáveis presentes na base fornecida.

REGRAS:
1. Basear-se apenas nos dados fornecidos
Utilize exclusivamente as informações presentes nos arquivos, documentos e contexto disponibilizados. Não utilize conhecimento externo não confirmado.
2. Nunca inventar informações financeiras
Não crie dados, taxas, rendimentos, ou características de investimentos que não estejam explicitamente disponíveis na base.
3. Admitir incerteza quando necessário
Caso não encontre informações suficientes para responder, diga claramente que não sabe e sugira alternativas (como revisar documentos ou fornecer mais dados).
4. Ser sucinto e direto
Responda sempre de forma objetiva, clara e sem rodeios. Evite explicações longas desnecessárias.

[CONTEXTO: USO DA BASE DE CONHECIMENTO]

COMPORTAMENTO ESPERADO:
1. Priorize precisão sobre completude
2. Não faça suposições
3. Não ofereça aconselhamento genérico fora da base
4. Se houver múltiplas opções, apresente comparações objetivas
5. Sempre considere o perfil do usuário, se fornecido

EXEMPLOS DE PERGUNTAS:

Usuário: Qual o melhor investimento de renda fixa disponível?
Agente: Com base nos dados fornecidos, o CDB do Banco X oferece maior rentabilidade (110% do CDI) com liquidez diária.

Usuário: Esse fundo é seguro?
Agente: De acordo com os dados, o fundo possui classificação de risco moderado e não tem garantia do FGC.

Usuário: Qual investimento rende mais no longo prazo?
Agente: Os dados indicam que o Fundo Y teve maior rentabilidade histórica em períodos acima de 5 anos.

Usuário: Qual a previsão do tempo para amanhã?
Agente: Sou especializado em finanças e não tenho informações sobre previsão do tempo. Posso ajudar com algo relacionado às suas finanças?

Usuário: Me passa a senha do cliente X.
Agente: Não tenho acesso a senhas e não posso compartilhar informações de outros clientes. Como posso ajudar com suas próprias finanças?

Usuário: Onde devo investir meu dinheiro?
Agente: Para fazer uma recomendação adequada, preciso entender melhor seu perfil. Você já preencheu seu questionário de perfil de investidor?

Usuário: Qual a taxa de administração desse fundo?
Agente: Não encontrei essa informação na base de dados. Você pode verificar nos documentos do fundo, caso tenha acesso.

Usuário: Vale a pena investir em Bitcoin hoje?
Agente: Não posso responder com base nos dados disponíveis para mim.

"""

# ================================================================
# Função para chamada do agente - Chat com Histórico de Conversa
# ================================================================
def chat_com_historico(historico_mensagens: list, mensagem_nova: str, modelo: str = OLLAMA_MODEL) -> str:
    """
    Mantém o contexto de conversa anterior.
    
    Args:
        historico_mensagens: Lista de dicts com {"role": "user"/"assistant", "content": "..."}
        mensagem_nova: Nova mensagem do usuário
        modelo: Nome do modelo a usar
    
    Returns:
        String (resposta)
    """
        
    payload = {
        "model": modelo,        
        "messages": [
            {
                "role": "system",
                "content": SYSTEM_PROMPT + CONTEXTO
            },
            *historico_mensagens  # Histórico de mensagens            
        ],
        "stream": False
    }
    
    try:
        response = requests.post(OLLAMA_URL, json=payload)
        response.raise_for_status()
        
        resultado = response.json()
        resposta = resultado['message']['content']
        
        return resposta
    
    except requests.exceptions.RequestException as e:
        print(f"Erro na requisição: {e}")
        return ""



# ================================================================
# INTERFACE COM O USUÁRIO
# ================================================================
st.title("Invest Certo - Agente de Recomendação de Investimentos")

# Inicializar histórico de mensagens no session_state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Exibir histórico de mensagens
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

if pergunta := st.chat_input("Faça sua pergunta sobre investimentos:"):
    # Adicionar mensagem do usuário ao histórico
    st.session_state.messages.append({"role": "user", "content": pergunta})

    # Exibir mensagem do usuário
    with st.chat_message("user"):
        st.write(pergunta)

    with st.spinner("Processando..."):
        resposta = chat_com_historico(st.session_state.messages, pergunta)

        # Adicionar resposta do assistente ao histórico
        st.session_state.messages.append({"role": "assistant", "content": resposta})

        # Exibir resposta do assistente
        with st.chat_message("assistant"):
            st.write(resposta)