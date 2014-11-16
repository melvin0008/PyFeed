#!/venv/bin/env python
#Copyright Melvin me@melvinphilips.com
import constants
from utilities import *


class CategorySubCat(object):
	"""docstring for Article"""
	categories=constants.cat
	subcategories=constants.subcat

	def getcategoryid(self,category=None):
		if category is None:
			return [ x for x in self.categories.keys()]	
		try :
			return self.categories[category]
		except KeyError:
			
			allcat=[x for x in self.categories.keys()]
			print "Error: Categories should be one of these "+", ".join(allcat)
			return None

	def getcategorysubcategoryids(self,category,subcategory=None):
		if subcategory is None:
			return [x[1] for x in self.subcategories.keys() if x[0]==category]
		try:
			ret=self.subcategories[category,subcategory]
			return ret['category_id'],ret['subcategory_id']
		except KeyError:
			return None
				

class Article(object):
	"""docstring for Article"""
	def __init__(self,list_title=None,description=None,articlelist=None):
		self.list_title = list_title
		self.description = description
		self.articlelist = articlelist

class ArticleItem(object):
	"""docstring for ArticleItem"""
	def __init__(self, publish_date=None,source=None,source_url=None,summary=None,title=None,url=None,author=None):
		self.publish_date=publish_date
		self.source=source
		self.source_url=source_url
		self.summary=summary
		self.title=title
		self.url=url
		self.author=author

