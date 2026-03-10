// Copyright (c) 2026, Donsol and contributors
// For license information, please see license.txt

// frappe.query_reports["Daily Branch Report"] = {
// 	"filters": [

// 	]
// };

frappe.query_reports["Daily Branch Report"] = {
    filters: [
        {
            fieldname: "branch",
            label: "Branch",
            fieldtype: "Link",
            options: "Branch Registration",
            placeholder: "Select Branch"
        },
        {
            fieldname: "id",
            label: "Currency Pair",
            fieldtype: "Link",
            options: "Exchange Rate",
            placeholder: "Select Currency Pair"
        },
        {
            fieldname: "transaction_date",
            label: "Date",
            fieldtype: "Date"
            // Note: No "default" set here. This keeps it empty on load.
        }
    ]
};