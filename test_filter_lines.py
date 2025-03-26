import pytest
from filter_lines import filter_lines


@pytest.fixture
def sample_file(tmp_path):
    content = "apple\nbanana\napple pie\norange\ngrape juice\napple tart\n"
    input_file = tmp_path / "test_input.txt"
    input_file.write_text(content)
    return input_file


@pytest.mark.parametrize("keyword,expected", [
    ("apple", ["apple\n", "apple pie\n", "apple tart\n"]),
    ("banana", ["banana\n"]),
    ("juice", ["grape juice\n"]),
    ("pie", ["apple pie\n"]),
    ("xyz", []),
])
def test_filter_lines(sample_file, tmp_path, keyword, expected):
    output_file = tmp_path / "result.txt"
    filter_lines(str(sample_file), keyword, str(output_file))
    assert output_file.read_text().splitlines(keepends=True) == expected
