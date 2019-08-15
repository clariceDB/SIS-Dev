from odoo import models, fields, api

from . import globals

class Marks(models.Model):
    _name = 'sis.marks'
    _description = 'Marks model'
    _rec_name = 'course'

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

    student = fields.Many2one('sis.student')
    userid = fields.Char(string='UserID')
    result = fields.Integer(string='Result')
    course = fields.Many2one(comodel_name='sis.course')

    current_user = fields.Many2one('res.users', compute=_get_current_user)
    # department = self.

    #res = Super.(Class_name,Self).create(vals)
    #res is your new record id



