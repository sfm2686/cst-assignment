# Survey Delivery System

This project is a Survey Delivery System that automates the delivery of survey links to administrators of specified domain names. It includes an API endpoint to accept survey details and a list of domains, and it sends emails to the administrators of those domains with the survey link. The project uses FastAPI for the API and SendGrid for sending emails.

## Features

- Accepts survey URL and a list of domain administrators via a POST request.
- Sends an email to each administrator with the survey link.
- Runs email sending tasks in the background.
- Includes logging for email delivery status.
- Dockerized for easy setup and deployment.

## How It Works

1. **API Endpoint**: The `/create-survey` endpoint accepts a JSON payload with the survey URL and a list of domains. 
2. **Background Tasks**: For each domain, a background task is created to send an email to the administrator.
3. **Email Sending**: Emails are sent using SendGrid, and the status of each email is logged.
**_Note:_** the emails received will most likely be found in the spam folder and not the inbox.
4. **Dockerized**: The project is containerized using Docker for easy deployment.

## Setup and Installation

### Prerequisites

- Docker and Docker Compose installed on your system.
- A SendGrid account and API key.

### Configuration

This project requires two environment variables to run, which should be placed in the `.env` file prior to running the Docker container. If any changes are made to the environment variables, the Docker container must be restarted, but there is no need for it to be rebuilt.

```plaintext
SENDGRID_API_KEY=<SENDGRID_API_KEY>
SENDGRID_SENDER_EMAIL=<SENDGRID_SENDER_EMAIL>
```

### Email Server

As for the email server, this project utilizes SendGrid, before the project is run please make sure a SendGrid account is configured.

1. Create a [SendGrid](https://sendgrid.com/en-us) account if you dont have one
2. Generate an API key and place it in the `.env` file to work as an environment variable for the docker container
```plaintext
SENDGRID_API_KEY=<Your newly generated API key>
```
3. Create and verify a [Sender in SendGrid](https://www.twilio.com/docs/sendgrid/ui/sending-email/senders)
4. Add your sender to the `.env` file in order to be used in the emails
```plaintext
SENDGRID_SENDER_EMAIL=<Your verified sender>
```

### Build the Docker Image

To build the Docker image, run:

```bash
docker-compose build
```

to start the application, run:
```bash
docker-compose up
```
or to run detached to the docker image
```bash
docker-compose up -d
```

This will start the FastAPI application on `http://localhost:8000`.

## Documentation
Project documentation can be accessed at the following URLs:

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

These documentation interfaces allows the view of the available endpoint, its required parameters, and the expected response. These interfaces can also be used to send requests to the API endpoint directly from the browser.

## Scripts
To format/reformat the implemented code, run the following script:
```bash
./scripts/format
```

To run the project locally without docker, run the following script:
```bash
./scripts/run-local.sh
```

## Future Enhancements

- Deploy the project
- Store the created surveys in order to avoid spamming and duplicates
- A user-friendly frontend for survey links to be created
- Keep track of the email status of each admin/domain in order to have resend functionality in case of failures

## Author

- [Sultan Mira](https://github.com/sfm2686) - initial work

Please feel free to contact me for any questions or suggestions.