from odoo import fields, models, api


class AccountMove(models.Model):
    _inherit = "account.move"

    sample_submission_id = fields.Many2one("sample.submission", string="Sample Submission", invisible=True)
    is_sample_submission = fields.Boolean()  # help to view the sample_submission from the corresponding invoice

    def action_sample_submission(self):
        return {
            "name": "Sample Submission",
            "type": "ir.actions.act_window",
            "res_model": "sample.submission",
            "res_id": self.sample_submission_id.id,
            "view_mode": "form",
            "target": "current",
        }

