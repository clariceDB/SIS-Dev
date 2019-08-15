# -*- coding: utf-8 -*-
{
    'name': "Student Information System",

    'summary': """
        Cape Winelands College Student Information System 
        """,

    'description': """
        A small tertiary institution, the Cape Winelands College requires an information system in order to manage various parts of their institution in relation to students and staff. Due to the extensive growth and increasing complexity of managing this information, they cannot use the simpler excel based methods. There is a need to develop a more sophisticated Student Information System (SIS) in order for them to do this effectively and in a scalable way. 
    """,

    'author': "Clarice, Qhama, Liso & Lucia",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Student Information System',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'mail', 'contacts'],

    # always loaded
    'data': [
        'security/sis_security.xml',
        'security/ir.model.access.csv',
        'views/student_view.xml',
        'views/menu_views.xml',
        'views/templates.xml',
        'views/add_course_view.xml',
        'views/add_programme_view.xml',
        'views/add_lec_view.xml',
        'views/applications_view.xml',
        'views/add_lecturer_marks_view.xml',
        'views/rollover_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
    'installable': True,
}
