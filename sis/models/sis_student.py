from datetime import datetime
from odoo import models, fields, api
import random


class Student(models.Model):

    _name = 'sis.student'
    _description = 'student model'

    name = fields.Char(string='Name',
                       required=True)
    surname = fields.Char(string='Surname', required=True)

    state = fields.Boolean(string='Accepted', default=False)
    unique = fields.Char(string='Student Number')

    dob = fields.Date('Date of Birth')

    id = fields.Integer(string='ID')
    password = fields.Char(string='Password', required=True)

    programme = fields.Char(string='Programme Name')

    current_year = fields.Integer(string='Current Year', required=True, default=1, readonly=True)
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

