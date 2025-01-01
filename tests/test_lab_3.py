import pytest
from lab_3.lab_3 import read, Data
from io import StringIO


@pytest.fixture
def test_input():
    return """3 2 1 10
              3 1 2 3
              2 2 3
              1 1
              1 2
           """


@pytest.fixture
def expected_output():
    return Data(
        n=3,
        m=2,
        start_room=1,
        initial_chips=10,
        rooms=[[1, 2, 3], [2, 3], [1]],
        costs=[1, 2]
    )


@pytest.fixture
def mock_open(monkeypatch, test_input):
    def _mock_open(*args, **kwargs):
        return StringIO(test_input)
    monkeypatch.setattr("builtins.open", _mock_open)


def test_read(mock_open, expected_output):
    result = read()
    assert result == expected_output
