import sys, os, pathlib
import logging as log
from core import INeedForceObject
log.getLogger().setLevel(log.DEBUG)


class BookObject(INeedForceObject):
    def __init__(self):
        super().__init__()
        self.__tags = []
        self.__name = None
        self.__description = None
        self.__serias = []
        self.__num_in_serias = None
        self.__authors = []
        self.__version = []
        self.__translations = {}
        self.__path_to_data = None

        # Create property
        self.tags = property(lambda: self.__tags)
        self.name = property(lambda: self.__name)
        self.description = property(lambda: self.__description)
        self.serias = property(lambda: self.__serias)
        self.num_in_serias = property(lambda: self.__num_in_serias)
        self.authors = property(lambda: self.__authors)
        self.version = property(lambda: self.__version)
        self.translations = property(lambda: self.__translations)
        self.path_to_data = property(lambda: self.__path_to_data)
        
        
    def addTag(self, tag: str, unique: bool = False):
        if unique and tag in self.tags:
            return
        self.__tags.append(tag)
    

    def removeTag(self, tag: str):
        try: 
            self.__tags.remove(tag)
            return True
        except ValueError as err:
            return False

 
    def renameTag(self, oldTag: str, newTag: str):
        try: 
            idx = self.__tags.index(oldTag)
            self.__tags[idx] = newTag
            return True
        except ValueError as err:
            return False

    
    def write_to_disc(self, path: pathlib.Path):

        # Check basic conditions
        if not (path.exists() and path.is_dir()):
            log.debug('Path not exists or not a Directory, <%s>'.format(str(path)))
    
    def convert_to(self, format):
        pass