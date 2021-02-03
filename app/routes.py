from app import app
from app import db
import pymongo
from flask import jsonify, request
from sentry_sdk import capture_exception

version = "1.0"


@app.route('/')
@app.route('/index')
def index():
    try:
        # collect teams collection
        teams = db.teams
        output = []
        for team in teams.find({}, sort=[('get_players_timestamp', pymongo.ASCENDING)]).limit(10):
            # convert record id object into string
            # to avoid TypeError: Object of type 'ObjectId' is not JSON serializable
            # or the need of a JSON encoder
            team_id = str(team["_id"])
            team["_id"] = team_id
            output.append(team)
            r_id, *_ = team.values()
            print(r_id)

        return jsonify({'result': output}), 200
    except Exception as e:
        # Log error to sentry
        capture_exception(e)


@app.route(f'/api/{version}/matches/daily/')
def matches():
    # GET ALL MATCHES FOR A GIVEN DATE. IF NO DATE GIVEN, RETURN TODAYS MATCHES
    match_date = request.args.get("date", "18.01.2021")
    matches = db.matches.find({"match_date": match_date})
    output = []
    for match in matches:
        # Unpack only match id and ignore the rest
        m_id, *_ = match.values()
        # Turn Object Id into a string
        match["_id"] = str(m_id)
        # Add match to output list
        output.append(match)

    return jsonify({'result': output}), 200


@app.route('/debug-sentry')
def trigger_error():
    # Test sentry logs
    division_by_zero = 1 / 0
