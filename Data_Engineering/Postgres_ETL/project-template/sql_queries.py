# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

songplay_table_create = ("""
CREATE TABLE IF NOT EXISTS songplays(songplay_id serial primary key, start_time BIGINT, user_id int, \
  level varchar, song_id varchar, artist_id varchar, session_id int, location varchar, user_agent varchar)
""")

user_table_create = ("""
CREATE TABLE IF NOT EXISTS users(user_id int, first_name varchar, last_name varchar,\
   gender char(1), level varchar)
""")

song_table_create = ("""
CREATE TABLE IF NOT EXISTS songs(song_id varchar primary key,title varchar, artist_id varchar, year int,\
   duration numeric)
""")

artist_table_create = ("""
CREATE TABLE IF NOT EXISTS artists(artist_id varchar, name varchar, location varchar,\
   longitude float, latitude float)

""")

time_table_create = ("""
CREATE TABLE IF NOT EXISTS time(start_time BIGINT, hour varchar, day varchar, week varchar,\
   month varchar, year varchar, weekday varchar)
""")

# INSERT RECORDS

songplay_table_insert = ("""
INSERT INTO songplays(songplay_id,start_time,user_id,level,song_id, artist_id, session_id, location, user_agent)\
   VALUES(DEFAULT,%s, %s,%s, %s, %s, %s, %s, %s)
""")

user_table_insert = ("""
INSERT INTO users(user_id,first_name, last_name, gender, level)\
   VALUES(%s,%s, %s,%s, %s)
""")

song_table_insert = ("""
INSERT INTO songs(song_id,title, artist_id, year, duration)\
   VALUES(%s,%s, %s,%s,%s)
""")


artist_table_insert = ("""
INSERT INTO artists(artist_id,name,location, longitude ,latitude)\
   VALUES(%s,%s, %s,%s, %s)
""")


time_table_insert = ("""
INSERT INTO time(start_time,hour,day, week ,month, year, weekday)\
   VALUES(%s,%s, %s,%s, %s, %s, %s)
""")

# FIND SONGS

song_select = ("""
SELECT s.song_id, a.artist_id FROM songs s JOIN artists a on s.artist_id = a.artist_id
where s.title = %s and a.name = %s and s.duration = %s
""")
#  where songs.title=%s and artists.name=%s and songs.duration=%s
# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]