# -*- coding: utf-8 -*-
from odoo import models, fields, api


class ticketInherit(models.Model):
    _inherit: 'helpdesk.ticket'

    campo_orden_sat = fields.Many2one(
        'mrp.repair', ondelete='set null', string="Orden SAT")