#!/usr/bin/env python
from json import load
import constants


class CategorySubCat(object):
	"""docstring for Article"""
	categories=constants.cat
	subcategories=constants.subcat

	def getcategoryid(self,category=None):
		if category is None:
			l=[]
			for x in self.categories.keys():
				l.append(x)
			return l
		return self.categories[category]

	def getcatandsubcatid(self,category,subcategory=None):
		if subcategory is None:
			l=[]
			for x in self.subcategories.keys():

				if x[0]==category:
					l.append(x[1])
			return l
		else:
			ret=self.subcategories[category,subcategory]
			return ret['category_id'],ret['subcategory_id']	

class Article(object):
	"""docstring for Article"""
	def __init__(self, arg):
		super(Article, self).__init__()
		self.arg = arg
		


c=CategorySubCat()
print c.getcatandsubcatid('art')
 
