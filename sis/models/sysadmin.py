from odoo import models, fields, api
import time


class SysAdmin(models.Model):
    _name = 'sis.sysadmin'
    _description = 'System admin model'

    @api.multi
    def _get_year(self):
        # prefetch
        year = time.strftime('%Y')
        self.current_year = str(year)

    name = fields.Char(string='Name', required=True)
    surname = fields.Char(string='Surname', required=True)
    id = fields.Integer(string='ID', required=True)
    password = fields.Char(string='Password', required=True)
    current_year = fields.Char(compute=_get_year, store=True)

    @api.depends('current_year')
    @api.multi
    def rollover_year(self):
        # data = {d['id']: d['current_year']
        #         for d in self.read(['current_year'])}
        current_year_int = int(self.current_year)
        current_year_int = current_year_int + 1
        self.current_year = str(current_year_int)



