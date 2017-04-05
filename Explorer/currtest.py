from yahoo_finance import Currency
eur_sek = Currency('EURSEK')
eur_sek.refresh()
print (eur_sek.get_bid())