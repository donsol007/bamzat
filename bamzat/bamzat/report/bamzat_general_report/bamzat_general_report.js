// Copyright (c) 2026, Donsol and contributors
// For license information, please see license.txt

// frappe.query_reports["Bamzat General Report"] = {
// 	"filters": [

// 	]
// };

frappe.query_reports["Bamzat General Report"] = {
    filters: [

        {
            "fieldname": "date_from",
            "label": "Date From",
            "fieldtype": "Date"
        },
        {
            "fieldname": "date_to",
            "label": "Date To",
            "fieldtype": "Date"
        },
        {
            fieldname: "branch",
            label: "Branch",
            fieldtype: "Link",
            options: "Branch Registration"
        },

        {
            fieldname: "id",
            label: "Currency Pair",
            fieldtype: "Link",
			options: "Exchange Rate"
        }

    ]
};