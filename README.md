PyFeed
======

Python Wrapper for Feedzilla Api

Feedzilla-Api
=====

Obtain News Feeds from All over the world using this python wrapper Feedzilla -Api

Usage
==========
## To get all Categories

### feed=FeedzillaApi()
### feed.knowallcategories()

## To Get a SubCategory of a known Category
### feed=FeedzillaApi()
### feed.knowallcategories(<name of the Category>)
### example : feed.knowallcategories("sports")


## To Get an Article
feed=FeedzillaApi()
feed.getArticles({{name of category}},{{name of SubCategory}}>,count={{count}},since={{since}},order={{popular | none(default) }},title_only={{1|0}})

**Parameters:**

| Name | Type | Description | Required or Not|Example     |
| ---- | ---- | ----------- | ----------- ---|------------|
| `category` | string | Name of the Category | Required| "art" |
| `subcategory` | string | Name of the SubCategory | Optional| "photography"|
| `count` | integer | Count of articles | Optional| 10 |
| `order` | string | The sort order of the list to be returned. | Optional| "popular" or "none"  |
| `title_only` | integer | returns only title if set to 1 | Optional| 1|


Examples
==========
###feed=FeedzillaApi()
### feed.getArticles("sports",order="popular")
###feed.getArticles("art","photography",count=5,since="2012-05-05")

## Returned Value is an Article which contains
### articlelist : A List of articleItem objects
### list_title: A String with the title of the list
### description : A String with the description 
--------
## An Article List contains ArticleItem objects which contains
### publish_date : A string with the publish date
### source : A string with the source of the article feed
### source_url : A string with the source url of the article
### summary : A string with the summary of the article
### title : A string with the title of the article
### url : A string with the url of the article

Parsing Examples
========
###feed=FeedzillaApi()
### article=feed.getArticles("sports",order="popular")
### articlelist=article.articlelist
### description=article.description
### list_title=article.list_title

### To get info of the any article
### articleurl = articlelist[0].url
### articlesource = articlelist[0].source
### articletitle = articlelist[0].title
### articlesourceurl = articlelist[0].source_url
### articlesummary = articlelist[0].summary
### articlepublishdate=articlelist[0].publish_date

Contribute
========

If you want to add any new features, or improve existing ones, feel free to send a pull request!
Will soon be adding the search query feature
