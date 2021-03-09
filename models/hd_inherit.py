# -*- coding: utf-8 -*-
from odoo import models, fields, api


class helpdeskticket(models.Model):
    _inherit = 'helpdesk.ticket'

    campo_orden_sat = fields.Many2one('mrp.repair', ondelete='set null', string="Orden SAT")
    product_id = fields.Many2one('product.product', ondelete='set null', string="Producto a reparar")
    lot_id = fields.Many2one('stock.production.lot', ondelete='set null', string="Lote/Nº de serie")
    
    for record in self:
        record['x_sn'] = record.lot_id

    print(lot_id)
