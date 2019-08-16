from datetime import datetime
from odoo import models, fields, api
import random


class Student(models.Model):

    # _inherit = 'sis_student'

    @api.depends('name', 'surname')
    def _make_unique(self):
        r = random.randint(1, 101)*100
        unique = self.name+self.surname+str(r)
        print(unique)
        return unique

    @api.depends('programme_name')
    def _get_programme(self):

        for rec in self:
            object = rec.env['sis.programme'].search([('name','=',rec.programme_name)])
            if object:
                rec.programme = object

        print('*^*^*^&*&*%&%&^*^*^*^*^')
        print(self.programme_name)
        print('***************************')
        print(object)
        print(object.name)



    _name = 'sis.student'
    _description = 'student model'

    name = fields.Char(string='Name',
                       required=True)
    surname = fields.Char(string='Surname', required=True)

    state = fields.Boolean(string='Accepted', default=False)
    unique = fields.Char( string='Student Number',readonly=True)

    dob = fields.Date('Date of Birth')

    id = fields.Integer(string='ID')
    password = fields.Char(string='Password', required=True)

    programme_name = fields.Char(string='Programme Name')
    # programme = fields.Many2one(compute="_get_programme", string='Programme')

    current_year = fields.Char(string='Current Year', required=True, default=1, readonly=True)
    transcript = fields.Binary(string='Transcript')

    address = fields.Char(string='Address')
    phone = fields.Char(string='Phone')
    email = fields.Char(string='Email', required=True)

    highest_qualification = fields.Selection([
        ('matric', 'Matric Certificate'),
        ('bachelors', 'Bachelors'),
        ('postgrad', 'Postgraduate'),
    ])
    school = fields.Char(string='School')

    userid = fields.Char(string='User ID', readonly=True)

