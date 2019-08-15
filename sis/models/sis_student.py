from datetime import datetime
from odoo import models, fields, api
import random


class Student(models.Model):

    # _inherit = 'sis_student'

    @api.depends('name', 'surname')
    def _make_unique(self):
        r = random.randint(1, 101)
        unique = self.name+self.surname+str(r)
        print(unique)
        return unique

    _name = 'sis.student'
    _description = 'student model'

    name = fields.Char(string='Name',
                       required=True)
    surname = fields.Char(string='Surname', required=True)

    state = fields.Boolean(string='Accepted', default=False)
    unique = fields.Char(compute=_make_unique, readonly=True)

    # dob = fields.Date('Date of Birth')
    # age = fields.Date(compute='calculate_age')

    id = fields.Integer(string='ID')
    password = fields.Char(string='Password', required=True)

    programme = fields.Char(string='Programme Name')

    current_year = fields.Integer(string='Current Year', required=True, default=1, readonly=True)
    transcript = fields.Binary(string='Transcript')

    address = fields.Char(string='Address')
    phone = fields.Char(string='Phone')
    email = fields.Char(string='email', required=True)

    highest_qualification = fields.Selection([
        ('matric', 'Matric Certificate'),
        ('bachelors', 'Bachelors')
    ])

    school = fields.Char(string='School')

    userid = fields.Char(string='User ID', readonly=True)

    @api.depends('dob')
    def calculate_age(self):
        """ Description:- This method calculates the age on the basis of the
        Birth Date entered in the 'dob' field. """
        for data in self:
            if data.dob:
                current_year = datetime.datetime.now().year
                birth_year = datetime.datetime.strptime(data.dob, "%Y-%m-%d").year
                age = current_year - birth_year
                data.age = age