from odoo import fields, models


class InvoiceWizard(models.TransientModel):
    _name = "inv.confirm.wizard"
    _description = "Invoice of Sample Submission Confirmation"

    sample_submission_id = fields.Many2one("sample.submission", string="Sample Submission")

    def action_confirm(self):
        self.sample_submission_id.stage = "invoiced"
