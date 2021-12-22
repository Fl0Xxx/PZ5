import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys





class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        # options = webdriver.ChromeOptions()
        # options.add_argument("--start-maximized")
        # self.driver = webdriver.Chrome(chrome_options=options)
        self.driver = webdriver.Chrome(executable_path=r'C:\Users\zloe_pechenko\Desktop\Tests')
        
        
    def test_keystone_1(self):
        """
        Тест-кейс №1 (Добавление в корзину продукта с keystone level равным 1)
        """
        driver = self.driver
        driver.get("http://carry.team/mythic")
        
        element = driver.find_element_by_name("level_select")
        all_options = element.find_elements_by_tag_name("option")
        option = all_options[0]
        option.click()
        assert option.text == "+1 (1 $)"
        assert driver.find_element_by_id("mythic_price").text == "1 $"
        
        element = driver.find_element_by_name("loot_traders")
        all_options = element.find_elements_by_tag_name("option")
        option = all_options[0]
        option.click()
        assert option.text == "No Traders"
        assert driver.find_element_by_id("mythic_price").text == "1 $"
        
        element = driver.find_element_by_id("radio1")
        element.click()
        element_inputs = element.find_elements_by_tag_name("input")
        element_input = element_inputs[0]
        assert element_input.get_attribute('checked') == "true"
        assert driver.find_element_by_id("mythic_price").text == "1 $"
        
        element = driver.find_element_by_id("mythic_plus_button")
        element.click()
        assert driver.find_element_by_id("cart_price").text == "1 $"
        
    
    # def test_keystone_1_traders_2(self):
    #     """
    #     Тест-кейс №2 (Добавление в корзину продукта с keystone level равным 1 и вторыми Traders)

    #     """
    #     driver = self.driver
    #     driver.get("http://carry.team/mythic")
        
    #     element = driver.find_element_by_name("level_select")
    #     all_options = element.find_elements_by_tag_name("option")
    #     option = all_options[0]
    #     option.click()
    #     assert option.text == "+1 (1 $)"
    #     assert driver.find_element_by_id("mythic_price").text == "1 $"
        
    #     element = driver.find_element_by_name("loot_traders")
    #     all_options = element.find_elements_by_tag_name("option")
    #     option = all_options[2]
    #     option.click()
    #     assert option.text == "2 Traders (30 $)"
    #     assert driver.find_element_by_id("mythic_price").text == "31 $"
        
    #     element = driver.find_element_by_id("radio1")
    #     element.click()
    #     element_inputs = element.find_elements_by_tag_name("input")
    #     element_input = element_inputs[0]
    #     assert element_input.get_attribute('checked') == "true"
    #     assert driver.find_element_by_id("mythic_price").text == "31 $"
        
    #     element = driver.find_element_by_id("mythic_plus_button")
    #     element.click()
    #     assert driver.find_element_by_id("cart_price").text == "31 $"
        
    
    # def test_keystone_10_traders_2(self):
    #     """
    #     Тест-кейс №3 (Добавление в корзину продукта с keystone level равным 10 и вторыми Traders)

    #     """
    #     driver = self.driver
    #     driver.get("http://carry.team/mythic")
        
    #     element = driver.find_element_by_name("level_select")
    #     all_options = element.find_elements_by_tag_name("option")
    #     option = all_options[9]
    #     option.click()
    #     assert option.text == "+10 (10 $)"
    #     assert driver.find_element_by_id("mythic_price").text == "10 $"
        
    #     element = driver.find_element_by_name("loot_traders")
    #     all_options = element.find_elements_by_tag_name("option")
    #     option = all_options[2]
    #     option.click()
    #     assert option.text == "2 Traders (30 $)"
    #     assert driver.find_element_by_id("mythic_price").text == "40 $"
        
    #     element = driver.find_element_by_id("radio1")
    #     element.click()
    #     element_inputs = element.find_elements_by_tag_name("input")
    #     element_input = element_inputs[0]
    #     assert element_input.get_attribute('checked') == "true"
    #     assert driver.find_element_by_id("mythic_price").text == "40 $"
        
    #     element = driver.find_element_by_id("mythic_plus_button")
    #     element.click()
    #     assert driver.find_element_by_id("cart_price").text == "40 $"
        
    
    # def test_keystone_1_runs_10(self):
    #     """
    #     Тест-кейс №4 (Добавление в корзину продукта с keystone level равным 1 и десятым раном)

    #     """
    #     driver = self.driver
    #     driver.get("http://carry.team/mythic")
        
    #     element = driver.find_element_by_name("level_select")
    #     all_options = element.find_elements_by_tag_name("option")
    #     option = all_options[0]
    #     option.click()
    #     assert option.text == "+1 (1 $)"
    #     assert driver.find_element_by_id("mythic_price").text == "1 $"
        
    #     element = driver.find_element_by_name("loot_traders")
    #     all_options = element.find_elements_by_tag_name("option")
    #     option = all_options[0]
    #     option.click()
    #     assert option.text == "No Traders"
    #     assert driver.find_element_by_id("mythic_price").text == "1 $"
        
    #     element = driver.find_element_by_id("radio3")
    #     element.click()
    #     element_inputs = element.find_elements_by_tag_name("input")
    #     element_input = element_inputs[0]
    #     assert element_input.get_attribute('checked') == "true"
    #     assert driver.find_element_by_id("mythic_price").text == "9 $"
        
    #     element = driver.find_element_by_id("mythic_plus_button")
    #     element.click()
    #     assert driver.find_element_by_id("cart_price").text == "9 $"
        
        
    # def test_keystone_5_traders_1_check_1_runs_4(self):
    #     """
    #     Тест-кейс №5 (Добавление в корзину продукта с keystone level равным 5,
    #     включенным первым чекбоксом и четвертым раном)

    #     """
    #     driver = self.driver
    #     driver.get("http://carry.team/mythic")
        
    #     element = driver.find_element_by_name("level_select")
    #     all_options = element.find_elements_by_tag_name("option")
    #     option = all_options[4]
    #     option.click()
    #     assert option.text == "+5 (5 $)"
    #     assert driver.find_element_by_id("mythic_price").text == "5 $"
        
    #     element = driver.find_element_by_name("loot_traders")
    #     all_options = element.find_elements_by_tag_name("option")
    #     option = all_options[1]
    #     option.click()
    #     assert option.text == "1 Trader (20 $)"
    #     assert driver.find_element_by_id("mythic_price").text == "25 $"
        
    #     element = driver.find_element_by_id("mythic_within_tamer")
    #     element_input = element.find_element_by_xpath('..')
    #     element_input.click()
    #     assert element.get_attribute('checked') == "true"
    #     assert driver.find_element_by_id("mythic_price").text == "35 $"
        
    #     element = driver.find_element_by_id("radio2")
    #     element.click()
    #     element_inputs = element.find_elements_by_tag_name("input")
    #     element_input = element_inputs[0]
    #     assert element_input.get_attribute('checked') == "true"
    #     assert driver.find_element_by_id("mythic_price").text == "133 $"
        
    #     element = driver.find_element_by_id("mythic_plus_button")
    #     element.click()
    #     assert driver.find_element_by_id("cart_price").text == "133 $"
        
        
    # def test_keystone_4_traders_1_check_2_runs_10(self):
    #     """
    #     Тест-кейс №6 (Добавление в корзину продукта с keystone level равным 4, 
    #     включенным вторым чекбоксом и десятым раном)

    #     """
    #     driver = self.driver
    #     driver.get("http://carry.team/mythic")
        
    #     element = driver.find_element_by_name("level_select")
    #     all_options = element.find_elements_by_tag_name("option")
    #     option = all_options[3]
    #     option.click()
    #     assert option.text == "+4 (4 $)"
    #     assert driver.find_element_by_id("mythic_price").text == "4 $"
        
    #     element = driver.find_element_by_name("loot_traders")
    #     all_options = element.find_elements_by_tag_name("option")
    #     option = all_options[1]
    #     option.click()
    #     assert option.text == "1 Trader (20 $)"
    #     assert driver.find_element_by_id("mythic_price").text == "24 $"
        
    #     element = driver.find_element_by_id("mythic_specific_dungeon")
    #     element_input = element.find_element_by_xpath('..')
    #     element_input.click()
    #     assert element.get_attribute('checked') == "true"
    #     assert driver.find_element_by_id("mythic_price").text == "34 $"
        
        
    #     element = driver.find_element_by_id("radio3")
    #     element.click()
    #     element_inputs = element.find_elements_by_tag_name("input")
    #     element_input = element_inputs[0]
    #     assert element_input.get_attribute('checked') == "true"
    #     assert driver.find_element_by_id("mythic_price").text == "306 $"
        
    #     element = driver.find_element_by_id("mythic_plus_button")
    #     element.click()
    #     assert driver.find_element_by_id("cart_price").text == "306 $"
        
        
    # def test_keystone_3_traders_1_check_1_2_runs_4(self):
    #     """
    #     Тест-кейс №7 (Добавление в корзину продукта с keystone level равным 3,
    #     двумя включенными чекбоксами и четвертым раном)

    #     """
    #     driver = self.driver
    #     driver.get("http://carry.team/mythic")
        
    #     element = driver.find_element_by_name("level_select")
    #     all_options = element.find_elements_by_tag_name("option")
    #     option = all_options[2]
    #     option.click()
    #     assert option.text == "+3 (3 $)"
    #     assert driver.find_element_by_id("mythic_price").text == "3 $"
        
    #     element = driver.find_element_by_name("loot_traders")
    #     all_options = element.find_elements_by_tag_name("option")
    #     option = all_options[2]
    #     option.click()
    #     assert option.text == "2 Traders (30 $)"
    #     assert driver.find_element_by_id("mythic_price").text == "33 $"
        
    #     element = driver.find_element_by_id("mythic_within_tamer")
    #     element_input = element.find_element_by_xpath('..')
    #     element_input.click()
    #     assert element.get_attribute('checked') == "true"
    #     assert driver.find_element_by_id("mythic_price").text == "43 $"
        
    #     element = driver.find_element_by_id("mythic_specific_dungeon")
    #     element_input = element.find_element_by_xpath('..')
    #     element_input.click()
    #     assert element.get_attribute('checked') == "true"
    #     assert driver.find_element_by_id("mythic_price").text == "53 $"
        
    #     element = driver.find_element_by_id("radio2")
    #     element.click()
    #     element_inputs = element.find_elements_by_tag_name("input")
    #     element_input = element_inputs[0]
    #     assert element_input.get_attribute('checked') == "true"
    #     assert driver.find_element_by_id("mythic_price").text == "202 $"
        
    #     element = driver.find_element_by_id("mythic_plus_button")
    #     element.click()
    #     assert driver.find_element_by_id("cart_price").text == "202 $"
    
    
    # def test_keystone_6_traders_2_check_1_2_runs_10_cart_1(self):
    #     """
    #     Тест-кейс №8 (Добавление в корзину продукта с keystone level равным 1, 
    #     включенными чекбоксами с предусловием стоимости корзины 1$):
    #     Перед этим выполним первый тест-кейс

    #     """
    #     driver = self.driver
    #     driver.get("http://carry.team/mythic")
        
    #     element = driver.find_element_by_name("level_select")
    #     all_options = element.find_elements_by_tag_name("option")
    #     option = all_options[0]
    #     option.click()
    #     assert option.text == "+1 (1 $)"
    #     assert driver.find_element_by_id("mythic_price").text == "1 $"
        
    #     element = driver.find_element_by_name("loot_traders")
    #     all_options = element.find_elements_by_tag_name("option")
    #     option = all_options[0]
    #     option.click()
    #     assert option.text == "No Traders"
    #     assert driver.find_element_by_id("mythic_price").text == "1 $"
        
    #     element = driver.find_element_by_id("radio1")
    #     element.click()
    #     element_inputs = element.find_elements_by_tag_name("input")
    #     element_input = element_inputs[0]
    #     assert element_input.get_attribute('checked') == "true"
    #     assert driver.find_element_by_id("mythic_price").text == "1 $"
        
    #     element = driver.find_element_by_id("mythic_plus_button")
    #     element.click()
    #     assert driver.find_element_by_id("cart_price").text == "1 $"
        
        
        
    #     element = driver.find_element_by_name("level_select")
    #     all_options = element.find_elements_by_tag_name("option")
    #     option = all_options[5]
    #     option.click()
    #     assert option.text == "+6 (6 $)"
    #     assert driver.find_element_by_id("mythic_price").text == "6 $"
        
    #     element = driver.find_element_by_name("loot_traders")
    #     all_options = element.find_elements_by_tag_name("option")
    #     option = all_options[2]
    #     option.click()
    #     assert option.text == "2 Traders (30 $)"
    #     assert driver.find_element_by_id("mythic_price").text == "36 $"
        
    #     element = driver.find_element_by_id("mythic_within_tamer")
    #     element_input = element.find_element_by_xpath('..')
    #     element_input.click()
    #     assert element.get_attribute('checked') == "true"
    #     assert driver.find_element_by_id("mythic_price").text == "46 $"
        
    #     element = driver.find_element_by_id("mythic_specific_dungeon")
    #     element_input = element.find_element_by_xpath('..')
    #     element_input.click()
    #     assert element.get_attribute('checked') == "true"
    #     assert driver.find_element_by_id("mythic_price").text == "56 $"
        
    #     element = driver.find_element_by_id("radio3")
    #     element.click()
    #     element_inputs = element.find_elements_by_tag_name("input")
    #     element_input = element_inputs[0]
    #     assert element_input.get_attribute('checked') == "true"
    #     assert driver.find_element_by_id("mythic_price").text == "504 $"
        
    #     element = driver.find_element_by_id("mythic_plus_button")
    #     element.click()
    #     assert driver.find_element_by_id("cart_price").text == "505 $"
    
    
    # def test_keystone_2_check_1_runs_1_cart_40(self):
    #     """
    #     Тест-кейс №9 (Добавление в корзину продукта с keystone level равным 2, 
    #     включенным чекбоксом с предусловием стоимости корзины 9$):
    #     """
    #     driver = self.driver
    #     driver.get("http://carry.team/mythic")
        
    #     element = driver.find_element_by_name("level_select")
    #     all_options = element.find_elements_by_tag_name("option")
    #     option = all_options[9]
    #     option.click()
    #     assert option.text == "+10 (10 $)"
    #     assert driver.find_element_by_id("mythic_price").text == "10 $"
        
    #     element = driver.find_element_by_name("loot_traders")
    #     all_options = element.find_elements_by_tag_name("option")
    #     option = all_options[2]
    #     option.click()
    #     assert option.text == "2 Traders (30 $)"
    #     assert driver.find_element_by_id("mythic_price").text == "40 $"
        
    #     element = driver.find_element_by_id("radio1")
    #     element.click()
    #     element_inputs = element.find_elements_by_tag_name("input")
    #     element_input = element_inputs[0]
    #     assert element_input.get_attribute('checked') == "true"
    #     assert driver.find_element_by_id("mythic_price").text == "40 $"
        
    #     element = driver.find_element_by_id("mythic_plus_button")
    #     element.click()
    #     assert driver.find_element_by_id("cart_price").text == "40 $"
        
        
        
    #     element = driver.find_element_by_name("level_select")
    #     all_options = element.find_elements_by_tag_name("option")
    #     option = all_options[1]
    #     option.click()
    #     assert option.text == "+2 (2 $)"
    #     assert driver.find_element_by_id("mythic_price").text == "2 $"
        
    #     element = driver.find_element_by_name("loot_traders")
    #     all_options = element.find_elements_by_tag_name("option")
    #     option = all_options[0]
    #     option.click()
    #     assert option.text == "No Traders"
    #     assert driver.find_element_by_id("mythic_price").text == "2 $"
        
    #     element = driver.find_element_by_id("mythic_within_tamer")
    #     element_input = element.find_element_by_xpath('..')
    #     element_input.click()
    #     assert element.get_attribute('checked') == "true"
    #     assert driver.find_element_by_id("mythic_price").text == "12 $"        
        
    #     element = driver.find_element_by_id("radio1")
    #     element.click()
    #     element_inputs = element.find_elements_by_tag_name("input")
    #     element_input = element_inputs[0]
    #     assert element_input.get_attribute('checked') == "true"
    #     assert driver.find_element_by_id("mythic_price").text == "12 $"
        
    #     element = driver.find_element_by_id("mythic_plus_button")
    #     element.click()
    #     assert driver.find_element_by_id("cart_price").text == "52 $"
    
    
    # def test_keystone_10_traders_2_check_1_2_runs_10_cart_202(self):
    #     """
    #     Тест-кейс №10 (Добавление в корзину продукта с keystone level равным 10, 
    #     включенными чекбоксами с предусловием стоимости корзины 202$)

    #     """
    #     driver = self.driver
    #     driver.get("http://carry.team/mythic")
        
    #     element = driver.find_element_by_name("level_select")
    #     all_options = element.find_elements_by_tag_name("option")
    #     option = all_options[2]
    #     option.click()
    #     assert option.text == "+3 (3 $)"
    #     assert driver.find_element_by_id("mythic_price").text == "3 $"
        
    #     element = driver.find_element_by_name("loot_traders")
    #     all_options = element.find_elements_by_tag_name("option")
    #     option = all_options[2]
    #     option.click()
    #     assert option.text == "2 Traders (30 $)"
    #     assert driver.find_element_by_id("mythic_price").text == "33 $"
        
    #     element = driver.find_element_by_id("mythic_within_tamer")
    #     element_input = element.find_element_by_xpath('..')
    #     element_input.click()
    #     assert element.get_attribute('checked') == "true"
    #     assert driver.find_element_by_id("mythic_price").text == "43 $"
        
    #     element = driver.find_element_by_id("mythic_specific_dungeon")
    #     element_input = element.find_element_by_xpath('..')
    #     element_input.click()
    #     assert element.get_attribute('checked') == "true"
    #     assert driver.find_element_by_id("mythic_price").text == "53 $"
        
    #     element = driver.find_element_by_id("radio2")
    #     element.click()
    #     element_inputs = element.find_elements_by_tag_name("input")
    #     element_input = element_inputs[0]
    #     assert element_input.get_attribute('checked') == "true"
    #     assert driver.find_element_by_id("mythic_price").text == "202 $"
        
    #     element = driver.find_element_by_id("mythic_plus_button")
    #     element.click()
    #     assert driver.find_element_by_id("cart_price").text == "202 $"
        
        
        
    #     element = driver.find_element_by_name("level_select")
    #     all_options = element.find_elements_by_tag_name("option")
    #     option = all_options[9]
    #     option.click()
    #     assert option.text == "+10 (10 $)"
    #     assert driver.find_element_by_id("mythic_price").text == "10 $"
        
    #     element = driver.find_element_by_name("loot_traders")
    #     all_options = element.find_elements_by_tag_name("option")
    #     option = all_options[2]
    #     option.click()
    #     assert option.text == "2 Traders (30 $)"
    #     assert driver.find_element_by_id("mythic_price").text == "40 $"
        
    #     element = driver.find_element_by_id("mythic_within_tamer")
    #     element_input = element.find_element_by_xpath('..')
    #     element_input.click()
    #     assert element.get_attribute('checked') == "true"
    #     assert driver.find_element_by_id("mythic_price").text == "50 $"
        
    #     element = driver.find_element_by_id("mythic_specific_dungeon")
    #     element_input = element.find_element_by_xpath('..')
    #     element_input.click()
    #     assert element.get_attribute('checked') == "true"
    #     assert driver.find_element_by_id("mythic_price").text == "60 $"
        
    #     element = driver.find_element_by_id("radio3")
    #     element.click()
    #     element_inputs = element.find_elements_by_tag_name("input")
    #     element_input = element_inputs[0]
    #     assert element_input.get_attribute('checked') == "true"
    #     assert driver.find_element_by_id("mythic_price").text == "540 $"
        
    #     element = driver.find_element_by_id("mythic_plus_button")
    #     element.click()
    #     assert driver.find_element_by_id("cart_price").text == "742 $"
    
        
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()