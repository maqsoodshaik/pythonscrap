import requests
import json

URL = "https://remoteok.io/api"
keys = ["date","company","position","url","tags"]



def get_jobs(wanted):
    resp = requests.get(URL)
    jobs_results = resp.json()

    jobs = []

    for job_res in jobs_results:

        job = {k: v for k,v in job_res.items() if k in keys }
        if job:
            tags = job.get("tags")
            tags = {tag.lower() for tag in tags}
            if tags.intersection(wanted):
                jobs.append(job)
    return jobs
if __name__ == "__main__":
    print(get_jobs())