import cx_Oracle
def connect_to_db(username, password, dsn):
    try:
        connection = cx_Oracle.connect(username, password, dsn)
        print("[+] Connected to Oracle Database!")
        return connection
    except cx_Oracle.Error as error:
        print(f"[-] Error: {error}")
        return None

def audit_users(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT username FROM all_users")
    users = []
    for row in cursor:
        users.append(f"User: {row[0]}")
    return users

def check_weak_passwords(connection):
    weak_passwords = ["password", "admin", "oracle", "123456"]
    cursor = connection.cursor()
    cursor.execute("SELECT username FROM all_users")
    weak_users = []
    for row in cursor:
        username = row[0]
        for password in weak_passwords:
            try:
                cx_Oracle.connect(username, password, connection.dsn)
                weak_users.append(f"Weak password detected for user: {username}")
                break
            except cx_Oracle.Error:
                continue
    return weak_users

def test_sql_injection(connection):
    cursor = connection.cursor()
    test_query = "SELECT * FROM dual WHERE 1=1"
    try:
        cursor.execute(test_query)
        return "[+] SQL Injection Vulnerability Found!"
    except cx_Oracle.Error:
        return "[-] No SQL Injection Vulnerability Detected."

def generate_report(filename, findings):
    with open(filename, "w") as file:
        file.write("Oracle Database Audit Report\n")
        file.write("=" * 30 + "\n")
        for finding in findings:
            file.write(finding + "\n")
    print(f"[+] Report generated: {filename}")

if __name__ == "__main__":
    username = "k214699"  
    password = "123"  
    dsn = "localhost/XE"  

    connection = connect_to_db(username, password, dsn)
    if connection:
        users = audit_users(connection)
        weak_passwords = check_weak_passwords(connection)
        sql_injection_result = test_sql_injection(connection)

        findings = users + weak_passwords + [sql_injection_result]

        generate_report("Secure-Oracle-Auditor/oracle_audit_report.txt", findings)

        connection.close()
