from odoo import fields, models


class InvoiceFilter(models.TransientModel):
    _name = "filter.invoice"
    _description = "Invoices Can Filter With Help of Dates"

    date_from = fields.Date(string="Date From")
    date_to = fields.Date(string="Date To")

    def action_apply_filter(self):
        # Initialize a domain for the date filter
        domain = []

        # Add date_from and date_to conditions to the domain
        if self.date_from:
            domain.append(('date_submission', '>=', self.date_from))
        if self.date_to:
            domain.append(('date_submission', '<=', self.date_to))

        # Search for sample submissions based on the date domain
        invoices = self.env["sample.submission"].search(domain)
        print(invoices.ids, "+++++++++ids")

        if invoices:
            # Return the report action for the filtered invoices
            return self.env.ref("sample_submission_app.sample_submission_report").report_action(invoices.ids)
        else:
            return {'type': 'ir.actions.act_window_close'}
