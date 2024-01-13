def get_existing_value(cursor, column, task):
    query = f"SELECT {column} FROM tasks WHERE description = ?"
    cursor.execute(query, (task,))
    result = cursor.fetchone()
    return result[0] if result is not None else None
