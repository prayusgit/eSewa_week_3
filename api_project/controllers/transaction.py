from fastapi import APIRouter
from ..schemas import transaction
from ..dependencies import db, cursor
import datetime as dt

router = APIRouter(prefix='/transaction', tags=['transactions'])

@router.post('/')
def create_transaction(request: transaction.Transaction):
    sql = ("INSERT INTO transaction(timestamp, sender, receiver, remark, amount, type)"
           "VALUES (%s, %s, %s, %s, %s, %s)")
    values = (dt.datetime.now(), request.sender_id, request.receiver_id, request.remark, request.amount, request.type_string)
    cursor.execute(sql, values)
    db.commit()



