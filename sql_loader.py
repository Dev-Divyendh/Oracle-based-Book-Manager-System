def execute_sql_file(cursor, filepath):
    try:
        with open(filepath, 'r') as file:
            sql_script = file.read()

        sql_commands = sql_script.split(';')
        for command in sql_commands:
            cmd = command.strip()
            if not cmd:
                continue
            try:
                cursor.execute(cmd)
            except Exception as e:
                print(f"Skipping error: {e}")
                continue
        return True
    except Exception as e:
        print(f"SQL Load Failed: {e}")
        return False
