from db.run_sql import run_sql
from models.album import Album
from models.artist import Artist
from repositories.artist_repository import artist_repository

def save(album):
    sql = "INSERT INTO ablums (title genre, artist) VALUES ( %s, %s, %s,) RETURNING id"
    values = [album.title, album.genre,artist.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    album.id = id
    return album

