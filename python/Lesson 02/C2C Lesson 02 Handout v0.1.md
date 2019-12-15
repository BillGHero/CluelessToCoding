<div title="header">

<font face="Liberation Mono, monospace">Clueless to Coding – Lesson 2 Handout</font>

</div>

<font style="font-size: 20pt" size="5">**<font style="font-size: 20pt" size="5">L</font><font style="font-size: 20pt" size="5">esson</font> <font style="font-size: 20pt" size="5">2</font><font style="font-size: 20pt" size="5">Handout</font><font style="font-size: 20pt" size="5">v0.</font><font style="font-size: 20pt" size="5">1</font>**</font>

1.  <font face="Liberation Sans, sans-serif"><font style="font-size: 14pt" size="4">Terminology</font></font>

    1.  **string** <span style="font-weight: normal">–</span> <span style="font-weight: normal">A data type that contains text. Essentially, this is a collection of individual characters that are ‘strung’ together much like beads on a necklace. Each character is actually a number that represents a character, but special references must be used to treat an individual character as its number.</span>

    2.  **concatenation** <span style="font-weight: normal">– ‘</span><span style="font-weight: normal">Adding’ two or more strings together to make a new string composed of all of them.</span>

    3.  **slicing** <span style="font-weight: normal">–</span> <span style="font-weight: normal">A technique that can be used on a collection of data items, such as the characters in a string. Sections of a string can be referenced based on a starting and ending position.</span>

    4.  **white space** <span style="font-weight: normal">–</span> <span style="font-weight: normal">Often means the blank space in a string.</span>

    5.  **dot-operator** <span style="font-weight: normal">–</span> <span style="font-weight: normal">When a period is used between twoe labels, it is a dot-operator.</span>

    6.  **object oriented programming** **(OOP)** <span style="font-weight: normal">–</span> <span style="font-weight: normal">A type of programming that always for labels to have a context sensitivity, among other things. OOP will be covered later.</span>

    7.  **nested function call** <span style="font-weight: normal">–</span> <span style="font-weight: normal">When a function call is included as an argument to another function call.</span>

    8.  **data-type-conversion** <span style="font-weight: normal">–</span> <span style="font-weight: normal">When the data of one type is converted to another type.</span>

    9.  **exception** <span style="font-weight: normal">–</span> <span style="font-weight: normal">A kind of error that can occur during the execution of a program.</span>

    10.  **input-validation** <span style="font-weight: normal">–</span> <span style="font-weight: normal">A technique in programming where data is evaluated to ensure it is of appropriate type and value. This will be covered later.</span>

2.  <font face="Liberation Sans, sans-serif"><font style="font-size: 14pt" size="4">Programming Elements</font></font>

    1.  <span style="font-style: normal">Operators:</span>

        1.  <span style="font-weight: normal">. -</span> <span style="font-weight: normal">The ‘dot’-operator. Used frequently in Object Oriented Programming.</span>

        2.  **+ - * /** <span style="font-weight: normal">% - mathematical operators (note that *, /,</span> <span style="font-weight: normal">and %</span> <span style="font-weight: normal">are multiply, divide,</span> <span style="font-weight: normal">and modulus</span> <span style="font-weight: normal">respectively)</span>

        3.  _**string_variable**_<span style="font-style: normal"> **+** </span>**_string_variable_**<span style="font-style: normal"> <span style="font-weight: normal">–</span> </span><span style="font-style: normal"><span style="font-weight: normal">Two or more string variables may be concatenated using the addition operator.</span></span>

        4.  _**string_variable**_<span style="font-style: normal">**[**</span>**_n_<span style="font-style: normal">]</span>**<span style="font-style: normal"> <span style="font-weight: normal">–</span> </span><span style="font-style: normal"><span style="font-weight: normal">Square brackets which immediately proceed a string variable can contain the position of a single character to reference from within it. Note that referencing a position outside of the string will result in an error or exception.</span></span>

        5.  _**string_variable**_<span style="font-style: normal">**[**</span>**_n1_<span style="font-style: normal">:</span>_n2_<span style="font-style: normal">]</span>**<span style="font-style: normal"> <span style="font-weight: normal">–</span> </span><span style="font-style: normal"><span style="font-weight: normal">A ‘slice’ or range of characters within a string can be referenced from within a string. Note that referencing a position outside of a string will result in an error or an exception.</span></span>

    2.  Python Keywords:

<span style="font-style: normal"><span style="font-weight: normal"></span></span>_<span style="font-weight: normal">This section left blank intentionally.</span>_

1.  Python Functions:

    1.  <span style="font-style: normal">**len(**</span>_**variable**_<span style="font-style: normal">**)**</span><span style="font-style: normal"> <span style="font-weight: normal">-</span> </span><span style="font-style: normal"><span style="font-weight: normal">This function will return an integer representing the ‘length’ of a variable. For strings this will normally be the number of characters it contains.</span></span>

    2.  <span style="font-style: normal">**str.strip(**</span>_**string**_<span style="font-style: normal">**)**</span><span style="font-style: normal"> <span style="font-weight: normal">–</span> </span><span style="font-style: normal"><span style="font-weight: normal">This function ‘strips’ white space from the front and back of a string.</span></span>

    3.  <span style="font-style: normal">**str.lower(**</span>_**string**_<span style="font-style: normal">**)**</span><span style="font-style: normal"> <span style="font-weight: normal">–</span> </span><span style="font-style: normal"><span style="font-weight: normal">This function changes all letters within a string to lower-case.</span></span>

    4.  <span style="font-style: normal">**str.upper(**</span>_**string**_<span style="font-style: normal">**)**</span><span style="font-style: normal"> <span style="font-weight: normal">–</span> </span><span style="font-style: normal"><span style="font-weight: normal">This function changes all letters within a string to upper-case.</span></span>

    5.  <span style="font-style: normal">**str.capitalize(**</span>_**string**_<span style="font-style: normal">**)**</span><span style="font-style: normal"> <span style="font-weight: normal">–</span> </span><span style="font-style: normal"><span style="font-weight: normal">This function capitalizes the first character within a string, and make all other alphabetical characters lower-case.</span></span>

    6.  <span style="font-style: normal">**str.title(**</span>_**string**_<span style="font-style: normal">**)**</span><span style="font-style: normal"> <span style="font-weight: normal">–</span> </span><span style="font-style: normal"><span style="font-weight: normal">This function finds each word within a string and capitalizes it.</span></span>

    7.  <span style="font-style: normal">**input(** </span>_**[option**__**al**__ **prompt string]** _<span style="font-style: normal">**)**</span><span style="font-style: normal"> <span style="font-weight: normal">-</span> </span><span style="font-style: normal"><span style="font-weight: normal">This function will collect input from a user and return it as a text string. An optional string may be included as an argument, which will be used as a prompt.</span></span>

    8.  <span style="font-style: normal">**str(**</span>_**argument**_<span style="font-style: normal">**)**</span><span style="font-style: normal"> <span style="font-weight: normal">– Returns a string version of the argument.</span></span>

    9.  <span style="font-style: normal">**int(**</span>_**argument**_<span style="font-style: normal">**)**</span><span style="font-style: normal"> <span style="font-weight: normal">– Attempts to find an integer value and returns it. Will throw an exception if the attempt fails; this typically happens when a string argument passed to it does not contain a n</span></span><span style="font-style: normal"><span style="font-weight: normal">umber</span></span><span style="font-style: normal"><span style="font-weight: normal">.</span></span>

    10.  <span style="font-style: normal">**float(**</span>_**argument**_<span style="font-style: normal">**)**</span><span style="font-style: normal"> <span style="font-weight: normal">– Attempts to find a floating point value and returns it. Will throw an exception if the attempt fails; this typically happens when a string argument passed to it does not contain a n</span></span><span style="font-style: normal"><span style="font-weight: normal">umber</span></span><span style="font-style: normal"><span style="font-weight: normal">.</span></span>