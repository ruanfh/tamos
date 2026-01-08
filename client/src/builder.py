import json


def build_gem(args) -> dict:
    """
    Build a gem from CLI arguments or a JSON file.
    Priority:
      1. --file (load full gem)
      2. CLI fields (description, url, author)
    """

    # 1. Load from JSON file
    if args.file:
        with open(args.file, "r", encoding="utf-8") as f:
            gem = json.load(f)
        # Remove date if present
        gem.pop("date", None)
        # Remove tags if present
        gem.pop("tags", None)
        return gem

    # 2. Build from CLI flags
    gem = {}

    if args.description:
        gem["description"] = args.description.strip()

    if args.url:
        gem["url"] = args.url.strip()

    if hasattr(args, "author") and args.author:
        gem["author"] = args.author.strip()

    return gem