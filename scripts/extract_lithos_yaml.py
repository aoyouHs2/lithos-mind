"""Extract YAML frontmatter from one local Markdown file."""

import argparse
import json
import sys
from pathlib import Path
from typing import Any

import yaml


class FrontmatterError(ValueError):
    """Raised when Markdown frontmatter cannot be extracted safely."""


def extract_frontmatter(path: Path) -> dict[str, Any]:
    """Read and parse YAML frontmatter without reading the Markdown body."""
    try:
        with path.open("r", encoding="utf-8-sig") as markdown_file:
            first_line = markdown_file.readline()
            if first_line.rstrip("\r\n") != "---":
                raise FrontmatterError(
                    "File does not start with YAML frontmatter (expected '---')."
                )

            yaml_lines: list[str] = []
            for line in markdown_file:
                if line.rstrip("\r\n") == "---":
                    break
                yaml_lines.append(line)
            else:
                raise FrontmatterError(
                    "YAML frontmatter is malformed: closing '---' was not found."
                )
    except UnicodeDecodeError as error:
        raise FrontmatterError("File is not valid UTF-8 text.") from error
    except OSError as error:
        raise FrontmatterError(f"Could not read file: {error}") from error

    try:
        parsed = yaml.safe_load("".join(yaml_lines))
    except yaml.YAMLError as error:
        raise FrontmatterError(f"YAML frontmatter is malformed: {error}") from error

    if not isinstance(parsed, dict) or not parsed:
        raise FrontmatterError(
            "YAML frontmatter must be a non-empty object/dictionary."
        )

    return parsed


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Extract YAML frontmatter from one local Markdown file."
    )
    parser.add_argument("markdown_path", help="Path to one local Markdown file")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    source_path = Path(args.markdown_path)

    if not source_path.exists():
        print(f"Error: File does not exist: {source_path}", file=sys.stderr)
        return 1
    if not source_path.is_file():
        print(f"Error: Path is not a file: {source_path}", file=sys.stderr)
        return 1

    try:
        frontmatter = extract_frontmatter(source_path)
        output = {
            "source_path": args.markdown_path,
            "yaml": frontmatter,
            "body_included": False,
        }
        print(json.dumps(output, indent=2, ensure_ascii=False))
    except FrontmatterError as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1
    except (TypeError, ValueError) as error:
        print(f"Error: YAML frontmatter cannot be represented as JSON: {error}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
