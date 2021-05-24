import webbrowser
import os
from fpdf import FPDF
from filestack import Client


class PdfReport:

    def __init__(self, filename) -> object:
        self.filename = filename

    def generate(self, item_1, item_2, item_3, invoice):
        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        # Add Image
        pdf.image("images/sweepsouth.png", w=50, h=50)

        # Insert Title
        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h=80, txt="Invoice", border=0, align='C', ln=1)

        # Insert Date
        pdf.set_font(family='Times', size=14, style='B')
        pdf.cell(w=100, h=40, txt="Date: ", border=0)
        pdf.cell(w=150, h=40, txt=str(invoice.date), border=0, ln=1)

        # Insert Contractor
        pdf.set_font(family='Times', size=14, style='B')
        pdf.cell(w=100, h=40, txt="Contractor: ", border=0)
        pdf.cell(w=150, h=40, txt=str(invoice.name_1), border=0)
        pdf.cell(w=100, h=40, txt="Company: ", border=0)
        pdf.cell(w=150, h=40, txt=str(invoice.company), border=0, ln=1)

        # Insert Customer Name
        pdf.set_font(family='Times', size=14, style='B')
        pdf.cell(w=100, h=40, txt="Customer: ", border=0)
        pdf.cell(w=150, h=40, txt=str(invoice.name_2), border=0)
        pdf.cell(w=100, h=40, txt="Address: ", border=0)
        pdf.cell(w=150, h=40, txt=str(invoice.address), border=0, ln=1)

        # Spacer
        pdf.cell(w=300, h=25, txt="", border=0, ln=1)

        # Insert Table Headings
        pdf.cell(w=150, h=25, txt='Description', border="B")
        pdf.cell(w=75, h=25, txt='Quantity', border="B")
        pdf.cell(w=50, h=25, txt='Price', border="B")
        pdf.cell(w=75, h=25, txt='Subtotal', border="B")
        pdf.cell(w=50, h=25, txt='Currency', border="B", ln=1)


        # Insert Description 1
        pdf.cell(w=150, h=25, txt=str(item_1.description), border=0)
        pdf.cell(w=75, h=25, txt=str(item_1.quantity), border=0)
        pdf.cell(w=50, h=25, txt=str(item_1.price), border=0)
        pdf.cell(w=75, h=25, txt=str(item_1.subtotal), border=0)
        pdf.cell(w=50, h=25, txt=str(invoice.currency1), border=0, ln=1)

        # Insert Description 2
        pdf.cell(w=150, h=25, txt=str(item_2.description), border=0)
        pdf.cell(w=75, h=25, txt=str(item_2.quantity), border=0)
        pdf.cell(w=50, h=25, txt=str(item_2.price), border=0)
        pdf.cell(w=75, h=25, txt=str(item_2.subtotal), border=0)
        pdf.cell(w=50, h=25, txt=str(invoice.currency1), border=0, ln=1)

        # Insert Description 3
        pdf.cell(w=150, h=25, txt=str(item_3.description), border=0)
        pdf.cell(w=75, h=25, txt=str(item_3.quantity), border=0)
        pdf.cell(w=50, h=25, txt=str(item_3.price), border=0)
        pdf.cell(w=75, h=25, txt=str(item_3.subtotal), border=0)
        pdf.cell(w=50, h=25, txt=str(invoice.currency1), border=0, ln=1)


        # Insert Total Price
        pdf.cell(w=225, h=40, txt="", border="T", align="R")
        pdf.cell(w=50, h=40, txt="Total = ", border="T", align="R")
        pdf.cell(w=75, h=40, txt=str(invoice.total), border="T")
        pdf.cell(w=50, h=40, txt=str(invoice.currency2), border="T", align="L")



        # Change directory
        #os.chdir("templates")

        # Ouput PDF
        pdf.output(self.filename)

        # Auto open in windows
        #webbrowser.open(self.filename)


class FileSharer:

    def __init__(self, filepath, api_key='AViVqp7suSQWWEdrl6hf9z'):
        self.api_key = api_key
        self.filepath = filepath

    # Uploads File and outputs URL link
    def share(self):
        client = Client(self.api_key)
        new_filelink = client.upload(filepath=self.filepath)
        return new_filelink.url