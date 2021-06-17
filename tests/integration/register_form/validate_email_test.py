from tests.base_test import BaseTest, db
from market.forms import RegisterForm
from wtforms.validators import ValidationError
from market.models import User

class TestValidateEmailMethod(BaseTest):

    def test_validate_email_method(self):
        # test validate email method works as expected
        with self.app:
            with self.app_context:
                
                # create user with email chibi@gmail.com
                self.app.post('/register', data=dict(username='chibi', email_address='chibi@gmail.com', password1='passme123', password2='passme123'),follow_redirects=True)

                # assert exists in db
                user = db.session.query(User).filter_by(username='chibi').first()
                self.assertIsNotNone(user)

                # creating an object because the form expects an object with data of email address
                class Chibi():
                    data = 'chibi@gmail.com'

                # Call the function that should raise the exception with a context. 
                # The context manager will store the caught exception object in its exception attribute
                with self.assertRaises(ValidationError) as context:
                    # call validate email method with object that has email that already exists in db
                    RegisterForm().validate_email_address(Chibi)
                    # assert that validation exception message is that email already exists
                    self.assertEqual(str(context.exception), 'Email Address already exists! Please try a different email address')
                