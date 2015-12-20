import urllib
import urllib2
import json
import re
import string
from ebay_project_api import search_api


class query_processor:

	def __init__(self):
		self.finding_service_url = 'https://svcs.ebay.com/services/search/FindingService/v1?'	

	def processor(self, user_input, my_appname):
	
		''' takes user input as keyword to process, validates it and cleans it up and uses 
		getSearchKeywordsRecommendation api to obtain best match query to look for user-input '''
	
		if(user_input.isspace()):
			return "Invalid input"
		elif not bool(re.search(r'[\w]',user_input,re.IGNORECASE)):
			return "Invalid input"
		else:
			user_input = user_input.lstrip().rstrip() #remove starting/ending spaces
			spcl_charset = set(string.punctuation)
			ls = list(user_input)
			valid_char = [x for x in ls if x not in spcl_charset]
			user_input = ''.join(valid_char)

	# get rid of stopwords if any now

		with open('./src_item_identical/stopwords.txt','r+') as f:
			stopwords = f.read().split('\n')
		f.close()
		parsed_input = ''
		for word in user_input.split():
			if word in stopwords:
				pass
			else:
				parsed_input += word + ' '
		parsed_input = parsed_input[:-1] 	#get rid of terminating space
		
	# attempt eBay getSearchKeywordsRecommendation API to deal with spell errors etc.

		corrector = search_api()
		processed_input = corrector.search_fn(parsed_input, my_appname, 'getSearchKeywordsRecommendation')

		if processed_input == 'ERROR' or not processed_input:
			return parsed_input
		else:
			return processed_input


