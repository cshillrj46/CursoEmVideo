import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://www.google.com.br')
except urllib.error.URLError:
    print('ERRO 404.')
else:
    print('Tudo OK.')
