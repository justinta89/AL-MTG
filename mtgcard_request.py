def mtgcard_request(cardname, cardset):
  
   import requests
   import json

   # The cardset is optional, but if included it will give the most accurate results
   response = requests.get('http://magictcgprices.appspot.com/api/tcgplayer/price.json?cardname=%s&cardset=%s' % (cardname, cardset)) # Card Image
   data = json.loads(response.text)

   price = "Low: %s \nMedium: %s \nHigh: %s" % (data[0], data[1], data[2])

   """
   Different places to check card prices, all using magictcgprices api:
           card image: http://magictcgprices.appspot.com/api/cfb/price.json?cardname=%s&cardset=%s  # mainly using this one. Outputs med price
           ebay:  http://magictcgprices.appspot.com/api/ebay/price.json?cardname=%s&cardset=%s
           tcgplayer:  http://magictcgprices.appspot.com/api/tcgplayer/price.json?cardname=%s&cardset=%s
                This one outputs low, medium, and high prices. 
           channel fireball:  http://magictcgprices.appspot.com/api/cfb/price.json?cardname=%s&setname=%s
   """

   return price

if __name__ == "__main__":
	import sys
	# cardname = sys.argv[1]
	# cardset = sys.argv[2]
	cardname = raw_input("What card do you want? ")
	cardset = raw_input("What set is it in? ")
	print mtgcard_request(cardname, cardset)
