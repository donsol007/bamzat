# Copyright (c) 2026, Donsol and contributors
# For license information, please see license.txt

import frappe
from frappe.utils import flt

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


def get_conditions(filters):

    conditions = ""
    values = {}

    if filters.get("branch"):
        conditions += " AND branch = %(branch)s"
        values["branch"] = filters.get("branch")

    if filters.get("from_date"):
        conditions += " AND transaction_date >= %(from_date)s"
        values["from_date"] = filters.get("from_date")

    if filters.get("to_date"):
        conditions += " AND transaction_date <= %(to_date)s"
        values["to_date"] = filters.get("to_date")

    return conditions, values


def get_data(filters):

    conditions, values = get_conditions(filters)

    data = frappe.db.sql(f"""
        SELECT
            branch,
            currency_pair,
            rate,
            amount,
            amount_to_receive,
            payment_mode,
            transaction_date
        FROM
            `tabExchange Transaction`
        WHERE
            docstatus < 2
            {conditions}
        ORDER BY
            transaction_date DESC
    """, values, as_dict=1)

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