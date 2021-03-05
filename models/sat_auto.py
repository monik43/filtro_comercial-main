# -*- coding: utf-8 -*-
from odoo import models, fields, api


class helpdeskTicket(models.Model):
    _inherit = 'helpdesk.ticket'

    @api.onchange('x_ordensat')
    def prueba(self):

        repair = self.env['helpdesk.ticket'].search([])
        print(repair)
