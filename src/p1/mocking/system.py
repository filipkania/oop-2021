from dataclasses import dataclass
from typing import Iterable
from unittest.mock import Mock, MagicMock


@dataclass
class User:
    id: int
    name: str


class Db:
    """
    Klasa dostępu do storeage'a userów... prawdopodobnie bazy na zewnętrznym serwerze.
    """

    def get_version(self):
        return '0.0.1'

    def all_users(self) -> Iterable[User]:
        """
        :return: Iterable of all users in the database.
        """
        raise NotImplemented()

    def add_user(self, u: User) -> bool:
        raise NotImplemented()

    def remove_user(self, id: int) -> bool:
        raise NotImplemented()


class AuthChecker:
    db: Db

    def __init__(self, db: Db):
        self.db = db

    def is_user(self, id: int):
        user_ids = [u.id for u in self.db.all_users()]
        return id in user_ids


if __name__ == '__main__':
    # tworzenie kontekstu
    db = Db()
    auth = AuthChecker(db)

    db.all_users = MagicMock(return_value=[])  # podmieniamy prawdziwą metodę, i piszemy co ma zwrócić

    print(db.all_users())

    # A
    res = auth.is_user(5)
    print(res)
    assert res is False
    db.all_users.assert_called()

    # B
    db.all_users.return_value = [User(1, "Test"), User(2, "Test")]
    db.all_users.reset_mock()

    print(db.all_users())

    res = auth.is_user(2)
    print(res)
    assert res is True
    db.all_users.assert_called()

    # C
    db.all_users.reset_mock()
    print(db.all_users())


    def add_user(u: User) -> bool:
        if auth.is_user(u.id):
            return False

        db.all_users.return_value.append(u)
        return True


    db.add_user = add_user

    for x in [(User(1, "A"), False), (User(5, "A"), True)]:
        res = db.add_user(x[0])
        print(res)
        assert res is x[1]
        db.all_users.assert_called()

        assert auth.is_user(x[0].id) is True

    # E
    db.all_users.reset_mock()


    def remove_user(id: int) -> bool:
        if not auth.is_user(id):
            return False

        for i, x in enumerate(db.all_users()):
            if x.id == id:
                db.all_users.return_value.pop(i)
                return True


    db.remove_user = remove_user

    print(db.all_users())
    db.remove_user(5)
    assert auth.is_user(5) is False
    db.all_users.assert_called()
    print(db.all_users())