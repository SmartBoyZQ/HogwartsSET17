from test_selenium.address_page.main_page import MainPage


class TestAddress:
    main=MainPage()
    main.goto_address().add_nember()
