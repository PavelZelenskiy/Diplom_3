from selenium.webdriver.common.by import By

class FeedPageLocators:
    h1_header = [By.XPATH, "//h1[contains(text(), 'Лента заказов')]"]
    today_counter = [By.XPATH, "//p[contains(text(), 'Выполнено за все время:')]/../p[2]"]
    all_time_counter = [By.XPATH, "//p[contains(text(), 'Выполнено за сегодня:')]/../p[2]"]
    in_process_orders = [By.XPATH, "//p[contains(text(), 'В работе:')]/../ul[2]/li"]