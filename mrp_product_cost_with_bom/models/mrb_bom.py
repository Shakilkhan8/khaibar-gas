# -*- coding: utf-8 -*-

from odoo import api, fields, models


class MrpBom(models.Model):
    _inherit = 'mrp.bom'

    @api.depends('bom_line_ids.sub_total', 'product_qty')
    def _amount_all(self):
        for order in self:
            order.total = sum([line.sub_total for line in order.bom_line_ids])
            order.single_unit_cost_in_bom = order.total / order.product_qty

    single_unit_cost_in_bom = fields.Monetary(
        "BOM Cost per Unit", compute='_amount_all')
    currency_id = fields.Many2one(
        'res.currency', string='Currency', required=True,
        default=lambda self: self.env.user.company_id.currency_id)
    total = fields.Monetary("Total", compute='_amount_all', readonly=True, store=True)


class MrpBomLine(models.Model):
    _inherit = 'mrp.bom.line'

    @api.depends('product_qty', 'cost', 'product_id')
    def _compute_subtotal(self):
        for line in self:
            line.sub_total = line.product_qty * line.cost
            line.cost = line.product_id.standard_price

    cost = fields.Float("Cost")
    sub_total = fields.Monetary(compute='_compute_subtotal',
                             string="Sub Total", readonly=True)
    currency_id = fields.Many2one(
        'res.currency', string='Currency', required=True,
        default=lambda self: self.env.user.company_id.currency_id)
