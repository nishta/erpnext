from __future__ import unicode_literals
from frappe import _

def get_data():
	return {
		"Accounts": {
			"color": "#3498db",
			"icon": "octicon octicon-repo",
			"type": "module"
		},
		"Buying": {
			"color": "#c0392b",
			"icon": "icon-shopping-cart",
			"icon": "octicon octicon-briefcase",
			"type": "module"
		},
		"HR": {
			"color": "#2ecc71",
			"icon": "icon-group",
			"icon": "octicon octicon-organization",
			"label": _("Human Resources"),
			"type": "module"
		},
		"Manufacturing": {
			"color": "#7f8c8d",
			"icon": "icon-cogs",
			"icon": "octicon octicon-tools",
			"type": "module"
		},
		"Project Management": {
			"color": "#7f8c8d",
			"icon": "icon-cogs",
			"icon": "octicon octicon-squirrel",
			"type": "module"
		},
		"POS": {
			"color": "#589494",
			"icon": "icon-th",
			"icon": "octicon octicon-credit-card",
			"type": "page",
			"link": "pos"
		},
		"Projects": {
			"color": "#8e44ad",
			"icon": "icon-puzzle-piece",
			"icon": "octicon octicon-rocket",
			"type": "module"
		},
		"Selling": {
			"color": "#1abc9c",
			"icon": "icon-tag",
			"icon": "octicon octicon-tag",
			"type": "module"
		},
		"CRM": {
			"color": "#EF4DB6",
			"icon": "octicon octicon-broadcast",
			"type": "module"
		},
		"Stock": {
			"color": "#f39c12",
			"icon": "icon-truck",
			"icon": "octicon octicon-package",
			"type": "module"
		},
		"Support": {
			"color": "#2c3e50",
			"icon": "icon-phone",
			"icon": "octicon octicon-issue-opened",
			"type": "module"
		},
		"Learn": {
			"color": "#7272FF",
			"force_show": True,
			"icon": "icon-facetime-video",
			"type": "module",
			"is_help": True
		}
	}
