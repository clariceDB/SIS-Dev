from odoo import models, fields, api
import random


class Application(models.Model):
    _name = 'sis.application'
    _description = 'application model'

    name = fields.Char(string='Name', required=True)
    surname = fields.Char(string='Surname', required=True)
    dob = fields.Date('Date of Birth')
    gender = fields.Selection([
        ('M', 'Male'),
        ('F', 'Female')
    ])
    id = fields.Integer(string='ID', required=True)
    password = fields.Char(string='Password', required=True)

    programme = fields.Many2one('sis.programme', required=True)

    # programme = fields.Selection([
    #     ('BSc', 'Science'),
    #     ('BAcc', 'Accounting'),
    # ])

    transcript = fields.Binary(string='Transcript')
    address = fields.Char(string='Address')
    phone = fields.Char(string='Phone')
    email = fields.Char(string='Email', required=True)
    highest_qualification = fields.Selection([
        ('matric', 'Matric Certificate'),
        ('bachelors', 'Bachelors'),
        ('postgrad', 'Postgraduate'),
    ])
    prev_school = fields.Char(string='School')
    status = fields.Boolean(default=False)

    def _make_unique(self):
        print('##########################')
        r = random.randint(1, 101)
        unique = self.firstname+self.surname+str(r)
        print(unique)
        return unique

