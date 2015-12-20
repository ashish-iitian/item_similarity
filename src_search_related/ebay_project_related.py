from collections import Counter

class related:

	@staticmethod
	def sim(titles, user_input):
		
		''' obtains user-input and returns a new query for retrieving items related to
		the user's query by learning from search-results for original query '''

		list_title_words = []
		word_list = []
		for title in titles:
			list_title_words.extend(title.split())

		for entry in list_title_words:
			ls = [x for x in entry if 0 < ord(x) <= 127]
			word = ''.join(ls)
			word_list.append(word)

		unique_words = set(word_list)

	# get rid of stopwords if any now

		with open('./src_search_related/stopwords.txt','r+') as f:
			stopwords = f.read().split('\n')
		f.close()
		
		filtered_words = unique_words - set(stopwords)
		title_words = [str(x).lower() for x in word_list if x in filtered_words and len(str(x)) > 2]
		occurences = list(Counter(title_words).items())
		occurences = sorted(occurences, key = lambda x: x[1], reverse = True)
		initial_input = user_input.lower().split()
		suffix = [ x[0] for x in occurences[:3] if x[0] not in initial_input ]
		return user_input+' '+suffix[0]
