from selene import browser, be, have


def test_google_search_with_fixtures(open_browser):
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('html').should(have.text('Об этой странице'))


def test_invalid_result_with_fixtures(open_browser):
    browser.element('[name="q"]').should(be.blank).type('cgyyyyyyyyyyyyyyyyyyyyydnhtfyhndtyh').press_enter()
    browser.element('html').should(have.text('ничего не найдено'))