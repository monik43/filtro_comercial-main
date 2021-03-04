# -*- coding: utf-8 -*-
from odoo import models, fields, api

class repairInherit(models.Model):
    _inherit = 'mrp.repair'

    @api.onchange('x_ticket')
    def onchange_x_ticket(self):
        if self.x_ticket and self.x_ticket.exists():
            print(self)
            print(self.x_ticket)
        