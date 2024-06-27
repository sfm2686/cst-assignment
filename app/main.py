from fastapi import FastAPI
import logging
import app.controllers.survey_controllers as survey_controllers

logging.getLogger('main').setLevel(logging.INFO)

app = FastAPI()

app.include_router(survey_controllers.router)
