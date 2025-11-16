from fastapi import FastAPI
from models import ConsultaRequest, ConsultaResponse
from guru_ia import gerar_resposta_com_memoria

# Inicialização do FastAPI
app = FastAPI(
    title="Tarot Conclusivo - Backend com Memória RAG",
    description="API para a Guru IA que utiliza Retrieval-Augmented Generation (RAG) para personalização."
)

@app.post("/consulta", response_model=ConsultaResponse)
async def fazer_consulta(dados_consulta: ConsultaRequest):
    """
    Endpoint principal para a consulta ao Tarot.
    Integra a lógica de memória RAG e a geração de resposta da IA.
    """
    
    # 1. Extrair os dados da requisição
    user_id = dados_consulta.user_id
    pergunta = dados_consulta.pergunta
    cartas = dados_consulta.cartas
    astrologia = dados_consulta.astrologia
    
    # 2. CHAMA A FUNÇÃO CENTRAL COM MEMÓRIA RAG
    resposta_final = gerar_resposta_com_memoria(
        user_id=user_id,
        pergunta=pergunta,
        cartas=cartas,
        astrologia=astrologia
    )
    
    # 3. Retorna a resposta
    return ConsultaResponse(resposta_guru=resposta_final)

# Exemplo de endpoint de saúde
@app.get("/health")
def health_check():
    return {"status": "ok", "message": "API está funcionando."}
