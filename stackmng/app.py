from flask import Flask, request
from stackmng.crawler import Crawler

app = Flask(__name__)

@app.route('/find_best_answer', methods=['POST'])
async def find_best_answer():
    crl = Crawler(max_depth=2)

    link = request.json['link']
    links = []
    async for link, html in crl.walk(link):
        links.append(link)
        
    return {
        'links': links
    }
