import urllib
import urllib2
import json
import sys
#from nltk.corpus import wordnet as wn
from ebay_project_parser import query_processor
from ebay_project_api import search_api
from ebay_project_related import related

def search_interface():

	''' main function that handles calls between different modules for query processing
		and item look-up to deliver related items '''

	user_input = sys.stdin.readline()
	my_ebay_appID = 'AshishKu-aa42-4edf-a0eb-0309204c7659'	#raw_input()
	query = query_processor()
	input_processed = query.processor(user_input,my_ebay_appID)
	if input_processed == 'Invalid input':
		print 'Invalid input. Please re-enter keyword'
		return
	searcher = search_api()
	operation = 'findItemsByKeywords'
	ret = searcher.search_fn(input_processed, my_ebay_appID, operation)
	if ret == '-1':
		print "\n No match found for the entered query. Search for something else.\n"
		return
	else:
		results, count = ret
		final_keyword = related.sim(results, input_processed)
		results = searcher.search_fn(final_keyword, my_ebay_appID, operation)	
		if results == '-1':
			print "No match found"
			return
		else:
			items, cnt = results
			print 'Item ID \t Item Title'
			print '------------ \t------------'
			print '\n'.join(items)	


print "Enter the keyword(s)\n" 
search_interface()
	
