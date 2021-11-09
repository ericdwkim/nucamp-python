import psycopg2

# Connect to your postgres DB
conn = psycopg2.connect(
    """
    dbname=week3 user=postgres host=localhost port=5432
    """
)
conn.set_session(autocommit=True)

# Open a cursor to perform database operations
cur = conn.cursor()

cur.execute(
    """
    DROP TABLE IF EXISTS veggies
    """
)

cur.execute(
    """
    CREATE TABLE veggies(
        id SERIAL PRIMARY KEY,
        name TEXT NOT NULL,
        color TEXT NOT NULL
    )
    """
)

cur.execute(
    """
    INSERT INTO veggies VALUES 
    (1, 'carrot', 'orange'),
    (2, 'onion', 'yellow'),
    (3, 'onion', 'red'),
    (4, 'zucchini', 'green'),
    (5, 'squash', 'yellow'),
    (6, 'pepper', 'red'),
    (7, 'pepper', 'green'),
    (8, 'pepper', 'orange'),
    (9, 'pepper', 'yellow'),
    (10, 'onion', 'white'),
    (11, 'green bean', 'green'),
    (12, 'jicama', 'tan'),
    (13, 'tomatillo', 'green'),
    (14, 'radicchio', 'purple'),
    (15, 'potato', 'brown')
    """
)

# Execute a query

cur.execute(
    """
    SELECT * FROM veggies
    """
)

# Retrieve query results

records = cur.fetchall()
print("INSERTED VEGGIES:", records, '\n')

cur.execute(
    """
    SELECT color, name FROM veggies
    """
)

# test query to see if pk can be added;
# name and color indices can also be reversed
# strictly accordingly to order of SELECT query
# cur.execute(
#     """
#     SELECT id, name, color FROM veggies
#     """
# )

veggies_records = cur.fetchall()
for v in veggies_records:
    print(v[0], v[1])

print('')  # new line

cur.execute(
    """
    SELECT color, name FROM veggies ORDER BY name, color
    """
)

veggie_records = cur.fetchall()

# enuermate(iterable, start=0) --> counter for iterables
# where iterable can be a list, string, tuple, or dict
# typically `for count, value in ...`
for i, v in enumerate(veggies_records):
    print(str(i+1) + ".", v[0].capitalize(), v[1].capitalize())

# where `i` = indexed numbers of the list items; this is why `i+1`
# since list indexes are zero-based, but we want to start counting @ `1.`

# where `v` = values; in this case would be 'color + name'
