import requests
from bs4 import BeautifulSoup
import random

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

url = 'https://i.reddit.com/r/shortscarystories/random'

def get_story():
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        story = soup.find('div', {'class': 'usertext-body'}).get_text(strip=True)
        return story
    else:
        return "No story found"

story = get_story()
with open('story.txt', 'w') as file:
    file.write(story)
