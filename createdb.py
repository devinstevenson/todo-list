from app import app
from models import db, Category, Priority, Todo

db.create_all()

work = Category(name=u'work')
home = Category(name=u'home')

db.session.add(work)
db.session.add(home)
db.session.commit()

high = Priority(name=u'high', value=3)
medium = Priority(name=u'medium', value=2)
low = Priority(name=u'low', value=1)

db.session.add(high)
db.session.add(medium)
db.session.add(low)
db.session.commit()

todo = Todo(category_id=1, priority_id=2, description=u'Read Email')
db.session.add(todo)
db.session.commit()


