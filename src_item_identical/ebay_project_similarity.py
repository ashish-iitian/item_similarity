import sys
from scipy import spatial


def strip_unicode(strn):

	''' get rid of unicode	'''
	
	ls = [x for x in strn if 0 < ord(x) <= 127]
	word = ''.join(ls)
	return word


class similarity:

	@staticmethod
	def sim(item_id, titles, item_count):
	
		''' takes list of items as input and returns list of items identical to it 
		using cosine similarity '''
	
		list_title_words = []
		word_list = []
		for title in titles:
			list_title_words.extend(title.split())

		# get rid of unicode

		for entry in list_title_words:
			word_list.append(strip_unicode(entry))

		unique_words = list(set(word_list))
		column = len(unique_words)

		# compute matrix for cosine similarity test between titles
		# define similarity threshold of 0.5

		matrix = [[0]*column for x in xrange(item_count)]
		for i in xrange(item_count):
			for word in titles[i].split():
				for j in xrange(column):
					if unique_words[j] == word:
						matrix[i][j] = 1
						break
		similar_item_list = []

		for x in xrange(item_count):
			score = 0.0
			temp_id = 0
			temp_title = ''
			ls = []
			for y in xrange(item_count):
				if x == y:
					continue
				temp = 0
				temp = 1 - spatial.distance.cosine(matrix[x], matrix[y])
				if score < temp:
					score = temp
					temp_id = item_id[y]
					temp_title = titles[y]
					ls = matrix[y]
			if score > 0.5:
				entry = str(str(item_id[x]) + '\t' + str(temp_id))
				similar_item_list.append(entry)

			else:
				entry = str(str(item_id[x]) + '\t' + 'No match found')
				similar_item_list.append(entry)
		return similar_item_list


