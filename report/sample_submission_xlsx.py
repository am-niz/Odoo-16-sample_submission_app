from odoo import models


class SampleSubmissionXlsx(models.AbstractModel):
    _name = 'report.sample_submission_app.report_sample_submission_xlsx'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, lines):
        # Define formatting for different elements
        format_title = workbook.add_format({"font_size": 14, "align": "center", "bold": True})
        format_header = workbook.add_format({"font_size": 14, "align": "left", "bold": True})
        format_data = workbook.add_format({"font_size": 12, "align": "left", "bold": False})

        sheet = workbook.add_worksheet("Sample Submission")

        # Set column widths for better readability
        sheet.set_column(2, 2, 30)  # Adjust the width of column 2 (for NAME)
        sheet.set_column(3, 3, 30)  # Adjust the width of column 3 (for CUSTOMER)
        sheet.set_column(4, 5, 20)  # Adjust the width of columns 4-5 (for DATE and PRICE)

        # Write Title (on the top)
        sheet.merge_range('B2:H2', 'SAMPLE SUBMISSION', format_title)

        # Write Headers (on row 4)
        sheet.write(4, 2, 'NAME', format_header)
        sheet.write(4, 3, 'CUSTOMER', format_header)
        sheet.write(4, 4, 'DATE', format_header)
        sheet.write(4, 5, 'PRICE', format_header)

        # Write Data starting from row 5 onwards
        row = 5  # Start on row 5 for the first record
        for line in lines:
            sheet.write(row, 2, line.name, format_data)
            sheet.write(row, 3, line.customer_id.translated_display_name, format_data)
            sheet.write(row, 4, str(line.date_submission), format_data)
            sheet.write(row, 5, line.price, format_data)
            row += 1  # Move to the next row for the next record
