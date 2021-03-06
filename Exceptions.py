"""Self defined Exceptions and Errors

..:: moduleauthor: WangBo <wangbomicro@gmail.com>

"""

class IllegalValueException(Exception):
    """Generic exception for Illegal Values."""
    
    def __inti__(self, msgs):
        Exception.__init__(self,msgs)
    
    def __str__(self):
        return '%d'%self.code + "-" + self.mssage
    
    def __repr__(self):
        return "%s: %d - %s" % (self.__class__, self.code, self.message)

class IllegalIssueNumberException(IllegalValueException):
    """Wrong value assigned to class attribute.
    
    Args:
        -arg: the wrong issueNumber 
    """
    def __init__(self, arg):
        msg = ("Wrong issueNumber assigned. ",
               "issueNumber given is: {}, which should be larger than zero".format(arg))
        self.code = 1001
        super(IllegalIssueNumberException, self).__init__(''.join(msg))
    
class IllegalYearException(IllegalValueException):
    """Wrong year value assigned to class attribute
    
    Args:
        -arg: the wrong year number
    """
    def __init__(self, arg):
        
        msg = ("Wrong year assigned. ",
               "year given is: {}, which should be larger than 1500 and smaller\
                then current year + 1".format(arg))
        self.code = 1002
        super(IllegalYearException, self).__init__(''.join(msg))
    
class IllegalAuthorsException(IllegalValueException):
    """Wrong authors value assigned to class attribute
    
    Args:
        -arg: the wrong authors value.
    
    """
    def __init__(self, arg):
        # Call the base class constructor with the parameters it needs
        msg = ("Wrong authors value assigned. ",
               "authors value given is: {}, which should be a list with element\
                'firstname, lastname'".format(arg))
        self.code = 1003
        super(IllegalAuthorsException, self).__init__(''.join(msg))
    
class IllegalPublicationIdException(IllegalValueException):
    """Wrong publicationID
    
    Args:
        -arg: the wrong ID.
    """
    def __init__(self, arg):
        # Call the base class constructor with the parameters it needs
        msg = ("Wrong publication ID assigned. "
               "ID given is: {}, which is not in the database".format(arg))
        self.code = 1004
        super(IllegalPublicationIdException, self).__init__(''.join(msg))
class IllegalWeightException(IllegalValueException):
    """Wrong weight
    
    Args:
        weight: the wroing weight.
    """
    def __init__(self, arg):
        # Call the base class constructor with the parameters it needs
        msg = ("Wrong weight assigned. "
               "Weight given is: {}, which is should be larger then zero".format(arg))
        self.code = 1005
        super(IllegalPublicationIdException, self).__init__(''.join(msg)) 
    
class IllegalStateException(Exception):
    """Generic exception for Illegal Values."""
    def __inti__(self, msgs):
        Exception.__init__(self,msgs)
    
    def __str__(self):
        return '%d'%self.code + "-" + self.mssage
    
    def __repr__(self):
        return "%s: %d - %s" % (self.__class__, self.code, self.message)
    
    
