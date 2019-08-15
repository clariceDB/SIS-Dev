from odoo import models, fields, api
import random
from odoo.exceptions import ValidationError
import re
from . import programme

EM = (r"[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$")


def emailvalidation(email):
    if email:
        EMAIL_REGEX = re.compile(EM)
        if not EMAIL_REGEX.match(email):
            raise ValidationError(_('''This seems not to be valid email.
            Please enter email in correct format!'''))
        else:
            return True


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

    password = fields.Char(string='Password', required=True)

    programme = fields.Many2one('sis.programme', required=True)

    transcript = fields.Binary(string='Transcript')
    address = fields.Char(string='Address')
    phone = fields.Char(string='Phone')
    email = fields.Char(string='Email', required=True)
    highest_qualification = fields.Selection([
        ('matric', 'Matric Certificate'),
        ('bachelors', 'Bachelors'),
        ('postgrad', 'Postgraduate'),
    ])
    prev_school = fields.Char(string='School/Academic Institution')

    status = fields.Selection([('pending', 'Pending'),
                               ('accepted', 'Accepted'),
                               ('declined', 'Declined')],
                              default='pending')

    @api.multi
    def button_accept(self):
        for rec in self:
            rec.write({'status': 'accepted'})


    @api.multi
    def button_declined(self):
        for rec in self:
            rec.write({'status': 'declined'})

    def _make_unique(self):
        print('##########################')
        r = random.randint(1, 101)
        unique = self.firstname + self.surname + str(r)
        print(unique)
        return unique
