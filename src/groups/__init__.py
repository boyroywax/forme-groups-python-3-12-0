import argparse


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Write package groups to a file.')
    parser.add_argument('help', metavar='help', type=str, nargs='+',
                        help='Get Help')
    args = parser.parse_args()
    # write_groups(args.groups)
