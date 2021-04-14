# -*- coding: utf-8 -*-
from odoo import models, fields, api

class stockpicking(models.Model):
    _inherit = 'stock.picking'

    @api.multi
    def report_etiqueta_stock_label(self):
        orden = self.env['purchase.order'].search('name','=',self.origin)
        print("//"*55, self.id)
        print("//"*88, orden.id)
        #return self.env.ref('filtro_comercial-main.cd_report_etiqueta_stock').report_action(orden)
    
class stockwarehouse(models.Model):
    _inherit = 'stock.warehouse'

    warehouse_type = fields.Char()

class stockpickingtype(models.Model):
    _inherit = 'stock.picking.type'

    warranty = fields.Char()

