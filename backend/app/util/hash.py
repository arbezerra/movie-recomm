import bcrypt


def hash(value):
    return bcrypt.hashpw(
        value.encode('utf-8'), bcrypt.gensalt()
    ).decode('utf-8')


def verify(value, hashed):
    return bcrypt.checkpw(
        value.encode('utf-8'),
        hashed.encode('utf-8')
    )
