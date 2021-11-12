#!/usr/bin/python3


import sys
import os
import re
import getopt


def main():
    """Main function"""

    def usage():
        print("")
        print("Usage:")
        print("    " + os.path.basename(sys.argv[0]) + " [OPTION] <INPUT FILE> [<OUTPUT FILE>]")
        print("")
        print("    -l --levels=N    Create TOC for N levels of headers. N in range 1 to 6.")
        print("    -c --clean       Clean anchors from all headers.")
        print("")
        print("This script reads Markdown INPUT FILE, prepend every header with anchor used")
        print("in Table of contents. If OUTPUT FILE is missing then conversion is done")
        print("in-place.")
        print("")

    def strip_anchor(line):
        """If line contains anchor then remove it"""
        return re.sub('<a id=".*"></a>', "", line)

    def build_link(curr_level):
        """Build new link"""
        s = "TOC"
        for no in header_numbers[1:curr_level+1]:
            s += "_" + str(no)
        return s

    def trim(s):
        """Strip newline from end, and spaces and tabs from beginning and end of string"""
        s = s.lstrip(" \t")
        return s.rstrip(" \t\n")

    def check_hash_header(line, curr_level):
        """Check if line contains the header marked with 1 to 6 hashes"""
        if re.match("^" + ("#" * curr_level) + "[ \t]", line):
            return trim(line[curr_level + 1:])
        else:
            return ""

    ############
    # BEGIN main
    try:
        opts, args = getopt.getopt(sys.argv[1:], "cl:?", ["help", "levels=", "clean"])
    except getopt.GetoptError as err:
        print(err)
        usage()
        sys.exit(2)

    clean_anchors = False
    toc_levels = 3
    for o, v in opts:
        if o in ("-l", "--levels"):
            try:
                toc_levels = int(v)
                if (toc_levels < 1) or (toc_levels > 6):
                    raise Exception
            except:
                print("Invalid value for toc_levels:", v)
                usage()
                sys.exit(2)
        elif o in ("-c", "--clean"):
            clean_anchors = True
        elif o in ("-?", "--help"):
            usage()
            sys.exit()
        else:
            print("Unknown option:", o)
            usage()
            sys.exit(2)
    if len(args) > 2:
        print("parameters", str(tuple(args[2:])), "ignored")
        usage()
        sys.exit(2)
    if len(args) < 1:
        print("infile parameter is mandatory")
        usage()
        sys.exit(2)
    if len(args) == 2:
        out_file_name = args[1]
    else:
        out_file_name = args[0]
    in_file_name = args[0]

    #                    1  2  3  4  5  6
    header_numbers = [0, 0, 0, 0, 0, 0, 0, 0]

    # Read input file
    fd = open(in_file_name, "r")
    in_lines = fd.readlines()
    fd.close()

    out_lines = []

    # Scan all lines of input file
    prev_line = ""
    for current_line in in_lines:
        level = 0  # no header in current line
        header = ""
        current_line_header = False

        # check if previous and current line contains header in the form
        # header line followed by line of dashes or equal signs or
        # current line contains header prepended with 1-6 hash characters.
        if current_line[0:3] == "===":
            header = strip_anchor(trim(prev_line))
            if len(header) > 0:
                level = 1
        elif current_line[0:3] == "---":
            header = strip_anchor(trim(prev_line))
            if len(header) > 0:
                level = 2
        else:
            for i in range(1, 6+1):
                header = strip_anchor(check_hash_header(current_line, i))
                if len(header) > 0:
                    current_line_header = True
                    level = i
                    break
        # If line contains header build and anchor and replace it with old one
        if (1 <= level) and (level <= toc_levels):
            header_numbers[level] += 1
            header_numbers[level + 1] = 0
            link = build_link(level)
            print("    " * (level - 1) + "* [" + header + "](#" + link + ")")
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
            if current_line_header:
                current_line = strip_anchor(current_line)
            else:
                prev_line = strip_anchor(prev_line)
        out_lines.append(prev_line)
        prev_line = current_line
    out_lines.append(prev_line)

    # Store result to output file
    fd = open(out_file_name, "w")
    for out_line in out_lines:
        # print (un)modified line to output file
        fd.write(out_line)
    fd.close()
    # END main
    ##########


################################################################################
if __name__ == '__main__':
    main()
