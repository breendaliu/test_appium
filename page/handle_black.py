import logging
import allure
from selenium.webdriver.common.by import By


def handle_black(func):
    logging.basicConfig(level=logging.INFO)

    def wrapper(*args, **kwargs):
        # todo “以后再说”报错，当前提示无法弹出，待再次验证
        _black_list = [
            (By.XPATH, '//*[@text="以后再说"]'),
            (By.ID, 'com.mstz.xf:id/agree'),
            (By.ID, "com.mstz.xf:id/title_back_img"),
            (By.XPATH, '//*[@text="始终允许"]'),
            (By.ID, "com.mstz.xf:id/confirm")
        ]
        from page.base_page import BasePage
        instance: BasePage = args[0]
        try:
            logging.info("run " + func.__name__ + "\n args: \n" + repr(args[1:]) + "\n" + repr(kwargs))
            element = func(*args, **kwargs)
            # 清空错误次数
            _error_num = 0
            instance.set_implicitly_wait(5)
            return element
        except Exception as e:
            instance.screenshot("tmp.png")
            with open("tmp.png", "rb") as f:
                content = f.read()
            allure.attach(content, attachment_type=allure.attachment_type.PNG)
            logging.error("element not found, handle black list")
            instance.set_implicitly_wait(5)
            # 如果次数太多，就退出异常逻辑，直接保错
            if instance._error_num > instance._max_err_num:
                instance._error_num = 0
                raise e
            # 记录一直异常的次数
            instance._error_num += 1
            # 对黑名单里的弹框进行处理
            for ele in instance._black_list:
                logging.info(ele)
                eles = instance.finds(ele)
                if len(eles) > 0:
                    eles[0].click()
                    # 继续寻找原来的正常控件
                    return wrapper(*args, **kwargs)
            # 如果黑名单也没有，就报错
            logging.warning("black list no one foound")
            raise ValueError("元素未找到，且不在黑名单中")

    return wrapper
