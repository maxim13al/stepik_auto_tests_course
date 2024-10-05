from stepik.pages.main_page import MainPage

class TestMainPage:
    def test_guest_can_go_to_login_page(self, browser, base_url):
        page = MainPage(browser, base_url)  
        page.open_main_page()           
        page.should_be_login_link()

        

     


