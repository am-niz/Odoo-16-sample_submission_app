from odoo import fields, models


class MaterialWizard(models.TransientModel):
    _name = "material.wizard"
    _description = 'Wizard to add materials to a sample submission'

    product_id = fields.Many2one("product.product", string="Material")
    quantity = fields.Float(string="Quantity")
    remarks = fields.Char(string="Remarks")

    def action_create_material_wizard(self):  # Add the material to the sample submission's notebook (material list)
        sample_submission_id = self.env.context.get("default_sample_submission_id")
        if sample_submission_id:
            self.env["sample.submission.material"].create({
                "sample_submission_id": sample_submission_id,
                "product_id": self.product_id.id,
                "quantity": self.quantity,
                "remarks": self.remarks,
            })
            sample_submission = self.env["sample.submission"].browse(sample_submission_id)
            sample_submission.stage = "completed"