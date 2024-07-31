from sqlalchemy import select

from fast_zero.models import User


def test_create_user(session) -> None:
    user = User(username='test1', password='test', email='test1@mail.com')

    session.add(user)
    session.commit()

    result = session.scalar(select(User).where(User.username == 'test1'))

    assert result.username == 'test1'
