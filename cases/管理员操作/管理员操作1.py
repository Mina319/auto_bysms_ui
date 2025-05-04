from lib.webui import *
# 该文件中的用例都拥有了下面的标签
force_tags = ['登录功能', '冒烟测试', 'UI测试']


class UI_0101:
    name = '管理员操作-0101'

    def teststeps(self):
        INFO('检查左侧菜单')
        STEP(1, '获取左侧菜单信息')
        wd = GSTORE['wd']
        eles = wd.find_elements(By.CSS_SELECTOR, '.sidebar-menu li span')
        menuText = [ele.text for ele in eles]
        INFO(menuText)
        STEP(2, '检查菜单栏')
        # 第1个参数是 webdriver 对象
        # width 参数为可选参数， 指定图片显示宽度
        SELENIUM_LOG_SCREEN(wd, width='70%')
        CHECK_POINT('左侧菜单检查', menuText[:3] == ['客户', '药品', '订单'])


class UI_0102:
    name = '管理员操作-0102'

    def teststeps(self):
        STEP(1, '添加客户')
        expected = ['南京中医院', '52276666', '南京市秦淮区大明路157号']
        addCustome(expected)

        # 检查
        wd = GSTORE['wd']
        infos = wd.find_elements(By.CSS_SELECTOR, '.container-fluid > div:nth-child(3) div span:nth-child(2)')
        texts = [i.text for i in infos]
        CHECK_POINT('客户信息和添加内容是否一致检查点', texts == expected)


class UI_0103:
    name = '管理员操作-0103'

    def teststeps(self):
        STEP(1, '添加客户')
        # 点击添加客户
        wd = GSTORE['wd']
        expected = ['南京中医院', '13913271898', '南京市秦淮区大明路157号']
        addCustome(expected)

        STEP(2, '编辑客户为“南京省中医院”')
        # 点击编辑
        (wd.find_element(By.XPATH, '//section[2]/div[3]/div[4]//label[1]')).click()
        input1 = wd.find_element(By.XPATH, '//section[2]/div[3]/div[1]//div[1]/input')
        input1.clear()
        input1.send_keys('南京省中医院')
        # 确定
        (wd.find_element(By.XPATH, '//section[2]/div[3]/div[2]//label[1]')).click()

        # 检查
        infos = wd.find_elements(By.CSS_SELECTOR, '.container-fluid > div:nth-child(3) div span:nth-child(2)')
        texts = [i.text for i in infos]
        expected1 = ['南京省中医院', '13913271898', '南京市秦淮区大明路157号']
        CHECK_POINT('客户信息和编辑内容是否一致检查点', texts == expected1)

