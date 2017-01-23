import urllib

produkterlaster = urllib.URLopener()
produkterlaster.retrieve("https://www.vinmonopolet.no/medias/sys_master/products/products/hbc/hb0/8834253127710/produkter.csv", "produkter_raw.csv")
produkterlaster.close()
