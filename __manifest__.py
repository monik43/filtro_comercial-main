# -*- coding: utf-8 -*-
{
    'name': "Cloudalia Educacion - Sales - Filtro comercial",

    'summary': """""",

    'description': """Módulo que añada varias modificaciones; entre ellas un filtro para el campo comercial y la generación del pdf de una etiqueta en los tíckets de helpdesk y en las reparaciones.""",

    'author': "Cloudalia Educacion",
    'website': "http://www.cloudaliaeducacion.com",

    'category': 'Sales',
    'version': '11.0.0.1',

    'depends': ['base', 'helpdesk', 'mrp_repair', 'cloudalia_purchase_from_repair', 'stock'],
    
    'data': [
        'views/res_partner_add_filter_view.xml',
        'views/mrp_repair_add_btn.xml',
        'views/stock_picking_add_btn.xml',
        'views/stock_warehouse_add_type.xml',
        'views/purchaseorder_mrp_add_fields.xml',
        'report/cloudalia_report_etiqueta_sat.xml',
        'report/cloudalia_report_etiqueta_stock.xml'
        #'views/hd_ticket_add_view.xml',
    ],
}