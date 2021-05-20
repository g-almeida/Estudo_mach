import urllib.request

def get_price():
    page = urllib.request.urlopen("http://beans-r-us.appspot.com/prices.html")
    text = page.read().decode("utf8")
    where = text.find('>$')
    inicio_do_preco = where+2
    fim_do_preco = inicio_do_preco+4
    print(text[inicio_do_preco+fim_do_preco])
    return(text[inicio_do_preco+fim_do_preco])

preco = get_price()

print(preco)
