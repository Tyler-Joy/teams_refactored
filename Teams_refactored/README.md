# Refactored Teams Django Project

This project demonstrates the three requested refactoring steps:

1. A `Team` dataclass stores each team's name, description, and member names. A `Dict[str, Team]` in `teams/data.py` provides lookup by URL slug.
2. There are two named URL patterns: `teams:team_list` and `teams:team_detail`. Templates use Django's `{% url %}` tag to build links.
3. Both the list and detail templates extend the shared `teams/base.html` template.

## Run the project

From the folder containing `manage.py`:

```bash
python -m venv .venv
```

Activate the environment:

- Windows PowerShell: `.venv\\Scripts\\Activate.ps1`
- Windows Command Prompt: `.venv\\Scripts\\activate.bat`
- macOS/Linux: `source .venv/bin/activate`

Install Django and start the server:

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Open http://127.0.0.1:8000/ in your browser.

## Customize the teams

Open `teams/data.py`. Edit the example entries in `TEAMS`, or add another entry using a URL-friendly key:

```python
'qa': Team(
    name='QA Team',
    description='The QA Team tests the application.',
    members=['Sam Example', 'Chris Example'],
),
```

The team list and detail page update automatically because they use the same data dictionary and one shared detail view/template.

## Note

The only uploaded source file was `manage.py`, so the project structure and sample team content in this finished starter project were created from the assignment requirements. Replace the sample teams and members with the exact information from your original coursework if it differs.
