#!/venv/bin/env python
from json import load
from pyfeedClass import CategorySubCat
from utilities import *
#class Category(object):
	
class FeedzillaApi(object):
	"""docstring for FeedzillaApi"""
	FeedzillaApicategories= "http://api.feedzilla.com/v1/categories/"
	FeedzillaApiSubcategory="/subcategories/"
	FeedzillaApiArticles="/articles.json"

	def buildquery(self,x,i,querypart):
		if not x:
			return querypart
		key,value =x.popitem()
		if value != None:
			if i==0:
				querypart=querypart+key+"="+str(value)
				i=1
			else:
				querypart=querypart+"&"+key+"="+str(value)
		return self.buildquery(x,i,querypart)
	
	def getArticles(self,category,subcategory=None,count=None,since=None,order=None,title_only=None):
		query=""
		if count!=None or since!=None or order!=None or title_only!=None:
			query=self.buildquery({"count":count,"since":since,"order":order,"title_only":title_only},0,"?")
			print query
		c=CategorySubCat()
		if subcategory==None:
			cid=c.getcategoryid(category)
			finalFeedzillaApi=self.FeedzillaApicategories+str(cid)+self.FeedzillaApiArticles+query	
		else:
			cid,subid=c.getcategorysubcategoryids(category,subcategory)
			finalFeedzillaApi=self.FeedzillaApicategories+str(cid)+self.FeedzillaApiSubcategory+str(subid)+self.FeedzillaApiArticles+query

		print finalFeedzillaApi

f=FeedzillaApi()
f.getArticles("art","photography",since="2012/05/05",title_only=1)

