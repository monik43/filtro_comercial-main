# -*- coding: utf-8 -*-
from odoo import models, fields, api


class helpdeskticket(models.Model):
    _inherit = 'helpdesk.ticket'

    fecha_entrada = create_date[-8]

    campo_orden_sat = fields.Many2one('mrp.repair', ondelete='set null', string="Orden SAT")
    product_id = fields.Many2one('stock.production.lot', ondelete='set null', string="Producto a reparar")
    lot_id = fields.Many2one('product.product', ondelete='set null', string="Lote/Nº de serie")