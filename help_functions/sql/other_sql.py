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


def delete_word(user_id, word):
    delete_word_table(user_id, word, 'Dictionary')
    delete_word_table(user_id, word, 'Weights')


# Удаление слова, которое человек знает
def delete_word_table(user_id, word, table):
    db.query(f"""DELETE 
                FROM {table} 
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
                        Weights (user_id, word, y) 
                        VALUES {info}""")


#Достаёт  словарь пользователя
def show_user_dict(user_id):
    d = db.fetchall(f"SELECT word, translate FROM Dictionary WHERE user_id = {user_id}")
    dict_text = ""
    for stack in d:
        e, r = stack
        line = f"{e}: {r}\n"
        dict_text += line
    return dict_text

def show_info():
    res = db.fetchall("""SELECT * FROM Data""")
    for i in res:
        print(i)

    res2 = db.fetchall("""SELECT * FROM Weights""")
    for i in res2:
        print(i)

