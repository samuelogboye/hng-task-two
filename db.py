import pymysql

try:
    conn = pymysql.connect(
        host='***',
        database='***',
        user='***',
        password='***',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )

    cursor = conn.cursor()
    sql_query = """CREATE TABLE IF NOT EXISTS `sql10646166`.`user` (
        `id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
        `name` VARCHAR(45) NULL)"""

    cursor.execute(sql_query)

    # Commit the changes to the database
    conn.commit()

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the database connection, whether an error occurred or not
    if 'conn' in locals():
        conn.close()
