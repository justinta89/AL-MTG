def mtgCardRequest(cardname, cardset):
  
   import requests
   import json

   # Ebay (lowest price)
   ebay_response = requests.get('http://magictcgprices.appspot.com/api/ebay/price.json?cardname=%s&cardset=%s' % (cardname, cardset))
   ebay_data = json.loads(ebay_response.text)

   # TCGPlayer, this gives 3 outputs. low, med, high
   tcgplayer_response = requests.get('http://magictcgprices.appspot.com/api/tcgplayer/price.json?cardname=%s&cardset=%s' % (cardname, cardset))
   tcg_data = json.loads(tcgplayer_response.text)

   # Set variable for each different api location
   ebay_price = ebay_data[0]
   tcg_low = tcg_data[0]
   tcg_med = tcg_data[1]
   tcg_high = tcg_data[2]

   # Price dictionary
   all_prices = {
         'Ebay': ebay_price,
         'TCGPlayer Low': tcg_low,
         'TCGPlayer Median': tcg_med,
         'TCGPlayer High': tcg_high
   }

   return all_prices

if __name__ == "__main__":
	import sys
	# cardname = sys.argv[1]
	# cardset = sys.argv[2]
	cardname = raw_input("What card do you want? ")
	cardset = raw_input("What set is it in? ")
	print mtgCardRequest(cardname, cardset)
