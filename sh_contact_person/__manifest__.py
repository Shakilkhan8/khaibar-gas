# -*- coding: utf-8 -*-
# Part of Softhealer Technologies.
{
    "name": "Contact Person",
    "author": "Softhealer Technologies",
    "website": "https://www.softhealer.com",
    "support": "support@softhealer.com",
    "license": "OPL-1",
    "version": "14.0.1",
    "category": "Extra Tools",
    "summary": """
Sales Contact Person Detail, Quotation Partner Detail,
Purchase Order Client Details, Request For Quotation Contact Detail,
Search Sale Order By Contact Person,Contact Person Purchase Order,
Sales By Contact Person Odoo
""",
    "description": """
This module provides a contact person field in the sale order/quotation
and purchase order/request for quotation. The contact person field
available in the tree view & form view. You can filter or group by
the sales order/purchase order by a contact person.
You can search the data by the contact person.
You can print the contact person details in the reports.
Contact Person Odoo, Manage Contact Person In Sales,
Partner Detail In Quotation, Client Details In Purchase Order,
Contact Detail In Request For Quotation, Search Sale Order By Contact Person,
Filter Sales By Contact Person, Purchase Order By Contact Person,
Sales By Contact Person Odoo, Sales Contact Person Detail,
Quotation Partner Detail, Purchase Order Client Details,
Request For Quotation Contact Detail, Search Sale Order By Contact Person,
Filter Sales By Contact Person, Contact Person Purchase Order,
Sales By Contact Person Odoo
""",
    "depends": [
        "sale_management",
        "purchase"
    ],
    "data": [
        "views/sale.xml",
        "views/purchase.xml",
        "report/order_report.xml",
    ],
    "images": ["static/description/background.png"],
    "auto_install": False,
    "application": True,
    "installable": True,
    "price": "15",
    "currency": "EUR"
}
