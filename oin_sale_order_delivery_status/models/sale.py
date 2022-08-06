# -*- coding: utf-8 -*-
##############################################################################
#
# Copyright 2021 Odoo IT now <http://www.odooitnow.com/>
# See LICENSE file for full copyright and licensing details.
#
##############################################################################

from odoo import api, fields, models, _


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.depends('state', 'procurement_group_id')
    def _compute_order_status(self):
        for rec in self:
            if rec.picking_ids:
                states = rec.picking_ids.mapped('state')
                if all(state == 'done' for state in states):
                    rec.delivery_status = 'delivered'
                elif any(state == 'done' for state in states):
                    rec.delivery_status = 'partially_deliver'
                elif all(state == 'waiting' for state in states):
                    rec.delivery_status = 'processing'
                else:
                    rec.delivery_status = 'to_deliver'
            else:
                rec.delivery_status = 'nothing_to_deliver'

    delivery_status = fields.Selection([
        ('nothing_to_deliver', 'Nothing to Deliver'),
        ('to_deliver', 'To Deliver'),
        ('partially_deliver', 'Partially Deliver'),
        ('delivered', 'Delivered'),
        ('processing', 'Processing'),
        ], compute='_compute_order_status')
