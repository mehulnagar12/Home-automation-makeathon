#stores global config

def init(database, userId):
    global db, id, wittyIR
    db = database
    id = userId
    wittyIR = False #IR call from Witty
