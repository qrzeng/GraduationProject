import whoosh.index as index  
from whoosh import columns, fields, index, sorting  
from whoosh.qparser import QueryParser  
  
ix = index.open_dir("indexdir1")  
searcher = ix.searcher()  
searchwords="人民"  
qp = QueryParser("title", schema=ix.schema)  
q = qp.parse(searchwords)  
results = searcher.search(q)  
for item in results:
	print(item) 