from account.utils import send_activation_code
from SuiseiRadioProject.celery import app

@app.task
def send_activation_code_task(email, activation_code):
    send_activation_code(email, activation_code)