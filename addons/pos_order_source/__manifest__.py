# -*- coding: utf-8 -*-
{
    'name': "POS Order Source",

   'summary': """
        POS Order Source""",
    'author': "ICS Globe",
    'website': "",
    'category': 'Uncategorized',
    'version': '15.0.1.0.1',
    'license': 'Other proprietary',
    'depends': ['base','point_of_sale'],

    
    'data': [
        'security/ir.model.access.csv',
        'views/source.xml', 
        'views/inheritOrder.xml',
        'views/customSearch.xml',
        'report/order-report.xml',
        'report/report.xml',
        
    ],
    
    'demo': [], 
    'application': True,
}
