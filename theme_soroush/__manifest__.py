# -*- encoding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Theme Soroush',
    'description': 'Soroush Website theme to customization possibilities.',
    'category': 'Theme/Ecommerce',
    'version': '1.0',
    'depends': ['website','product', 'sale','website_sale','theme_default'],
	'author':'Soroush Ebadi',
    'data': [
        'data/theme_default_data.xml',
        'views/theme_default_templates.xml',  
        'views/ecommerce_snippest_extra.xml'
    ],
    'images': [
		'static/description/icon.png'
        'static/description/cover.jpg'
        
    ],
    'application': False,
}
