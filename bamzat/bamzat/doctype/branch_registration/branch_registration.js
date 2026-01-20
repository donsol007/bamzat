// Copyright (c) 2025, Donsol and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Branch Registration", {
// 	refresh(frm) {

// 	},
// });

frappe.ui.form.on('Branch Registration', {
    branch_name: function(frm) {
        if (frm.doc.branch_name) {
            frm.set_value('branch_name', frm.doc.branch_name.toUpperCase());
        }
    }
});