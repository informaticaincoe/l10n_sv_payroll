{
    'name': 'Localización de Nómina El Salvador',
    'version': '1.0',
    'summary': 'Módulo para gestionar la nómina conforme a la legislación salvadoreña.',
    'author': 'Ing. Francisco Antonio Flores',
    'website': 'http://www.grupoincoe.com',
    'category': 'Localization/Payroll',
    'depends': ['hr_payroll'],
    'data': [
        'data/hr_rule_data.xml',
        'views/hr_employee_views.xml',
        'views/hr_contract_views.xml',
        'data/ir_cron_data.xml',
    ],
    'installable': True,
    'application': False,
}
