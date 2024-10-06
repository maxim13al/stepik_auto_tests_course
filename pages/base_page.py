from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
import math
from locators.locators import BasePageLocators
from selenium.common.exceptions import NoAlertPresentException

class BasePage:
    def __init__(self, browser, base_url, timeout=10):
        self.browser = browser
        self.base_url = base_url
        self.timeout = timeout


    def open_main_page(self):        
        self.browser.get(self.base_url)

 
    def go_to_login_page(self):
        self.click_element(BasePageLocators.LOGIN_LINK)

    def should_be_login_link(self):
        assert self.wait_for_element_to_be_visible(BasePageLocators.LOGIN_LINK)

    

    def get_locator(self, locator_tuple):
        if locator_tuple[0].lower() == 'xpath':
            return By.XPATH, locator_tuple[1]
        elif locator_tuple[0].lower() in ['css', 'css selector']:
            return By.CSS_SELECTOR, locator_tuple[1]
        elif locator_tuple[0].lower() == 'id':
            return By.ID, locator_tuple[1]
        elif locator_tuple[0].lower() == 'name':
            return By.NAME, locator_tuple[1]
        elif locator_tuple[0].lower() == 'class_name':
            return By.CLASS_NAME, locator_tuple[1]
        elif locator_tuple[0].lower() == 'tag_name':
            return By.TAG_NAME, locator_tuple[1]
        elif locator_tuple[0].lower() == 'link_text':
            return By.LINK_TEXT, locator_tuple[1]
        elif locator_tuple[0].lower() == 'partial_link_text':
            return By.PARTIAL_LINK_TEXT, locator_tuple[1]
        else:
            raise ValueError(f"Неизвестный способ локализации: {locator_tuple[0]}")

    def find_element(self, locator, timeout=None):
        """
        Поиск элемента на странице с явным ожиданием.

        :param locator: Локатор элемента, передается как кортеж (By.ID, 'element_id').
        :param timeout: Время ожидания элемента.
        :return: Найденный элемент.
        """
        timeout = timeout or self.timeout
        try:
            element = WebDriverWait(self.browser, timeout).until(
                EC.presence_of_element_located(self.get_locator(locator))
            )
            return element
        except TimeoutException:
            print(f"Элемент с локатором {locator} не был найден за {timeout} секунд.")
            return None

    def find_elements(self, locator, timeout=None):
        """
        Поиск нескольких элементов на странице с явным ожиданием.

        :param locator: Локатор элементов, передается как кортеж (By.CLASS_NAME, 'class_name').
        :param timeout: Время ожидания элементов.
        :return: Список найденных элементов.
        """
        timeout = timeout or self.timeout
        try:
            elements = WebDriverWait(self.browser, timeout).until(
                EC.presence_of_all_elements_located(self.get_locator(locator))
            )
            return elements
        except TimeoutException:
            print(f"Элементы с локатором {locator} не были найдены за {timeout} секунд.")
            return []

    def click_element(self, locator, timeout=None):
        element = self.find_element(self.get_locator(locator), timeout)
        if element:
            element.click()

    def enter_text(self, locator, text, timeout=None):
        """
        Ввод текста в поле.

        :param locator: Локатор элемента (поле ввода).
        :param text: Текст для ввода.
        :param timeout: Время ожидания элемента.
        """
        element = self.find_element(self.get_locator(locator), timeout)
        if element:
            element.click()
            element.clear()
            element.send_keys(text)

    def get_element_text(self, locator, timeout=None):
        """
        Получение текста из элемента.

        :param locator: Локатор элемента, текст которого нужно получить.
        :param timeout: Время ожидания элемента.
        :return: Текст элемента.
        """
        element = self.find_element(self.get_locator(locator), timeout)
        if element:
            return element.text
        return ""
    
    def wait_for_element_to_be_visible(self, locator, timeout=None):
        """
        Ожидание, что элемент станет видимым.

        :param locator: Локатор элемента.
        :param timeout: Время ожидания кликабельности элемента.
        :return: Элемент, который стал кликабельным.
        """
        timeout = timeout or self.timeout
        try:
            element = WebDriverWait(self.browser, timeout).until(
                EC.visibility_of_element_located(self.get_locator(locator))
            )
            return element
        except TimeoutException:
            print(f"Элемент с локатором {locator} не стал видимым за {timeout} секунд.")
            return None

    def wait_for_element_to_be_clickable(self, locator, timeout=None):
        """
        Ожидание, что элемент станет кликабельным.

        :param locator: Локатор элемента.
        :param timeout: Время ожидания кликабельности элемента.
        :return: Элемент, который стал кликабельным.
        """
        timeout = timeout or self.timeout
        try:
            element = WebDriverWait(self.browser, timeout).until(
                EC.element_to_be_clickable(self.get_locator(locator))
            )
            return element
        except TimeoutException:
            print(f"Элемент с локатором {locator} не стал кликабельным за {timeout} секунд.")
            return None

    def wait_for_element_to_disappear(self, locator, timeout=None):
        """
        Ожидание исчезновения элемента с страницы.

        :param locator: Локатор элемента.
        :param timeout: Время ожидания исчезновения элемента.
        """
        timeout = timeout or self.timeout
        try:
            WebDriverWait(self.browser, timeout).until(
                EC.invisibility_of_element_located(self.get_locator(locator))
            )
        except TimeoutException:
            print(f"Элемент с локатором {locator} не исчез за {timeout} секунд.")

    def is_not_element_present(self, locator, timeout=10):
        timeout = timeout or self.timeout
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located(self.get_locator(locator))
            )
        except TimeoutException:
            return True

        return False
    
    def is_disappeared(self, locator, timeout=10):
        timeout = timeout or self.timeout
        try:
            WebDriverWait(self.browser, timeout,1,  TimeoutException).\
                until_not(EC.presence_of_element_located(self.get_locator(locator))
                          )
        except TimeoutException:
            return False

        return True

    def get_current_url(self):
        """
        Получение текущего URL страницы.

        :return: Текущий URL.
        """
        return self.browser.current_url
    
    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
