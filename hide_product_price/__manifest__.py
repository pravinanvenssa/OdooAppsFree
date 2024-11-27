# __manifest__.py

{
    'name': 'Hide Product Price for Unauthenticated Users',
    'version': '17.0.1.0',
    'summary': 'Hide product prices for users not logged in',
    'category': 'Website',
    'author': 'Anvenssa AI',
    'license': 'LGPL-3',
    'depends': ['product', 'sale'],  
    'data': [
        'views/product_template_views.xml',
        'security/product_price_security.xml',
        'security/ir.model.access.csv',  
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}

