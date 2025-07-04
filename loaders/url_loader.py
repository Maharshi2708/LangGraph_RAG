import requests

def download_pdf(url, save_path="downloaded.pdf"):
    response = requests.get(url)
    with open(save_path, 'wb') as f:
        f.write(response.content)
    return save_path
