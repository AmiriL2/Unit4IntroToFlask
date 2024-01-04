import pymysql
import pymysql.cursors
from pprint import pprint as print

connect = pymysql.connect(
    database="world",
    user="alayne",
    password="228043303",
    host="10.100.33.60",
    cursorclass=pymysql.cursors.DictCursor
)

Cursor = connect.cursor()

Cursor.execute("SELECT `Name`, `HeadOfState` FROM `country`")

results = Cursor.fetchall()

print(results[0]["HeadOfState"])

for x in results:
    print(x['HeadOfState'])