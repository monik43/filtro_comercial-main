# -*- coding: utf-8 -*-
from odoo import models, fields, api


class repairInherit(models.Model):
    _inherit = 'mrp.repair'

    @api.multi
    def create_sat_order(self):
        ticket = helpdeskInherit()._get_actual_record()

        hd = self.env['helpdesk.ticket'].browse(ticket.id)
        #repair = self.env['helpdesk.ticket'].search(['hd.id', '=', 'name'])
        self.name = hd.name

class helpdeskInherit(models.Model):
    _inherit = 'helpdesk.ticket'

    @api.multi
    def _get_actual_record(self):
        self.ensure_one()
        return self
