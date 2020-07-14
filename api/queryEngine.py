class QueryEngine:
    def __init__(self, conn):
        self.__cursor = conn.cursor()

    # create and use a database
    def createDB(self, dbName):
        self.__cursor.execute('CREATE DATABASE IF NOT EXISTS {}'.format(dbName))
        self.__cursor.execute('USE {}'.format(dbName))

    # create a table requiring a name and schema
    def createTable(self, tableName, schemaDict):
        # base sql
        sql = 'CREATE TABLE IF NOT EXISTS {}('.format(tableName)

        count = 0 

        # convert the schema dictionary into SQL format
        for item in schemaDict:
            sql += '{} {}'.format(item, schemaDict[item])
            if count != len(schemaDict) - 1:
                sql += ', '
            count += 1

        sql += ')'

        self.__cursor.execute(sql)

    def getObjectById(self, tableName, id):
        self.__cursor.execute('SELECT * FROM {} WHERE id = %s'.format(tableName), (id,))
        return self.__cursor.fetchall()

    def getAllObjects(self, tableName):
        self.__cursor.execute('SELECT * FROM {}'.format(tableName))
        return self.__cursor.fetchall()

    # construct a query with a where clause based on chosen filters
    def getObjectsByFilter(self, tableName, filterParams, filterValues):
        newFilters = []
        for value in filterValues:
            newFilters.append('%{}%'.format(value))
        selectClause = 'SELECT * FROM {} WHERE '.format(tableName)
        whereClause = ''

        # iteratively build the where clause
        for i in range(len(filterParams)):
            whereClause += filterParams[i] + ' LIKE %s '
            if i < len(filterParams) - 1:
                whereClause += 'AND '

        sql = selectClause + whereClause

        self.__cursor.execute(sql, tuple(newFilters))

        return self.__cursor.fetchall()

    # pre-format SQL for insertion
    def __formatSQL(self, tableName, attrList):
        wildcards = '('
        values = '('

        for i in range(len(attrList)):
            wildcards += '%s'
            values += attrList[i]
            if i < len(attrList) - 1:
                wildcards += ', '
                values += ', '

        wildcards += ')'
        values += ')'

        return 'INSERT INTO {} {} VALUES {}'.format(tableName, values, wildcards)

    # insert a single resource
    def insertObject(self, tableName, attrList, objTuple):
        sql = self.__formatSQL(tableName, attrList)
        self.__cursor.execute(sql, objTuple)

    # insert a list of resources
    def insertObjects(self, tableName, attrList, objTupleList):
        sql = self.__formatSQL(tableName, attrList)

        self.__cursor.executemany(sql, objTupleList)

    # update a resource, given its id and parameters to change
    def updateObject(self, tableName, id, attrList, newParams):
        values = ''

        filteredParams = []
        for par in newParams:
            if par == 'true':
                filteredParams.append('1')
            elif par == 'false':
                filteredParams.append('0')
            else:
                filteredParams.append(par)


        for i in range(len(attrList)):
            values += attrList[i] + ' = %s'
            if i < len(attrList) - 1:
                values += ', '

        sql = 'UPDATE {} SET {} WHERE id = %s'.format(tableName, values)

        filteredParams.append(id)
        
        self.__cursor.execute(sql, tuple(filteredParams))

    def deleteObject(self, tableName, id):
        self.__cursor.execute('DELETE FROM {} WHERE id = %s'.format(tableName), (id,))

    def dropTable(self, tableName):
        self.__cursor.execute('DROP TABLE {}'.format(tableName))

    # specific queries
    def getBookingHistory(self, user_id):
        self.__cursor.execute('SELECT * FROM bookings WHERE user_id = %s', (user_id,))

        return self.__cursor.fetchall()