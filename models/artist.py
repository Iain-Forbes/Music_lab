from db.run_sql import run_sql
from models.album import Album
from models.artist import Artist

# CREATE
def create(artist):
    # inserting a user named JACK with id 10
    sql = "INSERT INTO artists (name) VALUES (%s) RETURNING id"
    values = [artist.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    artist.id = id
    return artist

# READ -- all
def select_all():
    artists = []
    sql = "SELECT * FROM artists"
    results = run_sql(sql)
    for row in results:
        new_artist = Artist(row['name'], row['id'])
        artists.append(new_artist)
    return artists

# READ -- one_by_id
def select(id):
    artist = None
    sql = "SELECT * FROM artists WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        artist = Artist(result['name'], result['id'])
    return artist

# UPDATE
def update(artist):
    sql = "UPDATE artists SET (name) = (%s) WHERE id = %s"
    values = [artist.name, artist.id]
    run_sql(sql, values)

# DELETE -- all
def delete_all():
    sql = "DELETE * FROM artists"
    run_sql(sql)

# DELETE -- one_by_id
def delete(id):
    sql = "DELETE * FROM artists WHERE id = %s"
    values = [id]
    run_sql(sql, values)
    