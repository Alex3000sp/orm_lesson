from models import User, Address
from db import engine, Base
from sqlalchemy import insert, select, delete, update

Base.metadata.create_all(engine)

def insert_one_user():
    stmt = insert(User).values(
        name = 'Larry',
        fullname = 'Larry Page',
        age = 35,
        gender = 'male'
        
    )
    with engine.connect() as conn:
        conn.execute(stmt)

# insert_one_user()

def insert_many_users(values):
    stmt = insert(User)
    with engine.connect() as conn:
        conn.execute(stmt, values)

values = [
    { 'name' : 'Kate', 'fullname' : 'Kate Kolkova', 'age' : 22, 'gender' : 'female' },
    { 'name' : 'Misha', 'fullname' : 'Mikhail None', 'age' : 35, 'gender' : 'male' },
    { 'name' : 'Ivan', 'fullname' : 'Ivan Susanin', 'age' : 55, 'gender' : 'male' },
    { 'name' : 'Alex', 'fullname' : 'Alex Dubow', 'age' : 11, 'gender' : 'male' },
    { 'name' : 'Olya', 'fullname' : 'Olga Kern', 'age' : 41, 'gender' : 'female' }
]

# insert_many_users(values)

def select_users():
    stmt = (
        select(User.name, User.fullname, Address.email_address)
        # .join(Address, User.id == Address.user_id)
        # .order_by(User.name.asc(), User.fullname)
    )
    with engine.connect() as conn:
        return list(conn.execute(stmt))

def select_three_oldest():
    stmt = (
        select(User.name)
        .where(
            (User.gender == 'male') & 
            ((User.name.like('H%')| User.name.like('L%')))
        )
        .order_by(User.age.desc())
        .limit(3)
    )
    with engine.connect() as conn:
        return list(conn.execute(stmt))

def insert_address():
    with engine.connect() as conn:
        conn.execute(insert(Address)
            .values(email_address = 'john@barsum', user_id = 1))

# insert_address()

def delete_user(id):
    stmt = (
        delete(User)
        .where(User.id == id)
    )
    with engine.connect() as conn:
        conn.execute(stmt)

delete_user(8)

def update_user():
    stmt = (
        update(User)
        .where(User.name == 'Johnny')
        .values(name = 'Johny')
    )
    with engine.connect() as conn: 
        conn.execute(stmt)

# update_user()

for row in select_three_oldest(): 
    print(row)
#     print(f'{row.name} has fullname {row.fullname}')
