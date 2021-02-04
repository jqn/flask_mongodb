from . import api
from . import db
from sentry_sdk import capture_exception
from flask import jsonify, request

VERSION = "1.0"


@api.route(f'/api/{VERSION}/matches/daily/')
def daily_matches():
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


@api.route(f'/api/{VERSION}/match/')
def match():
    # GET ALL MATCHES FOR A GIVEN DATE. IF NO DATE GIVEN, RETURN TODAYS MATCHES
    match_id = request.args.get("matchid", False)
    matches = db.matches.find({"match_id": match_id})
    output = []
    for match in matches:
        events_output = []
        events = db.events.find({"match_id": match_id})

        for event in events:
            # Unpack only match id and ignore the rest
            e_id, *_ = event.values()
            # Turn Object Id into a string
            event["_id"] = str(e_id)
            # Add match to output list
            events_output.append(event)

        # Unpack only match id and ignore the rest
        m_id, *_ = match.values()
        # Turn Object Id into a string
        match["_id"] = str(m_id)
        match["events"] = events_output
        # Add match to output list
        output.append(match)

    return jsonify({'result': output}), 200


@api.route(f'/api/{VERSION}/matchesEvents/')
def match_events():
    # GET ALL MATCHES FOR A GIVEN DATE. IF NO DATE GIVEN, RETURN TODAYS MATCHES
    match_date = request.args.get("date", "18.01.2021")
    matches = db.matches.find({"match_date": match_date})
    output = []
    for match in matches:
        events_output = []
        events = db.events.find(
            {"match_id": match['match_id']}).sort("eventId", -1)

        for event in events:
            # Unpack only match id and ignore the rest
            e_id, *_ = event.values()
            # Turn Object Id into a string
            event["_id"] = str(e_id)
            # Add match to output list
            events_output.append(event)

        # Unpack only match id and ignore the rest
        m_id, *_ = match.values()
        # Turn Object Id into a string
        match["_id"] = str(m_id)
        match["events"] = events_output
        # Add match to output list
        output.append(match)

    return jsonify({'result': output}), 200
