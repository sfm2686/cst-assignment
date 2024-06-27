from fastapi import APIRouter, BackgroundTasks

from app.models.survey_models import SurveyRequest
from app.views.survey_views import create_survey

router = APIRouter()


@router.post("/create-survey")
async def create_survey_endpoint(request: SurveyRequest, bgt: BackgroundTasks):
    return await create_survey(request, bgt)
