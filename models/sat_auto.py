# -*- coding: utf-8 -*-
from odoo import models, fields, api

class HelpdeskTicket(models.Model):
    _inherit: 'helpdesk.ticket'

    orden_sat = fields.Many2one('mrp.repair')