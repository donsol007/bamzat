// Copyright (c) 2026, Donsol and contributors
// For license information, please see license.txt

// frappe.query_reports["Bamzat General Report"] = {
// 	"filters": [

// 	]
// };

frappe.query_reports["Bamzat General Report"] = {
    filters: [
        
        {
            fieldname: "id",
            label: "Currency Pair",
            fieldtype: "Link",
            options: "Exchange Rate",
            placeholder: "Select Currency Pair"
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