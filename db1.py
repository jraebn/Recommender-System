import psycopg2






def connect_conn():
    conn = psycopg2.connect(database = "newbook", user = "postgres", password = "", host = "127.0.0.1", port = "5432")
    print("Opened database successfully")
    return conn


def connect_db():
    conn = psycopg2.connect(database = "newbook", user = "postgres", password = "", host = "127.0.0.1", port = "5432")
    print("Opened database successfully")
    cur = conn.cursor()
    return cur


#def create_tables_if_not_exist():
	    #cur=connect_db()
	    #print('Connected!')
        #conn.execute("CREATE TABLE IF NOT EXISTS books(booktitle STRING(200), author STRING(200), genre STRING(200)) ")
        #conn.close()
        #print('Closed!)'
