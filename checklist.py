import sqlite3

#import sql conditions and make new table if not already there
conn = sqlite3.connect('Review_Time.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Review_Time')
cur.execute('''CREATE TABLE Review_Time (team TEXT, date TEXT, hours INTEGER)''')



fname = input("Enter file name: ")
if (len(fname) < 1): fname = 'dummy.txt'
with open('check.txt', 'w') as g:
    g.write(fname)
    g.write('\n')

def checklist(x):
    fh = open(fname)
    name='\n' + x.upper()+":"
    name=str(name)
    with open('check.txt', 'a') as f:
        f.write(name)
        f.write('\n')
    for line in fh:
        if not x in line:
            continue
        line=line.rstrip()
        line='[]' + line +'\n'
        line=str(line)
        with open('check.txt', 'a') as f:
            f.write(line)


checklist('must')
checklist('will')
checklist('shall')
checklist('should')

rev=input('Would you like to log this review? ')
if rev == "yes" or rev == "Yes" or rev == "y" or rev == "Y":
    team1=input("Enter team or project this review was for")
    date1=input("Enter date in DD-MMM-YYYY")
    hours1=input("Enter integer number of hours estimated for this review")
    cur.execute("INSERT INTO Review_Time (team, date, hours) VALUES (?,?,?)", (team1, date1, hours1))
    conn.commit()
cur.close()
