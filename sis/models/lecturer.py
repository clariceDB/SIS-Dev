from odoo import models, fields


class Lecturer(models.Model):

    _name = 'sis.lecturer'
    _description = 'lecturer model'
    name = fields.Char(string='Name', required=True)
    surname = fields.Char(string='Surname', required=True)
    id = fields.Integer(string='ID', required=True)
    password = fields.Char(string='Password', required=True)
    level = fields.Char(string='Level', required=True)
    department = fields.Many2one('sis.department')
