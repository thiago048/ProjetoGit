
import sys
import os

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, ROOT_DIR)
import pytest
from pages.common_page import Common_Page
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.pix_page import PixPage

@pytest.fixture
def page(page):
    page.set_viewport_size({"width": 1920, "height": 1080})
    page.goto("https://leogcarvalho.github.io/simulabank/login.html")
    return page

@pytest.fixture
def common_page(page):
    return Common_Page(page)

@pytest.fixture
def login_page(page):
    return LoginPage(page)

@pytest.fixture 
def home_page(page):
    return HomePage(page)

@pytest.fixture 
def pix_page(page):
    return PixPage(page)

