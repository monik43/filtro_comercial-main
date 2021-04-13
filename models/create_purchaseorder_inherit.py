# -*- coding: utf-8 -*-
from odoo import models, fields, api

class createpurchaseordermrp(models.TransientModel):
    _inherit = 'create.purchaseorder_mrp'

    warehouse = fields.Many2one('purchase.order', string='Almacén', required = True)
