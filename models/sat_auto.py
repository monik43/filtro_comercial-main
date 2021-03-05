# -*- coding: utf-8 -*-
from odoo import models, fields, api

class repairInherit(models.Model):
    _inherit = 'mrp.repair'

    @api.onchange('x_ticket')
    def onchange_x_ticket(self):
        pacients = self.env['hospital.patient'].search([])
        print("pacients = ", pacients)
        