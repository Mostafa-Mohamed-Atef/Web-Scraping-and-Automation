import requests
from bs4 import BeautifulSoup
import os

# Replace with your course URL and login credentials
COURSE_URL = "https://www.datacamp.com/course/your-course-name"
LOGIN_URL = "https://www.datacamp.com/login"
EMAIL = "your@email.com"
PASSWORD = "your_password"

# Start a session to persist login
session = requests.Session()

# Login (if required)
login_data = {"email": EMAIL, "password": PASSWORD}
session.post(LOGIN_URL, data=login_data)

# Fetch course page
response = session.get(COURSE_URL)
soup = BeautifulSoup(response.text, "html.parser")

# Find all slide links (adjust the selector as needed)
slide_links = soup.select("a[href*='download-slides']")

# Download slides
for link in slide_links:
    slide_url = link["href"]
    slide_name = os.path.basename(slide_url)
    with open(slide_name, "wb") as f:
        slide_data = session.get(slide_url).content
        f.write(slide_data)
    print(f"Downloaded: {slide_name}")