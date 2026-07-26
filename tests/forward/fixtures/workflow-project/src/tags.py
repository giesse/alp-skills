def normalize_tags(tags: list[str]) -> list[str]:
    """Return non-blank tags with surrounding whitespace removed."""
    return [tag.strip() for tag in tags if tag.strip()]
