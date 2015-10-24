import urllib

produkterlaster = urllib.URLopener()
produkterlaster.retrieve("http://www.vinmonopolet.no/api/produkter", "produkter_raw.csv")
produkterlaster.close()
