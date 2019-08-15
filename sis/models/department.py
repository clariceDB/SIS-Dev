from odoo import models, fields


class Department(models.Model):
    _name = 'sis.department'
    _description = 'department'
    _rec_name = 'department'

    department = fields.Selection([
        ('Information Systems Management', 'Information Systems Management'),
        ('Computer Science', 'Computer Science'),
        ('Logistics', 'Logistics'),
        ('Applied Mathematics', 'Applied Mathematics'),
        ('Psychology', 'Psychology'),
        ('Mathematics', 'Mathematics'),
    ])

    lecturers = fields.One2many(comodel_name='sis.lecturer', inverse_name='department', string="Lecturers", readonly=True, copy=True)
    courses = fields.One2many(comodel_name='sis.course', inverse_name='department', string="Courses", readonly=True, copy=True)

