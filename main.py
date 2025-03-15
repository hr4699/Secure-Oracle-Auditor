import cx_Oracle

dsn_tns = cx_Oracle.makedsn("localhost", 1521, service_name="XE")  # Change "XE" if needed
connection = cx_Oracle.connect(user="k214699", password="123", dsn=dsn_tns)

print("Connected to Oracle Database Successfully!")

connection.close()
