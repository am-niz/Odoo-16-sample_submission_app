# -*- coding: utf-8 -*-
{
    'name': "sample_submission_app",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', "mail", "product", 'account'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/ir_sequence_data.xml',
        'wizard/material_wizard_views.xml',
        'wizard/inv_confirm_view.xml',
        'views/sample_submission_views.xml',
        'views/sameple_submission_menu.xml',
        'views/account_move_view.xml',
    ],
}
