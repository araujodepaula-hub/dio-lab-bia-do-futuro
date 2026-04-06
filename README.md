# 🤖 Invest Certo --- Agente Financeiro Inteligente

## 📌 Sobre o Projeto

O **Invest Certo** é um agente financeiro inteligente desenvolvido como
evolução de um projeto proposto em bootcamp.\
O sistema foi transformado em uma aplicação funcional com foco em
**recomendações de investimentos personalizadas**, utilizando
Inteligência Artificial e dados do cliente.

O agente analisa informações financeiras e comportamentais para oferecer
sugestões alinhadas ao perfil do investidor, simulando uma experiência
consultiva automatizada.

------------------------------------------------------------------------

## 🎯 Objetivo

Fornecer recomendações de investimentos personalizadas com base em:

-   Perfil do investidor
-   Preferências financeiras
-   Produtos disponíveis na instituição

------------------------------------------------------------------------

## ⚙️ Tecnologias Utilizadas

-   Python
-   Streamlit (interface interativa)
-   Ollama (modelo LLM local)
-   JSON e CSV (base de conhecimento)
-   Git & GitHub

------------------------------------------------------------------------

## 🧠 Arquitetura da Solução

O sistema é composto por:

-   **Frontend:** Chat interativo com Streamlit
-   **Backend:** Script único [app.py](src/app.py) responsável pela lógica
-   **LLM Local:** Integração com Ollama para geração de respostas
-   **Base de Conhecimento:**
    -   [historico_atendimento.csv](data/historico_atendimento.csv)
    -   [perfil_investidor.json](data/perfil_investidor.json)
    -   [produtos_financeiros.json](data/produtos_financeiros.json)

------------------------------------------------------------------------

## 🚀 Funcionalidades

### ✔️ Implementadas

-   Chatbot financeiro interativo
-   Leitura e interpretação de dados do cliente
-   Recomendações personalizadas de investimentos
-   Integração com modelo de linguagem local (LLM)

### 🔄 Evoluções Pós-Bootcamp

-   Transformação do projeto em aplicação funcional
-   Integração real com base de dados
-   Implementação com Streamlit
-   Uso de LLM local (Ollama)
-   Estrutura simplificada e funcional em um único arquivo

------------------------------------------------------------------------

## 🧪 Como Executar

``` bash
# Clone o repositório
git clone https://github.com/araujodepaula-hub/dio-lab-bia-do-futuro.git

# Acesse a pasta
cd dio-lab-bia-do-futuro

# Instale dependências
pip install streamlit
pip install pandas
pip install requests

# Execute a aplicação
streamlit run app.py
```

------------------------------------------------------------------------

## 📁 Documentação

Toda a documentação do projeto encontra-se na pasta docs:

-   [01-documentacao-agente.md](docs/01-documentacao-agente.md): caso de uso e arquitetura
-   [02-base-conhecimento.md](docs/02-base-conhecimento.md): estratégia de dados
-   [03-prompts.md](docs/03-prompts.md): engenharia de prompts
-   [04-metricas.md](docs/04-metricas.md): avaliação e métricas
-   [05-pitch.md](docs/05-pitch.md): roteiro do pitch

------------------------------------------------------------------------

## 💬 Exemplo de Uso

O usuário pode interagir com o agente perguntando, por exemplo:

-   "Quais investimentos são mais adequados para mim?"
-   "Como posso melhorar minha carteira?"
-   "Qual investimento mais adequado para o objetivo X?"

------------------------------------------------------------------------

## 📚 Aprendizados

Durante o desenvolvimento deste projeto, foram adquiridos conhecimentos
em:

-   Construção de chatbots com IA
-   Integração com modelos LLM locais
-   Manipulação de dados estruturados (CSV/JSON)
-   Criação de interfaces interativas com Streamlit
-   Estruturação de projetos para portfólio

------------------------------------------------------------------------

## 🛠️ Melhorias Futuras

-   [ ] Implementar múltiplos perfis de usuários
-   [ ] Adicionar autenticação
-   [ ] Melhorar a análise de risco dos investimentos
-   [ ] Criar dashboards visuais
-   [ ] Deploy em ambiente cloud

------------------------------------------------------------------------

## 👨‍💻 Autor

Rodrigo de Paula\
- GitHub: https://github.com/araujodepaula-hub

------------------------------------------------------------------------

## 📌 Observação

Este projeto foi originalmente baseado em um desafio educacional e
posteriormente poderá ser evoluído para uma aplicação prática com foco em portfólio
profissional.
