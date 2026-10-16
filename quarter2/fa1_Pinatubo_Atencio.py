class Publication:
  __title: str
  __author: str
  def __init__(self, title, author):
      self.__title = title
      self.__author = author
    def set_title(self):
      print(self.name, "is eating.")
    def set_author(self):
      print(self.name, "is sleeping.")
    def get_title(self):
      return self.__title
    def get_author(self):
      return self.__author

class Book(Publication):
  pass

class Magazine(Publication):
  pass 
