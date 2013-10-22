def mtgcard_request(cardname, cardset):
  
   import requests
   import json

   r = requests.get('http://magictcgprices.appspot.com/api/cfb/price.json?cardname=%s&cardset=%s' % (cardname, cardset))
   data = json.loads(r.text)

   price = data[0]

   return "Price of Card: %s" % price

if __name__ == "__main__":
	import sys
	# cardname = sys.argv[1]
	# cardset = sys.argv[2]
	cardname = raw_input("What card do you want? ")
	cardset = raw_input("What set is it in? ")
	print mtgcard_request(cardname, cardset)
