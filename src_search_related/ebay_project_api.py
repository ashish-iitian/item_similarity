import urllib
import urllib2
import json
import sys

def strip_unicode(strn):
		
	''' get rid of unicode'''
	
	ls = [x for x in strn if 0 < ord(x) <= 127]
	word = ''.join(ls)
	return word


class search_api:

	def __init__(self):
		self.service_url = 'https://svcs.ebay.com/services/search/FindingService/v1?'


	def search_fn(self, keyword, my_appname, operation):

		''' accepts user-entered query to perform item look-up or best match query look-up 
		for user-input by calling relevant api '''
	
		service_params = { 'OPERATION-NAME' : operation,
                           'SERVICE-VERSION' : '1.0.0',
                           'RESPONSE-DATA-FORMAT' : 'JSON',
                           'keywords' : keyword,
                           'SECURITY-APPNAME' : my_appname }
		my_url = self.service_url + urllib.urlencode(service_params)
		req = urllib2.Request(my_url)

		if operation == 'findItemsByKeywords':
			response = urllib2.urlopen(req)
			response_json = json.loads(response.read())
			ret_list = response_json['findItemsByKeywordsResponse'][0]['searchResult'][0]

			if int(ret_list['@count']) == 0:
				return "-1"
			else:
				item_list = ret_list['item']
				item_pairs = [item_list[i]['itemId'][0] + '\t' + strip_unicode(item_list[i]['title'][0]) for i in xrange(len(item_list))]
				return item_pairs, int(ret_list['@count'])
		
		elif operation == 'getSearchKeywordsRecommendation':
			
	# possible error handling or correct keyword extraction

			try:
				response = urllib2.urlopen(req)
				response_json = json.loads(response.read())
				keyword = response_json['getSearchKeywordsRecommendationResponse'][0]['keywords']#[0]['item']
				return str(keyword)[3:-2]
			
			except Exception as e:
				return "ERROR"	
			
