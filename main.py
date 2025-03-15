import cx_Oracle

# Replace with your Oracle Database credentials
dsn_tns = cx_Oracle.makedsn("localhost", 1521, service_name="XE")  # Use "orcl" if XE is not used
connection = cx_Oracle.connect(user="SYSTEM", password="yourpassword", dsn=dsn_tns)

print("Connected to Oracle Database Successfully!")

# Close the connection
connection.close()
