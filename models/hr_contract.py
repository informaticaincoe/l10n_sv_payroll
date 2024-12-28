from odoo import fields, models

class HrContract(models.Model):
    _inherit = 'hr.contract'

    isss_rate = fields.Float(string="Tasa ISSS (%)", default=3.0)
    afp_rate = fields.Float(string="Tasa AFP (%)", default=7.25)
    isr_rate = fields.Float(string="Tasa ISR (%)", default=10.0)
