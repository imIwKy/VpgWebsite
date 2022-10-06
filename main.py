from flask import Flask, render_template
import requests as re
import time

app = Flask(__name__)

def get_status():
        response = re.get('https://api.mcstatus.io/v2/status/java/play.mcvpg.org')
        return response.json()


def main():
        app.run(debug=True)
        while(True):
                get_status()
                time.sleep(60)



@app.route('/')
@app.route('/home')
def home_page():
        return render_template('home.html', status=get_status())

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