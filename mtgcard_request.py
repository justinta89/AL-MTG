def mtgcard_request(cardname, cardset):
  
   import requests
   import json

   # The cardset is optional, but if included it will give the most accurate results
   r = requests.get('http://magictcgprices.appspot.com/api/cfb/price.json?cardname=%s&cardset=%s' % (cardname, cardset))
   data = json.loads(r.text)
   """
   Different places to check card prices, all using magictcgprices api:
   	ebay:  http://magictcgprices.appspot.com/api/ebay/price.json?cardname=%s&cardset=%s
   	tcgplayer:  http://magictcgprices.appspot.com/api/tcgplayer/price.json?cardname=%s&cardset=%s
   	channel fireball:  http://magictcgprices.appspot.com/api/cfb/price.json?cardname=%s&setname=%s
   """
   
   price = data[0]

   return "Price of Card: %s" % price

if __name__ == "__main__":
	import sys
	# cardname = sys.argv[1]
	# cardset = sys.argv[2]
	cardname = raw_input("What card do you want? ")
	cardset = raw_input("What set is it in? ")
	print mtgcard_request(cardname, cardset)
