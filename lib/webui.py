from selenium import webdriver
from hytest import *
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import NoAlertPresentException


def open_browser():
    INFO('打开浏览器')
    options = webdriver.ChromeOptions()
    os.environ['SE_DRIVER_MIRROR_URL'] = 'https://cdn.npmmirror.com/binaries/chrome-for-testing'
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    wd = webdriver.Chrome(options=options)
    wd.implicitly_wait(10)
    #  使用 Hytest 的全局变量 GSTORE，把浏览器实例 wd 存进去，方便其他函数拿来用
    GSTORE['wd'] = wd


def mgr_login():
    wd = GSTORE['wd']
    wd.get('http://127.0.0.1/mgr/sign.html')
    wd.find_element(By.ID, 'username').send_keys('byhy')
    wd.find_element(By.ID, 'password').send_keys('88888888')
    # 点击登录
    (wd.find_element(By.CLASS_NAME, 'btn-flat')).click()


def addMedicine(ss):
    # ss = ['青霉素盒装1','YP-32342341','青霉素注射液，每支15ml，20支装']

    wd = GSTORE['wd']
    # 点击 药品
    (wd.find_element(By.CSS_SELECTOR, 'a[href="#/medicines"]')).click()
    # 点击 添加药品
    (wd.find_element(By.XPATH, '//section[2]/div[1]/button')).click()

    els = wd.find_elements(By.XPATH,
                           '//section[2]/div[1]/div[1]/div[1]/input | //section[2]/div[1]/div[1]/div[2]/input | '
                           '//section[2]/div[1]/div[1]/div[3]/textarea')
    for i, s in enumerate(els):
        s.send_keys(ss[i])
    # 点击创建
    (wd.find_element(By.XPATH, '//section[2]/div[1]/div[2]/button[1]')).click()
    sleep(2)


def delAllMedicine():
    # ss = ['南京中医院1','2551867851','江苏省-南京市-秦淮区-汉中路-501']
    wd = GSTORE['wd']
    wd.find_element(By.CSS_SELECTOR, 'a[href="#/medicines"]').click()

    # 判断是多页  还是  1页
    n = len(wd.find_elements(By.CSS_SELECTOR, '.row > .pagination'))
    if n > 0:
        # 多页，至少2页
        # 点击 尾页
        wd.find_element(By.XPATH, '//section[2]/div[2]/ul/li[last()]/a').click()
        # 找是active的页数
        a = wd.find_element(By.CSS_SELECTOR, '.pagination > li.active > a')
        # 订单个数
        nums = (int(a.text) - 1) * 5 + len(wd.find_elements(By.XPATH, '//section[2]//div[@class="search-result-item"]'))
        wd.find_element(By.XPATH, '//section[2]/div[2]/ul/li[3]/a').click()  # 点击第一页

        for i in range(nums):
            wd.find_element(By.XPATH, '//section[2]/div[3]/div[4]/div/label[2]').click()
            sleep(2)
            # 点击确认删除
            notify = wd.switch_to.alert.text
            CHECK_POINT('弹出提示:删除药品', notify == '确定要删除此药品吗？')
            # 点击确定按钮
            wd.switch_to.alert.accept()
            sleep(2)
    else:
        # 只有1页
        nums = len(wd.find_elements(By.XPATH, '//section[2]//div[@class="search-result-item"]'))
        if nums != 0:
            for i in range(nums):
                wd.find_element(By.XPATH, '//section[2]/div[3]/div[4]/div/label[2]').click()
                sleep(2)
                # 点击确认删除
                notify = wd.switch_to.alert.text
                CHECK_POINT('弹出提示:删除药品', notify == '确定要删除此药品吗？')
                # 点击确定按钮
                wd.switch_to.alert.accept()
                sleep(2)
        else:
            print('无药品，无需删除！')


def addCustome(ss):
    # ss = ['南京中医院1','2551867851','江苏省-南京市-秦淮区-汉中路-501']
    wd = GSTORE['wd']
    wd.find_element(By.CSS_SELECTOR, 'a[href="#/customers"]').click()
    wd.find_element(By.CSS_SELECTOR, '.add-one-area > button').click()

    custom = wd.find_element(By.CSS_SELECTOR, '.col-sm-8 > div:nth-child(1) > input')
    custom.send_keys(ss[0])
    phone = wd.find_element(By.CSS_SELECTOR, '.col-sm-8 > div:nth-child(2) > input')
    phone.send_keys(ss[1])
    address = wd.find_element(By.CSS_SELECTOR, '.col-sm-8 > div:nth-child(3) > textarea')
    address.send_keys(ss[2])
    # 点击创建
    (wd.find_element(By.XPATH, '//section[2]/div[1]/div[2]/button[1]')).click()
    sleep(2)


def delAllCustome():
    # ss = ['南京中医院1','2551867851','江苏省-南京市-秦淮区-汉中路-501']
    wd = GSTORE['wd']
    wd.find_element(By.CSS_SELECTOR, 'a[href="#/customers"]').click()

    # 判断是多页  还是  1页
    n = len(wd.find_elements(By.CSS_SELECTOR, '.row > .pagination'))
    if n > 0:
        # 多页，至少2页
        # 点击 尾页
        wd.find_element(By.XPATH, '//section[2]/div[2]/ul/li[last()]/a').click()
        # 找是active的页数
        a = wd.find_element(By.CSS_SELECTOR, '.pagination > li.active > a')
        # 订单个数
        nums = (int(a.text) - 1) * 5 + len(wd.find_elements(By.XPATH, '//section[2]//div[@class="search-result-item"]'))
        wd.find_element(By.XPATH, '//section[2]/div[2]/ul/li[3]/a').click()  # 点击第一页

        for i in range(nums):
            wd.find_element(By.XPATH, '//section[2]/div[3]/div[4]/div/label[2]').click()
            sleep(2)
            # 点击确认删除
            notify = wd.switch_to.alert.text
            CHECK_POINT('弹出提示：删除客户', notify == '确定要删除此客户吗？')
            # 点击确定按钮
            wd.switch_to.alert.accept()
            sleep(2)
    else:
        # 只有1页
        nums = len(wd.find_elements(By.XPATH, '//section[2]//div[@class="search-result-item"]'))
        if nums != 0:
            for i in range(nums):
                wd.find_element(By.XPATH, '//section[2]/div[3]/div[4]/div/label[2]').click()
                sleep(2)
                # 点击确认删除
                notify = wd.switch_to.alert.text
                CHECK_POINT('弹出提示：删除客户', notify == '确定要删除此客户吗？')
                # 点击确定按钮
                wd.switch_to.alert.accept()
                sleep(2)
        else:
            print('无客户，无需删除！')


def addOrder(ss):
    # ss = ['南京中医院2订单', '南京中医院2', '青霉素盒装1', '100']
    wd = GSTORE['wd']
    # 点击 订单
    wd.find_element(By.CSS_SELECTOR, 'a[href="#/orders"]').click()
    # 点击 添加订单
    wd.find_element(By.XPATH, '//*[@id="root"]/div/section[2]/div[1]/button').click()
    ele = wd.find_elements(By.XPATH, '//section[2]/div[1]/div[1]/div[1]/input | '
                                     '//section[2]/div[1]/div[1]/div[2]/select | '
                                     '//section[2]/div[1]/div[1]/div[3]/select')
    for i, e in enumerate(ele):
        if i == 0:
            ele[i].send_keys(ss[i])
        else:
            select = Select(ele[i])
            select.select_by_visible_text(ss[i])
    num_ele = wd.find_element(By.XPATH, '//section[2]/div[1]/div[1]/div[3]/div/input')
    num_ele.send_keys(ss[-1])

    # 创建
    (wd.find_element(By.XPATH, '//section[2]/div[1]/div[2]/button[1]')).click()


def delAllOrder():
    def del1(nums):
        for i in range(nums):
            wd.find_element(By.XPATH, '//section[2]/div[3]/div[5]/div/label').click()
            sleep(2)
            # 点击确认删除
            notify = wd.switch_to.alert.text
            CHECK_POINT('弹出提示：删除订单', notify == '确定要删除此订单吗？')
            # 点击确定按钮
            wd.switch_to.alert.accept()
            sleep(2)

    wd = GSTORE['wd']
    wd.find_element(By.CSS_SELECTOR, 'a[href="#/orders"]').click()

    # 判断是多页  还是  1页 订单
    n = len(wd.find_elements(By.CSS_SELECTOR, '.row > .pagination'))

    if n > 0:
        # 多页，2页起步
        # 点击 尾页
        wd.find_element(By.XPATH, '//section[2]/div[2]/ul/li[last()]/a').click()
        # 找是active的页数
        a = wd.find_element(By.CSS_SELECTOR, '.pagination > li.active > a')
        # 订单个数
        nums = (int(a.text) - 1) * 5 + len(wd.find_elements(By.XPATH, '//section[2]//div[@class="search-result-item"]'))
        wd.find_element(By.XPATH, '//section[2]/div[2]/ul/li[3]/a').click()  # 点击第一页
        del1(nums)
    else:
        # 删除单页
        nums = len(wd.find_elements(By.XPATH, '//section[2]//div[@class="search-result-item"]'))
        if nums != 0:
            del1(nums)
        else:
            print('没有订单，无需删除！')


def clickAlert():
    # 测试过程中，浏览器提示密码泄露
    # 有弹框，则点掉
    wd = GSTORE['wd']
    try:
        alert = wd.switch_to.alert
        alert_text = alert.text
        INFO(f'检测到弹窗，内容为: {alert_text}')
        alert.accept()
        INFO('已点击弹窗确定按钮')
    except NoAlertPresentException:
        INFO('当前页面没有弹窗')


