<div title="header">

<font face="Liberation Mono, monospace">Clueless to Coding – Lesson</font> <font face="Liberation Mono, monospace">5</font> <font face="Liberation Mono, monospace">Handout</font>

</div>

<font style="font-size: 20pt" size="5">**<font style="font-size: 20pt" size="5">L</font><font style="font-size: 20pt" size="5">esson</font> <font style="font-size: 20pt" size="5">5</font><font style="font-size: 20pt" size="5">Handout</font><font style="font-size: 20pt" size="5">v0.</font><font style="font-size: 20pt" size="5">1</font>**</font>

1.  <font face="Liberation Sans, sans-serif"><font style="font-size: 14pt" size="4">Terminology</font></font>

    1.  **function** <span style="font-weight: normal">–</span> <span style="font-weight: normal">Functions, in programming, are blocks of code which are associated with a function name and are able to return one or more values or references using a return statement.</span>

    2.  **function definition** <span style="font-weight: normal">–</span> <span style="font-weight: normal">The entire definition of a function includes its definition statement and the code that will be executed.</span>

    3.  **function definition statement** <span style="font-weight: normal">-</span> <span style="font-weight: normal">The function definition statement defines the name and other characteristics of a function.</span>

    4.  **module** <span style="font-weight: normal">–</span> <span style="font-weight: normal">In Python any file containing definitions and statements is technically a “module”.</span>

    5.  **return statement** <span style="font-weight: normal">–</span> <span style="font-weight: normal">A statement that starts with the “return” keyword and contains one or more data to be returned to the function call. When a value is returned the function call is treated as if it were “equal” to the returned value(s).</span>

    6.  **import** <span style="font-weight: normal">– Other modules may be imported into a Python script file/module.</span>

    7.  **docstrings** <span style="font-weight: normal">–</span> <span style="font-weight: normal">A useful feature of the Python language. A docstring is the first string literal that follows the beginning of a module, function definition, or class definition. These docstrings are associated with the defined items and stand as language supported documentation.</span>

    8.  **time module** <span style="font-weight: normal">–</span> <span style="font-weight: normal">The Python standard library of modules includes a “time” module which supports access to many time-related functions.</span>

    9.  **standard library** <span style="font-weight: normal">–</span> <span style="font-weight: normal">Most programming languages have a standard set of libraries which cover a wide range of commonly needed functions.</span>

    10.  **application** <span style="font-weight: normal">–</span> <span style="font-weight: normal">There are many definitions for “application” within Computer Science. As a noun, “application” can mean the set of files that make up a program which serves a specific function directly accessed by a human user.</span>

    11.  **<span style="font-style: normal">orphaned strings</span>**<span style="font-style: normal"> <span style="font-weight: normal">–</span> </span><span style="font-style: normal"><span style="font-weight: normal">When a string literal definition is not associated with an expression or asignemnt statement it can referred to as an “orphan”. The Python language supports using strings literals as commentary in that it does not throw an error when they are encountered. Also, see “docstrings” above.</span></span>

    12.  **<span style="font-style: normal">n</span><span style="font-style: normal">amespace</span>**<span style="font-style: normal"> <span style="font-weight: normal">and</span> </span>**<span style="font-style: normal">scope</span>**<span style="font-style: normal"> <span style="font-weight: normal">– Namespace and scope cover the mechanism by which a label used for a variable, module, or function can be reused for different purposes within different contexts of a program. The details of this are beyond the scope of this lesson, but they wil be covered in supplemental material.</span></span>

2.  <font face="Liberation Sans, sans-serif"><font style="font-size: 14pt" size="4">Programming Elements</font></font>

    1.  <span style="font-style: normal">Operators:</span>

        1.  **<span style="font-style: normal">:</span>**<span style="font-style: normal"> <span style="font-weight: normal">–</span> </span><span style="font-style: normal"><span style="font-weight: normal">The colon is used to end a line which immediately precedes a indented code-block. The Python documentation sometimes refers to a group of lines of code as a ‘suite’.</span></span>

    2.  Python Keywords:

        1.  <span style="font-style: normal">**d**</span><span style="font-style: normal">**ef** </span>_<span style="font-weight: normal">function_name</span> _<span style="font-style: normal">**(**</span>_<span style="font-weight: normal">optional_argument(s)</span>_<span style="font-style: normal">**):**</span>_ <span style="font-weight: normal">–</span>_<span style="font-style: normal"> <span style="font-weight: normal"></span> </span><span style="font-style: normal"><span style="font-weight: normal">A function definition statement.</span> </span>_<span style="font-weight: normal">optional_arguments</span>_<span style="font-style: normal"> <span style="font-weight: normal">can include both the local names to assign arguments sent to the function, as well as assignments to use when arguments are not sent.</span></span>

        2.  **<span style="font-style: normal">r</span><span style="font-style: normal">eturn</span>**<span style="font-style: normal"> <span style="font-weight: normal"></span> </span>_<span style="font-weight: normal">optional_return_value(s)</span>_<span style="font-style: normal"> <span style="font-weight: normal">–</span></span><span style="font-style: normal"> <span style="font-weight: normal"></span> </span><span style="font-style: normal"><span style="font-weight: normal">The return keyword is used to terminate the execution of a function and return any value to the function call.</span></span>

        3.  **<span style="font-style: normal">i</span><span style="font-style: normal">mport</span>**<span style="font-style: normal"> <span style="font-weight: normal"></span> </span>_<span style="font-weight: normal">module_name</span>_<span style="font-style: normal"> <span style="font-weight: normal">– Used to import the functions and other features from an external module. This supports reusability and modularity across multiple source files.</span></span>

        4.  **<span style="font-style: normal">from</span>**<span style="font-style: normal"> <span style="font-weight: normal"></span> </span>_<span style="font-weight: normal">module_name</span>_<span style="font-style: normal"> <span style="font-weight: normal"></span> </span>**<span style="font-style: normal">import</span>**_ <span style="font-weight: normal">function_name</span>_<span style="font-style: normal"> <span style="font-weight: normal">– This is used to import one or more function from an external module. This method causes the imported functions to be available by referencing them</span> </span>_<span style="font-weight: normal">without</span>_<span style="font-style: normal"> <span style="font-weight: normal">the module name.</span></span>

    3.  Python Functions:

        1.  _<span style="font-weight: normal">string.</span>_**isdigit()** <span style="font-weight: normal">–</span> <span style="font-weight: normal">A function that is part of Python’s built-in string library. It returns ‘True’ for strings which contain digits, and only digits. Otherwise it returns a ‘False’.</span>

        2.  **time.time()** <span style="font-weight: normal">- When used in this form time.time() returns a floating point value that is the number of seconds that has elapsed since some specific date/time. The exact date/time used can vary from system to system but this is generally not an issue since it is normally used for differential calculations for time measurement in real-time.</span>
