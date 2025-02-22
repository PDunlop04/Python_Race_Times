import doctest

class RaceTime:
    """ RaceTime: represents a race time result in 
    milliseconds (ms), seconds (sec), minutes (mins)
    Precondition, ms, sec, mins>=0, ms<1000, sec<60
    """

    def __init__(self, ms: int, sec: int, mins: int) -> None:
        """ initializes attributes of RaceTime instance
        >>> rt = RaceTime(88, 20, 4)
        """
        self.__ms = ms
        self.__sec = sec
        self.__mins = mins

    def get_ms(self) -> int:
        """ returns ms of self RaceTime instance
        >>> rt = RaceTime(88, 20, 4)
        >>> rt.get_ms()
        88
        """
        return self.__ms

    def get_sec(self) -> int:
        """ returns sec of self RaceTime instance
        >>> rt = RaceTime(88, 20, 4)
        >>> rt.get_sec()
        20
        """
        return self.__sec

    def get_mins(self) -> int:
        """ returns mins of self RaceTime instance
        >>> rt = RaceTime(88, 20, 4)
        >>> rt.get_mins()
        4
        """
        return self.__mins

    def __str__(self) -> str:
        """ returns a readable string with ms, sec, mins of RaceTime
        >>> rt = RaceTime(88, 20, 4)
        >>> str(rt)
        '4:20:88'
        """
        return f'{self.__mins}:{self.__sec}:{self.__ms}'

    def __repr__(self) -> str:
        """ returns a string representation of self RaceTime
        >>> rt = RaceTime(88, 20, 4)
        >>> repr(rt)
        'RaceTime(88, 20, 4)'
        """
        return f'RaceTime({self.__ms}, {self.__sec}, {self.__mins})'

    def __eq__(self, other: 'RaceTime') -> bool:
        """ returns True if self RaceTime has same ms, sec, mins as
        other RaceTime, otherwise False
        >>> rt121920a = RaceTime(12, 19, 20)
        >>> rt121920b = RaceTime(12, 19, 20)
        >>> rt121921  = RaceTime(12, 19, 21)
        >>> rt121820  = RaceTime(12, 18, 20)
        >>> rt111920  = RaceTime(11, 19, 20)

        >>> rt121920a == rt121920a
        True
        >>> rt121920a == rt121920b
        True
        >>> rt121920a == rt121921
        False
        >>> rt121920a == rt121820
        False
        >>> rt121920a == rt111920
        False
        """
        return (self.__ms == other.get_ms()
                and self.__sec == other.get_sec()
                and self.__mins == other.get_mins())
    
   
    def is_faster(self, other: 'RaceTime') -> bool:
        """
        Returns True if self is faster than other RaceTime, False otherwise
        returns True if self is faster than other racetime and False otherwise
        >>> test1 = RaceTime(12, 19, 20)
        >>> test2 = RaceTime(12, 19, 20)
        >>> test3 = RaceTime(12, 19, 21)
        >>> test4 = RaceTime(12, 18, 20)
        >>> test5 = RaceTime(11, 19, 20)
        >>> test6 = RaceTime(9, 15, 17)
        >>> test7 = RaceTime(2, 48, 9)

        >>> test1.is_faster(test1)
        False
        >>> test1.is_faster(test2)
        False
        >>> test1.is_faster(test3)
        True
        >>> test1.is_faster(test4)
        False
        >>> test1.is_faster(test5)
        False
        >>> test6.is_faster(test7)
        False
        >>> test7.is_faster(test6)
        True
        """
        if self.get_mins() < other.get_mins():
            return True
        elif (self.get_mins() == other.get_mins() 
              and self.get_sec() < other.get_sec()):
            return True
        elif (self.get_mins() == other.get_mins() 
              and self.get_sec() == other.get_sec() 
              and self.get_ms() < other.get_ms()):
            return True
        else:
            return False
            