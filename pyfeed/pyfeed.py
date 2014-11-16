#!/venv/bin/env python
#Copyright Melvin me@melvinphilips.com
from pyfeedClass import CategorySubCat
from pyfeedClass import ArticleItem
from pyfeedClass import Article
from utilities import *
import simplejson
from urllib2 import urlopen
from sys import exit
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
				if cid!=None:
					finalFeedzillaApi=self.FeedzillaApicategories+str(cid)+self.FeedzillaApiArticles+query
					print finalFeedzillaApi
				else:
					exit(1)
			else:
				try:
					cid,subid=c.getcategorysubcategoryids(category,subcategory)
					finalFeedzillaApi=self.FeedzillaApicategories+str(cid)+self.FeedzillaApiSubcategory+str(subid)+self.FeedzillaApiArticles+query
				except (TypeError):
					print "Incorrect Pair of Category and Subcategory"
					exit(1)

			feeds= self.openurldecodesimplejson(finalFeedzillaApi)
			articlelist=self.makefeedslist(getlistitem(feeds,'articles'))
			return Article(getlistitem(feeds,'list_title'),getlistitem(feeds,'description'),articlelist)


	def makefeedslist(self,articledictionary):
		articlelist=[]
		for article in 	articledictionary:
			articleitem=ArticleItem(getlistitem(article,'publish_date'),getlistitem(article,'source'),getlistitem(article,'source_url'),getlistitem(article,'summary'),getlistitem(article,'title'),getlistitem(article,'url'),getlistitem(article,'author'))
			articlelist.append(articleitem)
		return articlelist

	def openurldecodesimplejson(self, url):
		try:		
			query_data = urlopen(url).read()
			return simplejson.loads(query_data)
		except Exception:
			print "Error in connection to the Internet"
			exit(1)



if __name__ == '__main__':
    pass