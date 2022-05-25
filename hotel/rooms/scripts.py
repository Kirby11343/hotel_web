import psycopg2

from hotel.settings import DB_PASSWORD, DB_NAME, DB_USER, BASE_DIR

def do_request(select):
    conn = None
    try:
        conn = psycopg2.connect(host=BASE_DIR, database=DB_NAME, user=DB_USER, password=DB_PASSWORD)
        conn.autocommit = True
        cur = conn.cursor()
        try:
            cur.execute(f"""{select}""")
            services = cur.fetchall()
        except ValueError:
            raise
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            return services
        else:
            return 0