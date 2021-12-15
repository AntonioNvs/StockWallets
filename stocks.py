from urllib.request import urlopen
from bs4 import BeautifulSoup


def get_stocks_value(stocksSymbols: list):
  url = 'https://valorinveste.globo.com/cotacoes/'
  
  result = urlopen(url).read()
  soup = BeautifulSoup(result, 'html.parser')

  html_stocks = soup.find('table').find_all('tr')

  """
    Para cada 'tr', possui:
    - Nome do ativo
    - Código
    - Última cotação
    - Variação
    - Fechamento
  """

  stocks: list = []
  all_ = []

  for s in html_stocks:
    try:
      tds = s.find_all('td')
      
      symbol = tds[1].text.strip()
    
      if symbol in stocksSymbols:
        value = float(tds[3].text.replace('%', '').strip().replace(',', '.'))
        last_price = float(tds[2].text.replace(',', '.'))

        stocks.append((symbol, last_price, value))

      all_.append(tds[1].text)

    except IndexError as e:
      pass

  return stocks

if __name__ == '__main__':
  print(get_stocks_value(['ABEV3']))