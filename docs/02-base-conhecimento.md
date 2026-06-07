# Base de Conhecimento — PIM (v2 — dados reais)
<!--
  PARTE 2 DE 3 | Atualizada com os 4 arquivos reais do projeto.

  PARA COMEÇAR SEM CÓDIGO: vá à Seção 3 → copie o "Contexto Montado" e cole
  antes da primeira mensagem de cada conversa com o agente.
-->

---

## 1. Arquivos do Projeto

| Arquivo | Formato | O que contém |
|---|---|---|
| `perfil_investidor.json` | JSON | Perfil, renda, metas e tolerância a risco do cliente |
| `transacoes.csv` | CSV | Movimentações financeiras do mês atual |
| `produtos_financeiros.json` | JSON | Catálogo educativo de produtos (renda fixa e variável) |
| `historico_atendimento.csv` | CSV | Histórico de interações anteriores com o agente |

---

## 2. Estrutura Real dos Arquivos

### `perfil_investidor.json`

```json
{
  "nome": "João Silva",
  "idade": 32,
  "profissao": "Analista de Sistemas",
  "renda_mensal": 5000.00,
  "perfil_investidor": "moderado",
  "objetivo_principal": "Construir reserva de emergência",
  "patrimonio_total": 15000.00,
  "reserva_emergencia_atual": 10000.00,
  "aceita_risco": false,
  "metas": [
    {
      "meta": "Completar reserva de emergência",
      "valor_necessario": 15000.00,
      "prazo": "2026-06"
    },
    {
      "meta": "Entrada do apartamento",
      "valor_necessario": 50000.00,
      "prazo": "2027-12"
    }
  ]
}
```

---

### `transacoes.csv`

```csv
data,descricao,categoria,valor,tipo
2025-10-01,Salário,receita,5000.00,entrada
2025-10-02,Aluguel,moradia,1200.00,saida
2025-10-03,Supermercado,alimentacao,450.00,saida
2025-10-05,Netflix,lazer,55.90,saida
2025-10-07,Farmácia,saude,89.00,saida
2025-10-10,Restaurante,alimentacao,120.00,saida
2025-10-12,Uber,transporte,45.00,saida
2025-10-15,Conta de Luz,moradia,180.00,saida
2025-10-20,Academia,saude,99.00,saida
2025-10-25,Combustível,transporte,250.00,saida
```

---

### `produtos_financeiros.json`

```json
[
  {
    "nome": "Tesouro Selic",
    "categoria": "renda_fixa",
    "risco": "baixo",
    "rentabilidade": "100% da Selic",
    "aporte_minimo": 30.00,
    "indicado_para": "Reserva de emergência e iniciantes"
  },
  {
    "nome": "CDB Liquidez Diária",
    "categoria": "renda_fixa",
    "risco": "baixo",
    "rentabilidade": "102% do CDI",
    "aporte_minimo": 100.00,
    "indicado_para": "Quem busca segurança com rendimento diário"
  },
  {
    "nome": "LCI/LCA",
    "categoria": "renda_fixa",
    "risco": "baixo",
    "rentabilidade": "95% do CDI",
    "aporte_minimo": 1000.00,
    "indicado_para": "Quem pode esperar 90 dias (isento de IR)"
  },
  {
    "nome": "Fundos Imobiliários (FII)",
    "categoria": "fundo",
    "risco": "medio",
    "rentabilidade": "8% a 12% ao ano (dividendos + variação de cota)",
    "aporte_minimo": 100.00,
    "indicado_para": "Perfil moderado que busca renda passiva mensal"
  },
  {
    "nome": "Fundo de Ações",
    "categoria": "fundo",
    "risco": "alto",
    "rentabilidade": "Variável",
    "aporte_minimo": 100.00,
    "indicado_para": "Perfil arrojado com foco no longo prazo"
  }
]
```

---

### `historico_atendimento.csv`

```csv
data,canal,tema,resumo,resolvido
2025-09-15,chat,CDB,Cliente perguntou sobre rentabilidade e prazos,sim
2025-09-22,telefone,Problema no app,Erro ao visualizar extrato foi corrigido,sim
2025-10-01,chat,Tesouro Selic,Cliente pediu explicação sobre o Tesouro Direto,sim
2025-10-12,chat,Metas financeiras,Cliente acompanhou o progresso da reserva de emergência,sim
2025-10-25,email,Atualização cadastral,Cliente atualizou e-mail e telefone,sim
```

> **Para que serve o histórico?** O agente usa isso para manter continuidade.
> Ex: "Na nossa última conversa você estava acompanhando sua reserva de emergência — quer ver como está o progresso?"

---

## 3. Contexto Montado — João Silva (outubro/2025)
> Copie este bloco completo e cole antes da primeira mensagem de cada conversa.

```
=== CONTEXTO DO CLIENTE ===

PERFIL:
- Nome: João Silva (32 anos) | Analista de Sistemas
- Renda mensal: R$ 5.000,00
- Perfil de risco: Moderado | Aceita risco: Não
- Patrimônio total: R$ 15.000,00
- Reserva de emergência: R$ 10.000,00 acumulados (meta: + R$ 15.000,00 até Jun/2026)

METAS:
1. Completar reserva de emergência → precisa de R$ 15.000 até Jun/2026 (~8 meses)
2. Entrada do apartamento          → precisa de R$ 50.000 até Dez/2027 (~26 meses)

RESUMO DO MÊS (outubro/2025):
- Renda:          R$ 5.000,00
- Moradia:        R$ 1.380,00  (27,6% da renda — aluguel + luz)
- Alimentação:    R$   570,00  (11,4% — supermercado + restaurante)
- Transporte:     R$   295,00  ( 5,9% — combustível + Uber)
- Saúde:          R$   188,00  ( 3,8% — farmácia + academia)
- Lazer:          R$    55,90  ( 1,1% — Netflix)
- Total de gastos: R$ 2.488,90
- LIVRE PARA POUPAR: R$ 2.511,10

ANÁLISE RÁPIDA DAS METAS:
- Meta 1 (reserva): R$ 15.000 ÷ R$ 1.758/mês (70% do livre) = ~8,5 meses → viável até Jun/2026
- Meta 2 (apê): após Jun/2026, redirecionar R$ 2.511/mês → R$ 50.000 em ~20 meses (Fev/2028)
  → Para antecipar, pode começar pequenos aportes paralelos já agora.

ÚLTIMO ATENDIMENTO: 2025-10-12 | Tema: Metas financeiras | Canal: chat

PRODUTOS DISPONÍVEIS (apenas para referência educativa):
- Tesouro Selic    → risco baixo, liquidez diária, aporte mínimo R$ 30
- CDB Liq. Diária  → risco baixo, 102% CDI, aporte mínimo R$ 100
- LCI/LCA          → risco baixo, isento IR, carência 90 dias, aporte mínimo R$ 1.000
- FII              → risco médio, renda mensal, aporte mínimo R$ 100
- Fundo de Ações   → risco alto, longo prazo, aporte mínimo R$ 100

=== FIM DO CONTEXTO ===
```

---

## 4. Fontes de Dados Confiáveis

> O agente deve citar e usar apenas dados dessas fontes. Taxas mudam — atualize
> os valores abaixo mensalmente ou use o código da Seção 5 para buscar automaticamente.

### Taxas de Referência (BACEN — Banco Central do Brasil)

| Índice | O que é | Fonte oficial |
|---|---|---|
| **Selic** | Taxa básica de juros (benchmark da renda fixa) | `api.bcb.gov.br` — série 11 |
| **CDI** | Taxa interbancária (benchmark de CDBs e LCI/LCA) | `api.bcb.gov.br` — série 12 |
| **IPCA** | Inflação oficial do país (ajuste de metas de longo prazo) | `api.bcb.gov.br` — série 433 |
| **INPC** | Inflação para assalariados de baixa renda | `api.bcb.gov.br` — série 4390 |

**Valores de referência (atualize mensalmente):**
```json
{
  "taxa_selic_anual": "13,75%",
  "cdi_anual": "13,65%",
  "ipca_acumulado_12m": "4,83%",
  "fonte": "Banco Central do Brasil",
  "url": "https://api.bcb.gov.br/dados/serie/bcdata.sgs.{serie}/dados/ultimos/1?formato=json",
  "data_referencia": "atualizar mensalmente"
}
```

---

### Tesouro Direto (Tesouro Nacional)

Taxas e preços dos títulos públicos em tempo real:

```
URL: https://www.tesourodireto.com.br/json/br/com/b3/tesourodireto/model/dto/response/TesouroDiretoListaDTO.json
Portal educativo: https://www.tesourodireto.com.br
```

---

### Regras Padrão de Planejamento Financeiro

> Estas regras são consenso entre planejadores financeiros e certificações CFP.
> O agente pode usá-las como base para recomendar comportamentos (não ativos).

```json
{
  "reserva_emergencia": {
    "regra": "3 a 6 meses de despesas mensais totais",
    "clt": "3 meses (maior estabilidade de emprego)",
    "autonomo_pj": "6 meses (renda variável, maior risco)",
    "joao_silva": {
      "despesas_mensais": 2488.90,
      "meta_minima_3m": 7466.70,
      "meta_ideal_6m": 14933.40,
      "meta_adotada": 25000.00,
      "nota": "Meta acima do mínimo — conservador e adequado para perfil moderado"
    }
  },
  "orcamento_50_30_20": {
    "descricao": "Regra de orçamento popularizada por Elizabeth Warren",
    "necessidades": "até 50% da renda líquida (moradia, alimentação, transporte, saúde)",
    "qualidade_de_vida": "até 30% (lazer, cultura, restaurantes)",
    "poupanca_investimento": "mínimo 20%",
    "joao_silva": {
      "necessidades_atual": "49,7% — dentro do limite",
      "qualidade_de_vida_atual": "1,1% — muito abaixo do máximo",
      "poupanca_atual": "50,2% — excelente",
      "nota": "João está em ótima posição: poupo mais do que gasta em lazer"
    }
  },
  "piramide_de_liquidez": {
    "descricao": "Ordem recomendada de alocação do dinheiro",
    "etapa_1": "Reserva de emergência em renda fixa líquida (Tesouro Selic ou CDB Liq. Diária)",
    "etapa_2": "Objetivos de médio prazo em renda fixa (LCI/LCA, CDB com prazo)",
    "etapa_3": "Objetivos de longo prazo e renda variável (FIIs, ações) — somente após etapas 1 e 2"
  }
}
```

---

### Regulação (CVM — Comissão de Valores Mobiliários)

| Regra | O que significa para o agente |
|---|---|
| **Resolução CVM 35** | Vedado recomendar ativos sem habilitação como assessor ou consultor de investimentos |
| **Educação financeira** | Explicar COMO funcionam os produtos é permitido e incentivado |
| **Portal do Investidor** | Fonte oficial: `https://www.investidor.gov.br` |

---

### Dataset Público — Hugging Face (para aprimorar linguagem financeira)

```
Dataset: "nicholasKluge/financial-news-ptbr"
URL: https://huggingface.co/datasets/nicholasKluge/financial-news-ptbr
Uso: enriquecer a linguagem do agente com terminologia financeira em português

Dataset: "carolina-c4ai/common-pt-financial"
URL: https://huggingface.co/datasets
Uso: base de perguntas e respostas financeiras em português para testes de comportamento
```

---

## 5. Carregamento Automático com Taxas Reais (Python)
> Busca automaticamente Selic, CDI e IPCA do BACEN e monta o contexto completo.

```python
import requests
import pandas as pd
import json

# ── Busca taxas do BACEN ─────────────────────────────────────────────────────
def buscar_taxa_bcb(serie: int) -> float:
    url = f"https://api.bcb.gov.br/dados/serie/bcdata.sgs.{serie}/dados/ultimos/1?formato=json"
    resp = requests.get(url, timeout=5)
    return float(resp.json()[0]["valor"].replace(",", "."))

selic_diaria = buscar_taxa_bcb(11)   # Selic
cdi_diaria   = buscar_taxa_bcb(12)   # CDI
ipca_mensal  = buscar_taxa_bcb(433)  # IPCA

# ── Carrega arquivos do projeto ───────────────────────────────────────────────
with open("data/perfil_investidor.json", encoding="utf-8") as f:
    perfil = json.load(f)

with open("data/produtos_financeiros.json", encoding="utf-8") as f:
    produtos = json.load(f)

transacoes     = pd.read_csv("data/transacoes.csv")
historico      = pd.read_csv("data/historico_atendimento.csv")

# ── Calcula resumo mensal ─────────────────────────────────────────────────────
entradas   = transacoes[transacoes["tipo"] == "entrada"]["valor"].sum()
saidas     = transacoes[transacoes["tipo"] == "saida"]["valor"].sum()
por_cat    = transacoes[transacoes["tipo"] == "saida"].groupby("categoria")["valor"].sum().to_dict()
livre      = entradas - saidas
ultimo_at  = historico.sort_values("data").iloc[-1]

# ── Monta contexto ────────────────────────────────────────────────────────────
contexto = f"""
=== CONTEXTO DO CLIENTE ===

PERFIL: {perfil['nome']} | {perfil['profissao']} | {perfil['idade']} anos
Renda: R$ {perfil['renda_mensal']:.2f} | Perfil: {perfil['perfil_investidor']} | Risco: {'Não' if not perfil['aceita_risco'] else 'Sim'}
Patrimônio: R$ {perfil['patrimonio_total']:.2f} | Reserva atual: R$ {perfil['reserva_emergencia_atual']:.2f}

METAS:
{chr(10).join(f"  - {m['meta']}: R$ {m['valor_necessario']:.2f} até {m['prazo']}" for m in perfil['metas'])}

RESUMO DO MÊS:
  Renda: R$ {entradas:.2f} | Gastos: R$ {saidas:.2f} | Livre: R$ {livre:.2f}
  {' | '.join(f"{c}: R${v:.0f}" for c, v in sorted(por_cat.items(), key=lambda x: -x[1]))}

TAXAS ATUAIS (BACEN):
  Selic: {selic_diaria}% a.d. | CDI: {cdi_diaria}% a.d. | IPCA: {ipca_mensal}% a.m.

ÚLTIMO ATENDIMENTO: {ultimo_at['data']} | {ultimo_at['tema']} | {ultimo_at['canal']}

PRODUTOS: {[p['nome'] + ' (risco: ' + p['risco'] + ')' for p in produtos]}

=== FIM DO CONTEXTO ===
"""

print(contexto)
```
