from selene.support.shared import browser
from selene import be, have

def test_google_search_positive(open_browser):
    positive_search_text = 'selene'
    positive_search_result = 'yashaka/selene: User-oriented Web UI browser tests in Python'

    browser.element('[name="q"]').should(be.blank).type(positive_search_text).press_enter()
    browser.element('[id="search"]').should(have.text(positive_search_result))

def test_google_search_negative(open_browser):
    negative_search_text = 'asdasodiidajdqwhdjkhkjajsdhaskd'
    negative_search_result = 'Your search - asdasodiidajdqwhdjkhkjajsdhaskd - did not match any documents'

    browser.element('[name="q"]').should(be.blank).type(negative_search_text).press_enter()
    browser.element('[id= "center_col"]').should(have.text(negative_search_result))