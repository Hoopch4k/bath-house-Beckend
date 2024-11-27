import psycopg2

host = '127.0.0.1'
user = 'postgres'
password = 'qwerty'
bd_name = 'Venics'


try:
    # пытаемся подключиться к базе данных
    conn = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=bd_name
    )
    with conn.cursor() as cursor:
        cursor.execute(
            "SELECT version();"
        )
        
        print(f"server version:", cursor.fetchone())
    
except Exception as e:
    # в случае сбоя подключения будет выведено сообщение в STDOUT
    print('Can`t establish connection to database', e)
    

