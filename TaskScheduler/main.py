from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from EmailService import *
from datetime import datetime

app = FastAPI()

templates = Jinja2Templates(directory=".")
app.mount("/static", StaticFiles(directory="static", html = True), name="static")

# Algorithm: For sending emails
# Approach 1: Read the CSV file and start sending the emails
# Approach 2: Populate a data structure on the fly and read that as part of this script.

# Dictionary will be read by the cron to send emails across.
# {[date, time] : [(email, subject, description), email, subject, description]}. 
cachedListOfEmail = {}

@app.get("/", response_class=HTMLResponse)
async def get(request: Request):
    # Load static files
    return templates.TemplateResponse('index.html', {"request" : request})

@app.post('/schedule', response_class=HTMLResponse)
def schedule(request: Request, email: str = Form(...), Subject: str = Form(...), Description: str = Form(...), date: str = Form(...)):
    # Main logic for sending emails
    email_list = ["suvansharora07@gmail.com", "cu.16bcs1365@gmail.com","20mcs018@iiitdmj.ac.in", "cu.16bcs1351@gmail.com", "shubhamraghuvanshi7@gmail.com", "cu.16bcs1180@gmailc.com", "vasudev.arora6120@gmail.com"]
    ack = 'Registered!!! confirmation Email sent...'
    if email not in email_list:
        ack = "Email not registered!!!"
    else:
        try:
            # TODO: Input validation
            if date in cachedListOfEmail:
                cachedListOfEmail[date] += [[email, Subject, Description]]
            else:
                cachedListOfEmail[date] = [[email, Subject, Description]]
            # DEBUG: print(cachedListOfEmail)
            # Send a confirmation email
            send_email(email, Subject, Description)
        except:
            ack = "Issue sending email!!!"
    return templates.TemplateResponse("index.html", {"request": request, "sent": ack})
    

