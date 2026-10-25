"""Command-line interface for fibonacci_kata."""

import argparse

from fibonacci_kata import fibonacci


def build_parser() -> argparse.ArgumentParser:
    """Build the command-line argument parser."""
    parser = argparse.ArgumentParser(
        prog="fibonacci-kata",
        description="Print a Fibonacci number, or a range of Fibonacci numbers.",
    )
    parser.add_argument(
        "n",
        type=int,
        nargs="?",
        help="Index of a single Fibonacci number.",
    )
    parser.add_argument(
        "--start",
        type=int,
        help="Start of a range (inclusive).",
    )
    parser.add_argument(
        "--end",
        type=int,
        help="End of a range (inclusive).",
    )
    return parser


def main() -> None:
    """Run the Fibonacci command-line interface."""
    parser = build_parser()
    args = parser.parse_args()

    if args.start is not None and args.end is not None:
        if args.start < 0 or args.end < 0:
            parser.error("Fibonacci indices must be non-negative.")
        if args.start > args.end:
            parser.error("--start must be less than or equal to --end.")

        for i in range(args.start, args.end + 1):
            print(fibonacci(i))
    elif args.start is not None or args.end is not None:
        parser.error("Provide both --start and --end.")
    elif args.n is not None:
        try:
            print(fibonacci(args.n))
        except ValueError as error:
            parser.error(str(error))
    else:
        parser.error("Provide either a single number, or --start and --end.")


if __name__ == "__main__":
    main()
