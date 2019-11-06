# 00_First_Step.py
# 
# /\ See the line above? /\
# It is a fairly common to see the name of a file somewhere in the beginning
#  of a source-code or script file. There are various reasons why the author
#  may have done this. The specific reasons are not important fo this lesson.
#  Just know that comments can be used to serve many and diverse purposes.
#  For the most part, comments are ignored by the various interpreters and
#  compilers used in programming. However, there are situations where comments
#  play a role above and beyond documentation that is ignored by coding tools.
#
# This lesson makes use of comments, triple quoted strings, and docstrings. So,
#  before we begin this lessons program, we should take a quick look at how what
#  these things are, and how they will be used here.
#
#As you can see, Python uses the 'pound-sign (#)' as a prefix for comments. This
#  type of comment starts with the pound-sign and continues until the end of the
#  line. Many other languages have this style of single-line comment. Many other
#  languages also have a block style comment syntax that allow multiple lines to
#  be encapsulated by beginning and ending symbols so that a comment spans
#  multiple lines. Such bloc-comments can also be used to temporarily 'comment-
#  out' several lines of code.
#Python does not have a formal syntax for block commnets. But there is a way to
#  include strings within Python scripts that serve the same purpose. These are
#  Triple-Quoted-String-Literals. A string literal is simply a string which is
#  included directly within a source code file. A triple quoted string literal
#  is one which is enclosed in either a set of three single quotes or three
#  double quotes. Check it out:

''' Here we have
          a string literal
                    enclosed by
        "Three Single Quotes" '''

#And also check out:

""" A string literal
          enclosed by
    'Three Double Quotes' """

# As you can see, you can span multiple lines using these triple quotes. Another
#  useful thing demonstrated here is that, when a string is enclosed by double-
#  quotes, single quotes may be used within them. ANd the reverse is also true.
#  This is quite handy since it means that escape-sequences are not always
#  necessary to use quotes with a string literal. (For more information, search
#  for 'string literals and escape sequences' in the search engine of your
#  choice.)

#So far we have covered Comments and Triple-Quoted-Strings. The last feature we
#  need to cover is Docstrings. In Python Docstrings are simply triple-quoted
#  strings place directly in the beginning of a major element of a Python
#  script. When a triple-quoted-string is placed in the beginning of a module
#  (which is typically a python script file) or the beginning of a function
#  definition it becomes the Docstring for that element. It will then serve as
#  the main documentation for that element, and can be referenced when using
#  that element in other programs. More will be said later within this lesson,
#  but for further reading check out the articles at www.python.org on the
#  subject.

#Now we're ready to begin! Open 01_GoodTime.py and follow th direction contained
#  within its comments and triple-quoted-strings.

