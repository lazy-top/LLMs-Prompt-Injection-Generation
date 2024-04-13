 
import sqlite3

# 数据库连接及游标对象
def create_connection(database_path=":memory:"):
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()
    return conn, cursor

# 创建表
def create_table(cursor):
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL
        )
    """)

# 插入数据
def insert_user(conn, cursor, name, email):
    cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))
    conn.commit()

# 查询数据
def query_users(conn, cursor):
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    for row in rows:
        print(f"ID: {row[0]}, Name: {row[1]}, Email: {row[2]}")

# 更新数据
def update_user(conn, cursor, user_id, new_name=None, new_email=None):
    if new_name is not None and new_email is not None:
        cursor.execute(
            "UPDATE users SET name = ?, email = ? WHERE id = ?", (new_name, new_email, user_id)
        )
    elif new_name is not None:
        cursor.execute("UPDATE users SET name = ? WHERE id = ?", (new_name, user_id))
    elif new_email is not None:
        cursor.execute("UPDATE users SET email = ? WHERE id = ?", (new_email, user_id))
    else:
        print("No update field provided.")
        return

    conn.commit()

# 删除数据
def delete_user(conn, cursor, user_id):
    cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
    conn.commit()

if __name__ == "__main__":
    database_path = "local_data.db"  # 本地数据库文件路径，可替换为您想要的路径
    conn, cursor = create_connection(database_path)
    create_table(cursor)

    # 示例操作
    insert_user(conn, cursor, "Alice", "alice@example.com")
    insert_user(conn, cursor, "Bob", "bob@example.com")

    print("\n--- Query all users ---")
    query_users(conn, cursor)

    print("\n--- Update Alice's email ---")
    update_user(conn, cursor, 1, new_email="alice_new@e
 