from flask import current_app
import os
import shutil
import json


class SettingUtil:
    def __init__(self, config):
        self.config: dict = config

    def check_exit(self):
        file_path = self.config.get("SETTING_FILE")
        return os.path.exists(file_path)

    @staticmethod
    def setting_builder() -> dict:
        setting: dict = {
            "mail": {
                "enable": False,
                "host": "",
                "password": "",
                "port": 0,
                "pattern": ""
            },
            "host": ""
        }
        email_enable: str = input("enable email verification ([Y]/n): ")
        email_enable = email_enable.lower()
        if (email_enable == '' or email_enable == "y"):
            mail_setting: dict = setting["mail"]
            mail_setting["enable"] = True
            mail_setting["host"] = input("google account: ")
            mail_setting["password"] = input("google aplication password: ")
            mail_setting["port"] = 587
            mail_setting["pattern"] = input("input email pattern: ")
        setting["mail"]["enable"] = False
        setting["host"] = input("enter external ip address or domain name: ")
        return setting

    def load_setting(self):
        file_path = self.config.get("SETTING_FILE")
        if self.check_exit():
            # shutil.copy(os.path.join(os.path.abspath("./setting"),
            #             "setting.json"), self.config.get("SETTING_FILE"))
            with open(file_path, "r") as f:
                data = f.read()
            setting = json.loads(data)
        else:
            setting = self.setting_builder()
            with open(file_path, "w") as f:
                f.write(json.dumps(setting))
        return setting
