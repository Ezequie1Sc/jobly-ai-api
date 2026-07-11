from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(
    prefix="/recommendations",
    tags=["Recommendations"]
)


class Job(BaseModel):
    id: str
    title: str
    company: str
    skills: list[str]


class RecommendationRequest(BaseModel):
    cv_skills: list[str]
    jobs: list[Job]


@router.post("/")
def recommend_jobs(data: RecommendationRequest):
    user_skills = {
        skill.lower().strip()
        for skill in data.cv_skills
    }

    results = []

    for job in data.jobs:
        required_skills = {
            skill.lower().strip()
            for skill in job.skills
        }

        matches = required_skills.intersection(user_skills)
        missing = required_skills.difference(user_skills)

        compatibility = (
            round(len(matches) / len(required_skills) * 100)
            if required_skills
            else 0
        )

        results.append({
            "id": job.id,
            "title": job.title,
            "company": job.company,
            "compatibility": compatibility,
            "strengths": sorted(matches),
            "missing_skills": sorted(missing)
        })

    results.sort(
        key=lambda job: job["compatibility"],
        reverse=True
    )

    return {
        "success": True,
        "recommended_jobs": results[:5]
    }