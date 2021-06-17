from tests.base_test import BaseTest, db
from market.forms import RegisterForm
from wtforms.validators import ValidationError

class TestValidateUsernameMethod(BaseTest):

    def test_validate_username_method(self):
        # test validate username method works as expected
        with self.app:
            with self.app_context:
                
                # create user with username chibi
                self.app.post('/register', data=dict(username='chibi', email_address='chibi@gmail.com', password1='passme123', password2='passme123'),follow_redirects=True)

                # creating an object because the form expects an object with data of username
                class Chibi():
                    data = 'chibi'

                # Call the function that should raise the exception with a context. 
                # The context manager will store the caught exception object in its exception attribute
                with self.assertRaises(ValidationError) as context:
                    # call validate username method with object that has username that already exists in db
                    RegisterForm().validate_username(Chibi)
                    # assert that validation sexception message is that username already exists
                    self.assertEqual(str(context.exception), 'Username already exists! Please try a different username')
                