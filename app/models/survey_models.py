from typing import List

from pydantic import BaseModel, EmailStr, HttpUrl


class Domain(BaseModel):
    domain_name: str
    admin_email: EmailStr


class SurveyRequest(BaseModel):
    survey_url: HttpUrl
    domains: List[Domain]
