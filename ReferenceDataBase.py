"""A class representing a reference database, i.e., a collection of publications.

..:: moduleauthor: Wang Bo <wangbomicro@gmail.com>
..:: invar: The ReferenceDataBase must have proper publications.
"""

class ReferenceDataBase(object):
    
    def __init__(self):
        """Initialize this new ReferenceDatabase with no publications attached 
        to it. Only set its incrementID to 1001 so all the ID of new added 
        publications start counting from 1001.
     
        Post: 
            No publications are attached to this ReferenceDataBase.
        """
        ReferenceDataBase.incrementID = 1001
        
    def isTerminated(self):
        """
        """
        pass
    
    def terminate(self):
        """
        """
        pass
    
    def hasPublication(self, publication):
        """
        """
        pass
    
    def hasPublicationID(self, id):
        """
        """
        pass
    
    def getPublicationWithID(self, id):
        """
        """
        pass
    
    def hasProperPublication(self):
        """
        """
        pass
    
    def canHaveAsPublication(self):
        """
        """
        pass
    
    def addAsPublication(self, publication):
        """
        """
        pass
    
    def removePublication(self, publication):
        """
        """
        pass
    
    def getAllPublication(self):
        """
        """
        pass
    
    def isValidAuthor(self):
        """
        """
        pass
    
    def findByAuthor(self):
        """
        """
        pass
        
    def findByTitleWord(self):
        """
        """
        pass
    
    def addCitation(self, publicationId1, publicationId2):
        """
        """
        pass
    
    @classmethod
    def getCurrentIncrementID(cls):
        """
        """
        pass
    
    @classmethod
    def setCurrentIncrementID(cls):
        """
        """    
        pass
    
    
    
        
    
    
    
        