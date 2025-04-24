import oracledb

def connect_to_oracle(username, password, dsn):
    try:
        connection = oracledb.connect(user=username, password=password, dsn=dsn)
        return connection, connection.cursor()
    except Exception as e:
        raise e
