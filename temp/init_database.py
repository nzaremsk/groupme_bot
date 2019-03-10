import sqlite3

create_single_word_response_query = '''
CREATE TABLE single_word_response (
    keyword VARCHAR(20) PRIMARY KEY,
    response VARCHAR(1000) NOT NULL
);
'''

conn = sqlite3.connect('mysql://ls618xwn7q9v55vl:x376khqf42ex3kyi@tyduzbv3ggpf15sx.cbetxkdyhwsb.us-east-1.rds.amazonaws.com:3306/j5g6ia085a3rtzmv')
cursor = conn.cursor()
c.execute(create_single_word_response_query)

'''
# example:
conn = sqlite3.connect('example.db')
c = conn.cursor()

# Create table
c.execute('CREATE TABLE stocks(date text, trans text, symbol text, qty real, price real)')

# Insert a row of data
c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()
'''
