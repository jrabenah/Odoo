{
    'name': "Hello Odoo",

    'summary': "Mon tout premier module Odoo.",

    'description': """
Module pédagogique minimal pour comprendre la structure d'un module Odoo.
Il déclare un modèle simple, une vue liste, un formulaire, un menu et les droits d'accès.
    """,

    'author': "Jrabenah",   

    'website': "https://example.com",

    'category': 'Tools',

    'version': '18.0.1.0.0',

    'license': 'LGPL-3',
    'depends': ['base'],


    'data': [
        'security/ir.model.access.csv',
        'views/hello_record_views.xml',
        'views/hello_odoo_menus.xml',
    ],

    'application': True,

    'installable': True,
}