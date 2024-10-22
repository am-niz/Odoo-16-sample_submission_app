from importlib.resources import _
from odoo import fields, models, api


class SampleSubmission(models.Model):
    _name = "sample.submission"
    _description = "Sample Submission"
    _inherit = "mail.thread"

    sequence = fields.Char(string="Number", readonly=True)
    name = fields.Char(string="Name")
    customer_id = fields.Many2one("res.partner", string="Customer")
    date_submission = fields.Date(string="Date of Submission")
    description = fields.Text(string="Description")
    price = fields.Float(string="Price")
    discount = fields.Float(string="Discount")
    vat = fields.Float(string="VAT")

    material_ids = fields.One2many("sample.submission.material", "sample_submission_id", string="Materials")

    # Stages (Pending, Doing, Completed)
    stage = fields.Selection([
        ("pending", "Pending"),
        ("doing", "Doing"),
        ("completed", "Completed"),
        ("invoiced", "Invoiced")
    ], string="Stage", default="pending", tracking=3)

    # make status changes to doing when feeding the values
    @api.onchange("name")
    def _onchange_name(self):
        self.stage = "doing"

    # Automatically generate sequence number
    @api.model
    def create(self, vals):
        if vals.get('sequence', _('New')) == _('New'):
            vals['sequence'] = self.env['ir.sequence'].next_by_code('sample.submission') or _('New')
        res = super(SampleSubmission, self).create(vals)
        res.stage = "completed"
        return res

    def action_create_material(self):
        return {
            "name": "Create Material Records",
            "type": "ir.actions.act_window",
            "res_model": "material.wizard",
            "view_mode": "form",
            "context": {"default_sample_submission_id": self.id},
            "target": "new",
        }
