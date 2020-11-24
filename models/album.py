from db.run_sql import run_sql
from models.album import Album
from models.artist import Artist
from repositories.artist_repository import artist_repository

def save(album):
    sql = "INSERT INTO albums (title, genre, artist) VALUES (%s, %s, %s) RETURNING id"
    values = [album.title, album.genre, album.artist.id] 
    results = run_sql(sql, values)
    id = results[0]['id']
    album.id = id
    return album

def select_all():
    albums =[]
    sql = "SELECT * FROM albums"
    results = run_sql(sql)
    
    for row in results:
        artist = artist_repository.select(row['artist_id'])
        
        album = Album(row['title'], row['genre'], artist, row['id'])
        albums.append(album)

    return albums

def select(id):
    album = None
    sql = 'SELECT * FROM albums WHERE id = %s'
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        album = Album(result['name'],result['id'])
    return album

# UPDATE
def update(artist):
    sql = "UPDATE artists SET (name) = (%s) WHERE id = %s"
    values = [album.name, album.id]
    run_sql(sql, values)

# DELETE -- all
def delete_all():
    sql = "DELETE * FROM album"
    run_sql(sql)

# DELETE -- one_by_id
def delete(id):
    sql = "DELETE * FROM album WHERE id = %s"
    values = [id]
    run_sql(sql, values)   
