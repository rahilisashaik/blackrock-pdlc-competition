from bs4 import BeautifulSoup
import requests

def scrape_stack_overflow_content(url):
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')
    
    title = soup.find('a', class_='question-hyperlink').get_text(strip=True)
    
    question = soup.find('div', class_='postcell').get_text(strip=True)
    
    answers = soup.find_all('div', class_='answercell')
    answers_text = "\n\n".join([answer.get_text(strip=True) for answer in answers])
    
    return {
        "title": title,
        "question": question,
        "answers": answers_text
    }

