# -*- coding: utf-8 -*-
from odoo import models, fields, api


class helpdeskticket(models.Model):
    _inherit = 'helpdesk.ticket'

    campo_orden_sat = fields.Many2one('mrp.repair', ondelete='set null', string="Orden SAT")
    product_id = fields.Many2one('stock.production.lot', ondelete='set null', string="Producto a reparar")
    lot_id = fields.Many2one('product.product', ondelete='set null', string="Lote/Nº de serie")

    @api.multi
    def report_etiqueta_sat_label(self):
        return self.env.ref('filtro_comercial-main.cd_report_etiqueta_sat').report_action(self)