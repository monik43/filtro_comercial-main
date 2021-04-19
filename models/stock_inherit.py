# -*- coding: utf-8 -*-
from odoo import models, fields, api

class stockpicking(models.Model):
    _inherit = 'stock.picking'

    
    @api.multi
    def report_etiqueta_stock_label(self):
        purchase_order = self.env['purchase.order'].search([('picking_ids', '=', self.id)])
        return self.env.ref('filtro_comercial-main.cd_report_etiqueta_purchase_order').report_action(purchase_order)
    
class stockwarehouse(models.Model):
    _inherit = 'stock.warehouse'

    warehouse_type = fields.Char()

class stockpickingtype(models.Model):
    _inherit = 'stock.picking.type'

    warranty = fields.Char()

