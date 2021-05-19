# -*- coding: utf-8 -*-
from odoo import models, fields, api


class purchaseorder(models.Model):
    _inherit = 'purchase.order'

    partner_ref_eti = fields.Char(compute='_assign_printable_ref')

    @api.depends('partner_ref')
    def _assign_printable_ref(self):

        for record in self:

            record.partner_ref_eti = record.partner_ref

            if record.partner_ref:

                if record.partner_ref_eti.startswith('#'):

                    record.partner_ref_eti = record.partner_ref_eti[1:]

                if len(record.partner_ref_eti) > 17:

                    record.partner_ref_eti = record.partner_ref_eti[:17]

    @api.multi
    def report_etiqueta_purchase_order(self):

        return self.env.ref('filtro_comercial-main.cd_report_etiqueta_purchase_order').report_action(self)


class purchaseorderline(models.Model):
    _inherit = 'purchase.order.line'

    move_state = fields.Char(compute='_assign_movement_state')

    @api.depends('move_ids')
    def _assign_movement_state(self):

        def nuevo():
            return 'Nuevo'

        def esperando_movimiento():
            return 'Esperando movimiento'

        def esperando_disponibilidad():
            return 'Esperando disponibilidad'

        def parcialmente_disponible():
            return 'Parcialmente disponible'

        def reservado():
            return 'Reservado'

        def cancelado():
            return 'Cancelado'

        def hecho():
            return 'Hecho'

        def get_state(state):

            switcher_state = {
                'draft': nuevo(),
                'waiting': esperando_movimiento(),
                'confirmed': esperando_disponibilidad(),
                'partially_avaliable': parcialmente_disponible(),
                'assigned': reservado(),
                'cancel': cancelado(),
                'done': hecho()
            }

            return switcher_state.get(state, 'Sin estado')

        for record in self:

            record.move_state = get_state(record.move_ids.state)
