Pattern-Mathcing Paths
======================

The program accepts two lists of data: the first is a list of patterns, the second
is a list of slash-separated paths. It will print, for each path,
the pattern which best matches that path. 

A pattern is a comma-separated sequence of non-empty fields. For a
pattern to match a path, each field in the pattern must exactly match
the corresponding field in the path. For example, the pattern `x,y` can
only match the path `x/y`. Note that leading and trailing slashes in
paths are ignored, so that `x/y` and `/x/y/` are equivalent.

Patterns can also contain a special field consisting of a *single
asterisk*, which is a wildcard and can match any string in the path.

For example, the pattern `A,*,B,*,C` consists of five fields: three
strings and two wildcards. It will successfully match the paths
`A/foo/B/bar/C` and `A/123/B/456/C`, but not `A/B/C`,
`A/foo/bar/B/baz/C`, or `foo/B/bar/C`.


Input Format
------------

The first line contains an integer, N, specifying the number of
patterns. The following N lines contain one pattern per line. Every pattern should be unique. The next line contains a second integer,
M, specifying the number of paths. The following M lines contain one
path per line. Only ASCII characters will appear in the input.

Output Format
-------------

For each path encountered in the input, we print the *best-matching
pattern*. The best-matching pattern is the one which matches the path
using the fewest wildcards.

For example: given the patterns `*,*,c` and `*,b,*`, and the path
`/a/b/c/`, the best-matching pattern would be `*,b,*`.

If no pattern matches the path, we print `NO MATCH`.


Example Input
-------------

    6
    *,b,*
    a,*,*
    *,*,c
    foo,bar,baz
    w,x,*,*
    *,x,y,z
    5
    /w/x/y/z/
    a/b/c
    foo/
    foo/bar/
    foo/bar/baz/


Project Usage:
--------------

From the project root directory, run the following command to execute the main unit tests;

python -m unittest discover -p 'pattern_path_parser_test.py'

or to execure the application directly e.g. from the scooby directory;

cat ../test/file_01.txt | python pattern_path_parser.py


Dependancies:
-------------
    Python 2.7


