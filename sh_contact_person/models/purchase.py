# -*- coding: utf-8 -*-
# Part of Softhealer Technologies.

from odoo import models, fields, api


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    contact_person_id = fields.Many2one(
        'res.partner',
        string="Contact Person"
    )

    @api.onchange('partner_id')
    def sh_onchange_partner_id(self):
        self.contact_person_id = False
