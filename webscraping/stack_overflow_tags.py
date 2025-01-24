import requests

def get_most_popular_tags(site='stackoverflow', pagesize=100):
    url = f"https://api.stackexchange.com/2.3/tags?order=desc&sort=popular&site={site}&pagesize={pagesize}"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    tags = [item['name'] for item in data['items']]
    return tags

def save_tags_to_file(tags, file_path):
    with open(file_path, 'w') as file:
        for tag in tags:
            file.write(f"{tag}\n")

tags = get_most_popular_tags()
save_tags_to_file(tags, "popular_tags.txt")

