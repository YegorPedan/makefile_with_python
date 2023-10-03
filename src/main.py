import requests


google_html = requests.get('http://google.com').text
word_google = google_html.find('google')
print(google_html[word_google:word_google + 100])
