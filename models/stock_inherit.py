# -*- coding: utf-8 -*-
from odoo import models, fields, api

class stockpicking(models.Model):
    _inherit = 'stock.picking'

    
    @api.multi
    def report_etiqueta_stock_label(self):
        purchase_order = self.env['purchase.order'].search([(self.id, 'in', 'picking_ids')])
        return self.env.ref('filtro_comercial-main.cd_report_etiqueta_sat').report_action(purchase_order)
    
class stockwarehouse(models.Model):
    _inherit = 'stock.warehouse'

    warehouse_type = fields.Char()

class stockpickingtype(models.Model):
    _inherit = 'stock.picking.type'

    warranty = fields.Char()

