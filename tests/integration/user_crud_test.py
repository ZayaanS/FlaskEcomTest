from tests.base_test import BaseTest, db
from market.models import User

class UserCrudTest(BaseTest):
    def test_user_model_crud(self):
        with self.app:
            with self.app_context:
                new_user = User(username='Kate', email_address='kate@gmail.com', password_hash='#&*565&*&&^489846&*^%%$', budget=200000)

                # assert that user does not exist before saving to db
                self.assertIsNone(db.session.query(User).filter_by(email_address='kate@gmail.com').first())

                # assert that user exists after saving to db
                db.session.add(new_user)
                db.session.commit()
                self.assertIsNotNone(db.session.query(User).filter_by(email_address='kate@gmail.com').first())

                # assert that user does not exist after deleting from database
                db.session.delete(new_user)
                db.session.commit()
                self.assertIsNone(db.session.query(User).filter_by(email_address='kate@gmail.com').first())

