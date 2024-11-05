def get_results(division, n) -> str:
    """Gives the teams to be promoted and relegated from a given division.

    Takes in a list of teams with their points tally and works out which teams
    are promoted and relegated given an input number of teams to promote/relegate.

    Args:
        division - list of team dictionaries containing team name and points tally
        n - number of teams to be promoted and relegated

    Returns:
        String denoting the teams to be promoted and relegated

    Raises:
        Exception with error message if input division is too small for the
        given number of teams to promote and relegate.
    
    """
    
    if len(division) < n*2:
        raise Exception(f'Division is too small to have '
                        f'{n} promoted teams and '
                        f'{n} relegated teams')
    
    return_format = """Promote:
{}

Relegate:
{}
"""
    
    division_standings = sorted(division, key=lambda x: x['points'], reverse=True)
    promoted_teams = "\n".join([team["name"] for team in division_standings[:n]])
    relegated_teams = "\n".join([team["name"] for team in division_standings[-n:]])

    return return_format.format(promoted_teams, relegated_teams)