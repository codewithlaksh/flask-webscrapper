from flask import Flask, render_template, jsonify, request
import requests
import bs4
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/scrap", methods=["POST"])
def scrap_url():
    url = request.form.get("url")
    r = requests.get(url)
    soup = bs4.BeautifulSoup(r.content, 'html.parser')
    return soup.prettify()

if __name__ == "__main__":
    app.run(debug=True)