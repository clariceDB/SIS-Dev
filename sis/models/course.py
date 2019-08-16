from odoo import models, fields


class Course(models.Model):
    """Model used to create courses"""

    _name = 'sis.course'
    _description = 'course model'
    _rec_name = 'course_name'

    course_name = fields.Char(string='Name', required=True)
    id = fields.Integer(string='ID')
    credits = fields.Integer(string='Credits')
    year = fields.Integer(string='Year')
    student_id = fields.Char(string='student id')
    department = fields.Char(string="Department")
