import inspect

#CONSTANTS

URL = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

UserName = "Admin"

Password = "admin123"



def whoami():
    return inspect.stack()[1][3]