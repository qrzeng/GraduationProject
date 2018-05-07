import sqlite3
from whoosh.fields import Schema, STORED, NUMERIC, KEYWORD, TEXT
from whoosh.index import create_in
from whoosh.analysis import RegexAnalyzer

analyzer = RegexAnalyzer('([\u4e00-\u9fa5])|(\w+(\.?\w+)*)')
db_dir = 'news.db'
index_dir = 'indexdir1'
con = sqlite3.connect(db_dir)
cursor = con.cursor()
sql_str = 'select id, category, link, title, abstract from news'
cursor.execute(sql_str)
news = cursor.fetchall()

schema = Schema(news_id=NUMERIC(stored=True), 
	category=TEXT(stored=True,analyzer=analyzer),
	link=TEXT(stored=True,analyzer=analyzer),
	title=TEXT(stored=True,analyzer=analyzer),
	abstract=TEXT(stored=True,analyzer=analyzer))
ix = create_in(index_dir, schema)
writer = ix.writer()
for item in news:
	_id = item[0]
	_category = item[1]
	_link = item[2]
	_title = item[3]
	_abstract = item[4]
	writer.add_document(news_id=_id, category=_category, link=_link, title=_title, abstract=_abstract)
writer.commit()
con.close()
