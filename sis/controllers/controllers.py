# -*- coding: utf-8 -*-
from odoo import http

# class Sis(http.Controller):
#     @http.route('/sis/sis/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sis/sis/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('sis.listing', {
#             'root': '/sis/sis',
#             'objects': http.request.env['sis.sis'].search([]),
#         })

#     @http.route('/sis/sis/objects/<model("sis.sis"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sis.object', {
#             'object': obj
#         })