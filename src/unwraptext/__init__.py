import sys
import argparse
import select

from .unwraptext import unwrap_markdown


TYPELIST = ["markdown", "latex"]


def main():
    """Entry point for the application script"""
    parser = argparse.ArgumentParser()
    parser.add_argument("-ft", "--filetype", type=str, default="markdown")
    parser.add_argument('path', nargs='?')
    args = parser.parse_args()
    text = None
    if not args.path:
        if select.select([sys.stdin, ], [], [], 0.0)[0]:
            text = sys.stdin.read()
        else:
            parser.print_help(sys.stderr)
            sys.exit(1)
    else:
        with open(args.path) as f:
            text = f.read()
    if text is None:
        sys.exit(1)
    else:
        if args.filetype == "markdown" or args.filetype not in TYPELIST:
            sys.stdout.write(unwrap_markdown(text))
