# This thing is going crawl Bulbapedia for all Pokemon and their stats and store them as python classes so I can use them without typing up 803 classes.
# It's not close to finished


import urllib.request


pkmn = "Pikachu"
fp = urllib.request.urlopen("http://bulbapedia.bulbagarden.net/wiki/" + pkmn)
byteurl = fp.read()
strpage = byteurl.decode("utf-8").encode('utf-8')
fp.close()
statchunk = str(strpage)[str(strpage).find('<a href="/wiki/Statistic" title="Statistic">'):str(strpage).find('Minimum stats are calc')]
print(statchunk)