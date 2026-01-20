
import frappe

def get_context(context):
    # Redirect already logged-in users to /app
    if frappe.session.user != "Guest":
        frappe.local.flags.redirect_location = "/app"
        raise frappe.Redirect

    # Disable default Frappe layout (we use full custom HTML)
    # context.no_header = False
    # context.no_footer = True
    # context.show_sidebar = True
