from odoo import models, fields, api
from datetime import date
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
    unique = fields.Char(compute=_make_unique, String='unique')
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


    @ api.multi
    def enroll_student(self):
        self.env['sis.student'].create({
            'name': self.name,
            'surname': self.surname,
            'dob': self.dob,
            'unique': self.unique,
            'id': self.id,
            'password': self.password,
            'programme': self.programme,
            'current_year': self.current_year,
            'transcript': self.transcript,
            'address': self.address,
            'phone': self.phone,
            'email': self.email,
            'highest_qualification': self.highest_qualification,
            'school': self.school
        })
        res = self.env["res.users"].create({'name': self.name,
                                            'email': self.email,
                                            'login': self.email,
                                            'new_password': self.password})

        student_group = self.env.ref('sis.student_group')
        res.groups_id = student_group

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
            rec.write({'status': 'declined'})

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

def _make_unique(self):
    print('##########################')
    r = random.randint(1, 101)
    unique = self.firstname + self.surname + str(r)
    print(unique)
    return unique






