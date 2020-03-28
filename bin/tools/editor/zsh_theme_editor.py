import os
import re

class ThemeEditor:

	__profile_contents = ''
	__profile_path = ''

	def __init__(self,profile_contents,profile_path):
		self.__profile_contents = profile_contents
		self.__profile_path = profile_path

	def set_theme(self,theme):
		regex = re.compile(r"ZSH_THEME=\"[^\"]*\"", re.S)
		replacement = 'ZSH_THEME="'+theme+'"'
		new_profile = re.sub(regex, replacement, self.__profile_contents)
		with open(self.__profile_path, "w") as f:
			f.write(new_profile)