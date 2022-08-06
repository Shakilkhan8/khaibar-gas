# -*- coding: utf-8 -*-
# Part of Softhealer Technologies.

from odoo import models, fields, api, _
import random


class Directory(models.Model):
    _name = 'document.directory'
    _description = 'Document Directory'
    _rec_name = 'name'

    sequence = fields.Integer(string="Sequence")
    name = fields.Char(string='Name', required=True)
    image_medium = fields.Binary('Image')
    image_small = fields.Binary(
        "Small-sized image", attachment=True,
        help="Small-sized image of the product. It is automatically "
             "resized as a 64x64px image, with aspect ratio preserved. "
             "Use this field anywhere a small image is required.")
    file_count = fields.Integer('Files', compute='_compute_file_counts')
    sub_directory_count = fields.Integer(
        'Sub Directories', compute='_compute_sub_directory_count')
    parent_id = fields.Many2one('document.directory', 'Parent Directory')
    visible_directory = fields.Boolean('Visible Directory')
    directory_tag_ids = fields.Many2many(
        'directory.tags', string='Diractory Tags')
    attachment_ids = fields.One2many(
        'ir.attachment', 'directory_id', string="Files")
    directory_ids = fields.Many2many(
        'document.directory', string="Sub Directories", compute='_compute_sub_directory_count')
    files = fields.Integer(string="Files", compute='_compute_file_counts_btn')
    sub_directories = fields.Integer(
        string="Sub Directories", compute='_compute_sub_directory_count_btn')
    color = fields.Integer(string='Color Index')
    company_id = fields.Many2one(
        'res.company', string='Company', default=lambda self: self.env.company)

    @api.model
    def create(self, values):
        sequence = self.env['ir.sequence'].next_by_code('document.directory')
        number = random.randrange(1, 10)
        values['sequence'] = sequence
        values['color'] = number
        return super(Directory, self).create(values)

    def _compute_file_counts(self):
        if self:
            for rec in self:
                ir_attachment_ids = self.env['ir.attachment'].sudo().search(
                    [('directory_id', '=', rec.id)])
                if ir_attachment_ids:
                    rec.file_count = len(ir_attachment_ids.ids)
                else:
                    rec.file_count = 0

    def _compute_sub_directory_count(self):
        if self:
            for rec in self:
                sub_directory_ids = self.env['document.directory'].sudo().search(
                    [('parent_id', '=', rec.id)])
                if sub_directory_ids:
                    rec.sub_directory_count = len(sub_directory_ids.ids)
                    rec.directory_ids = [(6, 0, sub_directory_ids.ids)]
                else:
                    rec.sub_directory_count = 0
                    rec.directory_ids = False

    def _compute_file_counts_btn(self):
        if self:
            for rec in self:
                ir_attachment_ids = self.env['ir.attachment'].sudo().search(
                    [('directory_id', '=', rec.id)])
                if ir_attachment_ids:
                    rec.files = len(ir_attachment_ids.ids)
                else:
                    rec.files = 0

    def _compute_sub_directory_count_btn(self):
        if self:
            for rec in self:
                sub_directory_ids = self.env['document.directory'].sudo().search(
                    [('parent_id', '=', rec.id)])
                if sub_directory_ids:
                    rec.sub_directories = len(sub_directory_ids.ids)
                else:
                    rec.sub_directories = 0

    def action_view_sub_directory(self):
        if self:
            for rec in self:
                return {
                    'name': _('Sub Directories'),
                    'type': 'ir.actions.act_window',
                    'res_model': 'document.directory',
                    'view_type': 'form',
                    'view_mode': 'kanban,tree,form',
                    'domain': [('parent_id', '=', rec.id)],
                    'target': 'current'
                }

    def action_view_files(self):
        if self:
            for rec in self:
                return {
                    'name': _('Files'),
                    'type': 'ir.actions.act_window',
                    'res_model': 'ir.attachment',
                    'view_type': 'form',
                    'view_mode': 'kanban,tree,form',
                    'domain': [('directory_id', '=', rec.id)],
                    'target': 'current'
                }

    def action_view(self):
        if self:
            return {
                'name': _('Files'),
                'type': 'ir.actions.act_window',
                        'res_model': 'ir.attachment',
                        'view_type': 'form',
                        'view_mode': 'kanban,tree,form',
                        'domain': [('directory_id', '=', self.id)],
                        'target': 'current'
            }
