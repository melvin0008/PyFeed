#!/usr/bin/env python
from json import load
import constants


class Article(object):
	"""docstring for Article"""
	categories=constants.cat
	subcategories=constants.subcat

	def getcategory(self,category):

 