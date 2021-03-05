# -*- coding: utf-8 -*-
from odoo import models, fields, api


class repairInherit(models.Model):
    _inherit = 'mrp.repair'

    @api.onchange('x_ticket')
    def print_repair_order(self):
        hd = self.env['helpdesk.ticket']
        repair = self.env['helpdesk.ticket'].search(['hd.id', '=', 'self.name'])
        print(repair)
