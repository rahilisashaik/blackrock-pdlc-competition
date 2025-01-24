import requests

def search_stack_overflow(query, pagesize=10):
    url = f"https://api.stackexchange.com/2.3/search/advanced"
    params = {
        'order': 'desc',
        'sort': 'relevance',
        'q': query,
        'site': 'stackoverflow',
        'pagesize': pagesize
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    data = response.json()
    urls = [item['link'] for item in data['items']]
    return urls