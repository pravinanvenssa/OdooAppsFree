{
    'name': 'Shopify Connector',
    'version': '18.0.1.0',
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
   
    # 'images': ['static/description/icon.jpg'], 
    'images': ['static/description/images/icon-in.gif'], 
    'price': 50.00,
    'currency': 'USD',
    'author': 'Astratech Systems',
    'license': 'OPL-1', 
    'application': True,
    'installable': True,
    'icon': 'Shopify_Connectors/static/description/icon.png', 
}
