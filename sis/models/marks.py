from odoo import models, fields, api


class Marks(models.Model):
    _name = 'sis.marks'
    _description = 'Marks model'

    student = fields.Many2one('sis.student')
    result = fields.Integer(string='Result')
    course = fields.Many2one('sis.course')
