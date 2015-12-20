# item_similarity

There are two folders in here:
1. src_item_identical: contains my solution to pairwise-similar items' list printing part. 
2. src_search_related: contains the additional search-improvement part.

I decided to structure my code into 4 modules:
1) a search_interface() which works like a main function to handle calls between modules and finally prints the required output.
2 a query_processor module where the processor() is a function that cleans the userinput text into valid input. It also calls the "getSearchKeywordsRecommendation" present in a 3rd module and returns result to search_interface() if any recommendation obtained. 
Else, the processed user_input is returned to proceed with item lookup.
3) a search_api module where search_fn() is the function where my two finding API calls are present. The "getSearchKeywordsRecommendation" call is here. The "findItemsByKeywords" call is made by search_interface then to perform item lookup
with keyword returned by processor() earlier and it returns results found.
4) a similarity module where the sim() function works on the list of results returned by search_fn() earlier and implements the "similar item lookup".
