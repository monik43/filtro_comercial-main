# -*- coding: utf-8 -*-
from odoo import models, fields, api

class mrprepair(models.Model):
    _inherit = 'mrp.repair'

    @api.multi
    def report_etiqueta_sat_label(self):
        return self.env.ref('filtro_comercial.cd_report_etiqueta_sat').report_action(self)