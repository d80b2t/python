"""
http://docs.python-guide.org/en/latest/scenarios/scrape/
"""

from lxml import html
import requests

page = requests.get('http://econpy.pythonanywhere.com/ex/001.html')
#page = requests.get('http://www.politico.com/2016-election/results/map/president/pennsylvania//001.html')
tree = html.fromstring(page.content)


"""
In the .html:

<div title="buyer-name">Carson Busses</div>
<span class="item-price">$29.95</span>

"""


#This will create a list of buyers:
buyers = tree.xpath('//div[@title="buyer-name"]/text()')
#This will create a list of prices
prices = tree.xpath('//span[@class="item-price"]/text()')

print('Buyers: ', buyers)
print('Prices: ', prices)
