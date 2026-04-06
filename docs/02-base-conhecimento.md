# Base de Conhecimento

## Dados Utilizados

Descreva se usou os arquivos da pasta `data`, por exemplo:

| Arquivo | Formato | Utilização no Agente |
|---------|---------|---------------------|
| `historico_atendimento.csv` | CSV | Contextualizar interações anteriores |
| `perfil_investidor.json` | JSON | Personalizar recomendações |
| `produtos_financeiros.json` | JSON | Sugerir produtos adequados ao perfil |

---

## Adaptações nos Dados

> Você modificou ou expandiu os dados mockados? Descreva aqui.

- O arquivo de transações foi removido, pois não será necessário para o contexto do agente.
- No arquivo de produtos financeiros foi inserida a informação de liquidez e um novo produto (CDB - Prazo Fixo)

---

## Estratégia de Integração

### Como os dados são carregados?
> Descreva como seu agente acessa a base de conhecimento.

Os JSON/CSV da pasta data serão carregados via código Python.

### Como os dados são usados no prompt?
> Os dados vão no system prompt? São consultados dinamicamente?

Os dados carregados via código Python serão inseridos no system prompt do modelo.

---

## Exemplo de Contexto Montado

> Mostre um exemplo de como os dados são formatados para o agente.

Todos os dados existentes nos arquivos da pasta data serão disponibilizados para o modelo, uma vez que todas elas são informações importantes para a recomendação a ser sugerida pelo agente.
