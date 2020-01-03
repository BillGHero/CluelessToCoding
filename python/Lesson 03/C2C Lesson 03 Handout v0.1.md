<div title="header">

<font face="Liberation Mono, monospace">Clueless to Coding – Lesson 3 Handout</font>

</div>

<font style="font-size: 20pt" size="5">**<font style="font-size: 20pt" size="5">L</font><font style="font-size: 20pt" size="5">esson</font> <font style="font-size: 20pt" size="5">3</font><font style="font-size: 20pt" size="5">Handout</font><font style="font-size: 20pt" size="5">v0.</font><font style="font-size: 20pt" size="5">1</font>**</font>

1.  <font face="Liberation Sans, sans-serif"><font style="font-size: 14pt" size="4">Terminology</font></font>

    1.  **flow-control** <span style="font-weight: normal">–</span> <span style="font-weight: normal">Most programming languages possess language elements which allow for the branching of program execution. Selection of execution paths is often refered to as ‘flow-control’.</span>

    2.  **boolean** <span style="font-weight: normal">–</span> <span style="font-weight: normal">In programming, a boolean data type can either be ‘true’ or ‘false’.</span>

    3.  **logical** **expression** <span style="font-weight: normal">–</span> <span style="font-weight: normal">Logical expressions are made up of comparisons and logical operators. They will evaluate to either ‘true’ or ‘false’.</span>

    4.  **code-block** <span style="font-weight: normal">or</span> **suite** <span style="font-weight: normal">– Python is an indentation-aware programming language. This means that groups of lines of code that are related to each other are indented the same. Many other programming languages use the curly braces ( { } ) to isolate code blocks.</span>

    5.  **nesting** <span style="font-weight: normal">– When code blocks are placed inside other code blocks, this is sometimes called ‘nesting’. This can be seen in lesson 3 when an ‘if’ structure is placed within another ‘if’ structure.</span>

2.  <font face="Liberation Sans, sans-serif"><font style="font-size: 14pt" size="4">Programming Elements</font></font>

    1.  <span style="font-style: normal">Operators:</span>

        1.  **=****=** <span style="font-weight: normal">-</span> <span style="font-weight: normal">Used to check if two data are equal or</span> <span style="font-weight: normal">equivalent.</span> <span style="font-weight: normal">Normally one might expect a single eaul sign should be used for this purpose. However, that is already in use for the assignment operator.</span>

        2.  **>, >=, <, <=** <span style="font-weight: normal">-</span> <span style="font-weight: normal">Greater-Than, Greater-Than-or-Equal, Less-Than, Less-Than-or-Equal, respectively. These are the main comparison operators used in logical expressions.</span>

        3.  **and** <span style="font-weight: normal">–</span> <span style="font-weight: normal">The ‘and’ logical operator. When placed between two logical data or logical expressions it will result in true if, and only if, both are true. Otherwise it will produce a false result.</span>

        4.  **or** <span style="font-weight: normal">–</span> <span style="font-weight: normal">The ‘or’ logical operator. When placed between two logical data or logical expressions it will result in true if either are true. It will only result in flase if both are false.</span>

        5.  **not** <span style="font-weight: normal">–</span> <span style="font-weight: normal">The logical ‘not’ operator is placed before a logical data or expression. It has the effect of reversing the logical value of whatever it acts upon. True becomes false, and false becomes true.</span>

        6.  **!=** <span style="font-weight: normal">-</span> <span style="font-weight: normal">T</span><span style="font-weight: normal">he ‘not equal to’ operator.</span>

        7.  **<span style="font-style: normal">:</span>**<span style="font-style: normal"> <span style="font-weight: normal">–</span> </span><span style="font-style: normal"><span style="font-weight: normal">The colon is used to end a line which immediately precedes a indented code-block. The Python documentation sometimes refers to a group of lines of code as a ‘suite’.</span></span>

    2.  Python Keywords:

        1.  **<span style="font-style: normal">T</span><span style="font-style: normal">rue</span>**<span style="font-style: normal"> <span style="font-weight: normal">–</span> </span><span style="font-style: normal"><span style="font-weight: normal">The Python keyword for the logical value ‘true’.</span></span>

        2.  **<span style="font-style: normal">False</span>**<span style="font-style: normal"> <span style="font-weight: normal">–</span> </span><span style="font-style: normal"><span style="font-weight: normal">The Python keyword for the logical value ‘false’.</span></span>

        3.  **<span style="font-style: normal">None</span>**<span style="font-style: normal"> <span style="font-weight: normal">–</span> </span><span style="font-style: normal"><span style="font-weight: normal">The Python keyword for the state of ‘nothing’. When a variable is set to this it is, essentially, empty.</span></span>

        4.  **<span style="font-style: normal">if, elif, else</span>**<span style="font-style: normal"> <span style="font-weight: normal">–</span> </span><span style="font-style: normal"><span style="font-weight: normal">The three types of branches available for building a ‘if’ type conditional structure in Python. The structure must start with an ‘if’ clause and contain a logical expression. It may then contain zero or more ‘elif’ clauses – which must also have a logical expression. It may also, optionally, contain one ‘else’ clause – which should not have any expression. Each clause should end in a colon ‘:’. As the ‘if’ structure is evaluated one, and only one, clause (or branch) will be selected for execution. The other clauses (or branches) will be ignored.</span></span>

    3.  Python Functions:

        _<span style="font-weight: normal">T</span><span style="font-weight: normal">his section intentionally left blank.</span>_