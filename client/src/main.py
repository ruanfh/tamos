import argparse
import json
import sys

from config import get_server_url, set_server_url
from builder import build_gem
from validator import validate_gem_submission
from submitter import submit_gem


def cmd_submit(args):
    """Handle `tamos submit`."""
    server = get_server_url(args.server)

    # Build gem from CLI flags or JSON file
    gem = build_gem(args)

    # Validate locally
    errors = validate_gem_submission(gem)
    if errors:
        print("Gem validation failed:")
        for err in errors:
            print(" -", err)
        sys.exit(1)

    # Submit to server
    gem_id = submit_gem(server, gem)
    print(f"Gem submitted successfully. ID: {gem_id}")


def cmd_validate(args):
    """Handle `tamos validate`."""
    gem = build_gem(args)
    errors = validate_gem_submission(gem)

    if errors:
        print("Gem is invalid:")
        for err in errors:
            print(" -", err)
        sys.exit(1)

    print("Gem is valid.")


def cmd_config_set_server(args):
    """Handle `tamos config set-server`."""
    set_server_url(args.url)
    print(f"Default server set to: {args.url}")


def cmd_config_show(args):
    """Handle `tamos config show`."""
    try:
        server = get_server_url(None)
        print(json.dumps({"server": server}, indent=2))
    except RuntimeError:
        print("No server configured.")


def build_parser():
    parser = argparse.ArgumentParser(
        prog="tamos",
        description="TAMOS Client — submit gems to a TAMOS server"
    )

    sub = parser.add_subparsers(dest="command")

    # submit
    p_submit = sub.add_parser("submit", help="Submit a gem to the server")
    p_submit.add_argument("--server", help="Override server URL")
    p_submit.add_argument("--description", help="Gem description")
    p_submit.add_argument("--url", help="Gem URL")
    p_submit.add_argument("--author", help="Gem author (optional)")
    p_submit.add_argument("--file", help="Load gem from JSON file")
    p_submit.set_defaults(func=cmd_submit)

    # validate
    p_validate = sub.add_parser("validate", help="Validate a gem locally")
    p_validate.add_argument("--description", help="Gem description")
    p_validate.add_argument("--url", help="Gem URL")
    p_validate.add_argument("--author", help="Gem author (optional)")
    p_validate.add_argument("--file", help="Load gem from JSON file")
    p_validate.set_defaults(func=cmd_validate)

    # config
    p_config = sub.add_parser("config", help="Manage client configuration")
    config_sub = p_config.add_subparsers(dest="config_command")

    p_set = config_sub.add_parser("set-server", help="Set default server URL")
    p_set.add_argument("url")
    p_set.set_defaults(func=cmd_config_set_server)

    p_show = config_sub.add_parser("show", help="Show current config")
    p_show.set_defaults(func=cmd_config_show)

    return parser


def main():
    parser = build_parser()
    args = parser.parse_args()

    if not hasattr(args, "func"):
        parser.print_help()
        return

    args.func(args)


if __name__ == "__main__":
    main()