import requests
import json
from EmailSender import send_email

URL = "https://remoteok.io/api"

keys = ['date', 'company', 'position', 'tags', 'location', 'url']
 
wanted_tags = ["python", "internship"] #interest to search in url

def get_jobs():
    resp = requests.get(URL)
    job_results = resp.json()

    jobs = []

    for job_res in job_results:
        job = {k : v for k ,v in job_res.items() if k in keys}

        if job:
            tags = job.get('tags')
            tags = {tag.lower() for tag in tags}
            if tags.intersection(wanted_tags):
                jobs.append(job)
    
    return jobs

if __name__ == '__main__':

    python_jobs = get_jobs()

    if python_jobs:
        message = "Subject: Remote Python jobs!\n\n"
        message += "Found some cool Python jobs"

        for job in python_jobs:
            message += f"{json.dumps(job)}\n\n"

        send_email(message)

