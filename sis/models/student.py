from odoo import models, fields


class Student(models.Model):

    _name = 'sis.student'
    _description = 'student model'
    name = fields.Char(string='Name', required=True)
    surname = fields.Char(string='Surname', required=True)
    id = fields.Integer(string='ID', required=True)
    password = fields.Char(string='Password', required=True)
    programme = fields.Selection([
        ('CS', 'Computer Science'),
        ('ISM', 'Information Management Science'),
        ('AM', 'Applied Maths'),
        ('BM', 'Business Management')
    ])  # this is temp. Eventually link to programme model
    # programme = fields.Many2one(comodal_name='programme', string='programme'
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
