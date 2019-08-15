

# 目的：必须是主模块才执行游戏逻辑
from stage1.project_month01.game2048.usl import *

if __name__ == "__main__":
    view = GameConsoleView()
    view.start()
    view.update()