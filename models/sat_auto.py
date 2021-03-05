# -*- coding: utf-8 -*-
from odoo import models, fields, api


class repairInherit(models.Model):
    _inherit = 'mrp.repair'

    @api.onchange('x_ticket')
    def print_repair_order(self):
        hd = self.env.ref('helpdesk_ticket.1317')
        #repair = self.env['helpdesk.ticket'].search(['hd.id', '=', 'name'])
        print(hd.name)
