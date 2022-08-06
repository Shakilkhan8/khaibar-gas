# -*- coding: utf-8 -*-
{
    'name': "HR Biometric Attendance",
    'summary': """This Module designed for fetching bio metric attendance at local server then push via post request at cloud server""",
    'description': """This Module designed for fetching bio metric attendance at local server then push via post request at cloud server""",
    'author': "MUHAMMAD Imran",
    'website': "http://www.yourcompany.com",
    'category': 'attendance',
    'version': '0.1',
    'depends': ['base', 'hr_attendance'],
    'data': [
        # 'security/ir.model.access.csv',
        'views/check_biometric_attendance_cron.xml',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
