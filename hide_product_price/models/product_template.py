# models/product_template.py
from odoo import models, fields

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    def read(self, fields=None, load='_classic_read'):
        # Hide 'list_price' and 'standard_price' fields from regular users
        if fields:
            if 'list_price' in fields or 'standard_price' in fields:
                if not self.env.user.has_group('base.group_system'):
                    fields = [f for f in fields if f not in ('list_price', 'standard_price')]
        return super(ProductTemplate, self).read(fields, load)
