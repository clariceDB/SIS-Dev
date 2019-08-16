from odoo import models, fields, api
import time
from . import globals


class SysAdmin(models.Model):
    """The system admin model is used to create the system user and define methods accessible by the user"""
    _name = 'sis.sysadmin'
    _description = 'System admin model'

    @api.multi
    def _get_year(self):
        """Return the current year"""
        current_year = globals.Globals.get_year()
        return current_year

    name = fields.Char(string='Name', required=True)
    surname = fields.Char(string='Surname')
    email = fields.Char(string='Email', required=True)
    id = fields.Integer(string='ID', required=True)
    password = fields.Char(string='Password', required=True)
    current_year = fields.Char(default=globals.Globals.get_year('a'), string='Year', readonly=True)
    userid = fields.Char(default="no id", string='UserID', readonly=True)

    @api.depends('current_year')
    @api.multi
    def rollover_year(self):
        """This method changes the year from one year to the next. It rolls students over to the next academic year."""
        # data = {d['id']: d['current_year']
        #         for d in self.read(['current_year'])}
        current_year_int = int(self.current_year)
        current_year_int = current_year_int + 1
        self.current_year = str(current_year_int)

        globals.year = int(globals.year) + 1

        stage = self.env['sis.student'].search([])

        for record in stage:
            record.current_year = int(record.current_year) + 1


    @api.multi
    def make_sysadmin(self):
        """Create the system administrator user"""
        # MAKE USER
        res = self.env['res.users'].create({'name': self.name,
                                            'email': self.email,
                                            'login': self.email,
                                            'new_password': self.password})

        self.userid = res.id
        # Assign the group
        sysadmin_group = self.env.ref('sis.sys_admin_group')
        res.groups_id = sysadmin_group



