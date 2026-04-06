# Sympera AI Home Assignment

## Objective

The goal of this assignment is to convert raw banking transactions and external market context into concise, high-value signals that help a Bank Relationship Manager identify growth opportunities for Elite Builds LLC.

The broader construction industry is facing 15% inflation in raw material costs and average margins have dropped to 4%. Despite this, Elite Builds continues to generate positive cash flow and invest in future growth. :contentReference[oaicite:0]{index=0}

---

## Approach

I first summarized the transaction data into key financial metrics such as:
- Total revenue
- Total debit spend
- Net cash flow
- Inventory expense
- Growth-related expense
- Savings transfer

I then combined those metrics with the external market context to create two structured "Positive Signals" that an LLM can interpret easily.

The goal was not to summarize every transaction, but to highlight the most relevant information for a relationship manager in under 300 tokens. :contentReference[oaicite:1]{index=1}

---

## Positive Signal 1 – Margin Resilience

**Signal Name:** Margin Resilience

Although construction input costs have increased by 15% and average industry margins have fallen to 4%, Elite Builds still generated:

- Total client revenue: $112,000
- Net cash flow: $44,720

This indicates that the company is managing inflation pressure better than its peers and remains financially healthy despite difficult market conditions.

Why this matters:
A relationship manager should recognize that Elite Builds is outperforming the broader construction market and may represent a lower-risk lending opportunity.

---

## Positive Signal 2 – Strategic Growth Discipline

**Signal Name:** Strategic Growth Discipline

Elite Builds is not only profitable, but is also allocating capital in a disciplined way:

- $5,000 transferred into savings
- $10,650 invested into technology and growth
- $10,000 equipment downpayment for future capacity

This indicates that the company is planning for long-term growth while still preserving liquidity.

Why this matters:
The business is behaving like a company preparing to expand, not a company reacting to financial stress.

---

## Why These Signals Matter

The assignment asked for "hidden" positive trends that could help a relationship manager identify a growth opportunity. The two signals above are valuable because they combine:
- Internal financial behavior
- External market pressure
- Evidence of future growth

Instead of simply saying revenue is high, the signals explain why the company is strong relative to the industry. :contentReference[oaicite:2]{index=2}

---

## RM Product Recommendation

**Recommended Product:** Working Capital Line of Credit

Why:
Elite Builds appears financially healthy but still operates in a market where material costs are rising and banks are tightening credit. A working capital line of credit would allow the company to:
- Smooth cash flow between projects
- Purchase inventory without reducing liquidity
- Continue expanding while maintaining flexibility

A secondary opportunity could be a high-yield savings or treasury management product because the company already shows a pattern of transferring cash into savings.

---

## RM Outreach Hook

> Elite Builds has remained cash-positive and continued investing in growth despite rising construction costs across the industry. We would like to discuss a working capital facility that can help support upcoming projects while preserving your liquidity.

---

## Prompt Design

### System Prompt

```text
You are a commercial banking copilot for relationship managers. Use only the provided JSON knowledge object. Identify positive growth signals, explain why the company is attractive despite market conditions, and recommend the best banking product. Do not invent facts that are not present in the data.