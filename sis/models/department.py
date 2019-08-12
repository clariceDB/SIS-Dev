from odoo import models, fields


class Department(models.Model):

    _name = 'sis.department'
    _description = 'department'
    department = fields.Selection([
        ('ISM', 'Information Systems Management'),
        ('CS', 'Computer Science'),
        ('Log', 'Logistics'),
        ('AP', 'Applied Mathematics'),
        ('Psy', 'Psychology'),
        ('Math', 'Mathematics'),
    ])

