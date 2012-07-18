from itertools import *

try:
    amounts = [120.15, 764.05, 823.14]
except Exception as e:
    print( "Occured", type(e), e )


try:
    for checknum, amount in zip(count(1200), amounts):
        print('Check %d is for $%.2f' % (checknum, amount))
    # Expected:
    ## Check 1200 is for $120.15
    ## Check 1201 is for $764.05
    ## Check 1202 is for $823.14
    #
except Exception as e:
    print( "Occured", type(e), e )


try:
    import operator
except Exception as e:
    print( "Occured", type(e), e )


try:
    for cube in map(operator.pow, range(1,4), repeat(3)):
       print(cube)
    # Expected:
    ## 1
    ## 8
    ## 27
    #
except Exception as e:
    print( "Occured", type(e), e )


try:
    reportlines = ['EuroPython', 'Roster', '', 'alex', '', 'laura', '', 'martin', '', 'walter', '', 'samuele']
except Exception as e:
    print( "Occured", type(e), e )


try:
    for name in islice(reportlines, 3, None, 2):
       print(name.title())
    # Expected:
    ## Alex
    ## Laura
    ## Martin
    ## Walter
    ## Samuele
    #
except Exception as e:
    print( "Occured", type(e), e )


try:
    from operator import itemgetter
except Exception as e:
    print( "Occured", type(e), e )


try:
    d = dict(a=1, b=2, c=1, d=2, e=1, f=2, g=3)
except Exception as e:
    print( "Occured", type(e), e )


try:
    di = sorted(sorted(d.items()), key=itemgetter(1))
except Exception as e:
    print( "Occured", type(e), e )


try:
    for k, g in groupby(di, itemgetter(1)):
        print(k, list(map(itemgetter(0), g)))
    # Expected:
    ## 1 ['a', 'c', 'e']
    ## 2 ['b', 'd', 'f']
    ## 3 ['g']
    #
    # # Find runs of consecutive numbers using groupby.  The key to the solution
    # # is differencing with a range so that consecutive numbers all appear in
    # # same group.
except Exception as e:
    print( "Occured", type(e), e )


try:
    data = [ 1,  4,5,6, 10, 15,16,17,18, 22, 25,26,27,28]
except Exception as e:
    print( "Occured", type(e), e )


try:
    for k, g in groupby(enumerate(data), lambda t:t[0]-t[1]):
        print(list(map(operator.itemgetter(1), g)))
    # Expected:
    ## [1]
    ## [4, 5, 6]
    ## [10]
    ## [15, 16, 17, 18]
    ## [22]
    ## [25, 26, 27, 28]
    #
    def take(n, iterable):
        "Return first n items of the iterable as a list"
        return list(islice(iterable, n))
    #
    def enumerate(iterable, start=0):
        return zip(count(start), iterable)
    #
    def tabulate(function, start=0):
        "Return function(0), function(1), ..."
        return map(function, count(start))
    #
    def nth(iterable, n, default=None):
        "Returns the nth item or a default value"
        return next(islice(iterable, n, None), default)
    #
    def quantify(iterable, pred=bool):
        "Count how many times the predicate is true"
        return sum(map(pred, iterable))
    #
    def padnone(iterable):
        "Returns the sequence elements and then returns None indefinitely"
        return chain(iterable, repeat(None))
    #
    def ncycles(iterable, n):
        "Returns the sequence elements n times"
        return chain(*repeat(iterable, n))
    #
    def dotproduct(vec1, vec2):
        return sum(map(operator.mul, vec1, vec2))
    #
    def flatten(listOfLists):
        return list(chain.from_iterable(listOfLists))
    #
    def repeatfunc(func, times=None, *args):
        "Repeat calls to func with specified arguments."
        "   Example:  repeatfunc(random.random)"
        if times is None:
            return starmap(func, repeat(args))
        else:
            return starmap(func, repeat(args, times))
    #
    def pairwise(iterable):
        "s -> (s0,s1), (s1,s2), (s2, s3), ..."
        a, b = tee(iterable)
        try:
            next(b)
        except StopIteration:
            pass
        return zip(a, b)
    #
    def grouper(n, iterable, fillvalue=None):
        "grouper(3, 'ABCDEFG', 'x') --> ABC DEF Gxx"
        args = [iter(iterable)] * n
        return zip_longest(*args, fillvalue=fillvalue)
    #
    def roundrobin(*iterables):
        "roundrobin('ABC', 'D', 'EF') --> A D E B F C"
        # Recipe credited to George Sakkis
        pending = len(iterables)
        nexts = cycle(iter(it).__next__ for it in iterables)
        while pending:
            try:
                for next in nexts:
                    yield next()
            except StopIteration:
                pending -= 1
                nexts = cycle(islice(nexts, pending))
    #
    def powerset(iterable):
        "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
        s = list(iterable)
        return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))
    #
    def unique_everseen(iterable, key=None):
        "List unique elements, preserving order. Remember all elements ever seen."
        # unique_everseen('AAAABBBCCDAABBB') --> A B C D
        # unique_everseen('ABBCcAD', str.lower) --> A B C D
        seen = set()
        seen_add = seen.add
        if key is None:
            for element in iterable:
                if element not in seen:
                    seen_add(element)
                    yield element
        else:
            for element in iterable:
                k = key(element)
                if k not in seen:
                    seen_add(k)
                    yield element
    #
    def unique_justseen(iterable, key=None):
        "List unique elements, preserving order. Remember only the element just seen."
        # unique_justseen('AAAABBBCCDAABBB') --> A B C D A B
        # unique_justseen('ABBCcAD', str.lower) --> A B C A D
        return map(next, map(itemgetter(1), groupby(iterable, key)))
    #
    # This is not part of the examples but it tests to make sure the definitions
    # perform as purported.
    #
except Exception as e:
    print( "Occured", type(e), e )


try:
    take(10, count())
except Exception as e:
    print( "Occured", type(e), e )


try:
    list(enumerate('abc'))
except Exception as e:
    print( "Occured", type(e), e )


try:
    list(islice(tabulate(lambda x: 2*x), 4))
except Exception as e:
    print( "Occured", type(e), e )


try:
    nth('abcde', 3)
except Exception as e:
    print( "Occured", type(e), e )


try:
    nth('abcde', 9) is None
except Exception as e:
    print( "Occured", type(e), e )


try:
    quantify(range(99), lambda x: x%2==0)
except Exception as e:
    print( "Occured", type(e), e )


try:
    a = [[1, 2, 3], [4, 5, 6]]
except Exception as e:
    print( "Occured", type(e), e )


try:
    flatten(a)
except Exception as e:
    print( "Occured", type(e), e )


try:
    list(repeatfunc(pow, 5, 2, 3))
except Exception as e:
    print( "Occured", type(e), e )


try:
    import random
except Exception as e:
    print( "Occured", type(e), e )


try:
    take(5, map(int, repeatfunc(random.random)))
except Exception as e:
    print( "Occured", type(e), e )


try:
    list(pairwise('abcd'))
except Exception as e:
    print( "Occured", type(e), e )


try:
    list(pairwise([]))
except Exception as e:
    print( "Occured", type(e), e )


try:
    list(pairwise('a'))
except Exception as e:
    print( "Occured", type(e), e )


try:
    list(islice(padnone('abc'), 0, 6))
except Exception as e:
    print( "Occured", type(e), e )


try:
    list(ncycles('abc', 3))
except Exception as e:
    print( "Occured", type(e), e )


try:
    dotproduct([1,2,3], [4,5,6])
except Exception as e:
    print( "Occured", type(e), e )


try:
    list(grouper(3, 'abcdefg', 'x'))
except Exception as e:
    print( "Occured", type(e), e )


try:
    list(roundrobin('abc', 'd', 'ef'))
except Exception as e:
    print( "Occured", type(e), e )


try:
    list(powerset([1,2,3]))
except Exception as e:
    print( "Occured", type(e), e )


try:
    all(len(list(powerset(range(n)))) == 2**n for n in range(18))
except Exception as e:
    print( "Occured", type(e), e )


try:
    list(powerset('abcde')) == sorted(sorted(set(powerset('abcde'))), key=len)
except Exception as e:
    print( "Occured", type(e), e )


try:
    list(unique_everseen('AAAABBBCCDAABBB'))
except Exception as e:
    print( "Occured", type(e), e )


try:
    list(unique_everseen('ABBCcAD', str.lower))
except Exception as e:
    print( "Occured", type(e), e )


try:
    list(unique_justseen('AAAABBBCCDAABBB'))
except Exception as e:
    print( "Occured", type(e), e )


try:
    list(unique_justseen('ABBCcAD', str.lower))
except Exception as e:
    print( "Occured", type(e), e )
