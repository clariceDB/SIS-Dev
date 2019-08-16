from odoo import models, fields, api

from . import globals

class Marks(models.Model):
    _name = 'sis.marks'
    _description = 'Marks model'

    @api.multi
    def _get_current_user(self):
        for record in self:
            record.current_user = self.env.user
        print('^^^^^^^^')
        print(record.current_user)
        # self.update({'current_user': self.env.user.id})

    @api.multi
    def _test_method(self):
        print('*****************************')
        print(self.current_year)
        return '1'

    student = fields.Char(string='student id')
    course_id = fields.Char(string='Course ID')
    course_year = fields.Char(string='Course year')
    course_name = fields.Char(string='Course Name')
    course_credits = fields.Char(string="Course Credits")
    department = fields.Char(string='Department')
    result = fields.Integer(string='Result')
    course = fields.Many2one(comodel_name='sis.course')

    current_user = fields.Many2one('res.users', compute=_get_current_user)
    # department = self.

    #res = Super.(Class_name,Self).create(vals)
    #res is your new record id



