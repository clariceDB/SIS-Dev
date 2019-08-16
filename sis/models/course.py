from odoo import models, fields


class Course(models.Model):
    """Model used to create courses"""
    _name = 'sis.course'
    _description = 'course model'
    _rec_name = 'name'

    name = fields.Char(string='Name', required=True)
    id = fields.Integer(string='ID', required=True)
    credits = fields.Integer(string='Credits', required=True)
    year = fields.Integer(string='Year', required=True)
    # students = fields.

    department = fields.Many2one('sis.department')
