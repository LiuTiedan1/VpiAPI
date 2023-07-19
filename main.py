from flask import Flask, request, jsonify  
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)  

@app.route('/', methods=['GET'])  

@app.route('/api/data', methods=['GET'])  
def get_data():  
    data = request.args.get('data')
    movie_name = request.args.get("data")
    url = "https://v.qq.com/x/search/?q=" + data
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    result = soup.find("div", class_="result_item result_item_v")
    if result:
        play_url = result.find("a")["href"]
        return jsonify({'play_url': play_url})
    else:
        return "未找到该电影的播放网址。"

if __name__ == '__main__':  
    app.run(debug=True)