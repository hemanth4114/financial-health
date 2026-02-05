from flask import Flask, jsonify
from flask_cors import CORS
import pandas as pd

app = Flask(__name__)
CORS(app)

@app.route("/analyze")
def analyze():
    df = pd.read_csv("finance_data.csv")

    total_revenue = df["revenue"].sum()
    total_expense = df["expense"].sum()
    profit = total_revenue - total_expense

    if profit > 50000:
        health = "Good"
    elif profit > 0:
        health = "Average"
    else:
        health = "Risky"

    result = {
        "total_revenue": int(total_revenue),
        "total_expense": int(total_expense),
        "profit_or_loss": int(profit),
        "financial_health": health
    }

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)

