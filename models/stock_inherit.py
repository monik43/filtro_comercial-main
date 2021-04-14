# -*- coding: utf-8 -*-
from odoo import models, fields, api

class stockpicking(models.Model):
    _inherit = 'stock.picking'

    @api.multi
    def report_etiqueta_stock_label(self):
        orden = self.env['purchase.order'].search(self.picking_ids[0],'=', id)

        print("//"*25, orden)
        print("//"*25, self.id)
        #return self.env.ref('filtro_comercial-main.cd_report_etiqueta_stock').report_action(orden)
    
class stockwarehouse(models.Model):
    _inherit = 'stock.warehouse'

    warehouse_type = fields.Char()

class stockpickingtype(models.Model):
    _inherit = 'stock.picking.type'

    warranty = fields.Char()

