import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

s=Service('E:\Test\chromedriver.exe')
driver = webdriver.Chrome(service=s)
# Открытие сайта и авторизация
driver.get("https://qa.neapro.site/login")
#driver.set_window_size(1600, 1200)
driver.maximize_window()
driver.find_element(By.CSS_SELECTOR, ".fieldset:nth-child(1) input").click()
driver.find_element(By.CSS_SELECTOR, ".fieldset:nth-child(1) input").send_keys("duffer@mail.ru")
driver.find_element(By.CSS_SELECTOR, ".fieldset:nth-child(2) input").send_keys("12345678")
driver.find_element(By.CSS_SELECTOR, ".btn").click()
time.sleep(2)

# Открытие формы паспорта
driver.find_element(By.CSS_SELECTOR, ".form:nth-child(2) .document-tile:nth-child(1) > .document-name").click()

# Заполнение формы Паспорт
#Фамилия
driver.find_element(By.ID, "surname").clear()
driver.find_element(By.ID, "surname").send_keys("Самый")
#Имя
driver.find_element(By.ID, "name").clear()
driver.find_element(By.ID, "name").send_keys("Добрый")
#Отчество
driver.find_element(By.ID, "patronymic").clear()
driver.find_element(By.ID, "patronymic").send_keys("Злодей")
#Дата рождения
driver.find_element(By.NAME, "date").click()
driver.find_element(By.NAME, "date").clear()
driver.find_element(By.NAME, "date").send_keys("01.01.2001")
#Серия
driver.find_element(By.ID, "passportSeries").click()
driver.find_element(By.ID, "passportSeries").clear()
driver.find_element(By.ID, "passportSeries").send_keys("6666")
#Номер
driver.find_element(By.ID, "passportNumber").clear()
driver.find_element(By.ID, "passportNumber").send_keys("666666")
#Дата выдачи
#driver.find_element(By.XPATH, "dateOfIssue").click()
#driver.find_element(By.XPATH, "dateOfIssue").clear()
driver.find_element(By.CSS_SELECTOR, ".mx-input").send_keys(Keys.CONTROL+ "b")
driver.find_element(By.CSS_SELECTOR, ".mx-input").send_keys(Keys.DELETE)
driver.find_element(By.XPATH, '//*[@id="dateOfIssue"]/div/input').send_keys("11.11.2020")
time.sleep(1)
#Код подразделения
driver.find_element(By.ID, "code").click()
driver.find_element(By.ID, "code").clear()
driver.find_element(By.ID, "code").send_keys("123456")
#Снилс
driver.find_element(By.ID, "cardId").clear()
driver.find_element(By.ID, "cardId").send_keys("12345678901")
#Кем выдан
driver.find_element(By.ID, "issued").clear()
driver.find_element(By.ID, "issued").send_keys("ОВД")
#Адрес
driver.find_element(By.ID, "address").click()
driver.find_element(By.CSS_SELECTOR, ".vue-dadata__input").send_keys(Keys.CONTROL+ "a")
driver.find_element(By.CSS_SELECTOR, ".vue-dadata__input").send_keys(Keys.DELETE)
driver.find_element(By.CSS_SELECTOR, ".vue-dadata__input").send_keys("г Великий Новгород")
driver.find_element(By.XPATH, '//*[@id="address"]/div/div/input').send_keys(Keys.ARROW_DOWN)
driver.find_element(By.XPATH, '//*[@id="address"]/div/div/input').send_keys(Keys.ENTER)
time.sleep(5)
#Телефон
driver.find_element(By.ID, "phone").clear()
driver.find_element(By.ID, "phone").send_keys("1234567890")
#Чек-поинт
#два клика,так как уже кликнут в +
driver.find_element(By.ID, "privacy").click()
driver.find_element(By.ID, "privacy").click()
#Отправить
time.sleep(5)
driver.find_element(By.CSS_SELECTOR, ".btn fill").click()
time.sleep(5)





"""
driver.find_element(By.CSS_SELECTOR, "menu-header").click()
driver.find_element(By.CSS_SELECTOR, "logout").click()
driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div/div[2]/table/tbody/tr[3]/td[3]/div").click()
driver.find_element(By.XPATH, '//*[@id="dateOfIssue"]/div/input').send_keys("06.06.2016")


driver.find_element(By.XPATH, '//*[@id="address"]/div').click()
driver.find_element(By.XPATH, '//*[@id="address"]/div/div/input').clear()
time.sleep(3)
driver.find_element(By.XPATH, '//*[@id="address"]/div/div/input').send_keys("г Великий Новгород")
time.sleep(3)
driver.find_element(By.XPATH, '//*[@id="address"]/div').click()
driver.find_element(By.XPATH, '//*[@id="address"]/div/div/input').send_keys(Keys.ARROW_DOWN)
driver.find_element(By.XPATH, '//*[@id="address"]/div/div/input').send_keys(Keys.ENTER)
time.sleep(3)



driver.find_element(By.ID, "address").click()
driver.find_element(By.CSS_SELECTOR, ".vue-dadata__input").send_keys(Keys.CONTROL+ "a")
driver.find_element(By.CSS_SELECTOR, ".vue-dadata__input").send_keys(Keys.DELETE)
driver.find_element(By.CSS_SELECTOR, ".vue-dadata__input").send_keys("г Великий Новгород")
#driver.find_element(By.XPATH, ".vue-dadata__input").click()
time.sleep(5)
"""