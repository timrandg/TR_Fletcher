#!/Users/timrand/anaconda3/bin/python
import sys
import pickle
query_term, abs_num = sys.argv[1:3]
print(f'downloading {abs_num} abstracts for query: {query_term}...')


from metapub import PubMedFetcher
fetch = PubMedFetcher()

# Get the first n abstracts for a given search term
def get_abstracts(search_term, n):   
    # get n pmids for search query
    pmids = fetch.pmids_for_query(search_term, retmax=n)
    # get list of abstracts from pmids:
    abstracts = {}
    for pmid in pmids:
        abstracts[pmid] = fetch.article_by_pmid(pmid).abstract      
    return list(abstracts.values())

def down_load_and_pickle(query, num):
	try:
		abstracts = get_abstracts(query, num)
		out_file = f'../pickles/raw_abstracts/{query}_abstracts.pkl'
		pickle.dump( abstracts, open( out_file, "wb" ) )
	except:
		print('error occured')
	print('finished pickling abstracts to:' + out_file)

down_load_and_pickle(query_term, abs_num)

#loading:    
#loaded_p53 = pickle.load(open('pickles/raw_abstracts/p53_abstracts.pkl', 'rb'))