import urllib
import urllib2
import json
import sys

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
				item_id = [item_list[i]['itemId'][0] for i in xrange(len(item_list))]
				item_titles = [item_list[i]['title'][0] for i in xrange(len(item_list))] 

				return item_id, item_titles, int(ret_list['@count'])
		
		elif operation == 'getSearchKeywordsRecommendation':
			
	# implement error handling or best keyword recommendation

			try:
				response = urllib2.urlopen(req)
				response_json = json.loads(response.read())
				keyword = response_json['getSearchKeywordsRecommendationResponse'][0]['keywords']#[0]['item']
				return str(keyword)[3:-2]
			
			except Exception as e:
				print '\n SOMETHING WRONG IN RECOMMENDATION SYSTEM\n'
				return "ERROR"
			
