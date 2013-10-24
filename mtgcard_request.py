def mtgcard_request(cardname, cardset):
  
   import requests
   import json

   # Card Image
   ci_response = requests.get('http://magictcgprices.appspot.com/api/tcgplayer/price.json?cardname=%s&cardset=%s' % (cardname, cardset))
   ci_data = json.loads(ci_response.text)

   # Ebay (lowest price)
   ebay_response = requests.get('http://magictcgprices.appspot.com/api/ebay/price.json?cardname=%s&cardset=%s' % (cardname, cardset))
   ebay_data = json.loads(ebay_response.text)

   # Channel Fireball
   cfb_response = requests.get('http://magictcgprices.appspot.com/api/cfb/price.json?cardname=%s&setname=%s' % (cardname, cardset))
   cfb_data = json.loads(cfb_response.text)

   # TCGPlayer, this gives 3 outputs. low, med, high
   tcgplayer_response = requests.get('http://magictcgprices.appspot.com/api/tcgplayer/price.json?cardname=%s&cardset=%s' % (cardname, cardset))
   tcg_data = json.loads(tcgplayer_response.text)


   # Set variable for each different api location
   ci_price = "\nCard Image: %s" % (ci_data[0])
   ebay_price = "\nEbay (Lowest Price): %s" % (ebay_data[0])
   cfb_price = "\nChannel Fireball: %s" % (cfb_data[0])
   tcg_price = "\nTCGPlayer: \nLow: %s \nMedium: %s \nHigh: %s" % (tcg_data[0], tcg_data[1], tcg_data[2])
   
   all_prices = [ci_price, ebay_price, cfb_price, tcg_price]
   
   for ap in all_prices:
   	return ap
   

if __name__ == "__main__":
	import sys
	# cardname = sys.argv[1]
	# cardset = sys.argv[2]
	cardname = raw_input("What card do you want? ")
	cardset = raw_input("What set is it in? ")
	print mtgcard_request(cardname, cardset)
