from datetime import datetime, date, timedelta
import schedule
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import Select

faise = 0

def to_page(driver):
    time.sleep(1)
    driver.find_element_by_id("itembox2013").find_element_by_xpath("//li[1]/dl/dt/a").click()
    return 1

def into_cart(driver):
    time.sleep(1)
    driver.find_element_by_id("cart-add").click()
    return 2

def pay_list_click(driver):
    time.sleep(1)
    driver.find_element_by_id("pay_list").find_element_by_class_name("regi_btn").find_element(By.TAG_NAME, "input").click()
    return 3

def fill_out_form(driver):
    time.sleep(1)
    # ご購入者様情報入力
    driver.find_element_by_name("CUSTOMER[PURCHASE_POST_NUMBER]").send_keys("")  # 郵便番号
    time.sleep(1)
    driver.find_element_by_name("CUSTOMER[PURCHASE_NAME]").send_keys("")  # 名前
    time.sleep(1)
    driver.find_element_by_name("CUSTOMER[PURCHASE_KANA]").send_keys("")  # カナ
    time.sleep(1)
    driver.find_element_by_name("CUSTOMER[PURCHASE_TEL]").send_keys("")  # TEL
    time.sleep(1)
    driver.find_element_by_name("CUSTOMER[PURCHASE_MAIL]").send_keys("")  # mail
    time.sleep(1)
    driver.find_element_by_name("CUSTOMER[PURCHASE_MAIL_CONFIRM]").send_keys("")  # mail
    time.sleep(1)
    driver.find_element_by_name("CUSTOMER[PURCHASE_MUNICIPALITY]").send_keys("")  # 住所
    time.sleep(1)

    # お支払い方法
    driver.find_element_by_name("CUSTOMER[ORDER_PAYMENT_METHOD]").click()
    time.sleep(1)
    driver.find_element_by_name("card_number").send_keys("")  # クレジット番号
    time.sleep(1)
    Select(driver.find_element_by_name("expire_month")).select_by_value("")  # 月
    time.sleep(1)
    Select(driver.find_element_by_name("expire_year")).select_by_value("")  # 年
    time.sleep(1)
    driver.find_element_by_name("cvc").send_keys("")  # セキュリティコード
    time.sleep(1)
    # TODO exit()をはずす
    #exit()
    driver.find_element_by_id("regi_form").find_element_by_xpath("//input[5]").click()
    return 4

def conform(driver):
    time.sleep(1)
    driver.find_element_by_id("regi_form").find_element_by_xpath("//input[2]").click()
    return 5

def finish(driver):
    time.sleep(1)
    driver.find_element_by_id("itemnm")


def buy(driver):
    global faise
    driver.refresh()
    if faise == 0:
        faise = to_page(driver)
    if faise == 1:
        faise = into_cart(driver)
    if faise == 2:
        faise = pay_list_click(driver)
    if faise == 3:
        faise = fill_out_form(driver)
    if faise == 4:
        faise = conform(driver)
    if faise == 5:
        finish(driver)


def while_buy():
    page = "https://www.irisplaza.co.jp/index.php?KB=KAISO&CID=4065"  # マスクと検索したページ

    options = Options()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    capabilities = DesiredCapabilities.CHROME.copy()
    capabilities['acceptInsecureCerts'] = True
    # TODO set executable_path
    driver = webdriver.Chrome(executable_path="", chrome_options=options, desired_capabilities=capabilities)
    driver.maximize_window()

    driver.get(page)
    while True:
        try:
            buy(driver)
        except:
            print(datetime.now(), " error   :   faise  ", faise)
        else:
            print("購入完了")
            break


if __name__ == "__main__":
    """
    schedule.every().day.at("12:59").do(while_buy)
    
    while True:
        schedule.run_pending()
        time.sleep(1)
    """

    while_buy()
