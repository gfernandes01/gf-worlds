import pyshorteners

link = input('ENTRE com o LINK url: ')
print(pyshorteners.Shortener().clckru.short(link))