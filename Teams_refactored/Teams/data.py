from dataclasses import dataclass
from typing import Dict, List

@dataclass
class Team:
    name: str
    description: str
    members: List[str]

# Replace or add these examples with the teams from your assignment.
TEAMS: Dict[str, Team] = {
    'design': Team(
        name='Design Team',
        description='The Design Team plans the look, feel, and user experience of our projects.',
        members=['Alex Morgan', 'Jordan Lee', 'Taylor Smith'],
    ),
    'development': Team(
        name='Development Team',
        description='The Development Team builds, tests, and maintains our applications.',
        members=['Casey Brown', 'Riley Davis', 'Jamie Wilson'],
    ),
    'marketing': Team(
        name='Marketing Team',
        description='The Marketing Team shares project updates and helps connect our work with its audience.',
        members=['Morgan Taylor', 'Avery Johnson', 'Cameron White'],
    ),
}
