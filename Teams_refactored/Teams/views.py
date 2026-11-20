from django.http import Http404
from django.shortcuts import render

from .data import TEAMS

def team_list(request):
    return render(request, 'teams/team_list.html', {'teams': TEAMS.items()})

def team_detail(request, team_slug):
    # One view handles every team. The URL slug is used to find the Team object.
    team = TEAMS.get(team_slug)
    if team is None:
        raise Http404('Team not found')
    return render(request, 'teams/team_detail.html', {'team': team, 'team_slug': team_slug})
