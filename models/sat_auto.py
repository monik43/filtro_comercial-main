# -*- coding: utf-8 -*-
from odoo import models, fields, api


class repairInherit(models.Model):
    _inherit = 'mrp.repair'

    x_ordensat = fields.Many2one(
    'helpdesk.ticket', string="Orden SAT",
    default=lambda self: self.env['ir.model.data'].xmlid_to_res_id('helpdesk_ticket.view_record_id'))

class helpdeskInherit(models.Model):
    _inherit = 'helpdesk.ticket'

    def view_record_id(self):
        return self.id