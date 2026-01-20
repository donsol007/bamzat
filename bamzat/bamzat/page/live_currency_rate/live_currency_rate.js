// frappe.pages['live-currency-rate'].on_page_load = function(wrapper) {
// 	var page = frappe.ui.make_app_page({
// 		parent: wrapper,
// 		title: 'Current Exchange Rate',
// 		single_column: true
// 	});
// }
frappe.pages['live-currency-rate'].on_page_load = function(wrapper) {
    const page = frappe.ui.make_app_page({
        parent: wrapper,
        title: 'Live NGN Exchange Rates',
        single_column: true
    });

    // Add refresh button to page actions
    page.add_action_icon("refresh", () => {
        fetch_rates(true);
    });

    // Page body
    $(`
        <div class="card">
            <div class="card-body">
                <table class="table table-bordered table-hover text-center">
                    <thead class="table-dark">
                        <tr>
                            <th>Currency</th>
                            <th>Code</th>
                            <th>Rate (1 NGN)</th>
                        </tr>
                    </thead>
                    <tbody id="ngn-rate-table">
                        <tr>
                            <td colspan="3">Loading rates...</td>
                        </tr>
                    </tbody>
                </table>
                <div class="text-muted text-end mt-2" id="rate-date"></div>
            </div>
        </div>
    `).appendTo(page.body);

    // Initial load
    fetch_rates();

    function fetch_rates(is_refresh = false) {
        if (is_refresh) {
            $("#ngn-rate-table").html(`
                <tr>
                    <td colspan="3">Refreshing rates...</td>
                </tr>
            `);
        }

        frappe.call({
            method: "bamzat.ngn_rates.get_ngn_rates",
            callback: function(r) {
                if (!r.message) return;

                let rows = "";
                
                r.message.rates.forEach(rate => {
                    rows += `
                        <tr>
                            <td style="color:black;">${rate.name}</td>
                            <td style="color:black;"><strong>${rate.code}</strong></td>
                            <td style="color:black;">${(1 / rate.rate).toFixed(2)}</td>
                        </tr>
                    `;
                });

                $("#ngn-rate-table").html(rows);
                $("#rate-date").text("Rates Date: " + r.message.date);
            }
        });
    }
};
