from dotenv import load_dotenv
import os
import urllib.request
import urllib.error
import json
import time
import sys

# ============================================================
# TESTE_API GROQ V2
# ============================================================
# OBJETIVO
# Este script funciona como uma bancada inicial de avaliação de
# modelos da Groq para o MoAPP.
#
# ETAPA 1 - DESCOBERTA
# Consulta /models e identifica todos os modelos disponíveis
# para a API Key utilizada nesta execução.
#
# ETAPA 2 - BENCHMARK CONTROLADO
# Testa apenas os modelos selecionados em MODELOS_TESTE usando
# o mesmo system prompt, pergunta e parâmetros.
#
# MÉTRICAS
# - HTTP
# - tempo total observado
# - prompt_tokens
# - completion_tokens
# - total_tokens
# - resposta completa
#
# IMPORTANTE
# Nem todo modelo retornado por /models é conversacional. Podem
# existir modelos especializados em segurança, áudio e outras
# funções. Por isso a descoberta é automática, mas a seleção para
# benchmark é explícita e controlada.
# ============================================================

# Carrega GROQ_API_KEY do arquivo .env, quando existente.
load_dotenv()

API_KEY = os.getenv("GROQ_API_KEY")

URL_MODELS = "https://api.groq.com/openai/v1/models"
URL_CHAT = "https://api.groq.com/openai/v1/chat/completions"

# ------------------------------------------------------------
# VALIDAÇÃO DA API KEY
# ------------------------------------------------------------
if not API_KEY:
    print("\n" + "=" * 70)
    print("ERRO: GROQ_API_KEY NÃO ENCONTRADA")
    print("=" * 70)
    print("\nCrie ou atualize um arquivo .env contendo:")
    print("GROQ_API_KEY=sua_chave_aqui\n")
    sys.exit(1)

API_KEY = API_KEY.strip()


def criar_headers():
    """Centraliza os cabeçalhos HTTP usados nas chamadas à Groq."""
    return {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
        "User-Agent": "Mo-Groq-Model-Test-v2"
    }


# ============================================================
# ETAPA 1 - CONECTIVIDADE E DESCOBERTA DE MODELOS
# ============================================================

print("\n" + "=" * 70)
print("TESTE API GROQ - V2")
print("=" * 70)

# Nunca exibir a chave completa em logs.
print("\nINFORMAÇÕES DA API KEY")
print("Prefixo:", API_KEY[:4])
print("Tamanho:", len(API_KEY))
print("\nConsultando os modelos disponíveis para esta API Key...")

try:
    request = urllib.request.Request(
        URL_MODELS,
        headers=criar_headers(),
        method="GET"
    )

    inicio_consulta = time.time()

    with urllib.request.urlopen(request) as response:
        tempo_consulta = time.time() - inicio_consulta
        dados = json.loads(response.read().decode("utf-8"))

        print("\n" + "=" * 70)
        print("STATUS: CONEXÃO OK")
        print("HTTP:", response.status)
        print(f"Tempo da consulta: {tempo_consulta:.2f} segundos")
        print("=" * 70)

        modelos_disponiveis = dados.get("data", [])
        nomes_modelos = sorted(
            item.get("id")
            for item in modelos_disponiveis
            if item.get("id")
        )

        print("\nMODELOS DISPONÍVEIS PARA ESTA API KEY:\n")
        for model_id in nomes_modelos:
            print("-", model_id)

        print("\nTOTAL DE MODELOS DISPONÍVEIS:", len(nomes_modelos))

except urllib.error.HTTPError as erro:
    print("\n" + "=" * 70)
    print("ERRO AO CONSULTAR OS MODELOS DA GROQ")
    print("=" * 70)
    print("HTTP:", erro.code)
    print("Motivo:", erro.reason)
    try:
        print("\nRESPOSTA DA GROQ:")
        print(erro.read().decode("utf-8"))
    except Exception:
        pass
    sys.exit(1)

except Exception as erro:
    print("\nERRO INESPERADO DURANTE A DESCOBERTA DE MODELOS")
    print(type(erro).__name__)
    print(erro)
    sys.exit(1)


# ============================================================
# ETAPA 2 - SELEÇÃO CONTROLADA DOS MODELOS PARA BENCHMARK
# ============================================================
# Esta lista contém os candidatos conversacionais que desejamos
# comparar. Um candidato só será testado se também estiver na
# lista retornada pela API na etapa anterior.
#
# Para futuros perfis do MoAPP, altere esta lista ou evolua o
# procedimento para conjuntos de modelos por perfil.
# ============================================================

MODELOS_TESTE = [
    "openai/gpt-oss-20b",
    "openai/gpt-oss-120b",
    "qwen/qwen3.6-27b",
    "groq/compound-mini",
    "groq/compound"
]

print("\n" + "=" * 70)
print("SELEÇÃO DE MODELOS PARA BENCHMARK")
print("=" * 70)

modelos_validos = []

for modelo in MODELOS_TESTE:
    if modelo in nomes_modelos:
        modelos_validos.append(modelo)
    else:
        print(f"AVISO: modelo configurado, mas não disponível: {modelo}")

if not modelos_validos:
    print("\nNenhum modelo válido foi encontrado para o benchmark.")
    sys.exit(1)

print("\nMODELOS QUE SERÃO TESTADOS:\n")
for modelo in modelos_validos:
    print("-", modelo)


# ============================================================
# ETAPA 3 - CENÁRIO CONTROLADO
# ============================================================
# Todos os modelos recebem o mesmo cenário. Isso permite uma
# comparação operacional inicial, mas NÃO constitui uma avaliação
# científica completa de qualidade.
#
# Em futuras versões, cada perfil do MoAPP deverá possuir uma
# bateria de cenários representativos.
# ============================================================

SYSTEM_PROMPT = """
Você é Mo, um assistente inteligente, útil, objetivo e natural.
Responda em português brasileiro.
Seja claro e direto.
""".strip()

PERGUNTA = """
Olá! Você é Mo, um assistente inteligente integrado ao Discord.

Responda de forma breve, clara e natural.

Explique em uma frase o que significa governança de inteligência
artificial.
""".strip()

TEMPERATURE = 0.7
MAX_TOKENS = 300

print("\n" + "=" * 70)
print("CENÁRIO DE TESTE")
print("=" * 70)
print("\nSYSTEM PROMPT:")
print(SYSTEM_PROMPT)
print("\nPERGUNTA:")
print(PERGUNTA)
print("\nPARÂMETROS:")
print("Temperature:", TEMPERATURE)
print("Max tokens:", MAX_TOKENS)


# ============================================================
# ETAPA 4 - BENCHMARK
# ============================================================

resultados = []

for modelo in modelos_validos:
    print("\n\n" + "=" * 70)
    print("TESTANDO MODELO:", modelo)
    print("=" * 70)

    payload = {
        "model": modelo,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": PERGUNTA}
        ],
        "temperature": TEMPERATURE,
        "max_tokens": MAX_TOKENS
    }

    request = urllib.request.Request(
        URL_CHAT,
        data=json.dumps(payload).encode("utf-8"),
        headers=criar_headers(),
        method="POST"
    )

    # Mede o tempo total observado pelo cliente até receber a
    # resposta completa.
    inicio = time.time()

    try:
        with urllib.request.urlopen(request) as response:
            tempo = time.time() - inicio
            resultado = json.loads(response.read().decode("utf-8"))

            resposta = (
                resultado.get("choices", [{}])[0]
                .get("message", {})
                .get("content", "")
            )

            usage = resultado.get("usage", {})
            prompt_tokens = usage.get("prompt_tokens")
            completion_tokens = usage.get("completion_tokens")
            total_tokens = usage.get("total_tokens")

            print("\nSTATUS: OK")
            print("HTTP:", response.status)
            print(f"Tempo total: {tempo:.2f} segundos")

            print("\nRESPOSTA:")
            print("-" * 70)
            print(resposta)
            print("-" * 70)

            print("\nUSO DE TOKENS:")
            print("Prompt tokens:", prompt_tokens)
            print("Completion tokens:", completion_tokens)
            print("Total tokens:", total_tokens)

            resultados.append({
                "modelo": modelo,
                "status": "OK",
                "http": response.status,
                "tempo": tempo,
                "prompt_tokens": prompt_tokens,
                "completion_tokens": completion_tokens,
                "total_tokens": total_tokens,
                "resposta": resposta
            })

    except urllib.error.HTTPError as erro:
        tempo = time.time() - inicio
        print("\nSTATUS: ERRO")
        print("HTTP:", erro.code)
        print("Motivo:", erro.reason)

        try:
            corpo_erro = erro.read().decode("utf-8")
            print("\nRESPOSTA DA GROQ:")
            print(corpo_erro)
        except Exception:
            corpo_erro = None

        resultados.append({
            "modelo": modelo,
            "status": f"ERRO HTTP {erro.code}",
            "http": erro.code,
            "tempo": tempo,
            "prompt_tokens": None,
            "completion_tokens": None,
            "total_tokens": None,
            "resposta": corpo_erro
        })

    except Exception as erro:
        tempo = time.time() - inicio
        print("\nSTATUS: ERRO INESPERADO")
        print(type(erro).__name__)
        print(erro)

        resultados.append({
            "modelo": modelo,
            "status": "ERRO",
            "http": None,
            "tempo": tempo,
            "prompt_tokens": None,
            "completion_tokens": None,
            "total_tokens": None,
            "resposta": str(erro)
        })


# ============================================================
# ETAPA 5 - RESUMO COMPARATIVO
# ============================================================

print("\n\n" + "=" * 70)
print("RESUMO COMPARATIVO FINAL")
print("=" * 70)

for resultado in resultados:
    print("\nMODELO:", resultado["modelo"])
    print("Status:", resultado["status"])
    print("HTTP:", resultado["http"])
    print(f"Tempo: {resultado['tempo']:.2f} segundos")

    if resultado["total_tokens"] is not None:
        print("Prompt tokens:", resultado["prompt_tokens"])
        print("Completion tokens:", resultado["completion_tokens"])
        print("Total tokens:", resultado["total_tokens"])

    print("-" * 70)


# ============================================================
# INDICADOR OPERACIONAL - MENOR LATÊNCIA
# ============================================================
# O modelo mais rápido NÃO é automaticamente o melhor. Este bloco
# apenas identifica a menor latência observada nesta execução.
# A decisão deve considerar qualidade, adequação ao perfil,
# aderência às instruções, latência e consumo.
# ============================================================

resultados_ok = [
    resultado for resultado in resultados
    if resultado["status"] == "OK"
]

if resultados_ok:
    mais_rapido = min(resultados_ok, key=lambda x: x["tempo"])

    print("\n" + "=" * 70)
    print("MODELO COM MENOR LATÊNCIA NESTA EXECUÇÃO")
    print("=" * 70)
    print("Modelo:", mais_rapido["modelo"])
    print(f"Tempo: {mais_rapido['tempo']:.2f} segundos")

print("\n" + "=" * 70)
print("FIM DO TESTE")
print("=" * 70)
