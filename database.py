def GetConn():
    driver = "{ODBC Driver 17 for SQL Server}"
    server = "rtmonkey.database.windows.net"
    database = "Monkey"
    username = "RTM"
    password = "Monkey12345"
    connectionString = "DRIVER=" + driver + ";SERVER=" + server + ";DATABASE=" + database+ ";UID=" + username + ";PWD=" + password
    return connectionString