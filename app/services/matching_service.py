SKILLS = [
    "Angular",
    "React",
    "Vue",
    "TypeScript",
    "JavaScript",
    "HTML",
    "CSS",
    "Tailwind CSS",
    "Bootstrap",
    "RxJS",
    "Node.js",
    "Express",
    "Python",
    "FastAPI",
    "Flask",
    "Django",
    "Java",
    "Spring Boot",
    "C#",
    ".NET",
    "PHP",
    "Laravel",
    "PostgreSQL",
    "MySQL",
    "MongoDB",
    "SQLite",
    "Docker",
    "Kubernetes",
    "Git",
    "GitHub",
    "GitLab",
    "REST API",
    "GraphQL",
    "AWS",
    "Azure",
    "Google Cloud",
    "Flutter",
    "React Native",
    "Figma",
    "Scrum",
    "CI/CD",
]


def extract_skills(text: str) -> list[str]:
    """
    Busca habilidades conocidas dentro del texto del CV.
    """

    normalized_text = text.lower()

    found_skills = [
        skill
        for skill in SKILLS
        if skill.lower() in normalized_text
    ]

    return found_skills