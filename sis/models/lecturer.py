from odoo import models, fields, api


class Lecturer(models.Model):

    _name = 'sis.lecturer'
    _description = 'lecturer model'
    name = fields.Char(string='Name', required=True)
    surname = fields.Char(string='Surname', required=True)
    id = fields.Integer(string='ID', required=True)
    password = fields.Char('Password', required=True)
    level = fields.Char(string='Level', required=True)
    department = fields.Many2one('sis.department')

    partner_id = fields.Many2one(
        'res.partner',
        delegate=True,
        ondelete='cascade',
        required=True)

    @api.model
    def create(self, vals):
        # Create the user
        res = super(Lecturer, self).create(vals)
        self.env['res.users'].create({
            'name': vals['name'],
            'email': vals['email'],
            'login': vals['email'],
            'new_password': vals['password']
        })

        # Assign the group
        # self.assign_perms(res)
        # group = self.env.ref('student_group')
        # group.write({'users': [(4, self._uid)]})
        return res