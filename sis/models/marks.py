from odoo import models, fields, api
from . import globals


class Marks(models.Model):
    """The marks model is used to map students results to the particular student"""
    _name = 'sis.marks'
    _description = 'Marks model'
    _rec_name = 'course_name'

    @api.multi
    def _get_current_user(self):
        """Method for traversing through records to find the current user"""
        for record in self:
            record.current_user = self.env.user

    student = fields.Char(string='student id')
    course_id = fields.Char(string='Course ID')
    course_year = fields.Char(string='Course year')
    course_name = fields.Char(string='Course Name')
    course_credits = fields.Char(string="Course Credits")
    department = fields.Char(string='Department')
    result = fields.Integer(string='Result')
    course = fields.Many2one(comodel_name='sis.course')
    student_year = fields.Char(string="Student Year")

    current_user = fields.Many2one('res.users', compute=_get_current_user)




