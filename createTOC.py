#!/usr/bin/python3


import sys, os, re, getopt


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


def main() :
    """Main function"""

    def usage():
        print("")
        print("Usage:")
        print("    " + os.path.basename(sys.argv[0]) + " [OPTION] <INPUT FILE> [<OUTPUT FILE>]")
        print("")
        print("    -l --levels=N    Create TOC for N levels of headers. N in range 1 to 6.")
        print("")
        print("This script reads Markdown INPUT FILE, prepend every header with anchor used")
        print("in Table of contents. If OUTPUT FILE is missing then conversion is executed")
        print("in-place.")
        print("")

    ############
    # BEGIN main
    try:
        opts, args = getopt.getopt(sys.argv[1:], "l:?", ["help", "levels="])
    except getopt.GetoptError as err:
        print(err)
        usage()
        sys.exit(2)

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

    number = [0, 0, 0, 0, 0, 0, 0, 0]

    # Read input file
    fd = open(in_file_name, "r")
    in_lines = fd.readlines()
    fd.close()

    out_lines = []

    # Scan all lines of input file
    prev_line = ""
    for last_line in in_lines :
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
            print("  " * (level - 1) + "* [" + strip_anchor(header) + "](#" + link + ")")
            prev_line = strip_anchor(prev_line)
            anchor = '<a id="' + link + '"></a>'
            prefix = anchor
        out_lines.append(prefix + prev_line)
        prev_line = last_line
    out_lines.append(prev_line)

    # Store result to output file
    fd = open(out_file_name, "w")
    for out_line in out_lines :
        # print (un)modified line to output file
        fd.write(out_line)
    fd.close()
    # END main
    ##########

################################################################################
if __name__ == '__main__':
    main()