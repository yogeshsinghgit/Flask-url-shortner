from flask import Flask, render_template,url_for, redirect, session, request
import pyshorteners

app = Flask(__name__)
app.config['SECRET_KEY'] = "!2345@abc"

@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'POST':
        session['link'] = request.form.get('url')
        url = shortner(session['link'])
        return render_template('shortUrl.html',url=url)
    return render_template('home.html')

def shortner(url):
    # creating object 
    short = pyshorteners.Shortener()
    short_link = short.tinyurl.short(url)
    return short_link


if __name__ == "__main__":
    app.run(debug=True)