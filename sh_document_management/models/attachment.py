# -*- coding: utf-8 -*-
# Part of Softhealer Technologies.

from odoo import models, fields, api
import random


class Attachment(models.Model):
    _inherit = 'ir.attachment'

    directory_id = fields.Many2one('document.directory', string='Directory')
    document_tags = fields.Many2many('document.tags', string='Document Tags')
    color = fields.Integer(string='Color Index')

    @api.model
    def create(self, values):
        number = random.randrange(1, 10)
        values['color'] = number
        return super(Attachment, self).create(values)
