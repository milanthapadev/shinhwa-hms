app_name = "shinwa_hms"
app_title = "Shinwa Hms"
app_publisher = "Maddati Tech"
app_description = "HMS for shinwa hostel"
app_email = "tmilan0604@gmail.com"
app_license = "mit"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "shinwa_hms",
# 		"logo": "/assets/shinwa_hms/logo.png",
# 		"title": "Shinwa Hms",
# 		"route": "/shinwa_hms",
# 		"has_permission": "shinwa_hms.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/shinwa_hms/css/shinwa_hms.css"
# app_include_js = "/assets/shinwa_hms/js/shinwa_hms.js"

# include js, css files in header of web template
# web_include_css = "/assets/shinwa_hms/css/shinwa_hms.css"
# web_include_js = "/assets/shinwa_hms/js/shinwa_hms.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "shinwa_hms/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "shinwa_hms/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# automatically load and sync documents of this doctype from downstream apps
# importable_doctypes = [doctype_1]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "shinwa_hms.utils.jinja_methods",
# 	"filters": "shinwa_hms.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "shinwa_hms.install.before_install"
# after_install = "shinwa_hms.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "shinwa_hms.uninstall.before_uninstall"
# after_uninstall = "shinwa_hms.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "shinwa_hms.utils.before_app_install"
# after_app_install = "shinwa_hms.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "shinwa_hms.utils.before_app_uninstall"
# after_app_uninstall = "shinwa_hms.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "shinwa_hms.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

scheduler_events = {
    "daily": [
        "shinwa_hms.scheduled_tasks.auto_create_student_invoices",
        "shinwa_hms.scheduled_tasks.notify_upcoming_rent_payments",
        "shinwa_hms.scheduled_tasks.mark_overdue_invoices"
    ]
}

# Testing
# -------

# before_tests = "shinwa_hms.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "shinwa_hms.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
override_doctype_dashboards = {
    "Student": "shinwa_hms.shinwa_hms.config.student_dashboard.get_data"
}

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["shinwa_hms.utils.before_request"]
# after_request = ["shinwa_hms.utils.after_request"]

# Job Events
# ----------
# before_job = ["shinwa_hms.utils.before_job"]
# after_job = ["shinwa_hms.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"shinwa_hms.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

