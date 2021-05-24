from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField


currency_choices = [('ZAR', 'ZAR'), ('USD', 'USD'), ('NGN', 'NGN'),('KES', 'KES')]

class InvoiceForm(FlaskForm):
    name1 = StringField('Your Name', default="Greg")
    company = StringField('Company', default="PVT Dev")
    name2 = StringField("Customer's Name", default="Mr Ball")
    address = StringField('Address', default="89A Bree Street")

    item1 = StringField("Item 1", default="Cement")
    quantity1 = StringField('Quantity', default=30)
    price1 = StringField('Price', default=1)

    item2 = StringField("Item 2", default="Wood" )
    quantity2 = StringField('Quantity', default=30)
    price2 = StringField('Price',default=2)

    item3 = StringField("Item 3",default="Paint")
    quantity3 = StringField('Quantity',default=2)
    price3 = StringField('Price',default=5)

    currency1 = SelectField(u'Currency', choices=currency_choices)
    currency2 = SelectField(u'Currency', choices=currency_choices)

    submit = SubmitField('Generate Invoice')