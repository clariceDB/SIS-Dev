from odoo import models, fields


class AcademicAdmin(models.Model):

    _name = 'sis.academicadmin'
    _description = 'academic admin model'
    name = fields.Char(string='Name', required=True)
    surname = fields.Char(string='Surname', required=True)
    id = fields.Integer(string='ID', required=True)
    password = fields.Char(string='Password', required=True)
    department = fields.Char(string='Department', required=True)
