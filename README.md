# item_similarity

There are two folders in here:
1. src_item_identical: contains my solution to pairwise-similar items' list printing part. 
2. src_search_related: contains the additional search-improvement part.

I decided to structure my code into 4 modules:
1) a search_interface() which works like a main function to handle calls between modules and finally prints the required output.
2) a query_processor module where the processor() is a function that cleans the userinput text into valid input. It also calls the "getSearchKeywordsRecommendation" present in a 3rd module and returns result to search_interface() if any recommendation obtained. 
Else, the processed user_input is returned to proceed with item lookup.
3) a search_api module where search_fn() is the function where my two finding API calls are present. The "getSearchKeywordsRecommendation" call is here. The "findItemsByKeywords" call is made by search_interface then to perform item lookup
with keyword returned by processor() earlier and it returns results found.
4) a similarity module where the sim() function works on the list of results returned by search_fn() earlier and implements the "similar item lookup".

I decided to implement the definition of similarity from the perspective of title similarity i.e. how close do two titles match. By assigning a score to the match, I obtained the most similar item. I set a threshold on the score and only if the score exceeded the threshold would I keep that item pair. So, I used scipy's cosine similarity test for the same. I created a list of unique words present
in titles returned by "findItemsByKeywords". For 100 items returned, each with 5 words in their titles, I would create a list of all unique words from the pool of 500 words. Say, its length was m < 500.

Now, i also observed that duplicates were often present in the list of items returned by "findItemsByKeywords" and so, i stored only the unique items and passed their list to sim() function. This was done to ensure that the item most similar is not the current item itself. So, suppose we got n number of unique items out of 100 items returned. Then, we can construct a nxm matrix, representing each item title as a feature vector (vector[i] = 1 if title has matching word in ith column out of the m columns and 0 elsewhere). Thus, having obtained a feature vector for titles, I checked the feature vector of every other item and retained the item that scored highest on cosine similarity test and crossed a threshold value. I chose a threshold of 0.5 to make it bit strict. I returned the item pairs that satisfied the criteria to search_interface() that printed the same.
