from pyfeed import FeedzillaApi


feed=FeedzillaApi()
art1=feed.getArticles("art","photography",count=5,since="2014-05-05")
print art1.articlelist[0].url

allarticles=feed.getArticles("art")
print [x.url for x in allarticles.articlelist]

print feed.knowallcategories()
print feed.knowsubcategories("art")
allarticles=feed.getArticles("sports")
print [{"url":x.url,"source":x.source, "summary":x.summary} for x in allarticles.articlelist]
articlelist=allarticles.articlelist
print "Url"+articlelist[0].url