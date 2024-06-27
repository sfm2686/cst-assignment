import logging

import sendgrid
from fastapi import BackgroundTasks
from sendgrid.helpers.mail import Content, Email, Mail, To

from app.config import config
from app.models.survey_models import SurveyRequest

LOGGER = logging.getLogger(__name__)


def send_email(survey_url: str, admin_email: str, domain_name: str):
    sg = sendgrid.SendGridAPIClient(api_key=config.SENDGRID_API_KEY)

    from_email = Email(config.SENDGRID_SENDER_EMAIL)
    to_email = To(admin_email)
    subject = "Invitation to Participate in Survey"
    content = Content(
        "text/plain",
        f"""
    Dear Administrator,

    We are reaching out to inform you about a new survey that has been created for the domain {domain_name}. Your participation and feedback are highly valued.

    Please click on the link below to access the survey:
    {survey_url}

    Thank you for your time and cooperation.

    Best regards,
    Communications, Space & Technology Commission
    """,
    )

    mail = Mail(from_email, to_email, subject, content)

    try:
        response = sg.send(mail)
        LOGGER.info(f"Email sent to {admin_email}. Status Code: {response.status_code}")
    except Exception as e:
        LOGGER.info(f"Error sending email to {admin_email}: {e}")
        raise


async def create_survey(survey_request: SurveyRequest, bgt: BackgroundTasks):
    for domain in survey_request.domains:
        bgt.add_task(
            send_email,
            survey_request.survey_url,
            domain.admin_email,
            domain.domain_name,
        )
    return {"message": "Surveys are created, emails should be sent to admins shortly!"}
