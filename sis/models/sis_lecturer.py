from odoo import models, fields, api

from . import globals


class Lecturer(models.Model):

    _name = 'sis.lecturer'
    _description = 'lecturer model'

    name = fields.Char(string='Name', required=True)
    surname = fields.Char(string='Surname', required=True)
    id = fields.Integer(string='ID') #ID is done by the system
    email = fields.Char(string='Email', required=True)
    password = fields.Char('Password', required=True)
    level = fields.Char(string='Level')
    department = fields.Many2one('sis.department')

    test = fields.Char(default=globals.Globals.get_year('a'), string='year', readonly=True)

    @api.multi
    def make_lec(self):
        # MAKE USER
        res = self.env['res.users'].create({'name': self.name,
                                            'email': self.email,
                                            'login': self.email,
                                            'new_password': self.password})

        # Assign the group
        lecturer_group = self.env.ref('sis.lecturer_group')
        res.groups_id = lecturer_group
