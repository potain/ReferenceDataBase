"""A class of ConferencePaper as a special kind of publication. In addition to 
title.

..:: moduleauthor: WangBo <wangbomicro@gmail.com> 
"""
from Exceptions import IllegalStateException
import Publication

class ConferencePaper(Publication):
    """A class of conference paper as a special kind of publication. 
    In addition to title, authors, year, conferencePaper have a conference.
     
    Post: 
    The conference of this new conferencePaper is equal to the given conference.
    
    Args:
        title (str): The title of the publication.
        authors (list): The authors name of the publication
        year (int): The publish year.
        conference (str): The conference name of this conferencePaper.
    
    throws:
        IllegalAuthorException: if the given author is invalid
        IllegalYearException: if the given year is invalid
    """
    def __init__(self, title, authors, year, conference):
        super(ConferencePaper, self).__init__(title = title, authors = authors, 
                                              year = year)
        self._conference = conference

    @property
    def conference(self):
        """Return the name of the conference of this conferencePaper.
        """
        return self._conference
    
    @conference.setter
    def conference(self, val):
        """Set the conference of the conferencePaper as the given conference name.
        Args:
            val (str): The name of the conference to be set.
        Post:
            The name of the conference will be equal to the given name.
        throws:
            IllegalStateException: if the conferencePaper is terminated.
        """
        if self.isTerminated():
            raise IllegalStateException("The instance already terminated.")
        self._conference = val