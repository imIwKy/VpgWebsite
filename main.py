from flask import Flask, render_template
import requests as re

app = Flask(__name__)
response = re.get('https://api.mcstatus.io/v2/status/java/play.mcvpg.org')
server_status = response.json()

def main():
        app.run(debug=True)


@app.route('/')
@app.route('/home')
def home_page():
        return render_template('home.html', status=server_status)

@app.route('/vote')
def vote_page():
        return render_template('vote.html')

@app.route('/stats')
def stats_page():
        return render_template('stats.html')

@app.route('/archive')
def archive_page():
        return render_template('archive.html')

@app.route('/donate')
def donate_page():
        return render_template('donate.html')

@app.route('/wiki')
def wiki_page():
        return render_template('wiki.html')
        

if __name__ == '__main__':
        main()