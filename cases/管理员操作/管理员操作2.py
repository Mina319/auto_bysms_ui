import time
from lib.webui import *


class UI_0105:
    name = '管理员操作-0105'

    def teststeps(self):
        STEP(1, '点击药品')
        # 点击添加客户
        wd = GSTORE['wd']
        # 点击 药品
        (wd.find_element(By.CSS_SELECTOR, 'a[href="#/medicines"]')).click()
        # 点击 添加药品
        (wd.find_element(By.XPATH, '//section[2]/div[1]/button')).click()

        STEP(2, '添加药品')
        info = ['叶黄素', '3456876', '叶黄素叶黄素']
        ss = wd.find_elements(By.XPATH,
                              '//section[2]/div[1]/div[1]/div[1]/input | //section[2]/div[1]/div[1]/div[2]/input | '
                              '//section[2]/div[1]/div[1]/div[3]/textarea')
        for i, s in enumerate(ss):
            s.send_keys(info[i])
        # 点击创建
        (wd.find_element(By.XPATH, '//section[2]/div[1]/div[2]/button[1]')).click()
        time.sleep(2)
        # 检查
        infos = wd.find_elements(By.XPATH, '//section[2]/div[3]/div//span[2]')
        texts = [i.text for i in infos]
        CHECK_POINT('客户信息和添加内容是否一致检查点', texts == info)


class UI_0106:
    name = '管理员操作-0106'

    def teststeps(self):
        STEP(1, '点击链接白月黑羽网站')
        wd = GSTORE['wd']
        home = wd.current_window_handle
        # 点击 超链接
        (wd.find_element(By.XPATH, '//footer[@class="main-footer"]/div[1]/a')).click()

        STEP(2, '获取菜单')
        # 获取所有窗口句柄
        all_windows = wd.window_handles
        # 切换到新打开的窗口，确保它不是当前窗口
        for window in all_windows:
            if window != home:
                wd.switch_to.window(window)
                break
        # 最大化浏览器窗口，不然打印不出来
        wd.maximize_window()
        infos = wd.find_elements(By.XPATH, '//nav[@class="md-tabs"]//a')
        # .visible-links li , .hidden-links li
        info = [i.text for i in infos]
        expected = ['Python基础', 'Python进阶', 'Qt图形界面', 'Django', '自动化测试', '性能测试', 'JS语言', 'JS前端']
        CHECK_POINT('菜单是否一致检查点', info == expected)
        wd.close()
        wd.switch_to.window(home)


class UI_0107:
    name = '管理员操作-0107'

    def teststeps(self):
        STEP(1, '添加3种药品')
        # 点击添加客户
        addMedicine(['青霉素盒装1', 'YP-32342341', '青霉素注射液，每支15ml，20支装'])
        addMedicine(['青霉素盒装2', 'YP-32342342', '青霉素注射液，每支15ml，30支装'])
        addMedicine(['青霉素盒装3', 'YP-32342343', '青霉素注射液，每支15ml，40支装'])

        STEP(2, '添加3个客户')
        addCustome(['南京中医院1', '2551867851', '江苏省-南京市-秦淮区-汉中路-501'])
        addCustome(['南京中医院2', '2551867852', '江苏省-南京市-秦淮区-汉中路-502'])
        addCustome(['南京中医院3', '2551867853', '江苏省-南京市-秦淮区-汉中路-503'])

        STEP(3, '添加订单')
        mes = ['南京中医院2订单', '南京中医院2', '青霉素盒装1', '100']
        addOrder(mes)
        # 检查
        wd = GSTORE['wd']
        infos = wd.find_elements(By.XPATH, '//section[2]/div[3]/div//span[2]')
        texts = [i.text for i in infos]
        # print('------texts------1', texts)
        texts.pop(1)  # 删除日期
        t = wd.find_element(By.XPATH, '//section[2]/div[3]/div//p').text
        med, num = t.split('*')
        texts.append(med.strip())
        texts.append(num.strip())
        # print('------texts------2', texts)
        CHECK_POINT('添加订单成功', texts == mes)


class UI_0108:
    name = '管理员操作-0108'

    def setup(self):
        # 清除所有 订单、客户和药品
        delAllOrder()
        delAllCustome()
        delAllMedicine()
        pass

    def teststeps(self):
        STEP(1, '添加3种药品')
        # 点击添加客户
        addMedicine(['青霉素盒装1', 'YP-32342341', '青霉素注射液，每支15ml，20支装'])
        addMedicine(['青霉素盒装2', 'YP-32342342', '青霉素注射液，每支15ml，30支装'])
        addMedicine(['青霉素盒装3', 'YP-32342343', '青霉素注射液，每支15ml，40支装'])

        STEP(2, '添加3个客户')
        addCustome(['南京中医院1', '2551867851', '江苏省-南京市-秦淮区-汉中路-501'])
        addCustome(['南京中医院2', '2551867852', '江苏省-南京市-秦淮区-汉中路-502'])
        addCustome(['南京中医院3', '2551867853', '江苏省-南京市-秦淮区-汉中路-503'])

        STEP(3, '添加订单')
        order = ['南京中医院2订单', '南京中医院2', '青霉素盒装1', '100']
        addOrder(order)
        # 检查
        wd = GSTORE['wd']
        infos = wd.find_elements(By.XPATH, '//section[2]/div[3]/div//span[2]')
        texts = [i.text for i in infos]
        texts.pop(1)  # 删除日期
        t = wd.find_element(By.XPATH, '//section[2]/div[3]/div//p').text
        med, num = t.split('*')
        texts.append(med.strip())
        texts.append(num.strip())
        CHECK_POINT('添加订单成功', texts == order)

