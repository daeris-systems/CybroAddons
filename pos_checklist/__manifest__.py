# -*- coding: utf-8 -*-
{
    'name': "POS Checklist",
    'version': '11.0.1.0.0',
    'summary': """Checklist for Point Of sale Cashier""",
    'description': """Checklist for Point Of sale Cashier""",
    'category': 'Point Of Sale',
    'author': 'Cybrosys Techno Solutions',
    'company': 'Cybrosys Techno Solutions',
    'maintainer': 'Cybrosys Techno Solutions',
    'website': "https://www.cybrosys.com/odoo/industries/pos/",
    'depends': ['base', 'point_of_sale', 'document', 'hr'],
    'data': [
             'views/admin_view.xml',
             'security/ir.model.access.csv',
             'security/security.xml',
             'data/cron.xml',
            ],
    'qweb': [],
    'demo': [],
    'images': ['static/description/banner.png'],
    'license': "AGPL-3",
    'installable': True,
    'application': True,
}
