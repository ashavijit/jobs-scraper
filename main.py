import requests as r
import json
from bs4 import BeautifulSoup as bs4

resp = r.get('https://jobs.apple.com/en-gb/search')
print(resp.status_code)

soup = bs4(resp.content, 'html.parser')

job_titles = []
for tag in soup.find_all('a', class_="table--advanced-search__title"):
    job_titles.append(tag.text)

job_dates = []
for tag in soup.find_all('span', class_="table--advanced-search__date"):
    job_dates.append(tag.text)

job_departments = []
for tag in soup.find_all("span", class_="table--advanced-search__role"):
    job_departments.append(tag.text)

job_links = []
for tag in soup.find_all('a', class_="table--advanced-search__title"):
    job_links.append(tag['href'])

jobs = []
for title, date, department, apply_link in zip(job_titles, job_dates, job_departments, job_links):
    job = {
        'title': title,
        'date_posted': date,
        'department': department,
        'apply_link': 'https://jobs.apple.com' + apply_link,
    }
    jobs.append(job)

job_count = len(jobs)

data = {
    'job_count': job_count,
    'jobs': jobs
}

# Save the data in JSON format
with open('jobs.json', 'w') as jsonfile:
    json.dump(data, jsonfile, indent=4)
