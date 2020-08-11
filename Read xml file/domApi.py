from urllib.request import urlopen
from xml.dom.minidom import parse
import xml.dom.minidom
# DOMTree=xml.dom.minidom.parse("movies.xml")
DOMTree=xml.dom.minidom.parse(urlopen("https://www.nbkr.kg/XML/daily.xml"))
collection=DOMTree.documentElement

if collection.hasAttribute("Name"):
    print("Collection ",collection.getAttribute('Name'))

currencies=collection.getElementsByTagName('Currency')
for currency in currencies:
    code=currency.getAttribute('ISOCode')
    Nominal=currency.getElementsByTagName('Nominal')[0].childNodes[0].data
    value=currency.getElementsByTagName('Value')[0].childNodes[0].data
    print("Code:",code)
    print("Nominal:",Nominal)
    print("Value:",value)

# <CurrencyRates Name="Daily Exchange Rates" Date="11.08.2020">
# <Currency ISOCode="USD">
# <Nominal>1</Nominal>
# <Value>77,4202</Value>
# </Currency>
# <Currency ISOCode="EUR">
# <Nominal>1</Nominal>
# <Value>91,1352</Value>
# </Currency>
# <Currency ISOCode="KZT">
# <Nominal>1</Nominal>
# <Value>0,1851</Value>
# </Currency>
# <Currency ISOCode="RUB">
# <Nominal>1</Nominal>
# <Value>1,0494</Value>
# </Currency>
# </CurrencyRates>