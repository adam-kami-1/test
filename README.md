


test
================================================================================
My test repository used to some tests with markdown



Rules of formatting Markdown files
================================================================================

This rules extends standard rules of Markdown. They extend readability of
markdown file in text mode, and simplify automatic generation of:
* Table of contents
  (ready: see
  [createTOC.py](https://github.com/adam-kami-1/test/blob/master/createTOC.py))
* List of tables
* List of figures



Headers
--------------------------------------------------------------------------------



### Header level 1

Always precede header line with at least 3 empty lines. Standard requires
only one. Always use line with about 80 '=' characters in the next line after
header line. In standard only 3 are required. Standard allow also preceding
header with one '\#' character and some spaces.



### Header level 2

Always precede header line with at least 3 empty lines. Standard requires
only one. Always use line with about 80 hyphen '\-' characters in the next
line after header line. In standard only 3 are required. Standard allow
also preceding header with two '\#' characters and some spaces.



### Header level 3 - 6

Always precede header line with at least 3 empty lines. Standard requires
only one. Precede header with three to six '\#' characters and some spaces.



Tables
--------------------------------------------------------------------------------



### Table code example

```
Table 1. Name of the table

| Heading 01 | Heading 02 | Heading 03 |
|:-----------|-----------:|:----------:|
| Cell 11    | Cell 12    | Cell 13    |
| Cell 21    | Cell 22    | Cell 23    |
| Cell 31    | Cell 32    | Cell 33    |
| Cell 41    | Cell 42    | Cell 43    |
```



### Table rendering

Table 1. Name of the table

| Heading 01 | Heading 02 | Heading 03 |
|:-----------|-----------:|:----------:|
| Cell 11    | Cell 12    | Cell 13    |
| Cell 21    | Cell 22    | Cell 23    |
| Cell 31    | Cell 32    | Cell 33    |
| Cell 41    | Cell 42    | Cell 43    |



### Table notes

All table cells in one row have to fit into one line of markdown file.

Pipe characters '|' before first column and afters last column are optional,
but their presence increases readability of markdown file. The number of
hyphens '\-' between pipes '|' in line below headings have to be greater or
equall to three. Colons in this line can be used (they are optional) to
control alignment of data in cells in below rows.



Pictures
--------------------------------------------------------------------------------



### Picture code example

```
![alt_text](link_to/image_eg.png)

Figure 1. Name of picture
```



### Picture rendering

![alt_text](link_to/image_eg.png)

Figure 1. Name of picture



Links
--------------------------------------------------------------------------------



### Link code example

```
[About writing and formatting on GitHub](https://help.github.com/articles/about-writing-and-formatting-on-github/)
```



### Link rendering

[About writing and formatting on GitHub](https://help.github.com/articles/about-writing-and-formatting-on-github/)



Lists
--------------------------------------------------------------------------------



### Unordered lists

Prefixed with asterisk (standard alows also \- sign) and some spaces. Nested
lists indented by two spaces.

```
* first element (level 1)
  * level 2 - first
  * level 2 second
* second element (level 1)
* third element (level 1)
```

Rendered like below:

* first element (level 1)
  * level 2 - first
  * level 2 second
* second element (level 1)
* third element (level 1)



### Ordered list

```
1. first element
2. second element
3. third element
```

Renderd like below:

1. first element
2. second element
3. third element



### Unordered lists

You can mix unordered and ordered list on different nesting levels.

```
* first element (level 1)
  1. level 2 - first
  2. level 2 second
* second element (level 1)
  * level 2 - first
    1. level 3 - first
    2. level 3 second
  * level 2 second
* third element (level 1)
```

Rendered like below:

* first element (level 1)
  1. level 2 - first
  2. level 2 second
* second element (level 1)
  * level 2 - first
    1. level 3 - first
    2. level 3 second
  * level 2 second
* third element (level 1)




Formatting text
--------------------------------------------------------------------------------



### Paragraphs

Each paragraph is separated with at least one empty line from other paragraph.



### Bold and italic text

```
This text is **bold** while this is *italic*, but you can have **bold and
*italic*** text mixed.
```

This text is **bold** while this is *italic*, but you can have **bold and
*italic*** text mixed.

