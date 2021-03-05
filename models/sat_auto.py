# -*- coding: utf-8 -*-
from odoo import models, fields, api

class repairInherit(models.Model):
    _inherit = 'mrp.repair'

    @api.multi
    def print_repair_order(self):
        repair = self.env['mrp.repair'].search([])
        print(repair)