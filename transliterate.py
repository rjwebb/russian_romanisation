import argparse
import csv
import fileinput
import sys


def make_lookup_table(origin_script, target_script):
    return dict(zip(origin_script, target_script))


def do_transliteration(inputfile, lowercase_lookup, uppercase_lookup):

    for line in inputfile:
        for c in line:
            # Look up using the lowercase script
            new_c = lowercase_lookup.get(c, None)
            if new_c:
                yield new_c
                continue

            # Look up using the uppercase script
            new_c = uppercase_lookup.get(c, None)
            if new_c:
                yield new_c.upper()
                continue

            # Otherwise don't romanise this character
            yield c


if __name__=='__main__':

    # Load and parse the file containing the mapping from Cyrillic to the
    # various romanisations.
    data = csv.reader(open('russian_romanisation.csv'))

    data_t = list(map(list, zip(*data)))

    scripts = {l[0]:l[1:] for l in data_t}

    # Remove the Cyrillic input scripts
    lowercase_script = scripts.pop('lowercase')
    uppercase_script = scripts.pop('uppercase')

    # The names of the romanisations we can convert into
    available_scripts = list(scripts.keys())

    parser = argparse.ArgumentParser(
        description='Transliterate Russian using various romanisations'
    )
    parser.add_argument(
        'target', choices=available_scripts, help='The romanisation to use.'
    )
    parser.add_argument(
        'inputfile', nargs='?', type=argparse.FileType('r'), default=sys.stdin,
        help='The text to be translated. May be a file or piped stdin.'
    )

    args = parser.parse_args()

    target = scripts[args.target]

    lowercase_lookup = make_lookup_table(lowercase_script, target)
    uppercase_lookup = make_lookup_table(uppercase_script, target)

    if args.inputfile:
        result = do_transliteration(args.inputfile, lowercase_lookup, uppercase_lookup)
        for c in result:
            print(c, end='')
    else:
        # If no input data was provided, there is nothing to process
        pass
