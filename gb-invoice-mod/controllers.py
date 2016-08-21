# -*- coding: utf-8 -*-
from openerp import http

# class Gb-invoice-mod(http.Controller):
#     @http.route('/gb-invoice-mod/gb-invoice-mod/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/gb-invoice-mod/gb-invoice-mod/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('gb-invoice-mod.listing', {
#             'root': '/gb-invoice-mod/gb-invoice-mod',
#             'objects': http.request.env['gb-invoice-mod.gb-invoice-mod'].search([]),
#         })

#     @http.route('/gb-invoice-mod/gb-invoice-mod/objects/<model("gb-invoice-mod.gb-invoice-mod"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('gb-invoice-mod.object', {
#             'object': obj
#         })