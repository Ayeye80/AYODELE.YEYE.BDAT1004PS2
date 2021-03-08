#!/usr/bin/env python
# coding: utf-8

# # Question 1

# In[22]:


a = 0
def b():
    global a
a = c(a)
def c(a):
    return a + 2
print('f(0) = {}'.format(f(0)))


# Answer: a=6 and this is based on using global keyword to modify the variable outside of current scope.The keyword is used to create a global variable to make changes in a local scope.
# First b() defined a as global then modify the value by setting a to the value returned by c(a) and the total expression return 2 which set the global a = 2 from a = 0;
# Second b() also follows the same procedures as first b() but now using a = 2 instead of a = 0 since the value of a has been changed by the first b(), so the total expression set a = 4 from a = 2;
# And lastly, third b() also follows the same but used the value of a = 4 from last expression and altered the value of a from 4 to 6. 
# 

# # Question 2

# In[40]:


def fileLength(file):
    try:
        f = open(file, 'r')
        total_lin = 0
        for c in f:
            total_lin += 1

        print(f"Total Lines: {total_lin}")
        
    except Exception as e:
        print(f"File '{file}' not found. ")


fileLength('my1.txt')


# In[108]:


def fileLength(file):
     'converts first line of file filename to an integer and prints it'
fileLength('midterm.py')
try:
            infile = open(filename)
            strName = infile.readline()
            name = int(strName)
print('fileLength is',('midterm.py'))
        except FileNotFoundErrorr:
print('file not found.')
            
            fileLength('idterm.py')


# # Question 3

# In[110]:


class Marsupial:

    def __init__(self, x_coord=0, y_coord=0):
        self.__list = []
        self.x_coord = x_coord
        self.y_coord = y_coord

    def put_in_pouch(self, item):
        self.__list.append(item)

    def pouch_contents(self):
        return self.__list

m = Marsupial()
m.put_in_pouch('doll')
m.put_in_pouch('firetruck')
m.put_in_pouch('kitten')

m.pouch_contents()

class Marsupial:

    def __init__(self, x_coord=0, y_coord=0):
        self.__list = []
        self.x_coord = x_coord
        self.y_coord = y_coord

    def put_in_pouch(self, item):
        self.__list.append(item)

    def pouch_contents(self):
        return self.__list
        

def pouch_contents(self):
        return self.__list
        

class Kangaroo(Marsupial):

    def __init__(self, x_c=0, y_c=0):
        super().__init__(x_coord=x_c, y_coord=y_c)

    def jump(self, dx, dy):
        self.x_coord += dx
        self.y_coord += dy

    def __str__(self):
        return f"I am a Kangaroo located at coordinates ({self.x_coord},{self.y_coord})"


k = Kangaroo(0,0)
print(k)

k.put_in_pouch('doll')
k.put_in_pouch('firetruck')
k.put_in_pouch('kitten')
k.pouch_contents()

k.jump(1,0)
k.jump(1,0)
k.jump(1,0)
print(k)



# # Question 4

# In[111]:


def isEven(x):
    return x%2 == 0;

def collatz(x):
    if x == 1:
        print(1)
    elif isEven(x):
        print(int(x))
        return collatz(x/2)
    else:
        print(int(x))
        d = 3 * x + 1
        return collatz(d)


collatz(10)


# # Question 5

# In[118]:


def binary(n):
    'prints binary representation of n'
    if n < 10:
        print(n)
    else:
        binary(n//10)
        print(n%10)

integer_binary(10)


# # Question 6

# In[157]:


from html.parser import HTMLParser

class HeadingParser(HTMLParser):

        def handle_starttag(self, tag, attrs):
            print("Encountered a start tag:", tag)
                            
            def handle_starttag(self, tag):
                print("Encountered a start tag :", tag)
              
        def handle_endtag(self, tag):
            print("Encountered an end tag :", tag)
        
parser = MyHTMLParser()
parser.feed('<html><head><title></title></head>')
    


# # Question 7

# In[236]:


def frequency(itemList):
    'returns frequency of items in itemList'

    counters = {}
    for item in itemList:
        if item in counters: 
            counters[item] += 1
        else: 
            counters[item] = 1
    return counters


# In[249]:


def webdir():
    webdir('http://reed.cs.depaul.edu/lperkovic/csc242/test1.html'
, 2, 0)
for link in urls:
        print('{:45} {:10}'.format(url, link))
return urls(' http://reed.cs.depaul.edu/lperkovic/csc242/test4.html')
crawl2('http://reed.cs.depaul.edu/lperkovic/one.html')


# In[ ]:





# # Question 8

# In[161]:


import sqlite3
from sqlite3 import Error


# In[178]:


import sqlite3
con = sqlite3.connect('data.db')
cur = con.cursor()
cur.execute("CREATE TABLE Keywords (Url text, Word text, Freq int)")
cur.execute("INSERT INTO Keywords VALUES ('one.html', 'Beijing', 3)")


# In[172]:


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """


# In[173]:


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """


# In[182]:


def main():
    database = r"C:\sqlite\db\pythonsqlite.db"

    sql_create_data_table = """ CREATE TABLE IF NOT EXISTS projects (
                                        City VARCHAR(50) NOT NULL,
	Country VARCHAR(70) NOT NULL,
	Season VARCHAR(20) NOT NULL,
	Temperature FLOAT NOT NULL,
	Rainfall FLOAT NOT NULL

                                    ); """
    


# In[189]:


import sqlite3
 
conn = sqlite3.connect('web.db')
print('Connected to database successfully.')
cur = conn.cursor()
cur.execute("insert into data_table(City, Country, Season, Temperature, Rainfall) VALUES('Mumbai', 'India', 'Winter')", 24.8, 5.9);
cur.execute("INSERT INTO data_table(City, Country, Season, Temperature, Rainfall) VALUES('Mumbai', 'India', 'Spring')", 28.4, 16.2);
cur.execute("INSERT INTO data_table(City, Country, Season, Temperature, Rainfall) VALUES('Mumbai', 'India', 'Summer')", 27.9, 1549.4);
cur.execute("INSERT INTO data_table(City, Country, Season, Temperature, Rainfall) VALUES('Mumbai', 'India', 'Fall')", 27.6, 346.0);
cur.execute("INSERT INTO data_table(City, Country, Season, Temperature, Rainfall) VALUES('London', 'United Kngdom', 'Winter')", 4.2, 207.7);
cur.execute("INSERT INTO data_table(City, Country, Season, Temperature, Rainfall) VALUES('London', 'United Kngdom', 'Spring')", 8.3, 169.6);
cur.execute("INSERT INTO data_table(City, Country, Season, Temperature, Rainfall) VALUES('London', 'United Kngdom', 'Summer')", 15.7, 157.0);
cur.execute("INSERT INTO data_table(City, Country, Season, Temperature, Rainfall) VALUES('London', 'United Kngdom', 'Fall')", 10.4, 218.5);
cur.execute("INSERT INTO data_table(City, Country, Season, Temperature, Rainfall) VALUES('Cairo', 'Egypt', 'Winter')", 13.6, 16.5);
cur.execute("INSERT INTO data_table(City, Country, Season, Temperature, Rainfall) VALUES('Cairo', 'Egypt', 'Spring')", 20.7, 6.5);
cur.execute("INSERT INTO data_table(City, Country, Season, Temperature, Rainfall) VALUES('Cairo', 'Egypt', 'Summer')", 27.7, 0.1);
cur.execute("INSERT INTO data_table(City, Country, Season, Temperature, Rainfall) VALUES('Cairo', 'Egypt', 'Fall')", 22.2, 4.5);


# In[191]:


con = sqlite3.connect('web.db')
cur = con.cursor()
cur.execute('SELECT * FROM Keywords')
cur.fetchall()


# In[229]:


def select_all_tasks(conn):
    """
    Query all rows in the data_table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM data")

    rows = cur.fetchall()

    for row in rows:
        print(row)


# In[227]:


cur.execute('SELECT Temperature FROM data_table');
cur.execute('SELECT DISTINCT City FROM data_table');
cur.execute('SELECT FROM data_table WHERE Country = India');
cur.execute('SELECT FROM data_table WHERE Season = Fall');
cur.execute('SELECT City, Country, Season FROM data_table WHERE Rainfall > 200 AND Rainfall < 400');
cur.execute('SELECT City, Country FROM data_table WHERE Season = Fall AND Temperature > 20 ORDER BY Temperature');
cur.execute('SELECT SUM(Rainfall) FROM data_table WHERE City = Cairo');
cur.execute('SELECT SUM(Rainfall), Season FROM data_table GROUP BY Season');


# # Question 9

# In[208]:


words = ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']


#(a)
print([x.upper() for x in words])
#(b)
print([x.lower() for x in words])
#(c)
print([len(x) for x in words])
#(d)
print([[x.upper(), x.lower(), len(x)] for x in words])
#(e)
print([x for x in words if len(x) >= 4])


# In[ ]:




