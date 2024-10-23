from odoo import fields, models


class InvoiceWizard(models.TransientModel):
    _name = "inv.confirm.wizard"
    _description = "Invoice of Sample Submission Confirmation"

    sample_submission_id = fields.Many2one("sample.submission", string="Sample Submission")

    def action_confirm(self):
        self.sample_submission_id.stage = "invoiced"

        # Creating invoice
        new_inv = self.env["account.move"].create({
            "move_type": "out_invoice",  # "out_invoice" to specify it's a customer invoice
            "partner_id": self.sample_submission_id.customer_id.id,
            "invoice_date": self.sample_submission_id.date_submission,
            "sample_submission_id": self.sample_submission_id.id,
            "is_sample_submission": True,
            "invoice_line_ids": [(0, 0, {
                "name": self.sample_submission_id.name,
                "price_unit": self.sample_submission_id.price,
                "discount": self.sample_submission_id.discount,
                "tax_ids": [(6, 0, self.sample_submission_id.vat_ids.ids)],
                "quantity": 1.0,
            })]
        })

        material_ids = self.env["sample.submission.material"].search([
            ("sample_submission_id", "=", self.sample_submission_id.id)
        ])

        # Editing the related sample submission with the new datas
        self.sample_submission_id.write({
            "stage": "invoiced",
            "amount": float(new_inv.amount_total_signed),
            "invoice_status": "draft",
            "total_product_qty": sum(material_ids.mapped("quantity")),
            "sum_of_cost": sum(material_ids.mapped("quantity")),
            "inv_count": self.sample_submission_id.inv_count + 1,
        })
