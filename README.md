


test
================================================================================
First test repository used to some tests with markdown

# Rules of formatting Markdown files

This rules extends standard rules of Markdown. They extend readability of
markdown file in text mode, and simplify automatic generation of:
* Table of contents (ready see createTOC.py)
* List of tables
* List of figures



Headers
--------------------------------------------------------------------------------



### Header level 1

Always precede header line with header with 3 empty lines. Standard requires
only one. Always use line with about 80 \= characters in the next line after
header line. In standard only 3 are required. Standard allow also preceding
header with one \# character and some spaces.



### Header level 2

Always precede header line with header with 3 empty lines. Standard requires
only one. Always use line with about 80 \- characters in the next line after
header line. In standard only 3 are required. Standard allow also preceding
header with two \# characters and some spaces.



### Header level 3 - 6

Always precede header line with header with 3 empty lines. Standard requires
only one. Precede header with three to six \# character and some spaces.



Tables
--------------------------------------------------------------------------------

Example is below:

Table 1. Name of the table

'''
| Heading 01 | Heading 02 | Heading 03 |
|:-----------|-----------:|:----------:|
| Cell 11    | Cell 12    | Cell 13    |
| Cell 21    | Cell 22    | Cell 23    |
| Cell 31    | Cell 32    | Cell 33    |
| Cell 41    | Cell 42    | Cell 43    |
'''

It will be renered like table below:

Table 1. Name of the table

| Heading 01 | Heading 02 | Heading 03 |
|:-----------|-----------:|:----------:|
| Cell 11    | Cell 12    | Cell 13    |
| Cell 21    | Cell 22    | Cell 23    |
| Cell 31    | Cell 32    | Cell 33    |
| Cell 41    | Cell 42    | Cell 43    |



Pictures
--------------------------------------------------------------------------------

Exactly like in standard markdown:

'''
![alt_text](image_link)
'''

Figure 1. Name of picture

Rendered like this:

![alt_text](image_link)



Lists
--------------------------------------------------------------------------------



### Unordered lists

Prefixed with asterisk (standard alows also \- sign) and some spaces. Nested
lists indented by two spaces.

'''
* first element (level 1)
  * level 2 - first
  * level 2 second
* second element (level 1)
* third element (level 1)
'''

Rendered like below:

* first element (level 1)
  * level 2 - first
  * level 2 second
* second element (level 1)
* third element (level 1)



### Ordered list

'''
1. first element (level 1)
2. second element (level 1)
3. third element (level 1)
'''

Renderd like below:

1. first element (level 1)
2. second element (level 1)
3. third element (level 1)


