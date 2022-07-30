from loader import db
from message_texts import texts as tx

# Выдача правильного перевода
def give_translate_r(en_text):
    find = db.fetchall(f"""SELECT translate 
                            FROM Dictionary 
                            WHERE word = '{en_text}'
                        """)
    return find[0][0]


# Проверка на правильность русского
def check_word_e_r(en_text):
    find = db.fetchall(f"""SELECT translate 
                            FROM Dictionary 
                            WHERE word   = '{en_text}'
                        """)
    if find:
        return 1
    return 0


# Удаление слова, которое человек знает
def delete_word(user_id, word):
    db.query(f"""DELETE 
                FROM Dictionary 
                WHERE user_id = {user_id}
                AND word = '{word}'""")


def fill_dict(user_id):
    for i in tx.full_words:
        word = i
        translate = tx.full_words[i]
        info = (user_id, word, translate)
        db.query(f"""INSERT INTO 
                Dictionary (user_id, word, translate) 
                VALUES {info}""")


def fill_weight(user_id):
    for i in tx.full_words:
        word = i
        weight = 50
        info = (user_id, word, weight)
        db.query(f"""INSERT INTO 
                        Weights (u_id, word, y) 
                        VALUES {info}""")



