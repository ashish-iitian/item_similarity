I went on to design a better item search system to return list of products similar to what the user entered as keyword. So, the code structure I had was similar to what I explained above. Except that instead of the similarity module, i had a related module with sim() that took list of item titles as input. Then it counted the instances of each word in the pool of titlewords and picked a word not part of userentered text that occurred the most number of times in "findItemsByKeywords" result. This word was suffixed to the original user input to create a new keyword and such a keywordextension method was used to show a wider range of "similar" products to the user.