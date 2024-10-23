# -*- coding: utf-8 -*-
{
    'name': "sample_submission_app",

    'summary': """
        Streamline sample submission management, connecting customers to submission forms, tracking materials, 
        generating invoices, and creating customizable PDF and Excel reports.""",

    'description': """
        The Sample Submission app enables efficient management of sample submissions, 
    linking customers to submission forms and tracking related materials as products. 

    This module is designed to simplify and organize sample submission processes, 
    enhancing productivity and accuracy.
    """,

    'author': "NIZAMUDHEEN MJ",
    'website': "https://github.com/am-niz",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base', "mail", "product", 'account', 'report_xlsx'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'data/ir_sequence_data.xml',
        'wizard/filter_invoice_wizard_views.xml',
        'wizard/material_wizard_views.xml',
        'wizard/inv_confirm_view.xml',
        'views/sample_submission_views.xml',
        'views/sameple_submission_menu.xml',
        'views/account_move_view.xml',
        'report/sample_submission_report_template.xml',
        'report/sample_submission_report.xml',
    ],
}
