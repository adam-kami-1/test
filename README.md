
GitHub repository: test
================================================================================

My test repository used to some tests with markdown, but mainly to test 
some utilities written in Python 3.

Python 3 tools to automate some task when editing markdown files
================================================================================

Automatic generation of:
--------------------------------------------------------------------------------

* [x] Table of contents,
  see [createTOC.py](https://github.com/adam-kami-1/test/blob/master/createTOC.py)
* [ ] List of tables
* [ ] List of figures

Notes on Markdown
================================================================================

Formatting text
--------------------------------------------------------------------------------

### Paragraphs

Each paragraph is separated with at least one empty line from other paragraphs.

### Bold, italic, and strikethrough text

#### Formatting text example

```
This text is **bold** while this is *italic*, but you can have
**bold and *italic* ** text mixed. But the last does not work always as
expected.

Instead of asterisk '\*' you can use
underline '\_' character. It can be convenient to join
**bold and _italic_** or *italic with __bold__*.

Just one character
('\*' or '\_') means italic, while two ('\*\*' or '\_\_') mean bold.

You can use additionally two tildes '\~\~' to ~~strike through~~ some text.
```

#### Formatting text rendering

This text is **bold** while this is *italic*, but you can have
**bold and *italic* ** text mixed. But the last does not work always as
expected.

Instead of asterisk '\*' you can use
underline '\_' character. It can be convenient to join
**bold and _italic_** or *italic with __bold__*.

Just one character
('\*' or '\_') means italic, while two ('\*\*' or '\_\_') mean bold.

You can use additionally two tildes '\~\~' to ~~strike through~~ some text.

Headers
--------------------------------------------------------------------------------

### Header level 1

In standard only 3 '=' characters are required to mark preceding line as header level 1 text,
but it is OK to use line with about 80 '=' characters in the next line after header line.
This increases readability. Standard allows also preceding header with one '\#' character and some spaces or tabs.
Always precede header line with at least 1 empty line.

### Header level 2

In standard only 3 '-' characters are required to mark preceding line as header level 2 text,
but it is OK to use line with about 80 '-' characters in the next line after header line.
This increases readability. Standard allows also preceding header with two '\#\#' characters and some spaces or tabs.
Always precede header line with at least 1 empty line. 

### Header level 3 - 6

Precede header with three to six '\#' characters and some spaces or tabs.
Always precede header line with at least 1 empty line. 

Tables
--------------------------------------------------------------------------------

### Table example

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

All table cells from one table row have to fit into one line of markdown file.

Pipe characters '|' before first column and afters last column are optional,
but their presence increases readability of markdown file. The number of
hyphens '\-' between pipes '|' in line below headings have to be greater or
equal to three. Colons in this line can be used (they are optional) to
control alignment of data in cells in below rows.

Pictures
--------------------------------------------------------------------------------

### Picture example

```
![alt_text](link_to/image_eg.png)

Figure 1. Castle in Moszna
```

### Picture rendering

![alt_text](link_to/image_eg.png)

Figure 1. Castle in Moszna

Links
--------------------------------------------------------------------------------

### Link example

```
[About writing and formatting on
GitHub](https://help.github.com/articles/about-writing-and-formatting-on-github/)
```

### Link rendering

[About writing and formatting on
GitHub](https://help.github.com/articles/about-writing-and-formatting-on-github/)

Lists
--------------------------------------------------------------------------------

### Unordered lists

Prefixed with asterisk (standard alows also \- sign) and some spaces. Nested
lists indented by two spaces.

#### Unordered lists example

```
* first element (level 1)
  * level 2 - first
  * level 2 second
* second element (level 1)
* third element (level 1)
```

#### Unordered lists rendering

* first element (level 1)
  * level 2 - first
  * level 2 second
* second element (level 1)
* third element (level 1)

### Ordered list

#### Ordered lists example

```
1. first element
    1. level 2 - first
    1. level 2 second
1. second element
    1. level 2 - first
        1. level 3 - first
        1. level 3 second
    1. level 2 second
1. third element
```

#### Ordered lists rendering

1. first element
    1. level 2 - first
    1. level 2 second
1. second element
    1. level 2 - first
        1. level 3 - first
        1. level 3 second
    1. level 2 second
1. third element

### Mixed lists

You can mix unordered and ordered list on different nesting levels.

#### Mixed lists example

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

#### Mixed lists rendering

* first element (level 1)
    1. level 2 - first
    2. level 2 second
* second element (level 1)
    * level 2 - first
        1. level 3 - first
        2. level 3 second
    * level 2 second
* third element (level 1)
