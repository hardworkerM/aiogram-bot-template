from loader import db
from collections import defaultdict
import datetime, time



def take_weights(user_id):
    """
    Take weights (percents) for random choosing
    return dictionary of words and their weights
    """
    weigts = db.fetchall(f"""SELECT word, y
                            FROM Weights
                            WHERE u_id = {user_id}
                         """)
    words = {}
    for info in weigts:
        word, y = info
        words[word] = y

    return words


def change_weights(user_id, word, y):
    """
    Change value of word weight
    y - new weight
    word - word weight change to
    user_id - id of user in DB
    """
    db.query(f"""UPDATE Weight 
                SET y = {y}
                WHERE u_id = {user_id} 
                AND word = '{word}'
            """)


def fill_data(user_id, word, answer, ans_time, y_changes):
    """
    Insert new line of word statistic
    Table Data has columns:
    u_id int - user id
    word text - word
    tries int - number of translate tries
    correct int - number of correct answers
    combo int -  max correct answers in a row
    ans_time - time in which user send answer
    percents - chance of word to be showing
    """
    info = db.fetchall(f"""SELECT tries, correct, combo, percents
                        FROM Data
                        WHERE u_id = {user_id}
                        AND word = '{word}'
                        ORDER BY word DESC
                        LIMIT 1
                        """)
    print(info)
    if info:
        tries, correct, combo, percents = info[0]
    else:
        tries, correct, combo, percents = 0, 0, 0, 50
    if answer:
        combo += 1
    else:
        combo = 0
    percents += y_changes
    tries += 1
    info_in = (user_id, word, tries, correct, combo, ans_time, percents)
    db.query(f"""INSERT INTO 
                Data (u_id, word, tries, correct, combo, ans_time, percents)
                VALUES {info_in} 
            """)






