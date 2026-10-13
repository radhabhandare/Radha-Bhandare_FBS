import mysql.connector as c;
con = None
try:
  con = c.connect(host ='localhost',
                  user = 'root', 
                  password ='radha',
                  database ='abcd'
                  )
  cur = con.cursor()
  # cur.execute("create database abcd")
  cur.execute('create table student(rollno int, name varchar(20))')
  # cur.execute("show tables")
  # for i in cur:
  #   print(i)

  cur.execute('insert into student(name, rollno) values(%s,%s)',('Roht',45))
  
  cursor.execute("select *from student")
  d = cursor.fetchone()
  print(d)
  q = 'update Emp set ename =%s where eid = %s'
  val = [("manjul",2), ("swaroop, 100")]
  
  cursor.executemany(q,val)
  print(cursor.rowcount,"is Affected")
# qur = 'insert into student(name,rollno)'



except Exception as e:
  print(e)
  
# if con is not None:
#   print('connection is done')
# else:
#   print("something wrong")    cursor.execute("select *from student")

