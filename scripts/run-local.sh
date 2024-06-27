#!/bin/sh
exec uvicorn --reload-exclude --proxy-headers --host "0.0.0.0" --port "8000" --log-config "logging.ini" "app.main:app"