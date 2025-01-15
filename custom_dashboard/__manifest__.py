{
    'name': 'Shopify Dashboard',
    'version': '1.0',
    'summary': 'Custom Dashboard for Products, Customers, and Orders',
    'depends': ['base', 'sale', 'stock', 'product'],
    'data': [
        'views/dashboard_view.xml',
        'security/ir.model.access.csv',
    ],
    'assets': {
        'web.assets_backend': [
            '/custom_dashboard/static/src/js/dashboard_action.js',  # Ensure JS is loaded
        ],
    },
    'assets': {
        'web.assets_backend': [
            '/custom_dashboard/static/src/css/styles.css',
        ],
    },

   
    'price': 50.00,
    'currency': 'USD',
    'author': 'Astratech Systems',
    'application': True,
    'installable': True,
    'icon': 'custom_dashboard/static/description/icon.png',
}
