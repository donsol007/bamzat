// Copyright (c) 2026, Donsol and contributors
// For license information, please see license.txt

// frappe.query_reports["Branch Report"] = {
// 	"filters": [

// 	]
// };

frappe.query_reports["Branch Report"] = {
    filters: [

        {
            fieldname: "branch",
            label: "Branch",
            fieldtype: "Link",
            options: "Branch Registration"
        },

        {
            fieldname: "from_date",
            label: "From Date",
            fieldtype: "Date"
        },

        {
            fieldname: "to_date",
            label: "To Date",
            fieldtype: "Date"
        }

    ]
};