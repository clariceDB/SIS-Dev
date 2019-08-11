# -*- coding: utf-8 -*-

from odoo import models, fields, api

class sis(models.Model):
    _name = 'sis.sis'
    _description = 'Student Information Service'

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)

    @api.depends('value')
    def _value_pc(self):
        self.value2 = float(self.value) / 100