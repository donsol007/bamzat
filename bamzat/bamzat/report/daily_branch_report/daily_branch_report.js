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
            options: "Branch Registration"
        }
    ]
};