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

