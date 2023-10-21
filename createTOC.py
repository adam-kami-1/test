#!/usr/bin/python3
"""
createTOC.py

Create table of contents for markdown file. Use option -? or --help to get
more information.
"""


__author__ = "Adam Kaminski <adamkami1@wp.pl>"
__date__ = "13 November 2021"
__version__ = "1.0"


import sys
# import os
import re
import getopt


USAGE_TXT = """
Usage:
    createTOC.py [OPTION] <INPUT FILE> [<OUTPUT FILE>]

    -l --levels=N   Create table of contents for N levels of headers.
                    N in range 0 to 6. Default value: 3.
                    0 means: don't create table of contents. When
                    option --clean is used, removes table of contents
                    and all anchors.
    -c --clean      Clean anchors from all headers higher than N.
                    If N == 0 clean also table of contents

This script reads Markdown INPUT FILE, prepend every header with anchor
used in table of contents. If OUTPUT FILE is missing then conversion is
done in-place.
When INPUT FILE contains two lines, one containing marker :TOC: and the
other containing marker :COT: then all lines in INPUT FILE between
lines containing those markers are treated as old version of table of
contents to be removed or replaced by new table of contents created by
this script.
It is convenient to hide those markers inside HTML comment:
<!-- :TOC: -->
<!-- :COT: -->
If INPUT FILE does not contain :TOC: and :COT: markers, then newly
created table of contents is printed out into standard output.
"""


def main() -> None:
    """Main function"""

    def strip_anchor(line: str) -> str:
        """If line contains TOC anchor then return line without anchor"""
        return re.sub('<a id="TOC_.*"></a>', "", line)

    def build_link(curr_level: int) -> str:
        """Build new link in the form like: TOC_1_2_3"""
        s = "TOC"
        for no in header_numbers[1:curr_level+1]:
            s += "_" + str(no)
        return s

    def check_hash_header(line: str, curr_level: int) -> str:
        """Check if line contains the header marked with 1 to 6 hashes"""
        if re.match("^" + ("#" * curr_level) + "[ \t]", line):
            return line[curr_level + 1:].strip()
        else:
            return ""

    ############
    # BEGIN main
    try:
        opts, args = getopt.getopt(sys.argv[1:],
                                   "c?l:",
                                   ["clean", "help", "levels="])
    except getopt.GetoptError as err:
        print(err)
        print(USAGE_TXT)
        sys.exit(2)

    clean_anchors = False
    toc_levels = 3
    for option, value in opts:
        if option in ("-l", "--levels"):
            try:
                toc_levels = int(value)
                if (toc_levels < 0) or (toc_levels > 6):
                    raise ValueError
            except ValueError:
                print("Invalid value for --levels:", value)
                print(USAGE_TXT)
                sys.exit(2)
        elif option in ("-c", "--clean"):
            clean_anchors = True
        elif option in ("-?", "--help"):
            print(USAGE_TXT)
            sys.exit()
        else:
            print("Unknown option:", option)
            print(USAGE_TXT)
            sys.exit(2)
    if len(args) > 2:
        print("parameters", str(tuple(args[2:])), "ignored")
        print(USAGE_TXT)
        sys.exit(2)
    if len(args) < 1:
        print("infile parameter is mandatory")
        print(USAGE_TXT)
        sys.exit(2)
    if len(args) == 2:
        out_file_name = args[1]
    else:
        out_file_name = args[0]
    in_file_name = args[0]

    #                    1  2  3  4  5  6
    header_numbers = [0, 0, 0, 0, 0, 0, 0, 0]
    toc_start_line = -1
    toc_end_line = -1
    toc = []

    # Read input file
    with open(in_file_name, "r") as fd:
        in_lines = fd.readlines()

    out_lines = []

    # Scan all lines of input file
    prev_line = ""
    curr_line_no = 0
    for current_line in in_lines:
        level = 0  # no header in current line
        header = ""
        current_line_header = False

        # check if previous and current line contains header in the form
        # header line followed by line of dashes or equal signs or
        # current line contains header prepended with 1-6 hash characters.
        if current_line[0:3] == "===":
            # Header level 1 in previous line
            header = strip_anchor(prev_line.strip())
            if len(header) > 0:
                level = 1
        elif current_line[0:3] == "---":
            # Header level 2 in previous line
            header = strip_anchor(prev_line.strip())
            if len(header) > 0:
                level = 2
        else:
            for i in range(1, 6+1):
                header = strip_anchor(check_hash_header(current_line, i))
                if len(header) > 0:
                    current_line_header = True
                    level = i
                    break
            if level == 0:
                if toc_start_line == -1:
                    if current_line.find(":TOC:") != -1:
                        toc_start_line = curr_line_no
                if toc_end_line == -1:
                    if current_line.find(":COT:") != -1:
                        toc_end_line = curr_line_no
        if (1 <= level) and (level <= toc_levels):
            # If line contains header, build and anchor and replace the old one
            header_numbers[level] += 1
            header_numbers[level + 1] = 0
            link = build_link(level)
            toc.append("    " * (level - 1) + "* [" + header + "](#" + link + ")")
            anchor = '<a id="' + link + '"></a>'
            if current_line_header:
                current_line = strip_anchor(current_line)
                current_line = current_line.partition(header)
                current_line = current_line[0] + anchor + current_line[1] + current_line[2]
                pass
            else:
                prev_line = strip_anchor(prev_line)
                prev_line = anchor + prev_line
        elif clean_anchors and (level > toc_levels):
            # If line contains header, remove an anchor
            if current_line_header:
                current_line = strip_anchor(current_line)
            else:
                prev_line = strip_anchor(prev_line)
        if curr_line_no > 0:
            out_lines.append(prev_line)
        prev_line = current_line
        curr_line_no += 1
    out_lines.append(prev_line)

    # Store result to output file
    with open(out_file_name, "w") as fd:
        if (0 <= toc_start_line) and \
           (toc_start_line < toc_end_line) and \
           ((toc_levels > 0) or clean_anchors):
            for out_line in out_lines[0: toc_start_line + 1]:
                fd.write(out_line)
            # Insert new table of contents into OUTPUT FILE
            for out_line in toc:
                fd.write(out_line + "\n")
            for out_line in out_lines[toc_end_line:]:
                fd.write(out_line)
        else:
            for out_line in out_lines:
                fd.write(out_line)
            # Print out new table of contents
            for out_line in toc:
                print(out_line)
    # END main
    ##########


###############################################################################
if __name__ == '__main__':
    main()
