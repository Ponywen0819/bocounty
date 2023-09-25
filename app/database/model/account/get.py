from app.database.util import get
from app.database.model.account import TABLE, Account
from app.database.model.chatroom_member import ChatroomMember


def get_account_by_id(account_id):
    account_list = get(TABLE, {
        "id": account_id
    })

    if len(account_list) != 1:
        return

    return Account(**account_list[0])


def get_account_by_student_id(student_id):
    account_list = get(TABLE, {
        "student_id": student_id
    })

    if len(account_list) != 1:
        return

    return Account(**account_list[0])


def get_account_by_member_record(member_records: list[ChatroomMember]) -> list[Account]:
    account_list = []
    for member_record in member_records:
        account = get_account_by_id(member_record.account_id)
        account_list.append(account)

    return account_list
