# Copyright (c) 2026, Donsol and contributors
# For license information, please see license.txt

# Copyright (c) 2026, Donsol and contributors
# For license information, please see license.txt

# Copyright (c) 2026, Donsol and contributors
# For license information, please see license.txt

import frappe
from frappe.utils import flt

def execute(filters=None):
    columns = get_columns()
    data = get_data(filters)
    
    # Pass filters to summary for the dynamic labels
    summary = get_summary(data, filters)

    return columns, data, None, None, summary


def get_columns():
    return [
        {
            "label": "Currency Pair",
            "fieldname": "currency_pair",
            "fieldtype": "Data",
            "width": 150
        },
        {
            "label": "Rate",
            "fieldname": "rate",
            "fieldtype": "Float",
            "width": 120
        },
        {
            "label": "Amount",
            "fieldname": "amount",
            "fieldtype": "Data",
            "width": 120
        },
        {
            "label": "Amount to Receive",
            "fieldname": "amount_to_receive",
            "fieldtype": "Data",
            "width": 150
        },
        {
            "label": "Payment Mode",
            "fieldname": "payment_mode",
            "fieldtype": "Data",
            "width": 130
        },
        {
            "label": "Transaction Date",
            "fieldname": "transaction_date",
            "fieldtype": "Date",
            "width": 140
        }
    ]

def get_data(filters):
    # CHANGE: Check if date is provided. If not, return empty list immediately.
    # This ensures the report is empty on load.
    if not filters or not filters.get("transaction_date"):
        return []

    conditions = {
        "transaction_date": filters.get("transaction_date")
    }

    if filters.get("branch"):
        conditions["branch"] = filters.get("branch")
    
    if filters.get("id"):
        conditions["currency_pair"] = filters.get("id")
    
    data = frappe.get_all(
        "Exchange Transaction",
        filters=conditions,
        fields=[
            "branch",
            "currency_pair",
            "rate",
            "amount",
            "amount_to_receive",
            "payment_mode",
            "transaction_date"
        ],
        order_by="transaction_date desc"
    )

    return data


def get_summary(data, filters):
    if not data:
        return []

    total_amount = 0
    total_receive = 0

    for d in data:
        total_amount += flt(d.amount)
        total_receive += flt(d.amount_to_receive)

    # Default currency codes
    currency_from = ""
    currency_to = ""

    currency_pair = filters.get("id")

    if currency_pair:
        parts = currency_pair.split("-")
        if len(parts) == 2:
            currency_from = parts[0].strip()
            currency_to = parts[1].strip()

    # Format numbers: "{:,.0f}" adds commas but NO decimal places (e.g. 25,000)
    # If you want 2 decimal places (e.g. 25,000.00), change .0f to .2f
    formatted_amount = "{:,.0f}".format(total_amount)
    formatted_receive = "{:,.0f}".format(total_receive)

    # Concatenate Currency Code + Formatted Number
    # e.g. "NGN" + "200,000" = "NGN200,000"
    amount_display = f"{currency_from}{formatted_amount}"
    receive_display = f"{currency_to}{formatted_receive}"

    return [
        {
            "value": amount_display, 
            "indicator": "Green",
            "label": f"Total Amount Received in {currency_from}" if currency_from else "Total Amount Received",
            "datatype": "Data" # Set to "Data" because value is now a string
        },
        {
            "value": receive_display,
            "indicator": "Blue",
            "label": f"Total Amount Payout in {currency_to}" if currency_to else "Total Amount Payout",
            "datatype": "Data" # Set to "Data" because value is now a string
        }
    ]