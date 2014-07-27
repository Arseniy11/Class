def my_filter(function, iterable):
    """About filter() function. Python has a built-in filter
       function which takes two arguments, a function and a list,
       and returns a list. The function passed as the first argument
       to filter must itself take one argument, and the list that filter
       returns will contain all the elements from the list passed to
       filter for which the function passed to filter returns true.
       Source: http://www.diveintopython.net/functional_programming/filtering_lists.html.
       As I understand if we pass to filter a tuple or a string instead of a list,
       the result will be returned as a tuple or as a string."""
    result = []
    for check in iterable:
        if function(check) is True:
            result.append(check)
    if isinstance(iterable, str):
        result = str(result).strip('[]')
    elif isinstance(iterable, tuple):
        result = tuple(result)
    else: pass
    return result

def my_map(function, iterable):
    """About map() function.The purpose of this function
       is to perform some operation on each element of an
       iterable. It returns a list containing the result of
       those operations. Source: http://infohost.nmt.edu/tcc
       /help/pubs/python/web/map-function.html"""
    result = []
    for check in iterable:
        result.append(function(check))
    return result


        
        
