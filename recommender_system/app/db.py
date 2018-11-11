import psycopg2






def connect_conn():
    conn = psycopg2.connect(database = "BookDB", user = "postgres", password = "carrotcake092814", host = "127.0.0.1", port = "5432")
    print("Opened database successfully")
    return conn


def connect_db():
    conn = psycopg2.connect(database = "BookDB", user = "postgres", password = "carrotcake092814", host = "127.0.0.1", port = "5432")
    print("Opened database successfully")
    cur = conn.cursor()
    return cur



def create_tables_if_not_exist():
	cur=connect_db()
	print('Connected!')
	conn.execute("CREATE TABLE IF NOT EXISTS users(username String(26) PRIMARY KEY, firstname String(60), lastname String(60), password String(255))")
	conn.execute("CREATE TABLE IF NOT EXISTS books(isbn String(13) PRIMARY KEY, booktitle STRING(255), bookauthor String(255), yrpublished String(255), publisher String(255), imageurl1 String(255),imageurl2 String(255),imageurl3 String(255)) ")
	conn.close()
	print('Closed!')
















def get_dataset():

	dataset = {
	 276761: {

	 '033390804X': 0,
	 '3596218098': 8

	 },

	 276762: 

	 {'034544003X': 0,
	 '0380000059': 0,
	 '0380711524': 5,
	 '0451167317': 0,
	 '0451454952': 0,
	 '0843920262': 0,
	 '3404122879': 0,
	 '3404182928': 0,
	 '3404611306': 0,
	 '342662429': 0,
	 '3426690179': 0,
	 '3442424216': 0,
	 '3442425573': 0,
	 '3453092007': 8,
	 '3453157745': 0,
	 '3453176944': 0,
	 '3453185137': 0
	 },




	 276736: {'3257224281': 8},

	 276726: {'0155061224': 5},

	 276737: {'0600570967': 6}, 


	276727: {'0446520802': 0},

	276733: {'2080674722': 0}, 

	276744: {'038550120X': 7},

	276745: {'342310538': 10},

	276746: {'0425115801': 0, '0449006522': 0, '0553561618': 0, '055356451X': 0, '0786013990': 0, '0786014512': 0},

	276747: {'0060517794': 9, '0451192001': 0, '0609801279': 0, '0671537458': 9, '0679776818': 8, '0943066433': 7, '1570231028': 0, '1885408226': 7},

	276748: {'0747558167': 6, '3442437407': 0},

	276754: {'0684867621': 8},

	276760: {'8440682697': 10},

	276755: {'0451166892': 5},

	276729: {'052165615X': 3, '0521795028': 6}

	 }


	return datset
								