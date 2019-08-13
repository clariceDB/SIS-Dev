from odoo import models, fields, api
import random


class Application(models.Model):

    def _make_unique(self):
        print('##########################')
        r = random.randint(1, 101)
        unique = self.firstname+self.surname+str(r)
        print(unique)
        return unique

    _name = 'sis.application'
    _description = 'application model'

    firstname = fields.Char(string='FName', required=True)
    surname = fields.Char(string='Surname', required=True)
    unique = fields.Char(compute=_make_unique, string="")
    # unique = make_unique()
    dob = fields.Date('Date of Birth')
    state = fields.Boolean(string='Accepted', default=False)

    id = fields.Integer(string='ID', required=True)
    password = fields.Char(string='Password', required=True)

    programme = fields.Many2one('sis.programme')

    current_year = fields.Integer(string='Current Year', required=True, default=1)
    transcript = fields.Binary(string='Transcript')

    address = fields.Char(string='Address')
    phone = fields.Char(string='Phone')
    email = fields.Char(string='email', required=True)

    highest_qualification = fields.Selection([
        ('matric', 'Matric Certificate'),
        ('bachelors', 'Bachelors')
    ])

    school = fields.Char(string='School')



    # @api.model
    # def create(self, values):
    #     res = super(Application, self).create(values)
    #     # self.state = True
    #     x = self.create_application()
    #     return res
    #
    # @api.multi
    # def create_student(self):
    #     x = self.env['res.users'].create({'name':self.unique, 'email':self.email, 'login':self.email, 'new_password':self.password})
    #     group = self.env.ref('sis.student')
    #     group.write({'users': [(4, self._uid)]})