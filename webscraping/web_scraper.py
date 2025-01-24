import requests
from bs4 import BeautifulSoup
import markdown
from bs4 import BeautifulSoup
import requests


class WebScraper():
    def fetch_web_page(url):
        response = requests.get(url)
        response.raise_for_status()
        return response.text

    def parse_web_page(html_content):
        soup = BeautifulSoup(html_content, 'html.parser')
        
        setup_dependencies = soup.find('section', {'id': 'setup-dependencies'})
        overview = soup.find('section', {'id': 'overview'})
        example = soup.find('section', {'id': 'example'})
        business_applications = soup.find('section', {'id': 'business-applications'})
        
        return {
            "setup_dependencies": setup_dependencies.get_text(strip=True) if setup_dependencies else "N/A",
            "overview": overview.get_text(strip=True) if overview else "N/A",
            "example": example.get_text(strip=True) if example else "N/A",
            "business_applications": business_applications.get_text(strip=True) if business_applications else "N/A",
        }

    def generate_markdown(parsed_content, title):
        md_content = f"# {title}\n\n"
        md_content += "## Setup & Dependencies\n"
        md_content += parsed_content["setup_dependencies"] + "\n\n"
        md_content += "## Overview\n"
        md_content += parsed_content["overview"] + "\n\n"
        md_content += "## Example\n"
        md_content += parsed_content["example"] + "\n\n"
        md_content += "## Business Applications\n"
        md_content += parsed_content["business_applications"] + "\n"
        
        return md_content

    def save_markdown(md_content, file_path):
        with open(file_path, 'w') as file:
            file.write(md_content)