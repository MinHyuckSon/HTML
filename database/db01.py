import oracledb
#db연결함수
def getConnection():
    return oracledb.connect\
    (user="ora_user",password="1111",dsn="localhost:1521/xe")
# db연결
conn = getConnection()
cusor = conn.cursor()
#query구문
#query = "select * from member where name like '%홍%'"
#query = "select * from employees where salary>=6000"
query = "select * from member"

cusor.execute(query)

rows = cusor.fetchall()

print(f"아이디\t비밀번호\t이름\t전화번호\t이메일\t성별\t취미\t")
print("-"*65)

for row in rows:
    print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t".format(*row))

print("연결 : ",conn)
