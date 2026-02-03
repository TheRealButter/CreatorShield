"""Command line interface for CreatorShield."""

import argparse

from .core import shield_message


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Shield creator messages.")
    parser.add_argument("--message", required=True, help="Message to shield.")
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    print(shield_message(args.message))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
