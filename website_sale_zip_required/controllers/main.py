# -*- coding: utf-8 -*-

from openerp.addons.website_sale.controllers.main import website_sale


class WebsiteSale(website_sale):
    def checkout_form_validate(self, data):
        res = super(WebsiteSale, self).checkout_form_validate(data)
        if not data.get('zip'):
            res['zip'] = 'missing'
        return res
