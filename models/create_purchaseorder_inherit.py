# -*- coding: utf-8 -*-
from odoo import models, fields, api

class createpurchaseordermrp(models.TransientModel):
    _inherit = 'create.purchaseorder_mrp'

    warehouse = fields.Many2one('stock.warehouse', string='Almacén', required = True)
