from odoo import models, fields, api
import time
from . import globals
from . import sis_student


class SysAdmin(models.Model):
    _name = 'sis.sysadmin'
    _description = 'System admin model'

    @api.multi
    def _get_year(self):
        current_year = globals.Globals.get_year()
        return current_year

    name = fields.Char(string='Name', required=True)
    surname = fields.Char(string='Surname', required=True)
    id = fields.Integer(string='ID', required=True)
    password = fields.Char(string='Password', required=True)
    current_year = fields.Char(default=globals.Globals.get_year('a'), string='Year', readonly=True)

    @api.depends('current_year')
    @api.multi
    def rollover_year(self):
        # data = {d['id']: d['current_year']
        #         for d in self.read(['current_year'])}
        current_year_int = int(self.current_year)
        current_year_int = current_year_int + 1
        self.current_year = str(current_year_int)

        globals.year = int(globals.year) + 1

        stage = self.env['sis.student'].search([])

        for record in stage:
            record.current_year = int(record.current_year) + 1


    # @api.multi
    #     self.env['sis.student']



