#!/Users/timrand/anaconda3/bin/python
import sys
import pickle
query_term, abs_num, year = sys.argv[1:4]
print(f'downloading {abs_num} abstracts from year: {year} for query: {query_term}...')

from metapub import PubMedFetcher
fetch = PubMedFetcher()

# Get the first n abstracts for a given search term
def get_articles(search_term, n, year=None):   
	# get n pmids for search query
	pmids = fetch.pmids_for_query(search_term, retmax=n, year=year)
	# get list of abstracts from pmids:
	articles = {}
	final=[]
	for pmid in pmids:  
		articles[pmid] = fetch.article_by_pmid(pmid)
		_year = articles[pmid].year
		if _year != None and int(_year) in range(int(year)-1,int(year)+2):
			#print(f'adding article with date: {_year}')
			final.append(articles[pmid].abstract)
	return final

def down_load_and_pickle(query, num, year=None):
	out_file = f'../pickles/raw_abstracts/{year}_{query}_articles.pkl'
	try:
		articles = get_articles(query, num, year)
		pickle.dump( articles, open( out_file, "wb" ) )
	except:
		print('error occured')
	print('finished pickling articles to:' + out_file)

down_load_and_pickle(query_term, abs_num, year)

#loading:    
#loaded_p53 = pickle.load(open('pickles/raw_abstracts/p53_abstracts.pkl', 'rb'))