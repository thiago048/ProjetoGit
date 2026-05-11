from playwright.sync_api import Page, expect

class Common_Page:
    def __init__(self, page: Page):
        self.page = page

    def assert_text(self,text):
        expect(self.page.get_by_text(text)).to_be_visible()