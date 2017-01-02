"""A module of book as a special kind of publication. In addition to title,
 authors, year, book have a publisher.

..:: moduleauthor: WangBo <wangbomicro@gmail.com> 
"""
from Exceptions import IllegalStateException
import Publication

class Book(Publication):
    """A class of book as a special kind of publication. In addition to title,
     authors, year, book have a publisher.
     
    Post: The publisher of this new book is equal to the given publisher.
    
    Args:
    title (str): The title of the publication.
    authors (list): The authors name of the publication
    year (int): The publish year.
    Publisher (str): The publisher name of this book.
    
    throws:
    IllegalAuthorException: if the given author is invalid
    IllegalYearException: if the given year is invalid
    """
    def __init__(self, title, authors, year, publisher):
        super(Book, self).__init__(title = title, authors = authors, year = year)
        self._publisher = publisher

    @property
    def publisher(self):
        """Return the name of the publisher of this book.
        """
        return self._publisher
    
    @publisher.setter
    def publisher(self, val):
        """Set the publisher of the book as the given publisher name.
        Args:
            val (str): The name of the publisher to be set.
        Post:
            The name of the publisher will be equal to the given name.
        throws:
            IllegalStateException: if the book is terminated.
        """
        if self.isTerminated():
            raise IllegalStateException("The instance already terminated.")
        self._publisher = val