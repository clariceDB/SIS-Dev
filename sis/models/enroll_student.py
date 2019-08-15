from odoo import models, fields, api


class Enroll_Student(models.Model):
    ''' Accepting student applications and creating student users '''

    _name = "sis.enroll"
    _description = "Enroll Student"

