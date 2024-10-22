from odoo import fields, models, api


class SampleSubmissionMaterial(models.Model):
    _name = "sample.submission.material"
    _description = "Materials of Sample Submission"

    sample_submission_id = fields.Many2one("sample.submission", string="Sample Submission", ondelete="cascade")
    sl_no = fields.Integer(string="SI No", compute="_compute_sl_no")
    product_id = fields.Many2one("product.product", string="Material")
    quantity = fields.Float(string="Quantity")
    remarks = fields.Char(string="Remarks")

    @api.depends("sample_submission_id.material_ids")
    def _compute_sl_no(self):
        for record in self:
            # Get all the materials linked to the current sample submission
            materials = record.sample_submission_id.material_ids
            # Assign a sequential number based on the position in the materials list
            for index, material in enumerate(materials, start=1):
                material.sl_no = index
