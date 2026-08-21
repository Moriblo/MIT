import urllib.request
import urllib.error
import json
import time

# ============================================================
# CONFIGURAÇÃO
# ============================================================

API_KEY = "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"

URL = "https://api.groq.com/openai/v1/chat/completions"

MODELOS = [
    "openai/gpt-oss-20b",
    "qwen/qwen3.6-27b",
    "groq/compound-mini"
]

# Pergunta simples e igual para todos os modelos,
# permitindo comparar as respostas.
PERGUNTA = """
Olá! Você é o Mo, um assistente inteligente integrado ao Discord.

Responda de forma breve e natural:

Explique em uma frase o que significa governança de inteligência artificial.
"""

# ============================================================
# TESTE
# ============================================================

print("\n" + "=" * 60)
print("TESTE COMPARATIVO DE MODELOS - GROQ")
print("=" * 60)

print("\nPrefixo da API Key:", API_KEY.strip()[:4])
print("Modelos a testar:")

for modelo in MODELOS:
    print("-", modelo)

print("\nPergunta utilizada:")
print(PERGUNTA.strip())

resultados = []

for modelo in MODELOS:

    print("\n" + "=" * 60)
    print("TESTANDO:", modelo)
    print("=" * 60)

    payload = {
        "model": modelo,
        "messages": [
            {
                "role": "system",
                "content": (
                    "Você é Mo, um assistente inteligente, útil, "
                    "objetivo e natural."
                )
            },
            {
                "role": "user",
                "content": PERGUNTA.strip()
            }
        ],
        "temperature": 0.7,
        "max_tokens": 300
    }

    dados = json.dumps(payload).encode("utf-8")

    request = urllib.request.Request(
        URL,
        data=dados,
        headers={
            "Authorization": f"Bearer {API_KEY.strip()}",
            "Content-Type": "application/json",
            "User-Agent": "Mo-Groq-Model-Test"
        },
        method="POST"
    )

    inicio = time.time()

    try:
        with urllib.request.urlopen(request) as response:

            tempo = time.time() - inicio

            corpo = response.read().decode("utf-8")
            resultado = json.loads(corpo)

            resposta = (
                resultado
                .get("choices", [{}])[0]
                .get("message", {})
                .get("content", "")
            )

            usage = resultado.get("usage", {})

            print("\nSTATUS: OK")
            print(f"HTTP: {response.status}")
            print(f"Tempo: {tempo:.2f} segundos")

            print("\nRESPOSTA:")
            print("-" * 60)
            print(resposta)
            print("-" * 60)

            print("\nUSO:")
            print("Prompt tokens:", usage.get("prompt_tokens"))
            print("Completion tokens:", usage.get("completion_tokens"))
            print("Total tokens:", usage.get("total_tokens"))

            resultados.append({
                "modelo": modelo,
                "status": "OK",
                "tempo": tempo,
                "resposta": resposta,
                "tokens": usage.get("total_tokens")
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

        except Exception as e:
            print("Não foi possível ler o corpo do erro:", e)

        resultados.append({
            "modelo": modelo,
            "status": f"ERRO HTTP {erro.code}",
            "tempo": tempo,
            "resposta": None,
            "tokens": None
        })

    except Exception as erro:

        tempo = time.time() - inicio

        print("\nSTATUS: ERRO INESPERADO")
        print(type(erro).__name__)
        print(erro)

        resultados.append({
            "modelo": modelo,
            "status": "ERRO",
            "tempo": tempo,
            "resposta": None,
            "tokens": None
        })


# ============================================================
# RESUMO FINAL
# ============================================================

print("\n\n" + "=" * 60)
print("RESUMO COMPARATIVO")
print("=" * 60)

for resultado in resultados:

    print(f"\nModelo: {resultado['modelo']}")
    print(f"Status: {resultado['status']}")
    print(f"Tempo: {resultado['tempo']:.2f} segundos")

    if resultado["tokens"] is not None:
        print(f"Total de tokens: {resultado['tokens']}")

print("\n" + "=" * 60)
print("FIM DO TESTE")
print("=" * 60)