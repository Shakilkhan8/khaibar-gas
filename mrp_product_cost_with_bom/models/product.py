# -*- coding: utf-8 -*-

from odoo import api, fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    @api.depends('bom_ids', 'bom_ids.single_unit_cost_in_bom')
    def _compute_cost_included_bom(self):
        for res in self:
            if res.bom_ids:
                res.cost_included_bom = res.bom_ids[-1].single_unit_cost_in_bom
            else:
                res.cost_included_bom = 0.0

    cost_included_bom = fields.Float("Cost Price (as per BoM)", compute='_compute_cost_included_bom')


class ProductProduct(models.Model):
    _inherit = "product.product"

    @api.depends('bom_ids', 'bom_ids.single_unit_cost_in_bom')
    def _compute_cost_included_bom(self):
        for res in self:
            bom_id = self.env['mrp.bom'].search([('product_id', '=', res.id)], order="id desc", limit=1)
            if bom_id:
                res.cost_included_bom = bom_id.single_unit_cost_in_bom
            else:
                res.cost_included_bom = 0.0

    cost_included_bom = fields.Float("Cost Price (as per BoM)", compute='_compute_cost_included_bom')
