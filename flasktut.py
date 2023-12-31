from flask import Flask, request, jsonify
from datetime import datetime, timedelta
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)


# Endpoint to handle GET requests with query parameters slack_name and track
@app.route('/api', methods=['GET'])
def get_info():
    # Get query parameters
    slack_name = request.args.get('Love and')
    #slack_name = requests.get('https://hngix.slack.com/archives/D05M0H214D9').text
    track = request.args.get('track-Design')
    #track = requests.get('https://hngix.slack.com/archives/C05QJUWCJ6A').text
    #soup = BeautifulSoup(track, "html.parser")
    #trackname = soup.findAll('#track-design')

    # Get the current day of the week
    current_day = datetime.utcnow().strftime('%A')

    # Get the current UTC time with validation of +/-2 minutes
    current_utc_time = datetime.utcnow()
    allowed_time_window = timedelta(minutes=2)
    current_time_str = current_utc_time.strftime('%Y-%m-%dT%H:%M:%SZ')

    # Construct GitHub URLs
    github_file_url = "https://github.com/ajokukk/HNGx/blob/main/flasktut.py"
    github_repo_url = "https://github.com/ajokukk/HNGx"

    # Response JSON
    response_data = {
        "slack_name": slack_name,
        "current_day": current_day,
        "utc_time": current_time_str,
        "track": track,
        "github_file_url": github_file_url,
        "github_repo_url": github_repo_url,
        "status_code": 200
    }

    return jsonify(response_data)



if __name__ == '__main__':
    app.run(debug=True)
