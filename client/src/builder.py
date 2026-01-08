import json


def build_gem(args) -> dict:
    """
    Build a gem from CLI arguments or a JSON file.
    Priority:
      1. --file (load full gem)
      2. CLI fields (description, url, tags)
    """

    # 1. Load from JSON file
    if args.file:
        with open(args.file, "r", encoding="utf-8") as f:
            return json.load(f)

    # 2. Build from CLI flags
    gem = {}

    if args.description:
        gem["description"] = args.description.strip()

    if args.url:
        gem["url"] = args.url.strip()

    if args.tags:
        gem["tags"] = [t.strip() for t in args.tags]

    return gem