# -*- coding: utf-8 -*-
{
    'name': 'BOM Product Cost Price',
    'summary': "Product Cost Price Per Bill of Material",
    'description': "Product Cost Price Per Bill of Material",

    'author': 'iPredict IT Solutions Pvt. Ltd.',
    'website': 'http://ipredictitsolutions.com',
    'support': 'ipredictitsolutions@gmail.com',

    'category': 'Manufacturing',
    'version': '14.0.0.1.0',
    'depends': ['mrp'],

    'data': [
        'views/product_view.xml',
        'views/mrp_bom_views.xml',
    ],

    'license': "OPL-1",
    'price': 9,
    'currency': "EUR",

    'auto_install': False,
    'installable': True,

    'images': ['static/description/main.png'],
    'pre_init_hook': 'pre_init_check',
}
