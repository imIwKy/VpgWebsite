from flask import Flask, render_template
import requests as re

app = Flask(__name__)

#Get a response from Minecraft Server Status API
def get_response():
        response = re.get('https://api.mcstatus.io/v2/status/java/play.mcvpg.org')
        return response.json()

#From response get the MOTD and split it in half
def get_motd(response):
        motd = str(response['motd']['clean']).splitlines()
        return motd[1]



def main():
        app.run(debug=True)


#Route for home page
@app.route('/')
@app.route('/home')
def home_page():
        status = get_response()
        motd=get_motd(status)
        #You write the goal in first element current donations in second
        donation_goal = [100, 195]
        return render_template('home.html', status=status, motd=motd, donation_goal=donation_goal)

#Route for vote page
@app.route('/vote')
def vote_page():
        return render_template('vote.html')

#Route for stats page
@app.route('/stats')
def stats_page():
        return render_template('work_in_progress.html')

#Route for archive page
@app.route('/archive')
def archive_page():
        return render_template('archive.html')

#Route for donations page
@app.route('/donate')
def donate_page():
        return render_template('donate.html')
        

if __name__ == '__main__':
        main()