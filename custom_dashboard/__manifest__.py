{
    'name': 'Shopify Connector',
    'version': '1.0',
    'summary': 'Custom Dashboard for Products, Customers, and Orders',
    'description': """
        Shopify Dashboard Module
        ------------------------
        A module to manage Shopify products, customers, and orders in Odoo.
        Features include:
        - Product synchronization
        - Order management
        - Real-time updates
    """, 

    'depends': ['base', 'sale', 'stock', 'product'],
    'data': [
        'views/dashboard_view.xml',
        'security/ir.model.access.csv',
    ],
    'assets': {
        'web.assets_backend': [
            '/custom_dashboard/static/src/js/dashboard_action.js',  # JS file
            '/custom_dashboard/static/src/css/styles.css',  # CSS file
        ],
    },

    'images': ['static/description/icon.png'], 
    'price': 50.00,
    'currency': 'USD',
    'author': 'Astratech Systems',
    'license': 'OPL-1', 
    'application': True,
    'installable': True,
    'icon': 'custom_dashboard/static/description/icon.png', 
}
