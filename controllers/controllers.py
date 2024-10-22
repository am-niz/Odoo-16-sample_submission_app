# -*- coding: utf-8 -*-
# from odoo import http


# class SampleSubmissionApp(http.Controller):
#     @http.route('/sample_submission_app/sample_submission_app', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sample_submission_app/sample_submission_app/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('sample_submission_app.listing', {
#             'root': '/sample_submission_app/sample_submission_app',
#             'objects': http.request.env['sample_submission_app.sample_submission_app'].search([]),
#         })

#     @http.route('/sample_submission_app/sample_submission_app/objects/<model("sample_submission_app.sample_submission_app"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sample_submission_app.object', {
#             'object': obj
#         })
