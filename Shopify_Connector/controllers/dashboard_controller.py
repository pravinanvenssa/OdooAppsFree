from odoo import http
from odoo.http import request

class CustomDashboardController(http.Controller):

    @http.route('/custom_dashboard', type='http', auth='public', website=True)
    def custom_dashboard(self):
        product_count = request.env['product.template'].search_count([])
        customer_count = request.env['res.partner'].search_count([('customer_rank', '>', 0)])
        order_count = request.env['sale.order'].search_count([])

        return request.render('custom_dashboard.custom_dashboard_template', {
            'product_count': product_count,
            'customer_count': customer_count,
            'order_count': order_count,
        })
