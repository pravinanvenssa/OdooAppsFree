{
    'name': 'Shopify Connector',
    'version': '1.0',
    'summary': 'Custom Dashboard for Products, Customers, and Orders',
    'description': """
        Shopify Connector :- This module provides a custom dashboard for your Shopify store, allowing you to track products, customers, and orders efficiently
       
    """,
    'depends': ['base', 'sale', 'stock', 'product'],
    'data': [
        'views/dashboard_view.xml',
        'security/ir.model.access.csv',
    ],
    'assets': {
        'web.assets_backend': [
            '/shopify_connector/static/src/js/dashboard_action.js',  # Ensure JS is loaded
        ],
        'web.assets_backend': [
            '/shopify_connector/static/src/css/styles.css',  # Ensure CSS is loaded
        ],
    },
    'price': 50.00,
    'currency': 'USD',
    'author': 'Astratech Systems',
    'application': True,
    'installable': True,
    'icon': 'shopify_connector/static/description/icon.png',
    'license': 'GPL-3',
}
