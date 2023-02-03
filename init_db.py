"""
Place holder script for testing automation ith github

"""

from hello import db, User, variant

db.drop_all()
db.create_all()
# test_user = User(username="", password="")
# db.session.add(test_user)
# db.session.commit()
print("db initialized")
