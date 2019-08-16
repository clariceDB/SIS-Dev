from odoo import models, fields, api
import random
import math
from datetime import date


class Application(models.Model):
    """"Model to process the application form of prospective students"""
    _name = 'sis.application'
    _description = 'application model'

    # Student-t random number generator
    def student_t(self, nu):  # nu equals number of degrees of freedom
        x = random.gauss(0.0, 1.0)
        y = 2.0 * random.gammavariate(0.5 * nu, 2.0)
        z = x / (math.sqrt(y / nu))
        w = round(abs(z * 1000000))
        return w

    # Takes first and last name
    def make_random(self):
        for rec in self:
            one = rec.name[0:2]
            two = rec.surname[0:2]
            three = str(rec.student_t(5))
            uniq = one + two + three
            rec.unique = uniq[0:9]

    name = fields.Char(string='Name', required=True)
    surname = fields.Char(string='Surname', required=True)
    dob = fields.Date('Date of Birth')
    gender = fields.Selection([
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other')
    ])

    password = fields.Char(string='Password', required=True)
    current_year = date.today().year
    programme = fields.Many2one('sis.programme', required=True)
    unique = fields.Char(compute=make_random, string='Student Number')
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
                              default='pending', readonly=True)

    email_status = fields.Selection([('notsent', 'Not Sent'),
                                     ('sent', 'Sent')],
                                    default='notsent', readonly=True)

    @api.multi
    def button_accept(self):
        for rec in self:
            rec.write({'status': 'accepted'})
        self.env['sis.student'].create({
            'name': self.name,
            'surname': self.surname,
            'dob': self.dob,
            'unique': self.unique,
            'id': self.id,
            'password': self.password,
            'programme_name': self.programme.name,
            'current_year': self.current_year,
            'transcript': self.transcript,
            'address': self.address,
            'phone': self.phone,
            'email': self.email,
            'highest_qualification': self.highest_qualification,
            'school': self.school,
        })

        res = self.env["res.users"].create({'name': self.name,
                                            'email': self.email,
                                            'login': self.email,
                                            'new_password': self.password})

        student_group = self.env.ref('sis.student_group')
        res.groups_id = student_group

        for i in range(0, len(self.programme.courses)):
            course_name = self.programme.courses[i].course_name
            course_id = self.programme.courses[i].id
            course_credits = self.programme.courses[i].credits
            course_year = self.programme.courses[i].year
            department = self.programme.courses[i].department
            self.env['sis.marks'].create({
                'student': self.unique,
                'course_id': course_id,
                'course_name': course_name,
                'course_credits': course_credits,
                'course_year': course_year,
                'department': department,
                'student_year': self.current_year
            })

    @api.multi
    def button_declined(self):
        for rec in self:
            rec.write({'status': 'declined'})


    @api.one
    def send_accept_mail(self):
        message_body = "Congratulations!"
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


