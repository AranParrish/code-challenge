from src.main import get_results
import pytest

given_division = [
    {
        "name": "Rockets",
        "points": 64,
    },
    {
        "name": "Cardinals",
        "points": 77,
    },
    {
        "name": "Bruisers",
        "points": 51,
    },
    {
        "name": "Renegades",
        "points": 37,
    },
    {
        "name": "Porpoises",
        "points": 52,
    },
]


def test_returns_one_team_to_promote_and_one_team_to_relegate():
    result_string = """Promote:
Cardinals

Relegate:
Renegades
"""
    assert get_results(given_division, 1) == result_string


def test_returns_two_teams_to_promote_and_two_teams_to_relegate():
    result_string = """Promote:
Cardinals
Rockets

Relegate:
Bruisers
Renegades
"""
    assert get_results(given_division, 2) == result_string

def test_raises_exception_if_promoting_and_relegating_not_possible():
    with pytest.raises(Exception) as excinfo:
        get_results(given_division, 3)
    assert 'Division is too small' in str(excinfo.value)