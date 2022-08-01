from loader import db


def remember_sad(user_id, text):
    info = (user_id, text)
    db.query(f"""INSERT INTO Sad (user_id, about)
                VALUES {info}""")



def show_sadness(user_id):
    grief = db.fetchall(f"""SELECT about FROM Sad
                            WHERE user_id = {user_id}""")
    text = '<b>ГРУСТЬ</b>\n\n'
    for i in grief:
        memor  = f"{i[0]}\n"
        text += memor
    return text