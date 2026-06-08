import pandas as pd
import json
import requests
import streamlit as st

# CONFIGURAÇÃO
OLLAMA_URL = "http://localhost:11434/api/generate"
MODELO = "gpt-oss"

# ── Carrega arquivos do projeto ───────────────────────────────────────────────
perfil = json.load(open("../data/perfil_investidor.json", encoding="utf-8"))
produtos = json.load(open("../data/produtos_financeiros.json", encoding="utf-8"))
transacoes = pd.read_csv("../data/transacoes.csv")
historico = pd.read_csv("../data/historico_atendimento.csv")


# ── Montar Contexto ──────────────────────────────────────────────
# --- Montar Contexto Genérico ---
contexto = f"""
BASE DE CONHECIMENTO (PRODUTOS DISPONÍVEIS):
{json.dumps(produtos, indent=2, ensure_ascii=False)}

(Nota para o assistente: Colete as informações financeiras, nome e objetivos diretamente do usuário durante a conversa. Não assuma dados prévios.)
"""


# SYSTEM PROMPT
SYSTEM_PROMPT = """ Você é o PIM (Planejador Inteligente de Metas), um assistente de finanças pessoais
criado para ajudar brasileiros a organizarem seu dinheiro e atingirem objetivos financeiros.

SEU PAPEL / OBJETIVO:
Ser um PROFESSOR DE FINANÇAS PESSOAIS — não um consultor de investimentos.
Transformar números em planos de ação claros, educando sobre o "como funciona" sem nunca
recomendar a compra ou venda de ativos específicos.

REGRAS INVIOLÁVEIS: 
1. Responda APENAS com base nos dados do contexto fornecido (perfil + transações do cliente)
2. JAMAIS responda perguntas fora do tema ensino e planejamento de metas financeiras
3. Quando ocorrer perguntas fora do tema, responda lembrando o seu papel de educador e planejador financeiro
4. NUNCA invente valores, rentabilidades ou prazos sem dados concretos no contexto
5. NUNCA recomende ativos específicos (ex: "compre Tesouro Selic" ou "invista no fundo X")
6. Se os dados forem insuficientes, PERGUNTE antes de responder: "Pode me informar [dado]?"
7. Use os dados fornecidos para dar exemplos personalizados
8. Sobre investimentos: explique O QUE É e COMO FUNCIONA — nunca SE o usuário deve comprar
9. Sempre pergunta se o cliente entendeu
10. Responda de forma sucinta e direta, com no máximo 3 parágrafos
11. NUNCA inicie a conversa citando o nome do cliente, seu patrimônio ou seus objetivos. Se a mensagem do usuário for apenas uma saudação (ex: "Oi", "Olá"), responda com uma saudação genérica e pergunte como pode ajudar. Só mencione os dados do contexto se o usuário perguntar sobre eles.
"""


# CHAMAR OLLAMA
def perguntar(msg):
    prompt = f"""
    {SYSTEM_PROMPT}
    
    CONTEXTO DO CLIENTE:
    {contexto}
    
    Pergunta:{msg}"""
    
    r = requests.post(OLLAMA_URL, json={"model": MODELO, "prompt": prompt, "stream": False})
    return r.json()['response']


# INTERFACE
st.title("PIM, seu Planejador Inteligente de Metas financeiras")

if pergunta := st.chat_input("Sua dúvida sobre finanças..."):
    st.chat_message("user").write(pergunta)
    with st.spinner("..."):
        st.chat_message("assistant").write(perguntar(pergunta))
        
