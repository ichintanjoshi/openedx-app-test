"""
    Profile Screen Test Module
"""

from tests.ios.pages.ios_landing import IosLanding
from tests.ios.pages.ios_main_dashboard import IosMainDashboard
from tests.ios.pages.ios_profile import IosProfile
from tests.ios.pages.ios_whats_new import IosWhatsNew
from tests.common import values
from tests.common.globals import Globals


class TestIosProfile:
    """
    Profile screen's Test Case
    """

    def test_start_profile_screen_smoke(self, login, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify Profile is loaded successfully
        """

        setup_logging.info(f'Starting {TestIosProfile.__name__} Test Case')
        global_contents = Globals(setup_logging)
        whats_new_page = IosWhatsNew(set_capabilities, setup_logging)
        main_dashboard = IosMainDashboard(set_capabilities, setup_logging)

        if login and global_contents.whats_new_enable:
            assert whats_new_page.navigate_features().text == 'Done'
            whats_new_page.get_next_btn().click()
            setup_logging.info('Whats New screen is successfully loaded')

        profile_tab = main_dashboard.get_main_dashboard_profile_tab()
        assert profile_tab.text == values.MAIN_DASHBOARD_PROFILE_TAB
        profile_tab.click()
        assert profile_tab.get_attribute('value') == values.IOS_SELECTED_TAB_VALUE

    def test_ui_elements_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify that Profile screen will show following contents:
                Back icon, "Profile" as Title, Edit
                Profile Image, User Name, Video Settings
                Support Info, Contact Support, Terms of Use
                Privacy Policy, Cookie Policy, Personal Info
                View FAQ, App Version, Up to Date
                Logout button
        """

        ios_profile = IosProfile(set_capabilities, setup_logging)
        global_contents = Globals(setup_logging)

        assert global_contents.get_navigation_bar_title(set_capabilities)[0].get_attribute(
            'name') == values.PROFILE_SCREEN_TITLE
        assert ios_profile.get_profile_edit_button().text == values.PROFILE_EDIT_BUTTON_IOS
        assert ios_profile.get_profile_img_profile()
        assert ios_profile.get_profile_user_name_text().text == values.PROFILE_NAME_TEXT
        assert ios_profile.profile_user_username_text().text == values.PROFILE_USERNAME_TEXT
        assert ios_profile.def_profile_settings_text().text == values.PROFILE_SETTINGS_TEXT
        assert ios_profile.get_profile_video_settings_button().text == values.PROFILE_VIDEO_SETTINGS
        assert ios_profile.get_profile_support_info_text().text == values.PROFILE_SUPPORT_INFO
        assert ios_profile.get_profile_tos_text().text == values.PROFILE_TERMS_OF_USE
        assert ios_profile.get_profile_privacy_policy().text == values.PROFILE_PRIVACY_POLICY
        assert ios_profile.get_profile_cookies_policy().text == values.PROFILE_COOKIE_POLICY
        assert ios_profile.get_profile_dont_sell_data().text == values.PROFILE_PERSONAL_INFO
        assert ios_profile.get_profile_contact_support().text == values.PROFILE_CONTACT_SUPPORT
        assert ios_profile.get_profile_view_faq().text == values.PROFILE_FAQ
        assert ios_profile.get_profile_version_info().text == values.IOS_APP_VERSION
        assert ios_profile.get_profile_logout_button().text == values.PROFILE_LOGOUT_BUTTON

    def test_load_profile_elements(self, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify that tapping edit button should load Edit profile screen
            Verify that tapping back button should leave Edit profile screen
            Verify that tapping leave button should leave Edit profile screen
            Verify that tapping Video Settings should load Video Settings screen
            Verify that tapping back button should leave Video Settings screen
            Verify that tapping Terms of Use should load Terms of Use screen
            Verify that tapping back button should leave Terms of Use screen
            Verify that tapping Privacy Policy should load Privacy Policy screen
            Verify that tapping back button should leave Privacy Policy screen
            Verify that tapping Cookie Policy should load Cookie Policy screen
            Verify that tapping back button should leave Cookie Policy screen
            Verify that tapping Personal Info should load Personal Info screen
        """

        ios_profile = IosProfile(set_capabilities, setup_logging)
        global_contents = Globals(setup_logging)

        edit_profile = ios_profile.get_profile_edit_button()
        assert edit_profile.text == values.PROFILE_EDIT_BUTTON_IOS
        edit_profile.click()
        assert global_contents.get_navigation_bar_title(set_capabilities)[0].get_attribute(
            'name') == values.EDIT_PROFILE_TITLE_IOS
        back_button = ios_profile.get_back_button()
        assert back_button.text == values.LANDING_BACK_BUTTON
        back_button.click()

        video_settings = ios_profile.get_profile_video_settings_button()
        assert video_settings.text == values.PROFILE_VIDEO_SETTINGS
        video_settings.click()
        assert global_contents.get_navigation_bar_title(set_capabilities)[0].get_attribute(
            'name') == values.PROFILE_VIDEO_SETTINGS
        back_button = ios_profile.get_videos_back_button()
        assert back_button.text == values.MAIN_DASHBOARD_PROFILE_TAB
        back_button.click()

        terms_of_use = ios_profile.get_profile_tos_text()
        terms_of_use.click()
        assert global_contents.get_screen_heading_title(set_capabilities).text == values.PROFILE_TERMS_OF_USE
        ios_profile.get_header_back_button().click()

        ios_profile.get_profile_privacy_policy().click()
        assert global_contents.get_screen_heading_title(set_capabilities).text == values.PROFILE_PRIVACY_POLICY
        ios_profile.get_header_back_button().click()

        ios_profile.get_profile_cookies_policy().click()
        assert global_contents.get_screen_heading_title(set_capabilities).text == values.PROFILE_COOKIE_POLICY
        ios_profile.get_header_back_button().click()

        ios_profile.get_profile_dont_sell_data().click()
        assert global_contents.get_screen_heading_title(set_capabilities).text == values.PROFILE_PERSONAL_INFO
        ios_profile.get_header_back_button().click()

    def test_sign_out_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify that clicking logout button should load logout dialog
            Verify that tapping close button should leave logout dialog
            Verify that tapping logout button should logout from main dashboard screen
        """

        ios_profile = IosProfile(set_capabilities, setup_logging)
        ios_landing = IosLanding(set_capabilities, setup_logging)

        assert ios_profile.get_profile_logout_button().text == values.PROFILE_LOGOUT_BUTTON
        ios_profile.get_profile_logout_button().click()
        assert ios_profile.get_logout_close_button().text == 'Close'
        assert ios_profile.get_logout_dialog_title().text == values.LOGOUT_DIALOG_TITLE
        assert ios_profile.get_logout_button().text == values.PROFILE_LOGOUT_BUTTON
        ios_profile.get_logout_button().click()
        assert ios_landing.get_welcome_message().text == values.LANDING_MESSAGE_IOS
