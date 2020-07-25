# -*- coding: utf-8 -*-
from odoo import http

# class Mustafa(http.Controller):
#     @http.route('/mustafa/mustafa/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/mustafa/mustafa/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('mustafa.listing', {
#             'root': '/mustafa/mustafa',
#             'objects': http.request.env['mustafa.mustafa'].search([]),
#         })

#     @http.route('/mustafa/mustafa/objects/<model("mustafa.mustafa"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('mustafa.object', {
#             'object': obj
#         })