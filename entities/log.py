from datetime import datetime
from entities.user import User
from enums.log_type import LogType
from persistence.db import get_connection

class log:

    def __init__(self, id: int, date: datetime, user: User, description: str, type: LogType):
        self.id = id
        self.date = date
        self.user = user
        self.description = description
        self.type = type

    def save(date: datetime, user: User, description: str, type: LogType):
        try:
            connection = get_connection()
            cursor = connection.cursor()
            sql = "INSERT INTO log (date, user, description, type) VALUES (%s, %s, %s, %s)"

            cursor.execute(sql, (datetime.now(), user.id, description, type.value))
            connection.commit()

            cursor.close()
            connection.close()
            return True
        except Exception as ex:
            print(f"Error al guardar el log:{ex}")
            return False
