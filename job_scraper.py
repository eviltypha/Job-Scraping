import json
import re
from urllib.parse import urlsplit
from extruct.jsonld import JsonLdExtractor
import requests
from bs4 import BeautifulSoup
import sqlite3


HEADERS = ({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'})

jslde = JsonLdExtractor()

con = sqlite3.connect('./JobScraping/db.sqlite3')
cur = con.cursor()


def starter(URL):
    split_URL = urlsplit(URL)
    BASE = split_URL.scheme + "://" + split_URL.netloc

    markup = requests.get(URL, headers=HEADERS).text
    soup = BeautifulSoup(markup, 'html.parser')

    return BASE, soup


def dataCleaner(job):
    markup = requests.get(job, headers=HEADERS).text
    data = jslde.extract(markup)

    str_data = json.dumps(data)
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', str_data)
    data = json.loads(cleantext)

    for i in data:
        if i['@type'] != 'JobPosting':
            del i
        else:
            data = i

    for key in list(data):
        if key.startswith('@'):
            del data[key]

    return data


#########################################################################
# internshala

def internshala(URL):

    BASE, soup = starter(URL)

    jobs = []
    i = 1

    for item in soup.select('div.profile.heading_4_5'):
        jobs.append(BASE + item.a['href'])
        i = i + 1
        if i == 11:
            break

    count = 1

    for job in jobs:

        try:
            data = dataCleaner(job)

            org = ''
            org_url = ''
            for key, value in data['hiringOrganization'].items():
                if key.startswith('@') == False:
                    if key.startswith('name'):
                        org = value
                    if key.startswith('sameAs'):
                        org_url = value

            country = ''
            for key, value in data['applicantLocationRequirements'].items():
                if key.startswith('@') == False and value != None:
                    country = country + value + ' '

            emp_type = ''
            for key, value in data.items():
                if key == 'employmentType':
                    temp = json.loads(value)
                    for i in temp:
                        emp_type = emp_type + i + ' '

            address = ''
            if 'jobLocationType' in data.keys():
                address = data['jobLocationType']
                del data['jobLocationType']
            else:
                for key, value in data['jobLocation'][0]['address'].items():
                    if key.startswith('@') == False and value != None:
                        # print(key, value)
                        address = address + value + ' '

            curr_type = ''
            if 'salaryCurrency' in data.keys():
                curr_type = data['salaryCurrency']

            salary = ''
            if 'baseSalary' in data.keys():
                for key, value in data['baseSalary']['value'].items():
                    if key.startswith('@') == False:
                        salary = salary + str(value) + ' '

            data['applicantLocationRequirements'] = country
            data['hiringOrganization'] = org
            data['organizationURL'] = org_url
            data['employmentType'] = emp_type
            data['jobLocation'] = address
            data['salaryCurrency'] = curr_type
            data['baseSalary'] = salary

            query = "INSERT INTO posts_internshala VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
            columns = (count, data['title'], data['validThrough'], data['applicantLocationRequirements'], data['hiringOrganization'], data['employmentType'], data['directApply'],
                       data['jobLocation'], data['datePosted'], data['responsibilities'], data['salaryCurrency'], data['baseSalary'], data['description'], data['organizationURL'], "Computer Science")

            cur.execute(query, columns)

            print(data['title'])
            count = count + 1

        except:
            print('Skipping...')
            count = count + 1


#########################################################################
# iimjobs

def iimjobs(URL):

    BASE, soup = starter(URL)

    jobs = []
    i = 1

    for item in soup.select('a.hidden-xs.mrmob5'):
        jobs.append(item['href'])
        i = i + 1
        if i == 11:
            break

    i = 1

    for job in jobs:

        try:
            data = dataCleaner(job)

            address = ''
            for key, value in data['jobLocation']['address'].items():
                if key.startswith('@') == False and value != None:
                    address = address + value + ' '

            data['jobLocation'] = address

            query = "INSERT INTO posts_iimjobs VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
            columns = (i, data['description'], data['title'], data['industry'], data['experienceRequirements'], data['skills'],
                       data['datePosted'], data['validThrough'], data['hiringOrganization'], data['employmentType'], data['qualifications'], data['jobLocation'])

            cur.execute(query, columns)

            print(data['title'])
            i = i + 1

        except:
            print('Skipping...')
            i = i + 1


#########################################################################
# talentrack

def talentrack(URL):

    BASE, soup = starter(URL)

    jobs = []
    i = 1

    for item in soup.select('div.job-listing-new'):
        # print(item.a['title'])
        jobs.append(BASE + item.a['href'])
        i = i + 1
        if i == 11:
            break

    i = 1

    for job in jobs:

        try:
            data = dataCleaner(job)

            salary = ''
            for key, value in data['baseSalary'].items():
                if key.startswith('@') == False:
                    salary = salary + value + ' '

            location = ''
            for key, value in data['jobLocation']['address'].items():
                if key.startswith('@') == False and value != None:
                    location = location + value + ' '

            data['baseSalary'] = salary
            data['jobLocation'] = location
            data['hiringOrganization'] = data['hiringOrganization']['name']

            query = "INSERT INTO posts_talentrack VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
            columns = (i, data['datePosted'], data['description'], data['employmentType'], data['industry'], data['validThrough'],
                       data['baseSalary'], data['jobLocation'], data['hiringOrganization'], data['occupationalCategory'], data['title'])

            cur.execute(query, columns)

            print(data['title'])
            i = i + 1

        except:
            print('Skipping...')
            i = i + 1


internshala("https://internshala.com/internships/computer%20science-internship")
iimjobs("https://www.iimjobs.com/k/finance-and-accounts-jobs-362.html")
talentrack("https://www.talentrack.in/all-job-in-india")

con.commit()
con.close()
