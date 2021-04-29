# -*- coding: utf-8 -*-
from odoo import models, fields, api


class mrprepair(models.Model):
    _inherit = 'mrp.repair'

    ticket_rel = fields.Many2one(
        'helpdesk.ticket', string='Ticket relacionado')

    # la idea del método es pasar migrar del código escrito por odoo a partir de la creación
    # de variables visual del superadmin a código puro.
    def search_and_assign_ticket(self):
        # para ahorrar espacio
        hd_ticket = self.env['helpdesk.ticket']

        # busqueda por el campo x_ordensat
        if hd_ticket.search([('x_ordensat.id', '=', self.id)]):
            self.ticket_rel = hd_ticket.search([('x_ordensat', '=', self.id)])

            # verificamos si mrprep_rel existe en el ticket y si no somos nosotros nos asignamos.
            if self.ticket_rel.mrprep_rel.id != self.id:
                self.ticket_rel.mrprep_rel.id = self.id

        # útil cuando se vaya a migrar al formulario sin x_ordensat:
        elif hd_ticket.search([('mrprep_rel.id', '=', self.id)]):
            self.ticket_rel = hd_ticket.search([('mrprep_rel.id', '=', self.id)])

            # verificamos si x_ordensat existe en el ticket y si no somos nosotros nos asignamos.
            if self.ticket_rel.x_ordensat.id != self.id:
                self.ticket_rel.x_ordensat.id = self.id

        # si no está asignado x_ordensat en el ticket ni el ticket_rel en nuestro modelo,
        # buscamos a partir de la string del nombre (no recomendable, falla en algunos
        # nombres donde el formato no es el correcto. por eso es la última opción)
        elif hd_ticket.search([('id', '=', self.name[:4])]):
            self.ticket_rel = hd_ticket.search([('id', '=', self.name[:4])])

            if self.ticket_rel.x_ordensat.id != self.id:
                self.ticket_rel.x_ordensat = self.id

            if self.ticket_rel.mrprep_rel != self.id:
                self.ticket_rel.mrprep_rel = self.id

    @api.multi
    def report_etiqueta_sat_label(self):
        self.search_and_assign_ticket()
        return self.env.ref('filtro_comercial-main.cd_report_etiqueta_sat').report_action(self.ticket_rel)