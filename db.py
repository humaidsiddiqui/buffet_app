import psycopg2
def get_db():
    return psycopg2.connect(
        dbname="Buffetfinder",
        user="humaidsiddiqui",
        password="P@ssword500",
        host="localhost",
        port="5432"
    )
