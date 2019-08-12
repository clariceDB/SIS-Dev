from datetime import datetime

from odoo import models, fields, api


class Student(models.Model):

    _name = 'sis.student'
    _description = 'student model'

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

    name = fields.Char(string='Name', required=True)
    surname = fields.Char(string='Surname', required=True)
    dob = fields.Date('Date of Birth')

    # age = fields.Date(compute='calculate_age')

    id = fields.Integer(string='ID', required=True)
    password = fields.Char(string='Password', required=True)

    # programme = fields.Selection([
    #     ('CS', 'Computer Science'),
    #     ('ISM', 'Information Management Science'),
    #     ('AM', 'Applied Maths'),
    #     ('BM', 'Business Management')
    # ])  # this is temp. Eventually link to programme model

    programme = fields.Many2one('sis.programme')

    current_year = fields.Integer(string='Current Year', required=True)
    transcript = fields.Binary(string='Transcript')

    address = fields.Char(string='Address')
    phone = fields.Char(string='Phone')
    email = fields.Char(string='email')

    highest_qualification = fields.Selection([
        ('matric', 'Matric Certificate'),
        ('bachelors', 'Bachelors')
    ])

    school = fields.Char(string='School')
