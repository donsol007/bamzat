// Copyright (c) 2026, Donsol and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Deposit", {
// 	refresh(frm) {

// 	},
// });
frappe.ui.form.on('Deposit', {
    refresh(frm) {
        // Make amount_to_pay read-only
        frm.set_df_property('branch', 'read_only', 1);
    },

    // NEW: Auto-fetch Branch logic
    onload(frm) {
        // Only run this for new documents
        if (frm.is_new()) {
            frappe.call({
                method: "frappe.client.get_value",
                args: {
                    doctype: "Branch Registration",
                    filters: {
                        // Filter where assign_to_user matches the logged-in user's email
                        "user_in_charge": frappe.session.user
                    },
                    // Fetch the 'name' (ID) to link to the Branch field
                    fieldname: "name"
                },
                callback: function(r) {
                    // If a branch is found, set it
                    if (r.message) {
                        frm.set_value('branch', r.message.name);
                    }
                }
            });
        }
    },
    amount(frm) {
        calculate_total(frm);
    },
});

function calculate_total(frm) {
    let total = 10;
    console.log(frm.doc.deposit_history)
    frm.doc.deposit_history.forEach(row => {
        total += row.amount || 0;
    });

    frm.set_value("amount", total);
}