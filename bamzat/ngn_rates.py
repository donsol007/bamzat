import frappe
import requests

@frappe.whitelist()
def get_ngn_rates():
    url = "https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies/ngn.json"

    response = requests.get(url, timeout=10)
    response.raise_for_status()
    data = response.json()

    ngn = data.get("ngn", {})

    currencies = {
        "usd": "US Dollar",
        "xaf": "Central African CFA Franc",
        "eur": "Euro",
        "gbp": "British Pound",
        "cny": "Chinese Yuan"
    }

    rates = []
    for code, name in currencies.items():
        if code in ngn:
            rates.append({
                "code": code.upper(),
                "name": name,
                "rate": round(ngn[code], 6)
            })

    return {
        "date": data.get("date"),
        "rates": rates
    }
@frappe.whitelist()
def get_credit_exchange_transactions():
    return frappe.get_all(
        "Exchange Transaction",
        fields=[
            "transaction_date",
            "sender_name",
            "amount"
        ],
        filters={
            "payment_confirmation": "Credit"
        },
        order_by="transaction_date desc",
        limit_page_length=20
    )
