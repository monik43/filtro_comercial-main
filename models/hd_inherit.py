# -*- coding: utf-8 -*-
from odoo import models, fields, api


class helpdeskticket(models.Model):
    _inherit = 'helpdesk.ticket'

    campo_orden_sat = fields.Many2one(
        'mrp.repair', ondelete='set null', string="Orden SAT")
    product_id = fields.Many2one(
        'stock.production.lot', ondelete='set null', string="Producto a reparar")
    lot_id = fields.Many2one(
        'product.product', ondelete='set null', string="Lote/Nº de serie")

    mrprep_rel = fields.Many2one(
        'mrp.repair', string='Reparación relacionado')

    def assign_proper_repair(self):
        mrp_repair = self.env['mrp.repair']

        if hasattr(self, 'x_ordensat'):

            self.mrprep_rel = self.x_ordensat
            self.mrprep_rel.ticket_rel.id = self.id
        else:
            if mrp_repair.search([('ticket_rel.id', '=', self.id)]):
                self.mrprep_rel = mrp_repair.search([('ticket_rel.id', '=', self.id)])
            elif mrp_repair.search([(mrp_repair.name[:4], '=', self.id)]):
                self.mrprep_rel = mrp_repair.search([(mrp_repair.name[:4], '=', self.id)])

                self.mrprep_rel.ticket_rel.id = self.id


    @api.multi
    def report_etiqueta_sat_label(self):
        self.assign_proper_repair()
        return self.env.ref('filtro_comercial-main.cd_report_etiqueta_sat').report_action(self)
