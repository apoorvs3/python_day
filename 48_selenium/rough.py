import os

from dotenv import load_dotenv
load_dotenv()
print(os.getenv('fake_var1'))
print(os.getenv('fake_var2'))
