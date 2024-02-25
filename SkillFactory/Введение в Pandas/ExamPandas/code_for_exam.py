def time_function(arg: int) -> str:
    """0-6 night
    6-12 morning
    12-18 day
    18-23 evening"""
    if arg>=0 and arg<=6:
        return 'night'
    elif arg>6 and arg<=12:
        return 'morning'
    elif arg>12 and arg<=18:
        return 'day'
    elif arg>18 and arg<=23:
        return 'evening'
    
    
    
print(time_function(0))