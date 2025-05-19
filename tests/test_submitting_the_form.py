import allure
from model.pages.registration_page import RegistrationPage

def test_registration_form(browser_options):
    registration_page = RegistrationPage()

    registration_page.open()


    registration_page.fill_first_name('Luna')
    registration_page.fill_last_name('Lovegood')
    registration_page.fill_email('luna_love@test.com')
    registration_page.select_gender('Female')
    registration_page.fill_mobile('7924763817')
    registration_page.fill_date_of_birth('December', '1994', '16')
    registration_page.select_subject('History')
    registration_page.select_hobbies('Music')
    registration_page.select_picture('image.png')
    registration_page.fill_current_address('1234 Elm Street, Springfield, Illinois, 62704, USA')
    registration_page.select_state('NCR')
    registration_page.select_city('Noida')
    registration_page.click_submit()


    registration_page.should_title_submitting_the_form('Thanks for submitting the form')

    registration_page.should_have_registered(
        'Student Name Luna Lovegood',
        'Student Email luna_love@test.com',
        'Gender Female',
        'Mobile 7924763817',
        'Date of Birth 16 December,1994',
        'Subjects History',
        'Hobbies Music',
        'Picture image.png',
        'Address 1234 Elm Street, Springfield, Illinois, 62704, USA',
        'State and City NCR Noida')
















