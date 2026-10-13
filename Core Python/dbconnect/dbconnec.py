
import mysql.connector as c

con = None
cursor = None

try:
    con = c.connect(
        host='localhost',
        user='root',
        password='radha',
        database='julypython'
    )

    if con.is_connected():
        print('Database connected successfully')

    cursor = con.cursor()

    # Create table
    cursor.execute('create table if not exists Emp(eid int, ename varchar(20))')
    print('Table created')

    # INSERT
    query = 'insert into Emp(eid, ename) values (%s, %s)'
    values = [(1, 'Sindhu'), (2, 'Sanjana'), (3, 'Radha')]

    cursor.executemany(query, values)
    print(cursor.rowcount, 'records inserted')
    con.commit()

    # SELECT
    cursor.execute('select * from Emp')
    result = cursor.fetchall()

    print('Employee records:')
    for row in result:
        print(row)

    # UPDATE
    query = 'update Emp set ename=%s where eid=%s'
    values = [('Manjul', 2), ('Swaroop', 3)]

    cursor.executemany(query, values)
    print(cursor.rowcount, 'records updated')
    con.commit()

    # SELECT after update
    cursor.execute('select * from Emp')
    for row in cursor.fetchall():
        print(row)

    # DELETE
    query = 'delete from Emp where eid=%s'
    value = (1,)

    cursor.execute(query, value)
    print(cursor.rowcount, 'record deleted')
    con.commit()

    # TRUNCATE (removes all records from the table)
    # Uncomment these lines only when you want
    # to remove ALL employee records.
    # cursor.execute('truncate table Emp')
    # print('All records deleted')
    # con.commit()

except c.Error as e:
    print('Database error:', e)

finally:
    if cursor is not None:
        cursor.close()
        print('Cursor closed')

    if con is not None and con.is_connected():
        con.close()
        print('Connection closed')
