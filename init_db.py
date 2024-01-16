"""
Place holder script for testing automation with github
So far it only drops and recreates the user table
for a 'reset'
"""

from app import db, User, Variant

User.__table__.drop(db.engine)
User.__table__.create(db.engine)
print("User Table Reset")
# db.drop_all()
# db.create_all()
# test_user = User(username="", password="")
# db.session.add(test_user)
# db.session.commit()
