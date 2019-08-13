from datetime import datetime
from odoo import models, fields, api
import random


class Student(models.Model):

    # _inherit = 'sis_student'

    def _make_unique(self):
        r = random.randint(1, 101)
        unique = self.firstname+self.surname+str(r)
        print(unique)
        return unique

    _name = 'sis.student'
    _description = 'student model'

    firstname = fields.Char(string='Name', required=True)
    surname = fields.Char(string='Surname', required=True)
    dob = fields.Date('Date of Birth')
    state = fields.Boolean(string='Accepted', default=False)
    unique = fields.Char(compute=_make_unique)

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

    current_year = fields.Integer(string='Current Year', required=True, default=1)
    transcript = fields.Binary(string='Transcript')

    address = fields.Char(string='Address')
    phone = fields.Char(string='Phone')
    email = fields.Char(string='email', required=True)

    highest_qualification = fields.Selection([
        ('matric', 'Matric Certificate'),
        ('bachelors', 'Bachelors')
    ])

    school = fields.Char(string='School')

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


    @api.model
    def create(self, vals):

        res = super(Student, self).create(vals)
        self.env['res.users'].create({
            'name':vals['firstname'],
            'email':vals['email'],
            'login':vals['email'],
            'new_password':vals['password']
        })
        return res

    # @api.model
    # def create(self, vals):
    #     # cr, uid, vals, context = self
    #     # Your logic goes here or call your method
    #     res_id = super(Student, self).create(vals)
    #     self.env['res.users'].create({'name':self.unique, 'email':self.email, 'login':self.email, 'new_password':self.password})
    #     return res_id

    # @api.model
    # def create(self, values):
    #     res = super(Student, self).create(values)
    #     # self.state = True
    #     self.env['res.users'].create({'name':self.unique, 'email':self.email, 'login':self.email, 'new_password':self.password})
    #     group = self.env.search([('name', '=', 'student_group')])
    #     group.write({'users': [(4, self._uid)]})
    #     return res

    # @api.multi
    # def create_student(self):
    #     x = self.env['res.users'].create({'name':self.unique, 'email':self.email, 'login':self.email, 'new_password':self.password})
    #     group = self.env.search([('name', '=', 'student_group')])
    #     group.write({'users': [(4, self._uid)]})

    # def set_student_group(self, user_id):
    #     group = self.env.ref('sis.student')
    #     group.write({'users': [(4, user_id)]})