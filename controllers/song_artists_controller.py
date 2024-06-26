from flask_restful import Resource
from models import db, Artist, Song, SongArtist
from flask import make_response, request


class SongArtists(Resource):

    def post(self):
        song_artist = SongArtist (song_id = request.json['song_id'], artist_id = request.json['artist_id'])

        db.session.add(song_artist)
        db.session.commit()

        return make_response(song_artist.to_dict(), 201)