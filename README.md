# Sample Submission App

This custom Odoo module manages sample submissions, including customer details, material tracking, and invoicing. It aims to streamline sample submission workflows, track materials, and generate reports in both PDF and Excel formats.

## Features

- **Sample Submission Management**: Create, update, and manage sample submission records with fields like sample sequence, customer, submission date, price, discount, and VAT.
- **Material Management**: Track required materials for each sample submission with details like serial number, material (as a product from Inventory), quantity, and remarks.
- **Stages**: Manage the progress of sample submissions with stages such as Pending, Doing, and Completed.
- **Invoicing**: Generate invoices with sample submission details, including price, discount, VAT, and invoicing status.
- **Reports**: Generate PDF and Excel reports for sample submissions with custom formatting, logos, and date range filters.
- **Internal Linking**: Navigate between sample submission records and related invoices through internal links.
- **Export Data**: Export data from list views to Excel and PDF formats.

## Installation

### Prerequisite

Before installing the Sample Submission module, ensure that you have the `report_xlsx` module installed on your Odoo server to support Excel report generation.

- You can download and install the `report_xlsx` module from this link: [report_xlsx for Odoo 16](https://apps.odoo.com/apps/modules/16.0/report_xlsx/).

### Module Installation

1. Clone this repository to your Odoo addons directory:
    ```sh
    git clone https://github.com/am-niz/sample_submission_app.git
    ```

2. Install the `report_xlsx` module (see the prerequisite above).
   
3. Restart the Odoo server to load the new module:
    ```sh
    ./odoo-bin -c conf_file_name.conf -d database_name --xmlrpc-port port_number
    ```

4. Update the module list in Odoo:
    - Navigate to **Apps**.
    - Click on **Update Apps List**.
    - To explore the functionality and workflow of this module with screenshots, click on the module info on the sample_submission module.

5. Install the "Sample Submission" module from the Apps menu.

## Usage

1. To explore the functionality and workflow of this module with screenshots, click on the module info on the sample_submission module.
2. Navigate to the **Sample Submission** menu in Odoo.
3. Manage sample submission records, track materials, and generate invoices.
4. Use the **Report** button to generate reports in PDF or Excel format.
5. View and export data for sample submissions, including totals and profit calculations.
   

## Screen Recording

To see a demonstration of the module in action, check out the screen recording below:

[![Sample Submission Module Demo](https://img.youtube.com/vi/FOuBcOgGJ3U/0.jpg)](https://youtu.be/FOuBcOgGJ3U?si=oh6QRCjrrL_IuakB)

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contact

For any inquiries or support, please contact Nizamudheen MJ at [nizamudheenmj@gmail.com](mailto:nizamudheenmj@gmail.com).
