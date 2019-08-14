from odoo import models, fields, api

from . import globals

class Marks(models.Model):
    _name = 'sis.marks'
    _description = 'Marks model'
    _rec_name = 'course'


    @api.multi
    def _test_method(self):
        print('*****************************')
        print(self.current_year)
        return '1'

    student = fields.Many2one('sis.student')
    result = fields.Integer(string='Result')
    course = fields.Many2one(comodel_name='sis.course')

    # department = self.

    #res = Super.(Class_name,Self).create(vals)
    #res is your new record id



