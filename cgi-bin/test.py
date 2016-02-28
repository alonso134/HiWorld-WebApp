import re
import requests
import json
import cgi
import cgitb
from clarifai.client import ClarifaiApi

print("Content-type:text/html\r\n\r\n")
import cgitb
cgitb.enable()

img_url = input()
clarifai_api = ClarifaiApi()
result = clarifai_api.tag_image_urls(img_url)
tags = result['results'][0]['result']['tag']['classes']

user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'
header = {'User-Agent': user_agent}
vocab_url = "https://www.vocabulary.com/dictionary/"
facts_url = "http://www.thefactsite.com/?s="

session = requests.session()

html = session.get(vocab_url + tags[0])
defs = re.findall('''<a title="(.*?)" name="\w\d{3,5}" class="anchor">\w</a>\s*(.*?)</h3>''', html.text)
print("<br><h2>Definitions of {:s}</h2><br>".format(tags[0]))

for i in defs:
    print('<u><i>'+ i[0] + '</u></i>', i[1] + '<br>')

for word in tags:
    html = session.get(facts_url + word, headers=header)
    try:
        html = session.get(re.search('''<h2 class="entry-title"><a href="(.*?)">''', html.text).group(1), headers=header)
    except:
        continue
    title = re.search('''<h1 class="entry-title">(.*?)</h1>''', html.text).group(1)
    facts = []

    if word in title.lower():
        facts = re.findall('''<li>(.*?)\.</li>''', html.text)
        if facts:
            print("<h2>" + title + "</h2>")
            count = 1
            for j in facts:
                print('<b>' + str(count) + '</b>' + "." , j + '<br>')
                count += 1
            break
else:
    print("\n\nNo fun fact for this one.")