from . import __version__ as app_version

app_name = "astro_chat"
app_title = "Astro Chat"
app_publisher = "Nilesh Pithiya"
app_description = "this app for create a chat ui in frappe and astro"
app_email = "nilesh@sanskartechnolab.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/astro_chat/css/astro_chat.css"
app_include_js = "/assets/astro_chat/js/chatbot.js"

# include js, css files in header of desk.html
app_include_css = ['chat.bundle.css']
app_include_js = ['chat.bundle.js']

# include js, css files in header of web template
# web_include_css = "/assets/astro_chat/css/astro_chat.css"
# web_include_js = "/assets/astro_chat/js/astro_chat.js"

# include js, css files in header of web template
web_include_css = ['chat.bundle.css']
web_include_js = ['chat.bundle.js']

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "astro_chat/public/scss/website"

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

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "astro_chat.utils.jinja_methods",
#	"filters": "astro_chat.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "astro_chat.install.before_install"
# after_install = "astro_chat.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "astro_chat.uninstall.before_uninstall"
# after_uninstall = "astro_chat.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "astro_chat.utils.before_app_install"
# after_app_install = "astro_chat.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "astro_chat.utils.before_app_uninstall"
# after_app_uninstall = "astro_chat.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "astro_chat.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"astro_chat.tasks.all"
#	],
#	"daily": [
#		"astro_chat.tasks.daily"
#	],
#	"hourly": [
#		"astro_chat.tasks.hourly"
#	],
#	"weekly": [
#		"astro_chat.tasks.weekly"
#	],
#	"monthly": [
#		"astro_chat.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "astro_chat.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "astro_chat.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "astro_chat.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["astro_chat.utils.before_request"]
# after_request = ["astro_chat.utils.after_request"]

# Job Events
# ----------
# before_job = ["astro_chat.utils.before_job"]
# after_job = ["astro_chat.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"astro_chat.auth.validate"
# ]

sounds = [
    {'name': 'chat-notification', 'src': '/assets/chat/sounds/chat-notification.mp3', 'volume': 0.2},
    {'name': 'chat-message-send', 'src': '/assets/chat/sounds/chat-message-send.mp3', 'volume': 0.2},
    {'name': 'chat-message-receive', 'src': '/assets/chat/sounds/chat-message-receive.mp3', 'volume': 0.5}
]