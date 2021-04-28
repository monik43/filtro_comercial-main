# -*- coding: utf-8 -*-
from odoo import models, fields, api

class mrprepair(models.Model):
    _inherit = 'mrp.repair'

    #ticker_rel = fields.Many2one

    @api.multi
    def report_etiqueta_sat_label(self):
        ticket = self.env['helpdesk.ticket'].browse(self.name[:4])
        # error en produccion - mirar otra manera de acceder al ID



        return self.env.ref('filtro_comercial-main.cd_report_etiqueta_sat').report_action(ticket)