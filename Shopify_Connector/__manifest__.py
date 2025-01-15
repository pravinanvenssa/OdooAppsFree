{
    'name': 'Shopify Connector',
    'version': '1.0',
    'summary': 'Custom Dashboard for Products, Customers, and Orders',
    'depends': ['base', 'sale', 'stock', 'product'],
    'data': [
        'views/dashboard_view.xml',
        'security/ir.model.access.csv',
    ],
    'assets': {
        'web.assets_backend': [
            '/Shopify_Connector/static/src/js/dashboard_action.js',  # Ensure JS is loaded
        ],
    },
    'assets': {
        'web.assets_backend': [
            '/Shopify_Connector/static/src/css/styles.css',
        ],
    },

   
    'price': 50.00,
    'currency': 'USD',
    'author': 'Astratech Systems',
    'application': True,
    'installable': True,
    'icon': 'Shopify_Connector/static/description/icon.png',
}
