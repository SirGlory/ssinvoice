import requests


class Convert:

    def __init__(self, total, currency1, currency2):
        self.total = total
        self.currency1 = currency1
        self.currency2 = currency2

    def convert(self):
        # Pull latest exchange rates from Currency Layer
        response = requests.get("http://api.currencylayer.com/live?access_key=0449b3ea99942ddba9d1b44f748014bb")
        rates = response.json()['quotes']
        zar = rates['USDZAR']
        ngn = rates['USDNGN']
        kes = rates['USDKES']

        # Convert to USD as base
        if self.currency1=='ZAR':
            total_USD = self.total/zar
        elif self.currency1 == 'NGN':
            total_USD = self.total/ngn
        elif self.currency1 == 'KES':
            total_USD = self.total/ngn
        else :
            total_USD = self.total

        # Convert to Customer's Local Exchange Rate
        if self.currency2 =='ZAR':
            total_final = total_USD*zar
        elif self.currency2 == 'NGN':
            total_final = total_USD*ngn
        elif self.currency2 == 'KES':
            total_final = total_USD*kes
        else :
            total_final = total_USD

        total_final=round(total_final,2)
        return total_final




if __name__ == '__main__':
    converted = Convert(total=1400, currency1="ZAR", currency2="KES").convert()