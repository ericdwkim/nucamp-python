CREATE DATABASE week4;
\c week4

CREATE TABLE moma_artists (
    id SERIAL PRIMARY KEY,
    info JSONB NOT NULL
);

\copy moma_artists (id, info) from '/data/moma/artists.csv' WITH CSV HEADER QUOTE '"'

-- fix SERIAL sequence starting val
SELECT pg_catalog.setval(pg_get_serial_sequence('moma_artists', 'id'), MAX(id)) FROM moma_artists;

CREATE TABLE moma_works (
    id SERIAL PRIMARY KEY,
    title TEXT,
    artist TEXT,
    constituent_id TEXT, -- sometimes is multiple e.g. "1234, 3394"
    artist_bio TEXT,
    nationality TEXT,
    begin_date TEXT,
    end_date TEXT,
    gender TEXT,
    date TEXT,
    medium TEXT,
    dimensions TEXT,
    creditline TEXT,
    accessionnumber TEXT,
    classification TEXT,
    department TEXT,
    date_acquired DATE,
    cataloged TEXT,
    object_id INT,
    url TEXT,
    thumbnail_url TEXT,
    circumference NUMERIC,
    depth NUMERIC,
    diameter NUMERIC,
    height NUMERIC,
    length NUMERIC,
    weight NUMERIC,
    width NUMERIC,
    seat_height NUMERIC,
    duration NUMERIC
);

\copy moma_works (title, artist, constituent_id, artist_bio, nationality, begin_date, end_date, gender, date, medium, dimensions, creditline, accessionnumber, classification, department, date_acquired, cataloged, object_id, url, thumbnail_url, circumference, depth, diameter, height, length, weight, width, seat_height, duration) from '/data/moma/artworks.csv' WITH CSV HEADER QUOTE '"'

-- fix SERIAL sequence starting val
SELECT pg_catalog.setval(pg_get_serial_sequence('moma_works', 'id'), MAX(id)) FROM moma_works;
