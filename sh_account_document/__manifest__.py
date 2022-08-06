# -*- coding: utf-8 -*-
# Part of Softhealer Technologies.
{
    "name": "Account Document Management",

    "author": "Softhealer Technologies",

    "license": "OPL-1",

    "website": "https://www.softhealer.com",

    "support": "support@softhealer.com",

    "version": "14.0.1",

    "category": "Accounting",

    "summary": "Invoice Document Management,Bill Document Management,Credit Note Document Management,Debit Note Document Management, Manage Document,Manage Invoice Document,Manage Customer Documents,Customer Document Management,Employee Document Management Odoo",
    
    "description": """This module is very useful to manage important documents of the accounts(invoice, bill, credit note, debit note, payments). It helps to send email notifications to customers for document expiration. You can send notifications before/after the expiry date as well as when the document expires. We provide a multiple email feature that helps to send email notifications to multiple employees at a time. You can see the document without download using the document smart button. This module allows sending the notification using scheduled action or manually. cheers!""",

    "depends": ['account'],
    "data": [

        'security/account_document_security.xml',

        'data/account_document_email_notification_template.xml',
        'data/account_document_scheduler.xml',

        'views/sh_ir_attachments_views.xml',
        'views/account.xml',
        'views/general_config_settings.xml',
    ],
    "images": ["static/description/background.png", ],

    "installable": True,
    "auto_install": False,
    "application": True,
    "price": "12",
    "currency": "EUR"
}
