from odoo import models, fields, api


class Marks(models.Model):
    _name = 'sis.marks'
    _description = 'Marks model'
    _rec_name = 'course'

    student = fields.Many2one('sis.student')
    result = fields.Integer(string='Result')
    course = fields.Many2one(comodel_name='sis.course')

    # department = self.

    #res = Super.(Class_name,Self).create(vals)
    #res is your new record id


