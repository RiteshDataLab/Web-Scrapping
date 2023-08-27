from flask import Flask, render_template, request
from bs4 import BeautifulSoup
from urllib.request import urlopen

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_name = request.form.get('user_name')
        url = "https://www.instagram.com/" + user_name
        page = urlopen(url).read()
        soup = BeautifulSoup(page, "html.parser")
        description = soup.find("meta", property="og:description")['content']
        
        # Extracting user profile image URL
        profile_image_url = soup.find("meta", property="og:image")['content']

        return render_template("index.html", description=description, profile_image_url=profile_image_url)

    return render_template("index.html", description="", profile_image_url="")

if __name__ == "__main__":
    app.run()
