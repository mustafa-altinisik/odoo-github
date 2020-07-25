# -*- coding: utf-8 -*-
{
    'name': "deneme.modulu",

    'summary': """
        July 8 Firts custom module (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Bu modül, özelleştirilmiş modül kullanımının öğrenilmesi için yapılmıştır.
    """,

    'author': "m.altinisik",
    'website': "https://www.mustafa.altinisik.net",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
