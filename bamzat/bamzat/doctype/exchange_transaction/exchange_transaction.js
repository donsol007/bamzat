// Copyright (c) 2025, Donsol and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Exchange Transaction", {
// 	refresh(frm) {

// 	},
// });
frappe.ui.form.on('Exchange Transaction', {
    refresh(frm) {
        // Make amount_to_pay read-only
        frm.set_df_property('amount_to_receive', 'read_only', 1);
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

    rate(frm) {
        calculate_amount_to_receive(frm);
    },
    amount(frm) {
        calculate_amount_to_receive(frm);
    },
    currency_pair(frm) {
        update_amount_label(frm);
    },
});

function calculate_amount_to_receive(frm) {
    const rate = frm.doc.rate || 0;
    const amount = frm.doc.amount || 0;
    const total = rate * amount;
    frm.set_value('amount_to_receive', total);
}

function update_amount_label(frm) {
    const pair = frm.doc.currency_pair;

    if (!pair) {
        frm.set_df_property('amount', 'label', __('Amount'));
        frm.refresh_field('amount');
        return;
    }

    // Split currency pair (e.g. NGN-CFA → NGN)
    const base_currency = pair.split('-')[0]?.trim();
    const pair_currency = pair.split('-')[1]?.trim();

    if (base_currency) {
        frm.set_df_property(
            'amount',
            'label',
            __('Amount in {0}', [base_currency])
        );
        frm.refresh_field('amount');
    }
    if (base_currency) {
        frm.set_df_property(
            'amount_to_receive',
            'label',
            __('Amount to Receive in {0}', [pair_currency])
        );
        frm.refresh_field('amount_to_receive');
    }
}