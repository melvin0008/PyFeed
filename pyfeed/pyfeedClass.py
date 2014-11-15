#!/venv/bin/env python
from json import load
import constants
from utilities import *

class CategorySubCat(object):
	"""docstring for Article"""
	categories=constants.cat
	subcategories=constants.subcat

	def getcategoryid(self,category=None):
		if category is None:
			return [ x for x in self.categories.keys()]	
		return self.categories[category]

	def getcategorysubcategoryids(self,category,subcategory=None):
		if subcategory is None:
			return [x[1] for x in self.subcategories.keys() if x[0]==category]
		ret=self.subcategories[category,subcategory]
		return ret['category_id'],ret['subcategory_id']	

class Article(object):
	"""docstring for Article"""
	def __init__(self,list_title,description,articlelist):
		self.list_title = list_title
		self.description = description
		self.articlelist = articlelist
		



class ArticleItem(object):
	"""docstring for ArticleItem"""
	def __init__(self, publish_date,source,source_url,summary,title,url):
		self.publish_date=publish_date
		self.source=source
		self.source_url=source_url
		self.summary=summary
		self.title=title
		self.url=url

