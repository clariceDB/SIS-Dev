from odoo import models, fields, api


class Enroll_Student(models.Model):
    ''' Accepting student applications and creating student users '''

    _name = "sis.enroll"
    _description = "Enroll Student"

    @api.model
    def enroll_student(self):
        self.env['res.users'].create({
          'name': self._name,
          'surname': self.surname,
          'dob': self.dob,
          'unique': self.unique,
          'id': self.id,
          'password': self.password,
          'programme': self.programme,
          'current_year': self.current_year,
          'transcript': self.transcript,
          'address': self.address,
          'phone': self.phone,
          'email': self.email,
          'highest_qualification': self.highest_qualification,
          'school': self.school
          })
