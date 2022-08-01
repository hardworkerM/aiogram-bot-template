from loader import db


def add_word(user_id, en, ru):
    i_weights = (user_id, en, 50)
    db.query(f"""INSERT INTO Weights (user_id, word, y)
                VALUES {i_weights}""")
    i_dict = (user_id, en, ru)
    db.query(f"""INSERT INTO Dictionary (user_id, word, translate)
                VALUES {i_dict}""")