# Copyright (c) 2026, Donsol and contributors
# For license information, please see license.txt

# import frappe
import frappe
from frappe.utils import today, flt

def execute(filters=None):
    columns = get_columns()
    data = get_data(filters)

    summary = get_summary(data)

    return columns, data, None, None, summary


def get_columns():
    return [
        {
            "label": "Branch",
            "fieldname": "branch",
            "fieldtype": "Link",
            "options": "Branch Registration",
            "width": 150
        },
        {
            "label": "Currency Pair",
            "fieldname": "currency_pair",
            "fieldtype": "Data",
            "width": 140
        },
        {
            "label": "Rate",
            "fieldname": "rate",
            "fieldtype": "Float",
            "width": 110
        },
        {
            "label": "Amount",
            "fieldname": "amount",
            "fieldtype": "Currency",
            "width": 130
        },
        {
            "label": "Amount to Receive",
            "fieldname": "amount_to_receive",
            "fieldtype": "Currency",
            "width": 160
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

    conditions = []

    # Date range filter
    if filters.get("date_from") and filters.get("date_to"):
        conditions.append(["transaction_date", ">=", filters.get("date_from")])
        conditions.append(["transaction_date", "<=", filters.get("date_to")])
    else:
        # Default to today
        conditions.append(["transaction_date", "=", today()])

    # Branch filter
    if filters.get("branch"):
        conditions.append(["branch", "=", filters.get("branch")])

    # Currency pair filter
    if filters.get("id"):
        conditions.append(["currency_pair", "=", filters.get("id")])

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

def get_summary(data):

    total_amount = 0
    total_receive = 0

    for d in data:
        total_amount += flt(d.amount)
        total_receive += flt(d.amount_to_receive)

    return [
        {
            "value": total_amount,
            "indicator": "Green",
            "label": "Total Amount",
            "datatype": "Currency"
        },
        {
            "value": total_receive,
            "indicator": "Blue",
            "label": "Total Amount to Receive",
            "datatype": "Currency"
        }
    ]