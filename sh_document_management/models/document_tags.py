# -*- coding: utf-8 -*-
# Part of Softhealer Technologies.

from odoo import models, fields, api
import random


class DocumentTags(models.Model):
    _name = 'document.tags'
    _description = 'Document Tags'
    _rec_name = 'name'

    name = fields.Char('Name', required=True)
    color = fields.Integer(string='Color Index')

    @api.model
    def create(self, vals):
        res = super(DocumentTags, self).create(vals)
        number = random.randrange(1, 10)
        res.color = number
        return res
