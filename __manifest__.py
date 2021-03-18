# -*- coding: utf-8 -*-
{
    'name': "Cloudalia Educacion - Sales - Filtro comercial",

    'summary': """""",

    'description': """Filtro campo de comercial""",

    'author': "Cloudalia Educacion",
    'website': "http://www.cloudaliaeducacion.com",

    'category': 'Sales',
    'version': '11.0.0.1',

    'depends': ['base', 'helpdesk', 'mrp_repair', 'product', 'stock'],
    
    'data': [
        'views/res_partner_add_filter_view.xml',
        'views/mrp_repair_add_btn.xml',
        'report/sat_ticket_report.xml',
        #'views/hd_ticket_add_view.xml',
    ],
}