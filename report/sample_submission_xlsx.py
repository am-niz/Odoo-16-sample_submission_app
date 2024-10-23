from odoo import models


class SampleSubmissionXlsx(models.AbstractModel):
    _name = 'report.sample_submission_app.report_sample_submission_xlsx'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, lines):
        # Define formatting for different elements
        format_title = workbook.add_format({"font_size": 14, "align": "center", "bold": True})
        format_header = workbook.add_format({"font_size": 14, "align": "left", "bold": True})
        format_data = workbook.add_format({"font_size": 12, "align": "left", "bold": False})

        # Add worksheet with the title
        sheet = workbook.add_worksheet("Sample Submission")

        # Set column widths for better readability
        sheet.set_column(2, 2, 30)  # Adjust the width of column 2 (for NAME)
        sheet.set_column(3, 3, 30)  # Adjust the width of column 3 (for CUSTOMER)
        sheet.set_column(4, 5, 20)  # Adjust the width of columns 4-5 (for DATE and PRICE)

        # Write Title
        sheet.merge_range('B2:H2', 'SAMPLE SUBMISSION', format_title)  # Merge cells for title

        # Write Headers and Data
        sheet.write(4, 2, 'NAME', format_header)  # Header for Name
        sheet.write(5, 2, lines.name, format_data)  # Data for Name

        sheet.write(4, 3, 'CUSTOMER', format_header)  # Header for Customer
        sheet.write(5, 3, lines.customer_id.translated_display_name, format_data)  # Data for Customer

        sheet.write(4, 4, 'DATE', format_header)  # Header for Date
        sheet.write(5, 4, str(lines.date_submission), format_data)  # Data for Date (converted to string)

        sheet.write(4, 5, 'PRICE', format_header)  # Header for Price
        sheet.write(5, 5, lines.price, format_data)  # Data for Price
