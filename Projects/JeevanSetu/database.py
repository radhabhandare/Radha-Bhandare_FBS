import mysql.connector as c

con = None
cursor = None

def getconnection():
  try:
        con = c.connect(
            host='localhost',
            user='root',
            password='radha',
            database='jeevansetu'
        )
        
        if con.is_connected():
          print('Database is connected Successfully..')
          return con
        
  except c.Error as e:
    print('connection error:',e)
  return None

def create_tables():
  con = None
  cursor = None
  
  try:
    
    con = getconnection()
    
    if con is None:
      return False
    cursor = con.cursor()
    
    
    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS emergency_requests(
                request_id INT PRIMARY KEY AUTO_INCREMENT,
                user_id INT NOT NULL,
                title VARCHAR(100) NOT NULL,
                category VARCHAR(50) NOT NULL,
                quantity INT NOT NULL,
                location VARCHAR(100) NOT NULL,
                priority VARCHAR(20) DEFAULT 'medium',
                status VARCHAR(20) DEFAULT 'pending',
                FOREIGN KEY (user_id)
                    REFERENCES users(user_id)
                )
                   """)
    
    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS resources(
                     
                      resource_id INT PRIMARY KEY AUTO_INCREMENT,
                      name VARCHAR(100) NOT NULL,
                      category VARCHAR(50) NOT NULL,
                      quantity INT DEFAULT 0,
                      location VARCHAR(100) NOT NULL
                      
                      
                        )
                   """)
    
      
    con.commit()
    print('All Tables created...')
    return True
  
  except c.Error as e:
    print('Table error:',e)
  
    if con is None:
      con.rollback()
    return False
  
  finally:
    if cursor is not None:
      cursor.close()
      
    if con is not None and con.is_connected():
      con.close()


def execute_query(query , values = None, fetch = False):
  con = None
  cursor = None
  
  try:
    
    con = getconnection()
    
    if con is None:
      return None
    
    cursor = con.cursor(dictionary= True)
    cursor.execute(query,values or())
    
    if fetch:
      res = cursor.fetchall()
      return res
    
    con.commit()
    
    if cursor.lastrowid():
      return cursor.lastrowid
    
    return cursor.rowcount
  
  except c.Error as e:
    print('query error:',e)
    
    if con is not None:
      con.rollback()
      
    return None
  
  finally:
    if cursor is not None:
      cursor.close()
      
    if con is not None and con.is_connected():
      con.close()
      
def testconnection():
  con = getconnection()
    
  if con is not None:
    print('Database connected successfully..')
    con.close()
    return True
  
  return False

if __name__ == '__main__':
    if testconnection():
        create_tables()
      
      