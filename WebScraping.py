# from bs4 import BeautifulSoup
import requests

# # with open("rea","r") as Linkedin:
# #     doc = BeautifulSoup(linkedin,"html.parser")
# url ="https://www.linkedin.com/jobs/collections/recommended/?currentJobId=3464439907"
# result = requests.get(url)
# p= BeautifulSoup(result.text, "html.parser")
# print(p.prettify())
# # tag = doc.find("a")

# ---------------------------------------------------
# Login to website using just Python 3 Standard Library
# import urllib.parse
# import urllib.request
# import http.cookiejar
#
# def scraper_login():
#     ####### change variables here, like URL, action URL, user, pass
#     # your base URL here, will be used for headers and such, with and without https://
#     base_url = 'www.example.com'
#     https_base_url = 'https://' + base_url
#
#     # here goes URL that's found inside form action='.....'
#     #   adjust as needed, can be all kinds of weird stuff
#     authentication_url = https_base_url + '/login'
#
#     # username and password for login
#     username = 'yourusername'
#     password = 'SoMePassw0rd!'
#
#     # we will use this string to confirm a login at end
#     check_string = 'Logout'
#
#     ####### rest of the script is logic
#     # but you will need to tweak couple things maybe regarding "token" logic
#     #   (can be _token or token or _token_ or secret ... etc)
#
#     # big thing! you need a referer for most pages! and correct headers are the key
#     headers={"Content-Type":"application/x-www-form-urlencoded",
#     "User-agent":"Mozilla/5.0 Chrome/81.0.4044.92",    # Chrome 80+ as per web search
#     "Host":base_url,
#     "Origin":https_base_url,
#     "Referer":https_base_url}
#
#     # initiate the cookie jar (using : http.cookiejar and urllib.request)
#     cookie_jar = http.cookiejar.CookieJar()
#     opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie_jar))
#     urllib.request.install_opener(opener)
#
#     # first a simple request, just to get login page and parse out the token
#     #       (using : urllib.request)
#     request = urllib.request.Request(https_base_url)
#     response = urllib.request.urlopen(request)
#     contents = response.read()
#
#     # parse the page, we look for token eg. on my page it was something like this:
#     #    <input type="hidden" name="_token" value="random1234567890qwertzstring">
#     #       this can probably be done better with regex and similar
#     #       but I'm newb, so bear with me
#     html = contents.decode("utf-8")
#     # text just before start and just after end of your token string
#     mark_start = '<input type="hidden" name="_token" value="'
#     mark_end = '">'
#     # index of those two points
#     start_index = html.find(mark_start) + len(mark_start)
#     end_index = html.find(mark_end, start_index)
#     # and text between them is our token, store it for second step of actual login
#     token = html[start_index:end_index]
#
#     # here we craft our payload, it's all the form fields, including HIDDEN fields!
#     #   that includes token we scraped earler, as that's usually in hidden fields
#     #   make sure left side is from "name" attributes of the form,
#     #       and right side is what you want to post as "value"
#     #   and for hidden fields make sure you replicate the expected answer,
#     #       eg. "token" or "yes I agree" checkboxes and such
#     payload = {
#         '_token':token,
#     #    'name':'value',    # make sure this is the format of all additional fields !
#         'login':username,
#         'password':password
#     }
#
#     # now we prepare all we need for login
#     #   data - with our payload (user/pass/token) urlencoded and encoded as bytes
#     data = urllib.parse.urlencode(payload)
#     binary_data = data.encode('UTF-8')
#     # and put the URL + encoded data + correct headers into our POST request
#     #   btw, despite what I thought it is automatically treated as POST
#     #   I guess because of byte encoded data field you don't need to say it like this:
#     #       urllib.request.Request(authentication_url, binary_data, headers, method='POST')
#     request = urllib.request.Request(authentication_url, binary_data, headers)
#     response = urllib.request.urlopen(request)
#     contents = response.read()
#
#     # just for kicks, we confirm some element in the page that's secure behind the login
#     #   we use a particular string we know only occurs after login,
#     #   like "logout" or "welcome" or "member", etc. I found "Logout" is pretty safe so far
#     contents = contents.decode("utf-8")
#     index = contents.find(check_string)
#     # if we find it
#     if index != -1:
#         print(f"We found '{check_string}' at index position : {index}")
#     else:
#         print(f"String '{check_string}' was not found! Maybe we did not login ?!")
#
# scraper_login()
#
#
# ----------------------------------------------------------------------

# import mechanize
# from bs4 import BeautifulSoup
# import cookielib ## http.cookiejar in python3
#
#
# cj = cookielib.CookieJar()
# br = mechanize.Browser()
# br.set_cookiejar(cj)
#
# import urllib3
# http = urllib3.PoolManager()
# br = http.request('GET', '("https://www.linkedin.com/jobs/search/?currentJobId=3468309529&distance=25&f_E=4&f_JT=C&f_TPR=r86400&geoId=103644278&keywords=data%20engineer&start=50")')
# print(r.status)
# print( r.headers)
# print(r.data)
# # br.open("https://www.linkedin.com/jobs/search/?currentJobId=3468309529&distance=25&f_E=4&f_JT=C&f_TPR=r86400&geoId=103644278&keywords=data%20engineer&start=50")
#
# br.select_form(nr=0)
# br.form['username'] = 'saitejav987@gmail.com'
# br.form['password'] = 'saiteja98'
# br.submit()
#
# print(br.response().read())


#

import requests
from bs4 import BeautifulSoup

# Start a session
session = requests.Session()

# Make a request to the LinkedIn website
url = 'https://www.linkedin.com/jobs/search/?keywords=data%20engineer&location=United%20States&trk=public_jobs_jobs-search-bar_search-submit&redirect=false&position=1&pageNum=0'
response = session.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the form that contains the login information
    form = soup.find("form")
    if form:
        action = form['action']
        inputs = form.find_all('input')
        data = {}
        for input in inputs:
            name = input.get('saitejav987@gmail.com')
            value = input.get('Saiteja10@')
            if name:
                data[name] = value
        search_response = session.post(action, data=data)

        # Check if the search was successful
        if search_response.status_code == 200:
            # Parse the HTML content of the search results page
            search_soup = BeautifulSoup(search_response.content, 'html.parser')

            # Extract the job descriptions from the page
            job_descriptions = search_soup.find_all("div", {"class": "job-description"})
            for job_description in job_descriptions:
                text = job_description.get_text()
                print(text)
        else:
            print("Search request failed with status code:", search_response.status_code)
    else:
        print("Form not found")
else:
    print("Request failed with status code:", response.status_code)






