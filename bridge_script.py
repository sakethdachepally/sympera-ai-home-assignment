import pandas as pd
import json

# Load transaction data
df = pd.read_csv("data/transactions.csv")

# Convert amount column from currency string to float
df["amount"] = (
    df["amount"]
    .astype(str)
    .str.replace("$", "", regex=False)
    .str.replace(",", "", regex=False)
    .str.replace("+", "", regex=False)
    .str.replace("(", "-", regex=False)
    .str.replace(")", "", regex=False)
    .str.strip()
    .astype(float)
)

# Basic metrics
revenue = df[df["category"] == "Revenue"]["amount"].sum()
debits = abs(df[df["type"] == "Debit"]["amount"].sum())
credits = df[df["type"] == "Credit"]["amount"].sum()
net_cash_flow = credits - debits

inventory_spend = abs(df[df["category"] == "Inventory"]["amount"].sum())
growth_spend = abs(df[df["category"].isin(["Tech/Growth", "Growth"])]["amount"].sum())
savings = abs(df[df["category"] == "Savings"]["amount"].sum())

# Positive signals
signal_1 = {
    "name": "Margin Resilience",
    "description": "Despite 15% industry material inflation and sector margins falling to 4%, Elite Builds generated strong positive net cash flow and recurring client payments."
}

signal_2 = {
    "name": "Strategic Growth Discipline",
    "description": "The company transferred cash to savings and invested in technology and new equipment, indicating controlled expansion rather than financial stress."
}

# Knowledge object
knowledge_object = {
    "company": "Elite Builds LLC",
    "industry": "Construction",
    "market_context": {
        "material_cost_inflation": "15%",
        "sector_margin": "4%",
        "credit_tightening_trigger": "High Expense Velocity"
    },
    "financial_summary": {
        "total_revenue": revenue,
        "net_cash_flow": net_cash_flow,
        "inventory_spend": inventory_spend,
        "growth_spend": growth_spend,
        "savings_transfer": savings
    },
    "positive_signals": [signal_1, signal_2],
    "rm_recommendation": {
        "product": "Working Capital Line of Credit",
        "reason": "Helps support growth projects and manage inventory volatility while preserving strong liquidity."
    }
}

with open("sample_output.json", "w") as f:
    json.dump(knowledge_object, f, indent=2)

print("sample_output.json created")