from Sign_in.SignIn_testcase import *
from time import sleep
from api_test_case.parse_api import *

sleep(3)
authorization("qa_3", "Testing")
validate_user_info("qa_3", "UserName")
validate_user_info("en", "Language")

