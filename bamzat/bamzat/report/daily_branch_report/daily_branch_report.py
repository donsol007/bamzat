# Copyright (c) 2026, Donsol and contributors
# For license information, please see license.txt

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
            "fieldtype": "Currency",
            "width": 120
        },
        {
            "label": "Amount to Receive",
            "fieldname": "amount_to_receive",
            "fieldtype": "Currency",
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

    conditions = {
        "transaction_date": today()
    }

    if filters.get("branch"):
        conditions["branch"] = filters.get("branch")

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