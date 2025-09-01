# AGENT-AI

Ensaio para testar agentes de IA usando o strands.

## Pré-requisitos

Antes de executar o projeto, certifique-se de ter os seguintes pré-requisitos:

- Python 3.13
- strands-agents
- strands-agent-tools
- Streamlit
- Uma chave da API da OpenAI, Google ou Anthropic

## Uso

1. Clone o repositório para sua máquina local:

   ```bash
   git clone https://github.com/gapfranco/agent-ai.git
   cd agent-ia
   ```

2. Instale as dependências necessárias executando:
   ```bash
   uv venv
   source .venv/bin/activate
   uv sync
   ```

3. Prepare o ambiente com as opções de LLM:

   Renomeie o arquivo *.env.template* como *.env* e atualize as chaves de API para
   aquelas que deseja utilizar. Vai determinar as opções de LLM. 

   ```
   GOOGLE_API_KEY=1111
   OPENAI_API_KEY=2222
   ANTHROPIC_API_KEY=333
   ``` 
4. Execute o aplicativo Streamlit:
   ```bash
   streamlit run main.py
   ``` 
 