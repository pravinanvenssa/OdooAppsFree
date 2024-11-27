# __manifest__.py

{
    'name': 'Hide Product Price for Unauthenticated Users',
    'version': '17.0.1.0',
    'summary': 'Hide product prices for users not logged in',
    'category': 'Website',
    'author': 'Astratech Systems',
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

    'description': """
        This module hides product prices for users who are not logged in.
        Only authenticated users will be able to view product prices.
        
        Features:
        - Admin users can always see product prices.
        - Prices are hidden for all non-authenticated users.
        - Admins can view product prices in the inventory, sales, and product pages.
        - Product prices are hidden across the website to protect sensitive pricing information.
    """
}

