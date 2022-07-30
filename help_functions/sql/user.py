from loader import db


# Проверяет есть ли данные о пользователе
def check_user(user_id):
    user = db.fetchall(f"""SELECT u.id FROM Users u
                       WHERE u.id = {user_id}""")
    if user:
        return 1
    return 0


# Вносит данные о новом пользователе
def main_info_fill(info):
    db.query(f'INSERT INTO Users (id, u_name)  VALUES {info}')