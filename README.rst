first: The function you always missed in Python
===============================================

*first* is a MIT licensed Python package with a simple function that returns
the first true value from an iterable, or ``None`` if there is none.  If you
need more power, you can also supply a ``key`` function that is used to judge
the truth value of the element or a ``default`` value if ``None`` doesn’t fit
your use case.

   I’m using the term “true” consistently with Python docs for ``any()`` and
   ``all()`` — it means that the value evaluates to true like: ``True``, ``1``,
   ``"foo"`` or ``[None]``.  But **not**: ``None``, ``False`` or ``0``.  In
   JavaScript, they call this “truthy”.


Examples
========

A simple example to get started: ::

   >>> from first import first
   >>> first([0, None, False, [], (), 42])
   42

However, it’s especially useful for dealing with regular expressions in
``if/elif/else`` branches: ::

   import re

   from first import first


   re1 = re.compile('b(.*)')
   re2 = re.compile('a(.*)')

   m = first(regexp.match('abc') for regexp in [re1, re2])
   if not m:
      print('no match!')
   elif m.re is re1:
      print('re1', m.group(1))
   elif m.re is re2:
      print('re2', m.group(1))

The optional ``key`` function gives you even *more* selection power.  If you
want to return the first even number from a list, just do the following::

   >>> from first import first
   >>> first([1, 1, 3, 4, 5], key=lambda x: x % 2 == 0)
   4

``default`` on the other hand allows you to specify a value that is returned
if none of the elements is true: ::

   >>> from first import first
   >>> first([0, None, False, [], ()], default=42)
   42


Usage
=====

The package consists of one module consisting of one function::

   from first import first

   first(iterable, default=None, key=None)

This function returns the first element of ``iterable`` that is true if
``key`` is ``None``.  If there is no true element, the value of ``default`` is
returned, which is ``None`` by default.

If a callable is supplied in ``key``, the result of ``key(element)`` is
used to judge the truth value of the element, but the element itself is
returned.

*first* has no dependencies and should work with any Python available.  Of
course, it works with the awesome `Python 3`_ everybody should be using.


Alternatives
============

*first* brings nothing to the table that wasn’t possible before. However the
existing solutions aren’t very idiomatic for such a common and simple problem.

The following constructs are equivalent to ``first(seq)`` and work since Python
2.6: ::

   next(itertools.ifilter(None, seq), None)
   next(itertools.ifilter(bool, seq), None)
   next((x for x in seq if x), None)

None of them is as pretty as I’d like them to be. The ``re`` example from
above would look like the following: ::

   next(itertools.ifilter(None, (regexp.match('abc') for regexp in [re1, re2])), None)
   next((regexp.match('abc') for regexp in [re1, re2] if regexp.match('abc')), None)

Note that in the second case you have to call ``regexp.match()`` *twice*.  For
comparison, one more time the *first*-version: ::

   first(regexp.match('abc') for regexp in [re1, re2])

Idiomatic, clear and readable. Pythonic. :)


Background
==========

The idea for *first* goes back to a discussion I had with `Łukasz Langa`_ about
how the ``re`` example above is painful in Python.  We figured such a function
is missing Python, however it’s rather unlikely we’d get it in and even if, it
wouldn’t get in before 3.4 anyway, which is years away as of yours truly is
writing this.

So I decided to release it as a package for now.  If it proves popular enough,
it may even make it into Python’s stdlib in the end.


.. _`Python 3`: http://getpython3.com/
.. _`Łukasz Langa`: https://github.com/ambv
