import os
from tools.editor.zsh_alias_editor import AliasEditor
from tools.editor.zsh_theme_editor import ThemeEditor
from tools.editor.zsh_path_editor import PathEditor

class ZshEditor:

	__profile_path = ''
	__profile_contents = ''

	alias_editor = None
	theme_editor = None
	path_editor = None

	def __init__(self):
		self.profile_contents = ''
		self.__profile_path = os.path.join(os.path.expanduser('~'), '.zshrc')
		with open(self.__profile_path) as f:
			self.profile_contents = f.read()
		self.alias_editor = AliasEditor(self.profile_contents,self.__profile_path)
		self.theme_editor = ThemeEditor(self.profile_contents,self.__profile_path)
		self.path_editor = PathEditor(self.profile_contents,self.__profile_path)

	def open_editor(self):
		os.system('code '+self.__profile_path)

	def restore_defaults(self):
		with open(os.getcwd()+'/bin/tools/default.txt') as f:
			default_content = f.read()
		with open(self.__profile_path, "w") as f:
			f.write(default_content)
