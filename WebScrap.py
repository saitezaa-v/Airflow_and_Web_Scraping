# import requests
# from bs4 import BeautifulSoup
#
# # Step 1: Send a request to the LinkedIn login page
# login_url = 'https://www.linkedin.com/uas/login'
# login_response = requests.get(login_url)
#
# # Step 2: Submit the login form with your credentials
# soup = BeautifulSoup(login_response.text, 'html.parser')
# csrf = soup.find('input', {'name': 'loginCsrfParam'})['value']
# data = {
#     'session_key': 'saitejav987@gmail.com',
#     'session_password': 'Saiteja10@',
#     'loginCsrfParam': csrf,
# }
# headers = {
#     'Referer': login_url,
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36',
# }
# session = requests.Session()
# session.post(login_url, data=data, headers=headers)
#
# # Step 3: Send a request to the job search page
# search_url = 'https://www.linkedin.com/jobs/search/'
# search_response = session.get(search_url)
# soup = BeautifulSoup(search_response.text, 'html.parser')
#
# # Step 4: Submit the form to select the job and search for data engineer positions
# form = soup.find('form', {'id': 'job-search-form'})
# form = soup.find("form")
#
# if form:
#     action = form['action']
# else:
#     print("Form not found")
#     action =''
# data = {}
#
# form = soup.find("form")
# if form:
#     inputs = form.find_all('input')
#     for input in inputs:
#         if input.get('name'):
#             data[input['name']] = input.get('value', '')
# else:
#     print("Form not found")
# # for input in form.find_all('input'):
# #     if input.get('name'):
# #         data[input['name']] = input.get('value', '')
# data['keywords'] = 'data engineer'
# search_response = session.post(action, data=data)
#
# # Step 5: Extract the data you need from the search results page
# soup = BeautifulSoup(search_response.text, 'html.parser')
# results = soup.find_all('li', {'class': 'job-result-card'})
# results = soup.find_all('li', {'class': 'job-result-card'})
# for result in results:
#     job_title = result.find('a', {'class': 'job-title-link'}).text
#     job_description = result.find('p', {'class': 'job-description'}).text
#     print(job_title)
#     print(job_description)
#
# import requests
# from bs4 import BeautifulSoup
#
# # Step 1: Send a request to the LinkedIn login page
# login_url = 'https://www.linkedin.com/uas/login'
# login_response = requests.get(login_url)
#
# # Step 2: Submit the login form with your credentials
# soup = BeautifulSoup(login_response.text, 'html.parser')
# csrf = soup.find('input', {'name': 'loginCsrfParam'})['value']
# data = {
#     'session_key': 'saitejav987@gmail.com',
#     'session_password': 'Saiteja10@',
#     'loginCsrfParam': csrf,
# }
# headers = {
#     'Referer': login_url,
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36',
# }
# session = requests.Session()
# session.post(login_url, data=data, headers=headers)
#
# # Step 3: Send a request to the job search page
# search_url = 'https://www.linkedin.com/jobs/search/'
# search_response = session.get(search_url)
# soup = BeautifulSoup(search_response.text, 'html.parser')
#
# # Step 4: Submit the form to select the job and search for data engineer positions
# form = soup.find('form', {'id': 'job-search-form'})
# if form:
#     action = "https://www.linkedin.com" + form['action']
# else:
#     print("Form not found")
#     action = None
#
# data = {}
# if form:
#     inputs = form.find_all('input')
#     for input in inputs:
#         if input.get('name'):
#             data[input['name']] = input.get('value', '')
# else:
#     print("Form not found")
# data['keywords'] = 'data engineer'
#
# if action:
#     search_response = session.post(action, data=data)
#     # Step 5: Extract the data you need from the search results page
#     soup = BeautifulSoup(search_response.text, 'html.parser')
#     results = soup.find_all('li', {'class': 'job-result-card'})
#     for result in results:
#         job_title = result.find('a', {'class': 'job-title-link'}).text
#         job_description = result.find('p', {'class': 'job-description'}).text
#         print(job_title)
#         print(job_description)
# else:
#     print("No action found, cannot proceed with job search.")



import requests
from bs4 import BeautifulSoup

# Step 1: Send a request to the LinkedIn login page
login_url = 'https://www.linkedin.com/uas/login'
login_response = requests.get(login_url)

# Step 2: Submit the login form with your credentials
soup = BeautifulSoup(login_response.text, 'html.parser')
csrf = soup.find('input', {'name': 'loginCsrfParam'})['value']
data = {
    'session_key': 'saitejav987@gmail.com',
    'session_password': 'Saiteja10@',
    'loginCsrfParam': csrf,
}
headers = {
    'Referer': login_url,
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36',
}
session = requests.Session()
session.post(login_url, data=data, headers=headers)

# Step 3: Send a request to the job search page
search_url = 'https://www.linkedin.com/jobs/search/'
search_response = session.get(search_url)
soup = BeautifulSoup(search_response.text, 'html.parser')

# Step 4: Submit the form to select the job and search for data engineer positions
form = soup.find('form', {'id': 'job-search-form'})
if form:
    action = form['action']
    data = {}
    inputs = form.find_all('input')
    for input in inputs:
        if input.get('name'):
            data[input['name']] = input.get('value', '')
    data['keywords'] = 'data engineer'
    search_response = session.post(action, data=data)
else:
    print("Form not found")

# Step 5: Extract the data you need from the search results page
if 'search_response' in locals():
    soup = BeautifulSoup(search_response.text, 'html.parser')
    results = soup.find_all('li', {'class': 'job-result-card'})
    for result in results:
        job_title = result.find('a', {'class': 'job-title-link'}).text
        job_description = result.find('p', {'class': 'job-description'}).text
        print(job_title)
        print(job_description)
else:
    print("No action found, cannot proceed with job search.")

