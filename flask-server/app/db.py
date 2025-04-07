import psycopg2
from flask import g

def init_db(app):
    def connect_db():
        return psycopg2.connect(
            dbname=app.config['DB_NAME'],
            user=app.config['DB_USER'],
            password = app.config['DB_PASSWORD'],
            host=app.config['DB_HOST'],
            port=app.config['DB_CONFIG']
        )
    
    @app.before_request
    def before_request():
        g.db = connect_db() # make the connection before each request
        g.cursor = g.db.cursor() # store the cursor so we can run SQL

    @app.teardown_request
    def teardown_request(exception):
        cursor = g.pop('cursor', None)
        db = g.pop('db', None)
        if cursor:
            cursor.close() # close cursor after request
        if db:
            db.close() # close connection after request