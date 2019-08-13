from odoo import models, fields


class Course(models.Model):
    _name = 'sis.course'
    _description = 'course model'
    _rec_name = 'name'

    name = fields.Char(string='Name', required=True)
    id = fields.Integer(string='ID', required=True)
    credits = fields.Integer(string='Credits', required=True)
    level = fields.Integer(string='Level', required=True)
    # students = fields.

    department = fields.Many2one('sis.department')
