import os
import re

class PathEditor:

    __profile_contents = ''
    __profile_path = ''

    def __init__(self,profile_contents,profile_path):
        self.__profile_contents = profile_contents
        self.__profile_path = profile_path

    def set_path(self, name, path):
        if self.__path_exists(path):
            return self.__overwite_path(name, path)
        return self.__create_new_path(name, path)

    def delete_path(self, name):
        if self.__path_exists(name):
            existing = re.findall(r"\nalias\s"+name+r"\=.*",self.__profile_contents)[0]
            new_contents = self.__profile_contents.replace(existing,"")
            with open(self.__profile_path, "w") as f:
                f.write(new_contents)
        return True
    
    def clear_all_paths(self):
        new_contents = self.__profile_contents
        for alias in re.findall(r"\nalias\s[^=]+\=.*",self.__profile_contents):
            new_contents = new_contents.replace(alias,'')
        with open(self.__profile_path, "w") as f:
            f.write(new_contents)
        return True

    def __overwite_path(self, name, command):
        existing = re.findall(r"alias\s"+name+r"\=.+",self.__profile_contents)[0]
        new_contents = self.__profile_contents.replace(existing,"alias "+name+"=\""+command+"\"")
        with open(self.__profile_path, "w") as f:
            f.write(new_contents)
        return True

    def __create_new_path(self, name, command):
        point = self.__find_alias_anchor_point()
        new_contents = self.__profile_contents[:point]+"\nalias "+name+"=\""+command+"\""+self.__profile_contents[point:]
        with open(self.__profile_path, "w") as f:
            f.write(new_contents)
        return True

    def __find_alias_anchor_point(self):

        alias_labeled_point = self.__find_alias_labeled_point()
        if alias_labeled_point != None:
            return alias_labeled_point

        alias_last_added_point = self.__find_last_added_point()
        if alias_last_added_point != None:
            return alias_last_added_point

        return len(self.__profile_contents)

    def __find_alias_labeled_point(self):
        result = re.search(r"\#\s?Aliases[^\n]*", self.__profile_contents, re.MULTILINE | re.IGNORECASE)
        if result == None:
            return None
        return result.end()

    def __find_last_added_point(self):
        result = re.search(r"\nAlias\s+[^=]*\=.*", self.__profile_contents, re.MULTILINE | re.IGNORECASE)
        if result == None:
            return None
        return result.start()

    def __path_exists(self, name):
        if re.search(r"alias\s"+name+r"\=",self.__profile_contents) != None:
            return True
        return False
