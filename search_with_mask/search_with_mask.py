
import os, io
import re
import codecs


try:
    from argparse import ArgumentParser
except ImportError:  # for version < 3.0
    from ArgParse import ArgumentParser


__prog__ = "search_with_mask"
__description__ = "Search with mask"
__version__ = "0.1"
__version_string__ = '%s version %s' % (__prog__, __version__)



def get_args():
    """Run Argument Parser and get argument from command line"""
    parser = ArgumentParser(prog=__prog__,
                            description=__description__)
    parser.add_argument('-p', dest='path', action='append',
                        default=[],
                        help="""Path to run search files\n\
(default - current directory), example usage: -p. -p../DirName""")
    parser.add_argument('-m', dest='mask', action='append',
                        default=[],
                        help="mask for search\n\
1) hello - simple mask\n\
2) 'hello how are you' - masks(separated by space)")
    parser.add_argument('-a', dest='amask', action='append',
                        default=[],
                        help="additional mask for result\n\
1) hello - simple mask\n\
2) 'hello how are you' - masks(separated by space)")
    parser.add_argument('-V', '--version',
                        action='version',
                        version=__version_string__)
    parser.add_argument('--verbose', dest='verbose', action='store_true',
                        default=False,
                        help="Verbose search")
    return parser.parse_args()



def write_file(fname, s):
    """
Write output file.
"""
    f = io.open(fname, 'w')
    strings = u'%s\n' % s
    f.write(strings)
    f.close()



def run():
    args = get_args()
    path = args.path[0]

    mask = []
    mask = args.mask

    mask_file = "Keys.txt"
    # file exists
    if os.path.isfile(mask_file):
        with open(mask_file, 'r' ) as f:
            for myline in f:
                # убрать '\n'
                myline = myline.split('\n')
                myline = myline[0]
                mask.append(myline)

    amask = []
    amask = args.amask
    if len(amask) == 0:
        amask = mask

    verbose = args.verbose
    print('path: %s' % path)
    print('mask: %s' % mask)
    print('amask: %s' % amask)
    list_files = []
    print('List of files:')

    # составляем список
    for root, dirs, files in os.walk(path):
        for file in files:
            # только в файлах txt
            if file.endswith(".txt"):
                # только после маски, в нужной папке
                file_path = os.path.join(root, file)
                if re.match(".*\/[0-9][0-9]/.*", file_path):
                    print(file_path)
                    list_files.append(file_path)

    # перебираю список масок
    count = 0
    result = ''
    for m in mask:
        # ищу в списке файлов
        for f in list_files:

            with open(f, 'r') as ff:
                for myline in ff:
                    if m in myline:
                        count = count + 1
                        if verbose:
                            print('find %s in %s: %s' % (m,  f, myline))
                if count != 0:
                    result = "%s\nmask '%s' find in file %s times: %s" % (result, m, f , count)
                count = 0
            ff.close()

    write_file("search.log", result)

    # дополнительная маска
    result_new = result.splitlines()
    # for line in result_new:
    #     print('1: line: %s\n' % line)
    for m in amask:
        for line in result_new:
            if line.find(m) > 0:
                print('%s' % line)


if __name__ == '__main__':
    run()
