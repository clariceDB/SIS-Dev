from odoo import models, fields, api
import random
from datetime import date


class Application(models.Model):
    _name = 'sis.application'
    _description = 'application model'

    def _make_unique(self):
        print('##########################')
        r = random.randint(1, 101)
        unique = self.name + self.surname + str(r)
        print(unique)
        return unique

    name = fields.Char(string='Name', required=True)
    surname = fields.Char(string='Surname', required=True)
    dob = fields.Date('Date of Birth')
    gender = fields.Selection([
        ('M', 'Male'),
        ('F', 'Female')
    ])

    password = fields.Char(string='Password', required=True)
    current_year = date.today().year
    programme = fields.Many2one('sis.programme', required=True)
    unique = fields.Char(compute = _make_unique, String = 'unique')
    transcript = fields.Binary(string='Transcript')
    address = fields.Char(string='Address')
    phone = fields.Char(string='Phone')
    email = fields.Char(string='Email', required=True)
    highest_qualification = fields.Selection([
        ('matric', 'Matric Certificate'),
        ('bachelors', 'Bachelors'),
        ('postgrad', 'Postgraduate'),
    ])
    school = fields.Char(string='School/Academic Institution')

    status = fields.Selection([('pending', 'Pending'),
                               ('accepted', 'Accepted'),
                               ('declined', 'Declined')],
                              default='pending')

    email_status = fields.Selection([('notsent', 'Not Sent'),
                                     ('sent', 'Sent')],
                                    default='notsent')

    @api.multi
    def button_accept(self):
        for rec in self:
            rec.write({'status': 'accepted'})


    @api.multi
    def button_declined(self):
        for rec in self:
            rec.write({'status': 'declined'})

    @api.one
    def send_accept_mail(self):
        message_body = "<h1>You are a TWAT</h1>>"

        template_obj = self.env['mail.mail']
        template_data = {
            'subject': self.name,
            'body_html': message_body,
            'email_from': 'info.capewinelandscollege@gmail.com',
            'email_to': self.email
        }
        template_id = template_obj.create(template_data)
        template_obj.send(template_id)
        for rec in self:
            rec.write({'email_status': 'sent'})



    @api.one
    def send_decline_mail(self):
        message_body = "<h1>You are a TWAT</h1>>"

        template_obj = self.env['mail.mail']
        template_data = {
            'subject': self.name,
            'body_html': message_body,
            'email_from': 'info.capewinelandscollege@gmail.com',
            'email_to': self.email
        }
        template_id = template_obj.create(template_data)
        template_obj.send(template_id)
        for rec in self:
            rec.write({'email_status': 'sent'})


def _make_unique(self):
    print('##########################')
    r = random.randint(1, 101)
    unique = self.firstname + self.surname + str(r)
    print(unique)
    return unique


    @api.multi
    def button_declined(self):
        for rec in self:
            rec.write({'status': 'declined'})




