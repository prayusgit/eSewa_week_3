from fastapi import APIRouter
from ..schemas import user
from ..dependencies import db, cursor


router = APIRouter(prefix='/user', tags=['users'])


@router.post('/register')
def register(request: user.User):

    cursor.execute('SELECT * FROM User')
    user_datas = cursor.fetchall()

    usernames = [item[-1] for item in user_datas]

    if request.username in usernames:
        return {'detail': "User already exist try another name.\n"}
    else:
        sql = "INSERT INTO User (tier_id, amount, password, username) VALUES (%s, %s, %s, %s)"
        values = (1, 0, request.password, request.username)
        cursor.execute(sql, values)
        db.commit()
        return {'detail': "Successfully registered.\n"}


@router.get('/login')
def login(request: user.User):
    cursor.execute('SELECT u.username, u.id, u.password, u.amount, t.name, t.id, t.limit_amount FROM User u '
                   'JOIN tier t on u.tier_id = t.id')
    user_datas = cursor.fetchall()

    usernames = [item[0] for item in user_datas]
    user_ids = [item[1] for item in user_datas]
    passwords = [item[2] for item in user_datas]
    amounts = [item[3] for item in user_datas]
    tier_names = [item[4] for item in user_datas]
    tier_ids = [item[5] for item in user_datas]
    limit_amounts = [item[6] for item in user_datas]

    index = usernames.index(request.username)

    response = {}
    if (request.username in usernames) and (passwords[index] == request.password):
        response['username'] = request.username
        response['password'] = request.password
        response['user_id'] = user_ids[index]
        response['tier_name'] = tier_names[index]
        response['tier_id'] = tier_ids[index]
        response['amount'] = amounts[index]
        response['limit_amount'] = limit_amounts[index]
        response['authenticated'] = True

        return response
    else:
        return {'detail': "Username or password doesn't match. Do register.\n"}


