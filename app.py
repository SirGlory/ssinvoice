from datetime import date
from flask import Flask, render_template, request
from werkzeug.utils import redirect
from flask_bootstrap import Bootstrap
from convert import Convert
from forms import InvoiceForm
from pdfreport import PdfReport, FileSharer
from item import Invoice, Item

app = Flask(__name__)
app.secret_key = 'mrZball'


# set default button style and size, will be overwritten by macro parameters
app.config['BOOTSTRAP_BTN_STYLE'] = 'primary'
app.config['BOOTSTRAP_BTN_SIZE'] = 'sm'


bootstrap = Bootstrap(app)


@app.route('/')
def index():
    form = InvoiceForm()
    return render_template('index.html', form=form)


@app.route('/invoice', methods=['POST'])
def pdfgen():
    invoice_form = InvoiceForm(request.form)

    name_1 = invoice_form.name1.data
    company = invoice_form.company.data
    currency_1 = invoice_form.currency1.data
    name_2 = invoice_form.address.data
    address = invoice_form.address.data
    currency_2 = invoice_form.currency2.data

    description_1 = invoice_form.item1.data
    quantity_1 = int(invoice_form.quantity1.data)
    price_1 = float(invoice_form.price1.data)

    description_2 = invoice_form.item2.data
    quantity_2 = int(invoice_form.quantity2.data)
    price_2 = float(invoice_form.price2.data)

    description_3 = invoice_form.item3.data
    quantity_3 = int(invoice_form.quantity3.data)
    price_3 = float(invoice_form.price3.data)
    print(description_1)
    print(quantity_1)
    print(price_1)

    # Calculate and convert total
    total = quantity_1*price_1 + quantity_2*price_2 + quantity_3*price_3
    total_converted = Convert(total=total, currency1=currency_1, currency2=currency_2).convert()
    the_invoice = Invoice(date=date.today(), name_1=name_1, name_2=name_2, company=company, address=address,
                          currency1=currency_1, currency2=currency_2, total=total_converted)

    # Create objects to send as params in pdf_report
    item_1 = Item(description=description_1,quantity=quantity_1,  price=price_1)
    item_2 = Item(description=description_2,quantity=quantity_2,  price=price_2)
    item_3 = Item(description=description_3,quantity=quantity_3,  price=price_3)

    # Generate PDF
    pdf_report = PdfReport(filename=f"Invoice_{the_invoice.date}_{the_invoice.name_2}.pdf")
    pdf_report.generate(item_1=item_1, item_2=item_2, item_3=item_3, invoice=the_invoice)

    # Share file on Cloud
    file_sharer = FileSharer(filepath=pdf_report.filename)
    print(file_sharer.share())
    return redirect(file_sharer.share())


if __name__ == '__main__':
    app.run(host="localhost", port=8000, debug=True)