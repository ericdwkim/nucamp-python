import peewee

# connects to PostgresSQL db via db adapter class `PostgresqlDatabase` which accepts a
# single `Database` argument as a param
db = peewee.PostgresqlDatabase('week3', user='postgres',
                               host='localhost', port=5432)

# Veggie subclass of pewee superclass `Model`
# `peewee.Model` superclass typically represents a table in a db; the db table "object"
# NOTE: object instantiation is handled by peewee, not from the Veggie subclass


class Veggie(peewee.Model):

    # the (3) columns within the Veggie model are specified as class attributes: id, color, name
    # w/ their respective data types using the peewee package

    veggie_id = peewee.AutoField(primary_key=True)  # auto incremented integer
    color = peewee.TextField(null=False)
    name = peewee.TextField(null=False)

    # formats the color and name attributes
    def formatted_name(self):
        return self.color.capitalize() + " " + self.name.capitalize()


# metadata specified for Veggie model, including name of the table that it should map to


    class Meta:
        database = db
        table_name = 'veggies'


db.connect()
db.drop_tables([Veggie])

# list of dicts to "seed the table" with; defines the initial data we want to insert
# each dict contains (2) key-value pairs which represents a single record
# each key represents a single column; ie: name column, color column
# each value reprents a single value for its respective column; ie: value of "carrot" for column "name"

seed_data = [
    {'name': 'carrot', 'color': 'orange'},
    {'name': 'onion', 'color': 'yellow'},
    {'name': 'onion', 'color': 'red'},
    {'name': 'zucchini', 'color': 'green'},
    {'name': 'squash', 'color': 'yellow'},
    {'name': 'pepper', 'color': 'red'},
    {'name': 'pepper', 'color': 'green'},
    {'name': 'pepper', 'color': 'orange'},
    {'name': 'pepper', 'color': 'yellow'},
    {'name': 'onion', 'color': 'white'},
    {'name': 'green bean', 'color': 'green'},
    {'name': 'jicama', 'color': 'tan'},
    {'name': 'tomatillo', 'color': 'green'},
    {'name': 'radicchio', 'color': 'purple'},
    {'name': 'potato', 'color': 'brown'}
]

# uses peewee defined methods to insert the data into the table
insert = Veggie.insert_many(seed_data)
insert.execute()

# query all rows
# select() --> selects all the records from the given table
# then returns the result set as a list of objects instantiated from the Veggie model class
veggies = Veggie.select()
for v in veggies:
    print(v.color, v.name)

print("")  # line break

# query all rows, sort and format
veggies = Veggie.select().order_by(Veggie.name, Veggie.color)

# parallel for loop for veggies list
for i, v in enumerate(veggies):

    # prints numbered indices and elements starting at 1 w/
    # `v` elements being formatted using made method
    print(str(i+1) + ". " + v.formatted_name())
