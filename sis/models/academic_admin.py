from odoo import models, fields


class AcademicAdmin(models.Model):
    """Model for the academic admin of the institution"""

    _name = 'sis.academicadmin'
    _description = 'academic admin model'
    name = fields.Char(string='Name', required=True)
    surname = fields.Char(string='Surname', required=True)
    id = fields.Integer(string='ID', required=True)
    password = fields.Char(string='Password', required=True)
    department = fields.Many2one('sis.department')
