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
    vat_ids = fields.Many2many("account.tax", string="VAT")

    material_ids = fields.One2many("sample.submission.material", "sample_submission_id", string="Materials")

    # Stages (Pending, Doing, Completed)
    stage = fields.Selection([
        ("pending", "Pending"),
        ("doing", "Doing"),
        ("completed", "Completed"),
        ("invoiced", "Invoiced")
    ], string="Stage", default="pending", tracking=3)
    amount = fields.Float(string="Amount")
    invoice_status = fields.Selection([
        ("draft", "Draft"),
        ("posted", "Posted"),
        ("cancel", "Cancelled")
    ])
    collected_payment = fields.Float(string="Collected Payment")
    balance = fields.Float(string="Balance")
    total_product_qty = fields.Float(string="Total Product Qty")
    sum_of_cost = fields.Float(string="Sum of Cost")
    profit = fields.Float(string="Profit")

    inv_count = fields.Integer(string="Invoice Count", default=0)

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

    def action_create_invoice(self):
        return {
            "name": "Create Invoice",
            "type": "ir.actions.act_window",
            "res_model": "inv.confirm.wizard",
            "view_mode": "form",
            "context": {"default_sample_submission_id": self.id},
            "target": "new",
        }

    def action_view_invoice(self):
        return {
            "name": "Invoices",
            "type": "ir.actions.act_window",
            "res_model": "account.move",
            "view_mode": "tree,form",
            "domain": [("sample_submission_id", "=", self.id)],
            "target": "current",
        }
