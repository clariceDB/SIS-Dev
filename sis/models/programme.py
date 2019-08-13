from odoo import models, fields


class Programme(models.Model):
    _name = 'sis.programme'
    _description = 'programme model'

    name = fields.Char(string='Name', required=True)
    id = fields.Integer(string='ID', required=True)
    credits = fields.Integer(string='Credits', required=True)

    designation = fields.Selection([  # Needs to handle postgrad as well
        ('BComm', 'Bachelors in Commerce'),
        ('BSc', 'Bachelors in Science'),
        ('BAcc', 'Bachelors in Accounting'),
        ('BEng', 'Bachelors in Engineering'),
        ('BA', 'Bachelors in Art'),
        ('BEd', 'Bachelors in Education'),
    ])

    #courses = fields.Many2many('sis.course')

    level = fields.Selection([
        ('Test', 'Undergraduate Programme'),
        ('Test2', 'Postgraduate Programme'),
    ])

    # courses =
    # students = fields.Many2many('sis.students')
