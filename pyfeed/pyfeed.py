#!/venv/bin/env python
from json import load
from pyfeedClass import CategorySubCat
from utilities import *
import simplejson
from urllib2 import urlopen
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
		andvar=""
		if value != None:
			if i==0:
				i=1
			else:
				andvar="&"
			querypart=querypart+andvar+key+"="+str(value)
		return self.buildquery(x,i,querypart)

	def getArticles(self,category,subcategory=None,count=None,since=None,order=None,title_only=None):
		query=""
		if count!=None or since!=None or order!=None or title_only!=None:
			query=self.buildquery({"count":count,"since":since,"order":order,"title_only":title_only},0,"?")
							
		c=CategorySubCat()
		if subcategory==None:
			cid=c.getcategoryid(category)
			finalFeedzillaApi=self.FeedzillaApicategories+str(cid)+self.FeedzillaApiArticles+query	
		else:
			cid,subid=c.getcategorysubcategoryids(category,subcategory)
			finalFeedzillaApi=self.FeedzillaApicategories+str(cid)+self.FeedzillaApiSubcategory+str(subid)+self.FeedzillaApiArticles+query
		print self.openurldecodesimplejson(finalFeedzillaApi)

	def openurldecodejson(self, url):
	    #''' open a given url and returns the python object representation of a json string'''
	    query_data = urlopen(url)
	    return load(query_data)

	def openurldecodesimplejson(self, url):
		query_data = urlopen(url).read()
		print query_data
		return simplejson.loads(query_data)


f=FeedzillaApi()
f.getArticles("art",since="2012-05-05",title_only=1)

