from src.tags import normalize_tags


def test_removes_blank_tags_and_surrounding_space() -> None:
    assert normalize_tags(["  News ", " ", "Local"]) == ["News", "Local"]
