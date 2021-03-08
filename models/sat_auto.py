# -*- coding: utf-8 -*-
from odoo import models, fields, api

class repairInherit(models.Model):
    _inherit = 'mrp.repair'

class helpdeskInherit(models.Model):
    _inherit: 'helpdesk.ticket'

    orden_sat = fields.Many2one('mrp.repair', string='Orden SAT')