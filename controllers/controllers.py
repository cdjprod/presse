# -*- coding: utf-8 -*-
from odoo import http

# class Presse(http.Controller):
#     @http.route('/presse/presse/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/presse/presse/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('presse.listing', {
#             'root': '/presse/presse',
#             'objects': http.request.env['presse.presse'].search([]),
#         })

#     @http.route('/presse/presse/objects/<model("presse.presse"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('presse.object', {
#             'object': obj
#         })