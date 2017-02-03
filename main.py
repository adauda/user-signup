#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2, re

'''
def validate_username(s):
  if not s or ' ' in s:
    return False
  else:
    return True


def validate_password(s):
  if not s or ' ' in s:
    return False
  else:
    return True

def validate_verify(s1,s2):
  if s1 == s2:
    return True
  else:
    return False

def validate_email(s):
  if "@" in s and "." in s:
    return True
  else:
    return False
'''

USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
def valid_username(username):
    return username and USER_RE.match(username)

PASS_RE = re.compile(r"^.{3,20}$")
def valid_password(password):
    return password and PASS_RE.match(password)

def validate_verify(s1,s2):
  if s1 == s2:
    return True
  else:
    return False

EMAIL_RE  = re.compile(r'^[\S]+@[\S]+\.[\S]+$')
def valid_email(email):
    return not email or EMAIL_RE.match(email)


form = """
<form method="post">
    <h1>Signup</h1>
    <br>

    <table>
    <tr>
    <td><label>Username</label><td></td></td>
    <td><input type="text" name="username" value="%(username)s"></td>
    <td><div style="color:red"> %(name_error)s </div></td>
    </tr>

    <tr>
    <td><label>Password</label><td></td></td>
    <td><input type="password" name="password" value="%(password)s"</td>
    <td><div style="color:red"> %(password_error)s</div></td>
    </tr>

    <tr>
    <td><label>Verify Password</label><td></td></td>
    <td><input type="password" name="verify" value="%(verify)s"</td>
    <td><div style="color:red"> %(verify_error)s</div></td>
    </tr>

    <tr>
    <td><label>Email (optional)</label><td></td></td>
    <td><input type="text" name="email" value="%(email)s"></td>
    <td><div style="color:red"> %(email_error)s</div></td>
    </tr>
    </table>

    <br><br>

    <input type="submit">

</form>
"""


'''
body = """
<body>
    <h1>Thanks for signing up!</h1>
    <br>

    <table>
    <tr>
    <td><label>Welcome</label><td></td></td>
    <td><div style="color:red"> %(name_error)s </div></td>
    </tr>
    </table>
</body>
"""

'''

class MainPage(webapp2.RequestHandler):
    def write_form(self, error="", pass_error="", v_error="", e_error="",
                         username="", password="", verify="", email=""):

                         self.response.out.write(form % { "name_error": error,
                                                          "password_error":pass_error,
                                                          "verify_error":v_error,
                                                          "email_error":e_error,
                                                          "username": username,
                                                          "password":password,
                                                          "verify":verify,
                                                          "email":email})


    def get(self):
        self.write_form()

    def post(self):
        '''
        user_name = self.request.get('username')
        user_pass = self.request.get('password')
        verify_passwd = self.request.get('verify')
        e_mail = self.request.get('email')


        username = validate_username(user_name)
        password = validate_password(user_pass)
        verify = validate_verify(verify_passwd,user_pass)
        email = validate_email(e_mail)
        '''
        username = self.request.get('username')
        password = self.request.get('password')
        verify = self.request.get('verify')
        email = self.request.get('email')

        user_name = valid_username(username)
        user_password = valid_password(password)
        user_verify = validate_verify(verify,password)
        user_email = valid_email(email)


        if (user_name and user_password and user_verify and user_email):
            self.redirect("/welcome?username=" + username)
        else:
            user_name_error = ""
            if not user_name:
                user_name_error = "Not valid username"

            user_password_error = ""
            if not user_password:
                user_password_error = "Not a valid password"
            password_match_error = ""

            if not user_verify:
                password_match_error = "Your passwords didn't match."

            user_email_error = ""
            if not user_email:
                user_email_error ="Not a vaild email"

            self.write_form(user_name_error, user_password_error,password_match_error,user_email_error)



            '''
        if (username and password and verify and email):
            self.redirect("/welcome")
        else:
            user_name_error = ""
            if not username:
                user_name_error = "Not valid username"

            user_password_error = ""
            if not password:
                user_password_error = "Not a valid password"

            password_match_error = ""
            if not verify:
                password_match_error ="Not a valid verify password"

            user_email_error = ""
            if not email:
                user_email_error ="Not a vaild email"


            self.write_form(user_name_error, user_password_error,password_match_error,user_email_error)
            '''

class WelcomeHandler(webapp2.RequestHandler):

    def get(self):

        username = self.request.get("username")
        message = "Welcome "
        if valid_username(username):
            self.response.write(message + username)


    '''
    def post(self):
        user_name = self.request.get('username')
        message = "Name here"
        self.write_body(message)

    def get(self):
        content = "Welcome "

        self.response.write(content)

    def post(self):

        user_Name = self.request.get("username")
        content = "Welcome " + "<b>" + user_Name + "</b>"
        self.response.write(content)


    def get(self):
        user_Name = self.request.get("username")
        content = "Welcome " + "<b>" + user_Name + "</b>"
        self.response.write(content)
    '''

app = webapp2.WSGIApplication([ ('/', MainPage), ('/welcome', WelcomeHandler) ], debug=True)
