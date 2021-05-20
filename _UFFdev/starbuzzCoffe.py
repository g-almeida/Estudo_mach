import urllib.request

page = urllib.request.urlopen("http://www.beans-r-us.biz/prices.html")
text = page.read().decode("utf8")
localizacao = text.find('>$')
localizacao1 = localizacao + 1
localizacao2 = localizacao + 4
print (localizacao)
price = text[localizacao1 : localizacao2]
print(price)