# -*- coding: utf-8 -*- 
import json
cat={'art': {'category_id': 13, 'display_category_name': 'Art', 'english_category_name': 'Art'}, 'columnists': {'category_id': 588, 'display_category_name': 'Columnists', 'english_category_name': 'Columnists'}, 'celebrities': {'category_id': 5, 'display_category_name': 'Celebrities', 'english_category_name': 'Celebrities'}, 'it': {'category_id': 15, 'display_category_name': 'IT', 'english_category_name': 'IT'}, 'Sports': {'category_id': 1314, 'display_category_name': 'Sports', 'english_category_name': 'Sports'}, 'society': {'category_id': 4, 'display_category_name': 'Society', 'english_category_name': 'Society'}, 'religion-and-spirituality': {'category_id': 18, 'display_category_name': 'Religion And Spirituality', 'english_category_name': 'Religion And Spirituality'}, 'video': {'category_id': 590, 'display_category_name': 'Video', 'english_category_name': 'Video'}, 'hobbies': {'category_id': 14, 'display_category_name': 'Hobbies', 'english_category_name': 'Hobbies'}, 'politics': {'category_id': 3, 'display_category_name': 'Politics', 'english_category_name': 'Politics'}, 'technology': {'category_id': 30, 'display_category_name': 'Technology', 'english_category_name': 'Technology'}, 'universities': {'category_id': 12, 'display_category_name': 'Universities', 'english_category_name': 'Universities'}, 'world-news': {'category_id': 19, 'display_category_name': 'World News', 'english_category_name': 'World News'}, 'law': {'category_id': 591, 'display_category_name': 'Law', 'english_category_name': 'Law'}, 'usa': {'category_id': 7, 'display_category_name': 'USA', 'english_category_name': 'USA'}, 'entertainment': {'category_id': 6, 'display_category_name': 'Entertainment', 'english_category_name': 'Entertainment'}, 'top-blogs': {'category_id': 31, 'display_category_name': 'Top Blogs', 'english_category_name': 'Top Blogs'}, 'travel': {'category_id': 23, 'display_category_name': 'Travel', 'english_category_name': 'Travel'}, 'oddly-enough': {'category_id': 36, 'display_category_name': 'Oddly Enough', 'english_category_name': 'Oddly Enough'}, 'sports': {'category_id': 27, 'display_category_name': 'Sports', 'english_category_name': 'Sports'}, 'music': {'category_id': 29, 'display_category_name': 'Music', 'english_category_name': 'Music'}, 'internet': {'category_id': 28, 'display_category_name': 'Internet', 'english_category_name': 'Internet'}, 'health': {'category_id': 11, 'display_category_name': 'Health', 'english_category_name': 'Health'}, 'events': {'category_id': 17, 'display_category_name': 'Events', 'english_category_name': 'Events'}, 'video-games': {'category_id': 9, 'display_category_name': 'Video Games', 'english_category_name': 'Video Games'}, 'jobs': {'category_id': 33, 'display_category_name': 'Jobs', 'english_category_name': 'Jobs'}, 'business': {'category_id': 22, 'display_category_name': 'Business', 'english_category_name': 'Business'}, 'top-news': {'category_id': 26, 'display_category_name': 'Top News', 'english_category_name': 'Top News'}, 'general': {'category_id': 1168, 'display_category_name': 'General', 'english_category_name': 'General'}, 'life-style': {'category_id': 20, 'display_category_name': 'Life Style', 'english_category_name': 'Life Style'}, 'fun-stuff': {'category_id': 25, 'display_category_name': 'Fun Stuff', 'english_category_name': 'Fun Stuff'}, 'shopping': {'category_id': 34, 'display_category_name': 'Shopping', 'english_category_name': 'Shopping'}, 'science': {'category_id': 8, 'display_category_name': 'Science', 'english_category_name': 'Science'}, 'industry': {'category_id': 2, 'display_category_name': 'Industry', 'english_category_name': 'Industry'}, 'programming': {'category_id': 16, 'display_category_name': 'Programming', 'english_category_name': 'Programming'}, 'products': {'category_id': 10, 'display_category_name': 'Products', 'english_category_name': 'Products'}, 'blogs': {'category_id': 21, 'display_category_name': 'Blogs', 'english_category_name': 'Blogs'}}


d={}

for x in cat:
	 b={}
	 b['category_id']=x['category_id']
	 b['english_category_name']=x['english_category_name']
	 b['display_category_name']=x['display_category_name']
	 d[x['url_category_name']]=b

print d
	