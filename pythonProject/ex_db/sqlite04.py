import sqlite3
with sqlite3.connect('mydb.db') as conn:
    sql = """
        SELECT *
        FROM stocks
    """
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall() # 전체 조회 결과를 가져오겠다
    for row in rows:
        print(row)