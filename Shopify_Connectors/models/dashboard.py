from odoo import models, fields, api

class CustomDashboard(models.Model):
    _name = 'custom.dashboard'

    product_count = fields.Integer(string='Product Count', compute='_compute_counts')
    customer_count = fields.Integer(string='Customer Count', compute='_compute_counts')
    order_count = fields.Integer(string='Order Count', compute='_compute_counts')

    @api.depends('product_count', 'customer_count', 'order_count')
    def _compute_counts(self):
        # Count the number of products
        self.product_count = self.env['product.template'].search_count([])

        # Count the number of customers
        self.customer_count = self.env['res.partner'].search_count([('customer_rank', '>', 0)])

        # Count the number of orders
        self.order_count = self.env['sale.order'].search_count([])

    # @api.model
    # def action_shopify(self):
    #     # Define the logic here
    #     # For example, redirecting to a Shopify-related action
    #     return {
    #         'type': 'ir.actions.act_url',
    #         'url': 'https://www.shopify.com',
    #         'target': 'new',  # Opens the link in a new tab
    #     }
    def action_shopify(self):
        # Handle the method logic here
        return {
            'type': 'ir.actions.act_url',
            'url': 'https://www.shopify.com',
            'target': 'new',  # Opens the link in a new tab
        }


    

#  from odoo import models, fields

# class CustomDashboard(models.Model):
#     _name = 'custom.dashboard'

#     # Fields to show in the dashboard
#     product_count = fields.Integer(string="Products Count", compute='_compute_counts')
#     customer_count = fields.Integer(string="Customers Count", compute='_compute_counts')
#     order_count = fields.Integer(string="Orders Count", compute='_compute_counts')

#     def _compute_counts(self):
#         self.product_count = self.env['product.template'].search_count([])
#         self.customer_count = self.env['res.partner'].search_count([('customer_rank', '>', 0)])
#         self.order_count = self.env['sale.order'].search_count([])

