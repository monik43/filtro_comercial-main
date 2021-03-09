# -*- coding: utf-8 -*-
from odoo import models, fields, api


class helpdeskticket(models.Model):
    _inherit: 'helpdesk.ticket'

    orden_sat = fields.Many2one(
        'mrp.repair', ondelete='set null', string="Orden SAT")