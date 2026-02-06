from dataclasses import asdict

from sqlalchemy import select

from todolist_fastapi.models import User


def test_create_user(session):
    with mock_db_time(model=User) as time:
        new_user = User(username='alice', password='secret', email='test@test.com')
        session.add(new_user)
        session.commit()

    user = session.scalar(select(User).where(User.username == 'alice'))

    assert asdict(user) == {
        'id': 1,
        'username': 'alice',
        'password': 'secret',
        'email': 'teste@test',
        'created_at': time,
        'update_at': time,
    }
