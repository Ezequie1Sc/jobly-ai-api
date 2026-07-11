def generate_chat_response(
    message: str,
    cv_skills: list[str],
    job: dict | None = None
) -> str:
    question = message.lower().strip()

    skills_text = ", ".join(cv_skills) if cv_skills else "ninguna habilidad"

    if "habilidades" in question:
        return (
            f"He detectado estas habilidades en tu CV: {skills_text}."
        )

    if "vacante" in question or "empleo" in question:
        if not job:
            return (
                "Primero selecciona una vacante para poder analizarla "
                "y compararla con tu CV."
            )

        title = job.get("title", "Vacante")
        required_skills = job.get("skills", [])

        user_skills = {
            skill.lower(): skill
            for skill in cv_skills
        }

        matches = [
            skill
            for skill in required_skills
            if skill.lower() in user_skills
        ]

        missing = [
            skill
            for skill in required_skills
            if skill.lower() not in user_skills
        ]

        return (
            f"Para la vacante {title}, cumples con: "
            f"{', '.join(matches) or 'ninguna habilidad detectada'}. "
            f"Te faltaría reforzar: "
            f"{', '.join(missing) or 'ninguna habilidad importante'}."
        )

    if "mejorar" in question or "cv" in question:
        return (
            "Puedes mejorar tu CV agregando logros cuantificables, "
            "describiendo mejor tus proyectos y destacando las "
            "tecnologías más importantes para cada vacante."
        )

    return (
        "Puedo ayudarte a revisar tus habilidades, analizar una vacante "
        "o darte recomendaciones para mejorar tu CV."
    )