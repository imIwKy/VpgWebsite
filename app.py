from flask import Flask, render_template
import requests as re

app = Flask(__name__)

def get_response():
        response = re.get('https://api.mcstatus.io/v2/status/java/play.mcvpg.org')
        return response.json()

def get_motd(response):
        motd = str(response['motd']['clean']).splitlines()
        return motd[1]



def main():
        app.run(debug=True)



@app.route('/')
@app.route('/home')
def home_page():
        status = get_response()
        motd=get_motd(status)
        #You write the goal in first element current donations in second
        donation_goal = [100, 37.5]
        return render_template('home.html', status=status, motd=motd, donation_goal=donation_goal)

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

@app.route('/gallery')
def wiki_page():
        return render_template('gallery.html')
        

if __name__ == '__main__':
        main()