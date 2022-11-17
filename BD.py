import sqlite3
sql_con = sqlite3.connect('music_db')

# #cur.execute('''CREATE TABLE class
#         (id_class INTEGER PRIMARY KEY,
#         name_class VARCHAR(30) not null);''')
# cur.execute('''CREATE TABLE instrument
#             (id_instrum INTEGER PRIMARY KEY,
#             name_instrum VARCHAR(30) not null,
#             id_class INTEGER,
#             FOREIGN KEY (id_class)
#                 REFERENCES class(id_class));''')
# cur.execute ('''CREATE TABLE musician
#         (id_m integer primary key autoincrement,
#         id_instrum integer,
#         name_m varchar(30) not null,
#         foreign key (id_instrum)
#             references instrument(id_instrum));''')
# cur.execute('''insert into musician(id_instrum,id_m,name_m)
# values (8,null,'Микеланджело Росси' )''')
def InstrumClass():
    cur = sql_con.cursor()
    cur.execute('''select name_instrum, name_class 
    from class as cl inner join instrument as ins where
    cl.id_class == ins.id_class   ''')
    rows=cur.fetchall()
    cur.close()
    return rows
def musInstrum():
    cur = sql_con.cursor()
    cur.execute('''select name_instrum, name_m 
        from musician as mus inner join instrument as ins where
        mus.id_instrum == ins.id_instrum   ''')
    data = cur.fetchall()
    cur.close()

    return data

def execute_insert_commit(sql,data):
    cur=sql_con.cursor()
    cur.execute(sql, data)
    sql_con.commit()

def execute_fetch(sql):
    cur = sql_con.cursor()
    cur.execute(sql)
    data = cur.fetchall()
    cur.close()
    return data
def getAllInstrument():
    sql = '''
            SELECT id_instrum, instrument.name_instrum FROM instrument 
        '''
    return execute_fetch(sql)
def getAllClass():
    sql = '''
                SELECT id_class, class.name_class FROM class
            '''
    return execute_fetch(sql)

def addMusician(instrum_id, musician):
    sel = ''' INSERT INTO musician(id_instrum, name_m) VALUES (?,?)'''
    execute_insert_commit(sel, (instrum_id, musician))


def addInstrum(class_id, instrum_name):
    sel = ''' INSERT INTO instrument(id_class, name_instrum) VALUES (?,?)'''
    execute_insert_commit(sel, (class_id, instrum_name))
def getIndexClass(name_class):
    sql = ' SELECT id_class FROM class where name_class=?'
    print(sql)
    cur = sql_con.cursor()
    cur.execute(sql,(name_class,))
    data = cur.fetchall()
    cur.close()
    print(data)
    return data[0][0]



