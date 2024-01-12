def get_existing_value(cursor, column, task):
    cursor.execute(f"SELECT {column} FROM tasks WHERE description = ?", (task,))
    return cursor.fetchone()[0]
