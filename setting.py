class Settings:
    """设置游戏的各种参数的类"""
    def __init__(self):
        """初始化游戏的设置"""   
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)
ai_setting = Settings()
print(ai_setting.bg_color)