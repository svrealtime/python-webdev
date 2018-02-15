import argparse

from headers.app import HeaderChecker

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Checking http security headers.')
    parser.add_argument('url', help='The url to check the headers for.')
    args = parser.parse_args()

    checker = HeaderChecker(args.url)
    checker.check()
    checker.report()
