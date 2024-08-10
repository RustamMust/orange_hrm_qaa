from base.base_test import BaseTest
from generator.generator import generated_person


class TestProfileFeature(BaseTest):

    def test_change_profile_name(self):
        person_info = next(generated_person())
        first_name = person_info.first_name
        self.login_page.open()
        self.login_page.enter_login(self.data.LOGIN)
        self.login_page.enter_password(self.data.PASSWORD)
        self.login_page.click_submit_button()
        self.dashboard_page.is_opened()
        self.dashboard_page.click_my_info_link()
        self.personal_page.is_opened()
        self.personal_page.change_name(first_name)
        self.personal_page.save_changes()
        self.personal_page.is_changes_saved()




