import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.find = self.driver.find_element
        self.wait = WebDriverWait(self.driver, 10)

    #waits   

    @allure.step('Ожидание загрузки элемента')
    def wait_for_element_load(self, locator):
        self.wait.until(EC.visibility_of_element_located(locator))

    @allure.step('Ожидание удаления элемента из DOM дерева')
    def wait_for_element_unload(self, locator): 
        self.wait.until(EC.invisibility_of_element_located(locator))

    @allure.step('Ожидание смены url')
    def wait_for_url_contains(self,url):
        self.wait.until(EC.url_contains(url))

    @allure.step('Ожидание обновления элемента')
    def wait_for_element_text_update(self, locator, new_text):
        self.wait.until(EC.text_to_be_present_in_element((locator), new_text))

    @allure.step('Ожидание обновления элемента')
    def wait_for_element_to_be_clickable(self, locator):
        self.wait.until(EC.element_to_be_clickable((locator)))

    #click

    @allure.step('Нажатие на элемент')
    def click_element(self, locator):
        self.wait_for_element_load(locator)
        self.find(*locator).click()

    #element gets

    @allure.step('Получение элемента')
    def get_element(self, locator):
        self.wait_for_element_load(locator) 
        return self.find(*locator)
    
    @allure.step('Получение текста элемента')
    def get_element_text(self, locator):
        self.wait_for_element_load(locator) 
        return self.find(*locator).text
    
    @allure.step('Получение атрибута элемента')
    def get_element_attr(self, locator, attr):
        self.wait_for_element_load(locator)
        return self.find(*locator).get_attribute(attr)
    
    #scrolls
    
    @allure.step('Скролл к элементу')
    def scroll_to_element(self, locator):
        self.wait_for_element_load(locator)
        element = self.find(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Скролл к концу страницы')
    def scroll_to_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    #send keys    

    @allure.step('Заполнение поля')
    def send_keys(self, locator, keys):
        self.wait_for_element_load(locator)
        self.find(*locator).send_keys(keys)

    #tab change
    
    @allure.step('Переключение вкладки браузера')
    def switch_to_next_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    #urls
    
    @allure.step('Получение текущего url')
    def get_current_url(self):
        return self.driver.current_url
    
    