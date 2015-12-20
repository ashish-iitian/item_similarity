import urllib
import urllib2
import json
import sys
from ebay_project_parser import query_processor
from ebay_project_api import search_api
from ebay_project_similarity import similarity

def search_interface():

	''' main function that handles calls between different modules for query processing
		and item look-up to deliver identical item pairs '''

	user_input = sys.stdin.readline()
	my_ebay_appID = 'AshishKu-aa42-4edf-a0eb-0309204c7659'	#raw_input()
	query = query_processor()
	input_processed = query.processor(user_input,my_ebay_appID)
	if input_processed == 'Invalid input':
		print 'Invalid input. Please re-enter keyword'
		return
	print input_processed
	searcher = search_api()
	
	operation = 'findItemsByKeywords'
	ret = searcher.search_fn(input_processed, my_ebay_appID, operation)
	if ret == '-1':
		print "\n No match found for the entered query. Search for something else.\n"
		return
	else:
		results, result_titles, count = ret
		res = list(set(results))
		similar_items = similarity.sim(res, result_titles, len(res))
	
		print 'Item ID Is \t Most Similar To \t match score'
		print '------------ \t------------ \t'
		print '\n'.join(similar_items)
		return

print "\nEnter the keyword(s)\n"

search_interface()
	
