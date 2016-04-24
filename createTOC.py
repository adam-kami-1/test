#!/usr/bin/python


import sys, os, string, re


def trim(s) :
    """Strip newline from end, and spaces and tabs from beginning and end of string"""
    s = s.lstrip(" \t")
    return s.rstrip(" \t\n")


def check_hash_header(line, level) :
    """Check if line contains the header marked with 1 to 6 hashes"""
    if re.match("^" + ("#" * level) + "[ \t]", line) :
        return trim(line[level + 1:])
    else :
        return ""


def build_link(level, number) :
    """Build new link"""
    s = "TOC"
    for l in number[1:level+1] :
        s += "_" + str(l)
    return s


def strip_anchor(line) :
    """If line contains anchor then remove it"""
    return re.sub('<a id=".*"></a>', "", line)


def main(in_file, toc_levels) :
    """Main function"""
    out_file = '#' + in_file + '#'
    number = [0, 0, 0, 0, 0, 0, 0, 0]

    # Read input file
    fd = open(in_file, "r")
    lines = fd.readlines()
    fd.close()

    # Open temporary output file
    fd = open(out_file, "w")

    # Scan all lines of input file
    prev_line = ""
    for last_line in lines :
        prefix = ""
        level = 0

        # check if previous or last line contains header
        if last_line[0:3] == "===" :
            level = 1
            header = trim(prev_line)
        elif last_line[0:3] == "---" :
            level = 2
            header = trim(prev_line)
        else :
            for i in range(1, toc_levels+1) :
                header = check_hash_header(last_line, i)
                if len(header) > 0 :
                    level = i
                    break
        # If line contains header build anchor and replace it with old one
        if level > 0 :
            number[level] += 1
            number[level + 1] = 0
            link = build_link(level, number)
            print "  " * (level - 1) + "* [" + strip_anchor(header) + "](#" + link + ")"
            prev_line = strip_anchor(prev_line)
            anchor = '<a id="' + link + '"></a>'
            prefix = anchor

        # Print (un)modifiel line to temporary output file
        fd.write(prefix + prev_line)
        prev_line = last_line
    fd.write(prev_line)
    fd.close()

    # Swap temporay output and input file
    os.rename(in_file, in_file + "~")
    os.rename(out_file, in_file)

################################################################################

if len(sys.argv) < 2 :
    print "Usage:"
    print "    " + os.path.basename(sys.argv[0]) + " <input md file>"
    print ""
    print "This script reads Markdown file, prepend every header (levels 1 - 3)"
    print "with anchor used later in Table of contents. This table is printed"
    print "to standard output. You can store it in temporary file, and later"
    print "insert its content in to desired place of Markdown file."
    print ""
    quit()
main(sys.argv[1], 3)
