# -*- encoding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Theme Soroush',
    'description': 'website theme to showcase customization possibilities.',
    'category': 'Theme/Shoping',
    'sequence': 1000,
    'version': '1.0',
    'depends': ['website','product', 'sale','website_sale','theme_default'],
	'author':'Soroush Ebadi',
    'data': [
        'data/theme_default_data.xml',
        'views/theme_default_templates.xml',
        'views/pages.xml',
        'views/ecommerce_snippest_extra.xml'
    ],
    'images': [
        'static/description/cover.png',
        'static/description/theme-soroush.jpg',
    ],
    'application': False,
}