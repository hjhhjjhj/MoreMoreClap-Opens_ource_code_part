# 导入官方模块
import sys
import tkinter as tk
import easygui as g
import random
from time import sleep
import time
import re
import _thread


# 导入自己写的模块
from More_More_Clap_master.skill_panding_player import skill_panding_player
from More_More_Clap_master.qi_panding import qi_panding
from More_More_Clap_master.xt_use_skill import xt_use_skill


#处理图片路径
photo_egg = sys.argv[0]
photo_egg = re.sub("main.py", "", str(photo_egg))
photo_egg = str(photo_egg) + "More_More_Clap_master/image/SCP-XT-011.gif"


# ========初始化全局变量========
# 作战记录存储
txt_save = open(time.strftime("%Y-%m-%d %H点%M分%S秒", time.localtime()) + '战斗记录.txt', 'w')
# 常规初始化
skill = ''
hui = 0
jv = 0
xiqi = 3
qi = 0
xtqi = 0
xitonguse = []
skillpanduanreturn = ''
skillpanduanreturn_number = ''
MODE = ""
MMC_c_b_witer = 0

# ========初始化全局变量========


# ====各个模式技能默认不加低于自身模式的技能，实际使用时需进行用前处理====

# 普通人的技能
commonHuman = \
    {
        # 防御
        '挡': 0, '穿山甲': 0.5, '绵绵': 1,
        # 攻击/逃避
        '金遁': 1, '木遁': 2, '水遁': 3, '火遁': 4, '土遁': 5, '钻地土遁': 4,
        # 召唤
        '髌冰解锁': 0,
        # 吸气
        '吸气': xiqi

    }

# 初级模式的技能
elementary_commonHuman = \
    {
        # 普通人
        # 防御
        '挡': 0, '穿山甲': 0.5, '绵绵': 1,
        # 攻击/逃避
        '金遁': 1, '木遁': 2, '水遁': 3, '火遁': 4, '土遁': 5, '钻地土遁': 4,
        # 召唤
        '髌冰解锁': 0,
        # 吸气
        '吸气': xiqi,
        # 风
        '风挡': 0, '电风扇': 0.5, '低级风波': 1, '高级风波': 2, '龙卷风': 3, '低级风神下凡': 4, '高级风神下凡': 8,
        # 雨
        '雨挡': 0, '低级流星雨': 1, '高级流星雨': 2, '及时雨': 3, '黑时雨': 6, '低级雨神下凡': 4, '高级雨神下凡': 8,
        # 雷
        '雷挡': 0, '雷击': 1, '雷暴': 1, '低级五雷轰顶': 3, '高级五雷轰顶': 6, '低级雷神下凡': 4, '高级雷神下凡': 8,
        # 电
        '电挡': 0, '放电': 0.5, '双重放电': 3, '电网': 1, '电神下凡': 5,
        # 火
        '火挡': 0, '小火圈': 0.5, '大火圈': 3, '火神下凡': 5
    }

# 高级模式的技能
advanced_commonHuman = \
    {
        # 龙王
        # 汉堡
        # 哪吒
        # 老白
        # 观音
        # 如来
        # 二郎
        # 八戒
        # 悟空
        # 六耳
        # 唐僧
        # 盘古
    }

# 完全模式的技能
complete_commonHuman_a = \
    {
        #
        # 黑暗
        # 光明
        # 王者
    }

# 无尽模式的技能
endless_commonHuman = \
    {
        # ?
    }


# =======================================分割线=====================================
# 普通人模式    判断系统当前所有的气可用那些技能
def xtuse_commonHuman(xtqi1):
    global xitonguse

    # 初始化系统技能变量xtuse_commonHuman
    while True:

        # 测试代码
        sleep(0)
        print('系统可使用的技能初始化ing：' + str(xitonguse))

        n = len(xitonguse)
        if n > 0:
            del xitonguse[0:]
        elif n == 0:

            # 测试代码
            print('系统可使用的技能初始化完成：' + str(xitonguse))

            break
        else:
            break

    # 耗气0的技能
    a = ['挡', '髌冰解锁']
    # 耗气0.5的技能
    b = ['穿山甲']
    # 耗气1
    c = ['绵绵', '金遁']
    # 耗气2
    d = ['木遁']
    # 耗气3
    e = ['水遁']
    # 耗气4的技能
    f = ['火遁', '钻地土遁']
    # 耗气5的技能
    gg = ['土遁']
    # 吸气技能
    h = ['吸气']
    if xtqi1 >= 5:
        xitonguse = h + a + b + c + d + e + f + gg
    elif xtqi1 < 5:
        if xtqi1 >= 4:
            xitonguse = h + a + b + c + d + e + f
        elif xtqi1 < 4:
            if xtqi1 >= 3:
                xitonguse = h + a + b + c + d + e
            elif xtqi1 < 3:
                if xtqi1 >= 2:
                    xitonguse = h + a + b + c + d
                elif xtqi1 < 2:
                    if xtqi1 >= 1:
                        xitonguse = h + a + b + c
                    elif xtqi1 < 1:
                        if xtqi1 >= 0.5:
                            xitonguse = h + a + b
                        elif xtqi1 < 0.5:
                            if xtqi1 == 0:
                                xitonguse = h + a
                            elif xtqi1 != 0:
                                pass
                        else:
                            pass
                    else:
                        pass
                else:
                    pass
            else:
                pass
        else:
            pass
    else:
        pass


# 普通人模式    游戏运行主体
def main():
    # 测试代码
    print('普通人模式 游戏主体成功运行')

    while True:

        title_star = '游戏开始'
        msg_star = '请熟悉游戏规则，如果已经熟知，点击开始'
        choices_star = ['正式开始游戏', '查看规则']
        stargame = g.buttonbox(msg_star, title_star, choices_star)
        if stargame == '查看规则':
            title_a = '游戏规则'
            msg_a = '懒得写.jpg\n下次一定[doge]'
            ok_button_a = '已熟知规则'
            g.msgbox(msg_a, title_a, ok_button_a)
            pass
        elif stargame == '正式开始游戏':

            global xtqi
            global qi
            global jv
            global hui

            jv = int(1)

            while True:

                # 初始化玩家和系统所拥有的气以及回合
                global xtqi
                global qi
                global skill

                xtqi -= xtqi
                qi -= qi
                hui = int(1)

                # 测试代码
                print('成功初始化玩家和系统的气，以及回合')

                title_game = '第' + str(jv) + '局' + '第' + str(hui) + '回'
                msg_game = '请选择你要使用的技能'
                choices_game = ['吸气', '挡', '髌冰解锁', '穿山甲', '绵绵', '金遁', '木遁', '水遁', '火遁', '土遁', '钻地土遁']
                skill = g.buttonbox(msg_game, title_game, choices_game)

                choices_game2 = ['确定']

                txt_save.write('\n' + title_game + '\n')

                # 第一回判断
                if skill == '吸气':
                    qi = qi + xiqi
                    xitongjileng = choices_game[0]
                    xtqi = qi_panding.xitongqipanduan(xitongjileng, xtqi, xiqi)
                    msg_b_b = \
                        '你获得了' + str(xiqi) + '口气！' + '\n你现在有' + str(qi) + '口气！' + \
                        '\n系统1使用了' + str(xitongjileng) + '技能' + '系统有' + str(xtqi) + '口气'
                    g.buttonbox(msg_b_b, title_game, choices_game2)

                    hui += 1

                    txt_save.write('\n' + msg_b_b + '\n')

                    pass

                else:
                    msg_b_a = '你爆死了！'
                    choices_b_a = ['重新开始', '结束游戏']
                    b_a = g.buttonbox(msg_b_a, title_game, choices_b_a)

                    txt_save.write(msg_b_a + '\n' + b_a + '\n')

                    if b_a == '重新开始':
                        pass
                    elif b_a == '结束游戏':
                        txt_save.close()
                        sys.exit(0)
                    else:
                        txt_save.close()
                        sys.exit(0)

                # 第二回合后的判断
                while True:

                    if hui == 1:
                        break
                    elif hui > 1:
                        pass
                    else:
                        txt_save.write('\n第二回合后判断模块异常\n')
                        txt_save.close()
                        sys.exit(0)

                    # 测试代码
                    print('成功启动模块“第二回合后的判断”')

                    title_game = '第' + str(jv) + '局' + '第' + str(hui) + '回'
                    msg_game = '请选择你要使用的技能'
                    skill = g.buttonbox(msg_game, title_game, choices_game)

                    txt_save.write('\n' + title_game + '\n')

                    # 系统和玩家技能耗气计算
                    qi = qi_panding.playerqipanduan(skill, qi, xiqi)
                    xtuse_commonHuman(xtqi)
                    n = len(xitonguse)
                    n -= 1
                    xitongjileng = xitonguse[random.randint(0, n)]
                    xtqi = qi_panding.xitongqipanduan(xitongjileng, xtqi, xiqi)

                    # 测试代码
                    print('成功运行模块"系统和玩家技能耗气计算"')

                    # 玩家耗气存活判断
                    if qi < 0:

                        # 测试代码
                        print('成功判断玩家死否耗气暴死')

                        msg_c_a = '你使用了' + str(skill) + '技能\n' + '你现在有' + str(qi) + '口气\n' + \
                                  '系统1使用了' + str(xitongjileng) + '技能\n' + '系统现在有' + str(xtqi) + '口气\n' + \
                                  '你爆死了'
                        g.buttonbox(msg_c_a, title_game, choices_game2)

                        txt_save.write(msg_c_a + '\n')

                        break

                    else:

                        # 测试代码
                        print('成功判断玩家死否耗气暴死')

                        # 初始化？
                        global skillpanduanreturn
                        global skillpanduanreturn_number

                        # 开始技能判定
                        skillpanduanreturn, skillpanduanreturn_number, different_a = \
                            skill_panding_player.skillpanding(skill, xitongjileng)

                        txt_save.write(skillpanduanreturn)

                        # 判定金遁和木遁是否打在了髌冰解锁上
                        if different_a == 'None':
                            if skillpanduanreturn == '双方存活':
                                msg_c_a = '你使用了' + str(skill) + '技能\n' + '你现在有' + str(qi) + '口气\n' + \
                                          '系统1使用了' + str(xitongjileng) + '技能\n' + '系统现在有' + str(xtqi) + '口气\n' + \
                                          str(skillpanduanreturn_number) + str(skillpanduanreturn)
                                g.buttonbox(msg_c_a, title_game, choices_game2)

                                txt_save.write(msg_c_a + '\n')
                                pass

                            elif skillpanduanreturn == '玩家胜利':
                                msg_c_b = '你使用了' + str(skill) + '技能\n' + '你现在有' + str(qi) + '口气\n' + \
                                          '系统1使用了' + str(xitongjileng) + '技能\n' + '系统现在有' + str(xtqi) + '口气\n' + \
                                          str(skillpanduanreturn_number) + str(skillpanduanreturn)
                                choices_c_b = ['重新开始', '结束游戏']
                                c_a = g.buttonbox(msg_c_b, title_game, choices_c_b)

                                txt_save.write(msg_c_b + '\n')

                                if c_a == '重新开始':
                                    break
                                elif c_a == '结束游戏':
                                    txt_save.close()
                                    sys.exit(0)
                                else:
                                    txt_save.close()
                                    sys.exit(0)
                            elif skillpanduanreturn == '系统胜利':
                                msg_c_c = '你使用了' + str(skill) + '技能\n' + '你现在有' + str(qi) + '口气\n' + \
                                          '系统1使用了' + str(xitongjileng) + '技能\n' + '系统现在有' + str(xtqi) + '口气\n' + \
                                          str(skillpanduanreturn_number) + str(skillpanduanreturn)
                                choices_c_c = ['重新开始', '结束游戏']
                                c_c = g.buttonbox(msg_c_c, title_game, choices_c_c)

                                txt_save.write(msg_c_c + '\n')

                                if c_c == '重新开始':
                                    break
                                elif c_c == '结束游戏':
                                    txt_save.close()
                                    sys.exit(0)
                                else:
                                    txt_save.close()
                                    sys.exit(0)
                            else:
                                print('嗯？？？')
                                break
                        elif different_a == 'a':

                            # 2021.9.25髌冰解锁bug修复程序
                            ########################################################################################
                            # 测试代码
                            print('髌冰解锁修复代码启动成功')

                            hui += 1

                            msg_c_d = '你使用了' + str(skill) + '技能\n' + '你现在有' + str(qi) + '口气\n' + \
                                      '系统1使用了' + str(xitongjileng) + '技能\n' + '系统现在有' + str(xtqi) + '口气\n' + \
                                      str(skillpanduanreturn_number) + str(skillpanduanreturn)
                            skill = g.buttonbox(msg_c_d, title_game, choices_game)

                            txt_save.write('\n' + title_game + '\n')

                            # 系统和玩家技能耗气计算
                            qi = qi_panding.playerqipanduan(skill, qi, xiqi)
                            xtuse_commonHuman(xtqi)
                            n = len(xitonguse)
                            n -= 1
                            xitongjileng = xitonguse[0]
                            xtqi = qi_panding.xitongqipanduan(xitongjileng, xtqi, xiqi)

                            # 测试代码
                            print('成功运行模块"系统和玩家技能耗气计算"')

                            # 技能判定
                            skillpanduanreturn, skillpanduanreturn_number = \
                                skill_panding_player.skillpanding_a(skill, xitongjileng)

                            ###########################################################

                            if skillpanduanreturn == '双方存活':
                                msg_c_a = '你使用了' + str(skill) + '技能\n' + '你现在有' + str(qi) + '口气\n' + \
                                          '系统1使用了' + str(xitongjileng) + '技能\n' + '系统现在有' + str(xtqi) + '口气\n' + \
                                          str(skillpanduanreturn_number) + str(skillpanduanreturn)
                                g.buttonbox(msg_c_a, title_game, choices_game2)

                                txt_save.write(msg_c_a + '\n')
                                pass

                            elif skillpanduanreturn == '系统胜利':
                                msg_c_c = '你使用了' + str(skill) + '技能\n' + '你现在有' + str(qi) + '口气\n' + \
                                          '系统1使用了' + str(xitongjileng) + '技能\n' + '系统现在有' + str(xtqi) + '口气\n' + \
                                          str(skillpanduanreturn_number) + str(skillpanduanreturn)
                                choices_c_c = ['重新开始', '结束游戏']
                                c_c = g.buttonbox(msg_c_c, title_game, choices_c_c)

                                txt_save.write(msg_c_c + '\n')

                                if c_c == '重新开始':
                                    break
                                elif c_c == '结束游戏':
                                    txt_save.close()
                                    sys.exit(0)
                                else:
                                    txt_save.close()
                                    sys.exit(0)
                            else:
                                print('嗯？？？')
                                break
                            pass
                        ########################################################################################
                        else:
                            txt_save.close()
                            sys.exit(0)

                    hui += 1

                    # 测试代码
                    print('"第二会合后判断"模块成功运行完毕')

                # 本局结束，局数加一
                jv += 1
                pass
        else:
            title_error = '程序错误'
            msg_error = '你干了个啥玩意，好好的安流程走不好吗？恼火.jpg'
            choices_error = ['重新开始', '退出游戏']
            error_a = g.buttonbox(msg_error, title_error, choices_error)
            if error_a == '重新开始':
                pass
            elif error_a == '退出游戏':
                txt_save.close()
                sys.exit(0)
            else:
                txt_save.close()
                sys.exit(0)


# =======================================分割线=====================================
# 初级模式游戏运行主体
def elementary_main():
    print('初级模式 游戏主体运行成功')

    # 开始界面窗口设置
    window_elementary_main = tk.Tk()
    window_elementary_main.title('哆哆吸(初级模式)')
    window_elementary_main.geometry('800x600')

    # 初始化需要用到的函数

    def elementary_exit():
        txt_save.close()
        sys.exit(0)

    def elementary_rule():
        # 规则界面组件设置
        window_elementary_main_rule = tk.Tk()
        window_elementary_main_rule.title('哆哆吸(初级模式) 规则查看')
        window_elementary_main_rule.geometry('800x600')

        rule_a = tk.Label(master=window_elementary_main_rule, text='懒得写awa\n下次一定\nQwQ')
        rule_a.pack(side='top', padx='0.c', pady='2.c')

        window_elementary_main_rule.mainloop()
        pass

    # 游戏开始！
    def elementary_game():

        # 变量初始化处理
        global photo_egg

        global jv
        global hui
        global renwu
        jv = 1
        hui = 0
        renwu = -1

        # 状态变量，处理无限递归问题用
        # 当ztjv=0时，表示玩家无事；ztjv=1时，表示本次游戏结束。
        # 当zthui=0时，表示玩家无事；zthui=1时，表示玩家胜利；zthui=2时，表示系统胜利。
        global ztjv
        global zthui
        ztjv = 0
        zthui = 0

        global xtqi
        global qi
        xtqi = 0
        qi = 0

        global bbjs_xiqi
        bbjs_xiqi = 0

        # 必要函数初始化处理
        def game_exit():
            txt_save.write('运行异常')
            txt_save.close()
            sys.exit(0)

        # 善后处理
        star_b_a.forget()
        window_elementary_main.update()
        window_elementary_main.destroy()

        # 初始化处理
        window_elementary_main_game = tk.Tk()
        window_elementary_main_game.title('哆哆吸(初级模式) 游戏开始')
        window_elementary_main_game.geometry('1000x600')

        renwu_list = ["风", "雨", "雷", "电", "火"]

        # 组件初始化处理====
        # 总容器控件===
        # 总状态容器==
        game_box_a = tk.Frame(master=window_elementary_main_game, bg='yellow', width=200, height=600)
        game_box_a.place(width=200, height=600)
        # 系统的
        game_box_a_a = tk.Frame(master=game_box_a, bg='yellow', width=200, height=600)
        game_box_a_a.place(width=200, height=300)
        # 玩家的
        game_box_a_b = tk.Frame(master=game_box_a, bg='yellow', width=200, height=600)
        game_box_a_b.place(width=200, height=300, y='300')
        # 总放作战行进过程==
        game_box_b = tk.Frame(master=window_elementary_main_game, bg='white', width=800, height=600)
        game_box_b.place(width=800, height=600, x='200')
        # 游戏对象使用技能反馈容器
        game_box_b_show = tk.Frame(master=game_box_b, width=600, bg='gray', height=200)
        game_box_b_show.place(width=600, height=200)
        # 用户选着技能位置容器
        game_box_b_skill = tk.Frame(master=game_box_b, width=600, bg='white', height=400)
        game_box_b_skill.place(width=600, height=400, y='200')
        game_box_b_skill_humanskill = tk.Frame(master=game_box_b_skill, width=200, bg='white', height=200)
        game_box_b_skill_humanskill.place(width=200, height=200)
        game_box_b_skill_fengskill = tk.Frame(master=game_box_b_skill, width=200, bg='LightYellow', height=200)
        game_box_b_skill_fengskill.place(width=200, height=200, x=200, y=0)
        game_box_b_skill_yvskill = tk.Frame(master=game_box_b_skill, width=200, bg='DeepSkyBlue', height=200)
        game_box_b_skill_yvskill.place(width=200, height=200, x=400, y=0)
        game_box_b_skill_leiskill = tk.Frame(master=game_box_b_skill, width=200, bg='SlateBlue', height=200)
        game_box_b_skill_leiskill.place(width=200, height=200, x=0, y=200)
        game_box_b_skill_dianskill = tk.Frame(master=game_box_b_skill, width=200, bg='LightSteelBlue', height=200)
        game_box_b_skill_dianskill.place(width=200, height=200, x=200, y=200)
        game_box_b_skill_huoskill = tk.Frame(master=game_box_b_skill, width=200, bg='OrangeRed', height=200)
        game_box_b_skill_huoskill.place(width=200, height=200, x=400, y=200)

        # 这个容器放彩蛋==
        game_box_c = tk.Frame(master=window_elementary_main_game, width=200, height=600)
        game_box_c.place(width=200, height=600, x='1000')

        #界面优化
        global name_a
        show_up_place_a = []

        def show_up(name, text, master, bg, width, height):

            #测试代码
            print("成功调用show_up")
            print('show_up传入参数显示: ' + str(text) + ' ## ' + str(master) + ' ## ' + str(bg) + ' ## ' + str(width) + ' ## ' + str(height))

            #声明变量
            global a, aa, aaa, aaaa, aaaaa, aaaaaa
            a = name
            aa = text
            aaa = master
            aaaa = bg
            aaaaa = width
            aaaaaa = height


        def show_up_place(width, height, x, y):

            #测试代码
            print("成功调用show_up_place")

            # 声明变量
            global name_a
            global a, aa, aaa, aaaa, aaaaa, aaaaaa

            # 实现颜射渐变
            def show_up_place_a():
                pass


            """
                global name_a
                global a, aa, aaa, aaaa, aaaaa, aaaaaa

                name_a = a
                if aaaa == "gray":
                    for i in ['white', 'snow', 'whitesmoke', 'gainsboro', 'lightgrey', "gray"]:
                        print('i==' + str(i))
                        name_a = tk.Label(text=aa, master=aaa, bg=i, width=aaaaa, height=aaaaaa)
                        name_a.place(width=width, height=height, x=x, y=y)
                        time.sleep(0.01)
                elif aaaa == "yellow":
                    for i in ['lightyellow', 'lightgoldenrodyellow', 'lemonchiffon', 'palegoldenrod', 'khaki', "yellow"]:
                        print('i==' + str(i))
                        name_a = tk.Label(text=aa, master=aaa, bg=i, width=aaaaa, height=aaaaaa)
                        name_a.place(width=width, height=height, x=x, y=y)
                        time.sleep(0.01)
                else:
                    print('没有调用成功啦>_<！')
                    pass

                # 重置变量
                name_a = ""
                a = ''
                aa = ''
                aaa = ''
                aaaa = ''
                aaaaa = ''
                aaaaaa = ''

            """

            _thread.start_new_thread(show_up_place_a, ("Thread-1", 2,))

            ###


        # 真·运行游戏（？
        def elementary_main_play(a):

            # 一点小处理
            global skill
            global xitong_skill
            skill = a
            xitong_skill = ""

            # 测试代码
            print('游戏开始！')

            # 初始化处理
            global jv
            global ztjv
            global zthui
            global xt_renwu_list
            global user_renwu_list

            # ztjv判定处理
            if jv > 5:
                ztjv = 1
            elif jv <= 4:
                ztjv = 0

            if ztjv == 1:
                # 本局为结算
                print("进入结算回合判定")

                # 初始化玩家和系统所拥有的气以及回合
                global hui
                global xtqi
                global qi
                global renwu
                global xiqi
                global renwu
                global bbjs_xiqi

                # 结算
                global xt_renwu_list
                global user_renwu_list

                skill_show_a = str("结算回合")
                game_name_show_b = tk.Label(text=skill_show_a, master=game_box_b_show, bg='gray', width=200, height=20)
                game_name_show_b.place(width=200, height=20, x='200')
                show_up(game_name_show_b, text=skill_show_a, master=game_box_b_show, bg='gray', width=200, height=20)
                show_up_place(width=200, height=20, x='200', y='0')

                # 显示结果
                skill_computer = str('系统共拥有人物：' + str(xt_renwu_list))
                game_name_show = tk.Label(text=skill_computer, master=game_box_b_show, bg='gray', width=240, height=20)
                game_name_show.place(width=200, height=30, x='240', y='20')
                show_up(game_name_show, text=skill_computer, master=game_box_b_show, bg='gray', width=240, height=20)
                show_up_place(width=200, height=30, x='240', y='20')
                skill_computer = str('玩家共拥有人物：' + str(user_renwu_list))
                game_name_show = tk.Label(text=skill_computer, master=game_box_b_show, bg='gray', width=240, height=20)
                game_name_show.place(width=200, height=30, x='240', y='50')
                show_up(game_name_show, text=skill_computer, master=game_box_b_show, bg='gray', width=240, height=20)
                show_up_place(width=200, height=30, x='240', y='50')
                if len(xt_renwu_list) > len(user_renwu_list):
                    skill_computer = str('结算：' + "系统获得最终胜利！")
                    game_name_show = tk.Label(text=skill_computer, master=game_box_b_show, bg='gray', width=200, height=20)
                    game_name_show.place(width=200, height=30, x='200', y='80')
                    show_up(game_name_show, text=skill_computer, master=game_box_b_show, bg='gray', width=200, height=20)
                    show_up_place(width=200, height=30, x='200', y='80')
                elif len(xt_renwu_list) == len(user_renwu_list):
                    skill_computer = str('结算：' + "双方平局！")
                    game_name_show = tk.Label(text=skill_computer, master=game_box_b_show, bg='gray', width=200, height=20)
                    game_name_show.place(width=200, height=30, x='200', y='80')
                    show_up(game_name_show, text=skill_computer, master=game_box_b_show, bg='gray', width=200, height=20)
                    show_up_place(width=200, height=30, x='200', y='80')
                elif len(xt_renwu_list) < len(user_renwu_list):
                    skill_computer = str('结算：' + "玩家获得最终胜利！")
                    game_name_show = tk.Label(text=skill_computer, master=game_box_b_show, bg='gray', width=200, height=20)
                    game_name_show.place(width=200, height=30, x='200', y='80')
                    show_up(game_name_show, text=skill_computer, master=game_box_b_show, bg='gray', width=200, height=20)
                    show_up_place(width=200, height=30, x='200', y='80')
                else:
                    print("出错了")
                    sys.exit(0)

                #重置游戏
                jv = 1
                hui = 0
                renwu = -1
                ztjv = 0
                zthui = 0
                xtqi = 0
                qi = 0

                # 重置后的系统状态结果显示(气、祥龙、人物)
                xt_renwu_list = ['普通人']
                game_name_computer = tk.Label(text=str(xtqi), master=game_box_a_a, bg='yellow', width=200, height=20)
                game_name_computer.place(width=140, height=20, x='60', y='20')
                show_up(game_name_computer, text=str(xtqi), master=game_box_a_a, bg='yellow', width=200, height=20)
                show_up_place(width=140, height=20, x='60', y='20')
                game_name_computer = tk.Label(text='0', master=game_box_a_a, bg='yellow', width=200, height=20)
                game_name_computer.place(width=140, height=20, x='60', y='40')
                show_up(game_name_computer, text='0', master=game_box_a_a, bg='yellow', width=200, height=20)
                show_up_place(width=140, height=20, x='60', y='40')
                game_name_computer = tk.Label(text=xt_renwu_list[0:], master=game_box_a_a, bg='yellow', width=200, height=40)
                game_name_computer.place(width=140, height=40, x='60', y='60')
                show_up(game_name_computer, text=xt_renwu_list[0:], master=game_box_a_a, bg='yellow', width=200, height=40)
                show_up_place(width=140, height=40, x='60', y='60')

                # 重置后的玩家状态结果显示（气、祥龙、人物）
                user_renwu_list = ['普通人']
                game_name_player = tk.Label(text=str(qi), master=game_box_a_b, bg='yellow', width=200, height=20)
                game_name_player.place(width=140, height=20, x='60', y='20')
                show_up(game_name_player, text=str(qi), master=game_box_a_b, bg='yellow', width=200, height=20)
                show_up_place(width=140, height=20, x='60', y='20')
                game_name_player = tk.Label(text='0', master=game_box_a_b, bg='yellow', width=200, height=20)
                game_name_player.place(width=140, height=20, x='60', y='40')
                show_up(game_name_player, text='0', master=game_box_a_b, bg='yellow', width=200, height=20)
                show_up_place(width=140, height=20, x='60', y='40')
                game_name_player = tk.Label(text=user_renwu_list[0:], master=game_box_a_b, bg='yellow', width=200, height=40)
                game_name_player.place(width=140, height=40, x='60', y='60')
                show_up(game_name_player, text=user_renwu_list[0:], master=game_box_a_b, bg='yellow', width=200, height=40)
                show_up_place(width=140, height=40, x='60', y='60')

            elif ztjv == 0:

                # 初始化玩家和系统所拥有的气以及回合
                #global hui
                #global xtqi
                #global qi
                #global renwu
                #global xiqi
                #global renwu

                # 初始化处理
                print("renwu变量处理初始化成功：" + str(renwu))
                skill_show_a = str('第' + str(jv) + '局 第' + str(hui) + '回')
                game_name_show_b = tk.Label(text=skill_show_a, master=game_box_b_show, bg='gray', width=200, height=20)
                game_name_show_b.place(width=200, height=20, x='200')
                show_up(game_name_show_b, text=skill_show_a, master=game_box_b_show, bg='gray', width=200, height=20)
                show_up_place(width=200, height=20, x='200', y='0')

                #兵宾解锁预处理
                if bbjs_xiqi == 0:

                    # 系统技能使用处理
                    print("系统技能处理前的系统人物:" + str(xt_renwu_list))
                    b = xt_renwu_list
                    xitong_skill = xt_use_skill.xt_use_skill_elementary(xtqi, hui, b)
                    print("系统技能处理后的系统人物:" + str(xt_renwu_list))

                    # 系统耗气判定
                    xtqi = qi_panding.elementary_qi_panding(xitong_skill, xtqi, xiqi)

                    # 测试代码
                    print("系统气=" + str(xtqi))

                    # 玩家耗气判定
                    qi = qi_panding.elementary_qi_panding(skill, qi, xiqi)

                    # 测试代码
                    print("玩家气=" + str(qi))

                elif bbjs_xiqi == 1:
                    pass

                else:
                    game_exit()

                #是否bbjs的分支判断
                if bbjs_xiqi == 1:
                    xitong_skill = "吸气"
                    if str(skill) != "吸气":
                        # 玩家暴死
                        zthui = 2

                        # 人物处理
                        renwu += 1
                        xt_renwu_list.append(renwu_list[renwu])

                        # 显示结果
                        skill_computer = str('系统使用了：' + str(xitong_skill))
                        game_name_show = tk.Label(text=skill_computer, master=game_box_b_show, bg='gray', width=200, height=20)
                        game_name_show.place(width=200, height=30, x='200', y='20')
                        show_up(game_name_show, text=skill_computer, master=game_box_b_show, bg='gray', width=200, height=20)
                        show_up_place(width=200, height=30, x='200', y='20')
                        skill_computer = str('你使用了：' + str(skill))
                        game_name_show = tk.Label(text=skill_computer, master=game_box_b_show, bg='gray', width=200, height=20)
                        game_name_show.place(width=200, height=30, x='200', y='50')
                        show_up(game_name_show, text=skill_computer, master=game_box_b_show, bg='gray', width=200, height=20)
                        show_up_place(width=200, height=30, x='200', y='50')
                        skill_computer = str('结果：' + "髌冰解锁后你没吸气，暴死了！")
                        game_name_show = tk.Label(text=skill_computer, master=game_box_b_show, bg='gray', width=240, height=20)
                        game_name_show.place(width=240, height=30, x='200', y='80')
                        show_up(game_name_show, ext=skill_computer, master=game_box_b_show, bg='gray', width=240, height=20)
                        show_up_place(width=240, height=30, x='200', y='80')

                        # 系统状态结果显示(气、祥龙、人物)
                        game_name_computer = tk.Label(text=str(xtqi), master=game_box_a_a, bg='yellow', width=200, height=20)
                        game_name_computer.place(width=140, height=20, x='60', y='20')
                        show_up(game_name_computer, text=str(xtqi), master=game_box_a_a, bg='yellow', width=200, height=20)
                        show_up_place(width=140, height=20, x='60', y='20')
                        game_name_computer = tk.Label(text='0', master=game_box_a_a, bg='yellow', width=200, height=20)
                        game_name_computer.place(width=140, height=20, x='60', y='40')
                        show_up(game_name_computer, text='0', master=game_box_a_a, bg='yellow', width=200, height=20)
                        show_up_place(width=140, height=20, x='60', y='40')
                        game_name_computer = tk.Label(text=xt_renwu_list[0:], master=game_box_a_a, bg='yellow', width=200, height=40)
                        game_name_computer.place(width=140, height=40, x='60', y='60')
                        show_up(game_name_computer, text='0', master=game_box_a_a, bg='yellow', width=200, height=20)
                        show_up_place(width=140, height=40, x='60', y='60')

                        # 玩家状态结果显示（气、祥龙、人物）
                        game_name_player = tk.Label(text=str(qi), master=game_box_a_b, bg='yellow', width=200, height=20)
                        game_name_player.place(width=140, height=20, x='60', y='20')
                        show_up(game_name_player, text=str(qi), master=game_box_a_b, bg='yellow', width=200, height=20)
                        show_up_place(width=140, height=20, x='60', y='20')
                        game_name_player = tk.Label(text='0', master=game_box_a_b, bg='yellow', width=200, height=20)
                        game_name_player.place(width=140, height=20, x='60', y='40')
                        show_up(game_name_player, text='0', master=game_box_a_b, bg='yellow', width=200, height=20)
                        show_up_place(width=140, height=20, x='60', y='40')
                        game_name_player = tk.Label(text=user_renwu_list[0:], master=game_box_a_b, bg='yellow', width=200, height=40)
                        game_name_player.place(width=140, height=40, x='60', y='60')
                        show_up(game_name_player, text=user_renwu_list[0:], master=game_box_a_b, bg='yellow', width=200, height=40)
                        show_up_place(width=140, height=40, x='60', y='60')

                        # 暴死后，未开始下一局游戏处理处理
                        if zthui == 2:
                            # 系统胜利
                            jv += 1
                            hui = 0
                            skill_show_a = str('第' + str(jv) + '局 第' + str(hui) + '回')
                            game_name_show_b = tk.Label(text=skill_show_a, master=game_box_b_show, bg='gray', width=200, height=20)
                            game_name_show_b.place(width=240, height=20, x='200')
                            show_up(game_name_show_b, text=skill_show_a, master=game_box_b_show, bg='gray', width=200, height=20)
                            show_up_place(width=240, height=20, x='200')
                            qi = 0
                            xtqi = 0
                            pass

                        elif zthui == 1:
                            # 玩家胜利
                            jv += 1
                            hui = 0
                            skill_show_a = str('第' + str(jv) + '局 第' + str(hui) + '回')
                            game_name_show_b = tk.Label(text=skill_show_a, master=game_box_b_show, bg='gray', width=200, height=20)
                            game_name_show_b.place(width=240, height=20, x='200')
                            show_up(game_name_show_b, text=skill_show_a, master=game_box_b_show, bg='gray', width=200, height=20)
                            show_up_place(width=240, height=20, x='200')
                            qi = 0
                            xtqi = 0
                            pass

                        elif zthui == 0:
                            print("zthui被调用，且数值为0")
                            # 无事发生
                            jv = jv
                            hui += 1
                            skill_show_a = str('第' + str(jv) + '局 第' + str(hui) + '回')
                            game_name_show_b = tk.Label(text=skill_show_a, master=game_box_b_show, bg='gray', width=200, height=20)
                            game_name_show_b.place(width=240, height=20, x='200')
                            show_up(game_name_show_b, text=skill_show_a, master=game_box_b_show, bg='gray', width=200, height=20)
                            show_up_place(width=240, height=20, x='200')
                            pass

                    elif str(skill) == "吸气":
                        # 技能判定
                        show_return, zhuangtai, bbjs_xiqi = skill_panding_player.elementary_skillpanding(skill, xitong_skill, hui)
                        print("技能判定返回测试" + show_return + zhuangtai)

                        # 系统耗气判定
                        xtqi = qi_panding.elementary_qi_panding(xitong_skill, xtqi, xiqi)

                        # 测试代码
                        print("系统气=" + str(xtqi))

                        # 玩家耗气判定
                        qi = qi_panding.elementary_qi_panding(skill, qi, xiqi)

                        # 测试代码
                        print("玩家气=" + str(qi))

                        # 判定
                        if str(zhuangtai) == "双方存活":
                            zthui = 0
                            print("1")
                        else:
                            print("出错了！" + zhuangtai)
                            sys.exit(0)

                        # 显示结果
                        skill_computer = str('系统使用了：' + str(xitong_skill))
                        game_name_show = tk.Label(text=skill_computer, master=game_box_b_show, bg='gray', width=200, height=20)
                        game_name_show.place(width=200, height=30, x='200', y='20')
                        show_up(game_name_show, text=skill_computer, master=game_box_b_show, bg='gray', width=200, height=20)
                        show_up_place(width=200, height=30, x='200', y='20')
                        skill_computer = str('你使用了：' + str(skill))
                        game_name_show = tk.Label(text=skill_computer, master=game_box_b_show, bg='gray', width=200, height=20)
                        game_name_show.place(width=200, height=30, x='200', y='50')
                        show_up(game_name_show, text=skill_computer, master=game_box_b_show, bg='gray', width=200, height=20)
                        show_up_place(width=200, height=30, x='200', y='50')
                        skill_computer = str('结果：' + str(show_return) + str(zhuangtai))
                        game_name_show = tk.Label(text=skill_computer, master=game_box_b_show, bg='gray', width=240, height=20)
                        game_name_show.place(width=240, height=30, x='200', y='80')
                        show_up(game_name_show, text=skill_computer, master=game_box_b_show, bg='gray', width=240, height=20)
                        show_up_place(width=240, height=30, x='200', y='80')

                        # 系统状态结果显示(气、祥龙、人物)
                        game_name_computer = tk.Label(text=str(xtqi), master=game_box_a_a, bg='yellow', width=200, height=20)
                        game_name_computer.place(width=140, height=20, x='60', y='20')
                        show_up(game_name_computer, text=str(xtqi), master=game_box_a_a, bg='yellow', width=200, height=20)
                        show_up_place(width=140, height=20, x='60', y='20')
                        game_name_computer = tk.Label(text='0', master=game_box_a_a, bg='yellow', width=200, height=20)
                        game_name_computer.place(width=140, height=20, x='60', y='40')
                        show_up(game_name_computer, text='0', master=game_box_a_a, bg='yellow', width=200, height=20)
                        show_up_place(width=140, height=20, x='60', y='40')
                        game_name_computer = tk.Label(text=xt_renwu_list[0:], master=game_box_a_a, bg='yellow', width=200, height=40)
                        game_name_computer.place(width=140, height=40, x='60', y='60')
                        show_up(game_name_computer, text=xt_renwu_list[0:], master=game_box_a_a, bg='yellow', width=200, height=40)
                        show_up_place(width=140, height=40, x='60', y='60')

                        # 玩家状态结果显示（气、祥龙、人物）
                        game_name_player = tk.Label(text=str(qi), master=game_box_a_b, bg='yellow', width=200, height=20)
                        game_name_player.place(width=140, height=20, x='60', y='20')
                        show_up(game_name_player, text=str(qi), master=game_box_a_b, bg='yellow', width=200, height=20)
                        show_up_place(width=140, height=20, x='60', y='20')
                        game_name_player = tk.Label(text='0', master=game_box_a_b, bg='yellow', width=200, height=20)
                        game_name_player.place(width=140, height=20, x='60', y='40')
                        show_up(game_name_player, text='0', master=game_box_a_b, bg='yellow', width=200, height=20)
                        show_up_place(width=140, height=20, x='60', y='40')
                        game_name_player = tk.Label(text=user_renwu_list[0:], master=game_box_a_b, bg='yellow', width=200, height=40)
                        game_name_player.place(width=140, height=40, x='60', y='60')
                        show_up(game_name_player, text=user_renwu_list[0:], master=game_box_a_b, bg='yellow', width=200, height=40)
                        show_up_place(width=140, height=40, x='60', y='60')

                        if zthui == 0:
                            print("zthui被调用，且数值为0")
                            # 无事发生
                            jv = jv
                            hui += 1
                            skill_show_a = str('第' + str(jv) + '局 第' + str(hui) + '回')
                            game_name_show_b = tk.Label(text=skill_show_a, master=game_box_b_show, bg='gray', width=200, height=20)
                            game_name_show_b.place(width=200, height=20, x='200')
                            show_up(game_name_show_b, text=skill_show_a, master=game_box_b_show, bg='gray', width=200, height=20)
                            show_up_place(width=200, height=20, x='200')
                        else:
                            game_exit()


                    else:
                        game_exit()
                elif bbjs_xiqi == 0:
                    if qi < 0:
                        # 玩家暴死
                        zthui = 2

                        # 人物处理
                        renwu += 1
                        xt_renwu_list.append(renwu_list[renwu])

                        # 显示结果
                        skill_computer = str('系统使用了：' + str(xitong_skill))
                        game_name_show = tk.Label(text=skill_computer, master=game_box_b_show, bg='gray', width=200, height=20)
                        game_name_show.place(width=200, height=30, x='200', y='20')
                        show_up(game_name_show, text=skill_computer, master=game_box_b_show, bg='gray', width=200, height=20)
                        show_up_place(width=200, height=30, x='200', y='20')
                        skill_computer = str('你使用了：' + str(skill))
                        game_name_show = tk.Label(text=skill_computer, master=game_box_b_show, bg='gray', width=200, height=20)
                        game_name_show.place(width=200, height=30, x='200', y='50')
                        show_up(game_name_show, text=skill_computer, master=game_box_b_show, bg='gray', width=200, height=20)
                        show_up_place(width=200, height=30, x='200', y='50')
                        skill_computer = str('结果：' + "你气不够，暴死了！")
                        game_name_show = tk.Label(text=skill_computer, master=game_box_b_show, bg='gray', width=240, height=20)
                        game_name_show.place(width=240, height=30, x='200', y='80')
                        show_up(game_name_show, text=skill_computer, master=game_box_b_show, bg='gray', width=240, height=20)
                        show_up_place(width=240, height=30, x='200', y='80')

                        # 系统状态结果显示(气、祥龙、人物)
                        game_name_computer = tk.Label(text=str(xtqi), master=game_box_a_a, bg='yellow', width=200, height=20)
                        game_name_computer.place(width=140, height=20, x='60', y='20')
                        show_up(game_name_computer, text=str(xtqi), master=game_box_a_a, bg='yellow', width=200, height=20)
                        show_up_place(width=140, height=20, x='60', y='20')
                        game_name_computer = tk.Label(text='0', master=game_box_a_a, bg='yellow', width=200, height=20)
                        game_name_computer.place(width=140, height=20, x='60', y='40')
                        show_up(game_name_computer, text='0', master=game_box_a_a, bg='yellow', width=200, height=20)
                        show_up_place(width=140, height=20, x='60', y='40')
                        game_name_computer = tk.Label(text=xt_renwu_list[0:], master=game_box_a_a, bg='yellow', width=200, height=40)
                        game_name_computer.place(width=140, height=40, x='60', y='60')
                        show_up(game_name_computer, text=xt_renwu_list[0:], master=game_box_a_a, bg='yellow', width=200, height=40)
                        show_up_place(width=140, height=40, x='60', y='60')

                        # 玩家状态结果显示（气、祥龙、人物）
                        game_name_player = tk.Label(text=str(qi), master=game_box_a_b, bg='yellow', width=200, height=20)
                        game_name_player.place(width=140, height=20, x='60', y='20')
                        show_up(game_name_player, text=str(qi), master=game_box_a_b, bg='yellow', width=200, height=20)
                        show_up_place(width=140, height=20, x='60', y='20')
                        game_name_player = tk.Label(text='0', master=game_box_a_b, bg='yellow', width=200, height=20)
                        game_name_player.place(width=140, height=20, x='60', y='40')
                        show_up(game_name_player, text='0', master=game_box_a_b, bg='yellow', width=200, height=20)
                        show_up_place(width=140, height=20, x='60', y='40')
                        game_name_player = tk.Label(text=user_renwu_list[0:], master=game_box_a_b, bg='yellow', width=200, height=40)
                        game_name_player.place(width=140, height=40, x='60', y='60')
                        show_up(game_name_player, text=user_renwu_list[0:], master=game_box_a_b, bg='yellow', width=200, height=40)
                        show_up_place(idth=140, height=40, x='60', y='60')

                        # time.sleep(2)

                    elif qi >= 0:
                        # 游戏继续
                        # 判定你用的技能是否属于你
                        a = skill_panding_player.elementary_renwu_skillpanding(skill)
                        if a in user_renwu_list:
                            # 技能判定
                            show_return, zhuangtai, bbjs_xiqi = skill_panding_player.elementary_skillpanding(skill, xitong_skill, hui)
                            print("技能判定返回测试" + show_return + zhuangtai)

                            # 测试代码
                            print(zhuangtai)

                            # 判定
                            if str(zhuangtai) == "对方胜利":
                                zthui = 2
                                # 人物处理
                                renwu += 1
                                xt_renwu_list.append(renwu_list[renwu])

                            elif str(zhuangtai) == "你胜利了":
                                zthui = 1
                                # 人物处理
                                renwu += 1
                                user_renwu_list.append(renwu_list[renwu])

                            elif str(zhuangtai) == "双方存活":
                                zthui = 0
                                print("1")
                            else:
                                print("出错了！" + zhuangtai)
                                sys.exit(0)

                            # 显示结果
                            skill_computer = str('系统使用了：' + str(xitong_skill))
                            game_name_show = tk.Label(text=skill_computer, master=game_box_b_show, bg='gray', width=200, height=20)
                            game_name_show.place(width=200, height=30, x='200', y='20')
                            show_up(game_name_show, text=skill_computer, master=game_box_b_show, bg='gray', width=200, height=20)
                            show_up_place(width=200, height=30, x='200', y='20')
                            skill_computer = str('你使用了：' + str(skill))
                            game_name_show = tk.Label(text=skill_computer, master=game_box_b_show, bg='gray', width=200, height=20)
                            game_name_show.place(width=200, height=30, x='200', y='50')
                            show_up(game_name_show, text=skill_computer, master=game_box_b_show, bg='gray', width=200, height=20)
                            show_up_place(width=200, height=30, x='200', y='50')
                            skill_computer = str('结果：' + str(show_return) + str(zhuangtai))
                            game_name_show = tk.Label(text=skill_computer, master=game_box_b_show, bg='gray', width=240, height=20)
                            game_name_show.place(width=240, height=30, x='200', y='80')
                            show_up(game_name_show, text=skill_computer, master=game_box_b_show, bg='gray', width=240, height=20)
                            show_up_place(width=240, height=30, x='200', y='80')

                            # 系统状态结果显示(气、祥龙、人物)
                            game_name_computer = tk.Label(text=str(xtqi), master=game_box_a_a, bg='yellow', width=200, height=20)
                            game_name_computer.place(width=140, height=20, x='60', y='20')
                            show_up(game_name_computer, text=str(xtqi), master=game_box_a_a, bg='yellow', width=200, height=20)
                            show_up_place(width=140, height=20, x='60', y='20')
                            game_name_computer = tk.Label(text='0', master=game_box_a_a, bg='yellow', width=200, height=20)
                            game_name_computer.place(width=140, height=20, x='60', y='40')
                            show_up(game_name_computer, text='0', master=game_box_a_a, bg='yellow', width=200, height=20)
                            show_up_place(width=140, height=20, x='60', y='40')
                            game_name_computer = tk.Label(text=xt_renwu_list[0:], master=game_box_a_a, bg='yellow', width=200, height=40)
                            game_name_computer.place(width=140, height=40, x='60', y='60')
                            show_up(game_name_computer, text=xt_renwu_list[0:], master=game_box_a_a, bg='yellow', width=200, height=40)
                            show_up_place(width=140, height=40, x='60', y='60')

                            # 玩家状态结果显示（气、祥龙、人物）
                            game_name_player = tk.Label(text=str(qi), master=game_box_a_b, bg='yellow', width=200, height=20)
                            game_name_player.place(width=140, height=20, x='60', y='20')
                            show_up(game_name_player, text=str(qi), master=game_box_a_b, bg='yellow', width=200, height=20)
                            show_up_place(width=140, height=20, x='60', y='20')
                            game_name_player = tk.Label(text='0', master=game_box_a_b, bg='yellow', width=200, height=20)
                            game_name_player.place(width=140, height=20, x='60', y='40')
                            show_up(game_name_player, text='0', master=game_box_a_b, bg='yellow', width=200, height=20)
                            show_up_place(width=140, height=20, x='60', y='40')
                            game_name_player = tk.Label(text=user_renwu_list[0:], master=game_box_a_b, bg='yellow', width=200, height=40)
                            game_name_player.place(width=140, height=40, x='60', y='60')
                            show_up(game_name_player, text=user_renwu_list[0:], master=game_box_a_b, bg='yellow', width=200, height=40)
                            show_up_place(width=140, height=40, x='60', y='60')

                            # 延时（？
                            # time.sleep(2)


                        else:
                            zthui = 2

                            # 人物处理
                            renwu += 1
                            xt_renwu_list.append(renwu_list[renwu])

                            # 显示结果
                            skill_computer = str('系统使用了：' + str(xitong_skill))
                            game_name_show = tk.Label(text=skill_computer, master=game_box_b_show, bg='gray', width=200, height=20)
                            game_name_show.place(width=200, height=30, x='200', y='20')
                            show_up(skill_computer, text=skill_computer, master=game_box_b_show, bg='gray', width=200, height=20)
                            show_up_place(width=200, height=30, x='200', y='20')
                            skill_computer = str('你使用了：' + str(skill))
                            game_name_show = tk.Label(text=skill_computer, master=game_box_b_show, bg='gray', width=200, height=20)
                            game_name_show.place(width=200, height=30, x='200', y='50')
                            show_up(skill_computer, text=skill_computer, master=game_box_b_show, bg='gray', width=200, height=20)
                            show_up_place(width=200, height=30, x='200', y='50')
                            skill_computer = str('结果：' + "你使用了你没有的技能！你暴死了！")
                            game_name_show = tk.Label(text=skill_computer, master=game_box_b_show, bg='gray', width=240, height=20)
                            game_name_show.place(width=240, height=30, x='200', y='80')
                            show_up(skill_computer, text=skill_computer, master=game_box_b_show, bg='gray', width=240, height=20)
                            show_up_place(width=240, height=30, x='200', y='80')

                            # 系统状态结果显示(气、祥龙、人物)
                            game_name_computer = tk.Label(text=str(xtqi), master=game_box_a_a, bg='yellow', width=200, height=20)
                            game_name_computer.place(width=140, height=20, x='60', y='20')
                            show_up(game_name_computer, text=str(xtqi), master=game_box_a_a, bg='yellow', width=200, height=20)
                            show_up_place(width=140, height=20, x='60', y='20')
                            game_name_computer = tk.Label(text='0', master=game_box_a_a, bg='yellow', width=200, height=20)
                            game_name_computer.place(width=140, height=20, x='60', y='40')
                            show_up(game_name_computer, text='0', master=game_box_a_a, bg='yellow', width=200, height=20)
                            show_up_place(width=140, height=20, x='60', y='40')
                            game_name_computer = tk.Label(text=xt_renwu_list[0:], master=game_box_a_a, bg='yellow', width=200, height=40)
                            game_name_computer.place(width=140, height=40, x='60', y='60')
                            show_up(game_name_computer, text=xt_renwu_list[0:], master=game_box_a_a, bg='yellow', width=200, height=40)
                            show_up_place(width=140, height=40, x='60', y='60')

                            # 玩家状态结果显示（气、祥龙、人物）
                            game_name_player = tk.Label(text=str(qi), master=game_box_a_b, bg='yellow', width=200, height=20)
                            game_name_player.place(width=140, height=20, x='60', y='20')
                            show_up(game_name_player, text=str(qi), master=game_box_a_b, bg='yellow', width=200, height=20)
                            show_up_place(width=140, height=20, x='60', y='20')
                            game_name_player = tk.Label(text='0', master=game_box_a_b, bg='yellow', width=200, height=20)
                            game_name_player.place(width=140, height=20, x='60', y='40')
                            show_up(game_name_player, text='0', master=game_box_a_b, bg='yellow', width=200, height=20)
                            show_up_place(width=140, height=20, x='60', y='40')
                            game_name_player = tk.Label(text=user_renwu_list[0:], master=game_box_a_b, bg='yellow', width=200, height=40)
                            game_name_player.place(width=140, height=40, x='60', y='60')
                            show_up(game_name_player, text=user_renwu_list[0:], master=game_box_a_b, bg='yellow', width=200, height=40)
                            show_up_place(width=140, height=40, x='60', y='60')

                            # time.sleep(2)

                    else:
                        print("理论上这里不可能出错啊...")

                    if zthui == 2:
                        # 系统胜利
                        jv += 1
                        hui = 0
                        skill_show_a = str('第' + str(jv) + '局 第' + str(hui) + '回')
                        game_name_show_b = tk.Label(text=skill_show_a, master=game_box_b_show, bg='gray', width=200, height=20)
                        game_name_show_b.place(width=200, height=20, x='200')
                        show_up(game_name_show_b, text=skill_show_a, master=game_box_b_show, bg='gray', width=200, height=20)
                        show_up_place(width=200, height=20, x='200', y='0')
                        qi = 0
                        xtqi = 0
                        pass

                    elif zthui == 1:
                        # 玩家胜利
                        jv += 1
                        hui = 0
                        skill_show_a = str('第' + str(jv) + '局 第' + str(hui) + '回')
                        game_name_show_b = tk.Label(text=skill_show_a, master=game_box_b_show, bg='gray', width=200, height=20)
                        game_name_show_b.place(width=200, height=20, x='200')
                        show_up(game_name_show_b, text=skill_show_a, master=game_box_b_show, bg='gray', width=200, height=20)
                        show_up_place(width=200, height=20, x='200', y='0')
                        qi = 0
                        xtqi = 0
                        pass

                    elif zthui == 0:
                        print("zthui被调用，且数值为0")
                        # 无事发生
                        jv = jv
                        hui += 1
                        skill_show_a = str('第' + str(jv) + '局 第' + str(hui) + '回')
                        game_name_show_b = tk.Label(text=skill_show_a, master=game_box_b_show, bg='gray', width=200, height=20)
                        game_name_show_b.place(width=200, height=20, x='200')
                        show_up(game_name_show_b, text=skill_show_a, master=game_box_b_show, bg='gray', width=200, height=20)
                        show_up_place(width=200, height=20, x='200', y='0')
                        pass

                    else:
                        game_exit()
                else:
                    game_exit()
            else:
                game_exit()



        # 技能处理===========================
        # 普通人技能跳转
        def human_skill_a():
            elementary_main_play('挡')
            pass

        def human_skill_b():
            elementary_main_play('穿山甲')
            pass

        def human_skill_c():
            elementary_main_play('绵绵')
            pass

        def human_skill_d():
            elementary_main_play('金遁')
            pass

        def human_skill_e():
            elementary_main_play('木遁')
            pass

        def human_skill_f():
            elementary_main_play('水遁')
            pass

        def human_skill_g():
            elementary_main_play('火遁')
            pass

        def human_skill_h():
            elementary_main_play('土遁')
            pass

        def human_skill_i():
            elementary_main_play('钻地土遁')
            pass

        def human_skill_j():
            elementary_main_play('髌冰解锁')
            pass

        def human_skill_k():
            elementary_main_play('吸气')
            pass

        # 风技能跳转
        def feng_skill_a():
            elementary_main_play('风挡')
            pass

        def feng_skill_b():
            elementary_main_play('电风扇')
            pass

        def feng_skill_c():
            elementary_main_play('低级风波')
            pass

        def feng_skill_d():
            elementary_main_play('高级风波')
            pass

        def feng_skill_e():
            elementary_main_play('龙卷风')
            pass

        def feng_skill_f():
            elementary_main_play('低级风神下凡')
            pass

        def feng_skill_g():
            elementary_main_play('高级风神下凡')
            pass

        # 雨技能跳转
        def yv_skill_a():
            elementary_main_play('雨挡')
            pass

        def yv_skill_b():
            elementary_main_play('低级流星雨')
            pass

        def yv_skill_c():
            elementary_main_play('高级流星雨')
            pass

        def yv_skill_d():
            elementary_main_play('及时雨')
            pass

        def yv_skill_e():
            elementary_main_play('黑时雨')
            pass

        def yv_skill_f():
            elementary_main_play('低级雨神下凡')
            pass

        def yv_skill_g():
            elementary_main_play('高级雨神下凡')
            pass

        # 雷技能跳转
        def lei_skill_a():
            elementary_main_play('雷挡')
            pass

        def lei_skill_b():
            elementary_main_play('雷击')
            pass

        def lei_skill_c():
            elementary_main_play('雷暴')
            pass

        def lei_skill_d():
            elementary_main_play('低级五雷轰顶')
            pass

        def lei_skill_e():
            elementary_main_play('高级五雷轰顶')
            pass

        def lei_skill_f():
            elementary_main_play('低级雷神下凡')
            pass

        def lei_skill_g():
            elementary_main_play('高级雷神下凡')
            pass

        # 电技能跳转
        def dian_skill_a():
            elementary_main_play('电挡')
            pass

        def dian_skill_b():
            elementary_main_play('放电')
            pass

        def dian_skill_c():
            elementary_main_play('双重放电')
            pass

        def dian_skill_d():
            elementary_main_play('电网')
            pass

        def dian_skill_e():
            elementary_main_play('电神下凡')
            pass

        # 火技能跳转
        def huo_skill_a():
            elementary_main_play('火挡')
            pass

        def huo_skill_b():
            elementary_main_play('小火圈')
            pass

        def huo_skill_c():
            elementary_main_play('大火圈')
            pass

        def huo_skill_d():
            elementary_main_play('火神下凡')
            pass

        # 效果发生控件==

        global xt_renwu_list
        global user_renwu_list

        # 状态容器

        game_name_computer = tk.Label(text='系统状态', master=game_box_a_a, width=200, height=20)
        game_name_computer.place(width=200, height=20, y='0')
        game_name_computer = tk.Label(text='气：', master=game_box_a_a, bg='yellow', width=200, height=20)
        game_name_computer.place(width=60, height=20, y='20')
        game_name_computer = tk.Label(text='0', master=game_box_a_a, bg='yellow', width=200, height=20)
        game_name_computer.place(width=140, height=20, x='60', y='20')
        game_name_computer = tk.Label(text='祥龙：', master=game_box_a_a, bg='yellow', width=200, height=20)
        game_name_computer.place(width=60, height=20, y='40')
        game_name_computer = tk.Label(text='0', master=game_box_a_a, bg='yellow', width=200, height=20)
        game_name_computer.place(width=140, height=20, x='60', y='40')
        game_name_computer = tk.Label(text='人物：', master=game_box_a_a, bg='yellow', width=200, height=40)
        game_name_computer.place(width=60, height=40, y='60')
        xt_renwu_list = ["普通人"]
        game_name_computer = tk.Label(text=xt_renwu_list[0:], master=game_box_a_a, bg='yellow', width=200, height=40)
        game_name_computer.place(width=140, height=40, x='60', y='60')

        game_name_player = tk.Label(text='玩家状态', master=game_box_a_b, width=200, height=20)
        game_name_player.place(width=200, height=20, y='0')
        game_name_player = tk.Label(text='气：', master=game_box_a_b, bg='yellow', width=200, height=20)
        game_name_player.place(width=60, height=20, y='20')
        game_name_player = tk.Label(text='0', master=game_box_a_b, bg='yellow', width=200, height=20)
        game_name_player.place(width=140, height=20, x='60', y='20')
        game_name_player = tk.Label(text='祥龙：', master=game_box_a_b, bg='yellow', width=200, height=20)
        game_name_player.place(width=60, height=20, y='40')
        game_name_player = tk.Label(text='0', master=game_box_a_b, bg='yellow', width=200, height=20)
        game_name_player.place(width=140, height=20, x='60', y='40')
        game_name_player = tk.Label(text='人物：', master=game_box_a_b, bg='yellow', width=200, height=40)
        game_name_player.place(width=60, height=40, y='60')
        user_renwu_list = ["普通人"]
        game_name_player = tk.Label(text=user_renwu_list[0:], master=game_box_a_b, bg='yellow', width=200, height=40)
        game_name_player.place(width=140, height=40, x='60', y='60')

        skill_show = str('第' + str(jv) + '局 第' + str(hui) + '回')
        game_name_show = tk.Label(text=skill_show, master=game_box_b_show, bg='gray', width=200, height=20)
        game_name_show.place(width=200, height=20, x='200')
        xitong_skill = ''
        skill_computer = str('系统使用了：' + str(xitong_skill))
        game_name_show = tk.Label(text=skill_computer, master=game_box_b_show, bg='gray', width=200, height=20)
        game_name_show.place(width=200, height=30, x='200', y='20')
        skill = ''
        skill_computer = str('你使用了：' + str(skill))
        game_name_show = tk.Label(text=skill_computer, master=game_box_b_show, bg='gray', width=200, height=20)
        game_name_show.place(width=200, height=30, x='200', y='50')
        show_return = ""
        zhuangtai = ""
        skill_computer = str('结果：' + str(show_return) + str(zhuangtai))
        game_name_show = tk.Label(text=skill_computer, master=game_box_b_show, bg='gray', width=200, height=20)
        game_name_show.place(width=240, height=30, x='200', y='80')

        # 普融人技能放置x=200,y=200
        game_name_show = tk.Label(text='普通人技能', master=game_box_b_skill_humanskill, width=200, height=20)
        game_name_show.place(width=200, height=20)
        game_name_show_human_skill_return = tk.Button(text='挡', master=game_box_b_skill_humanskill, width=10, height=10, command=human_skill_a)
        game_name_show_human_skill_return.place(width=40, height=60, x='0', y='20')
        game_name_show_human_skill_return = tk.Button(text='穿山甲', master=game_box_b_skill_humanskill, width=10, height=10, command=human_skill_b)
        game_name_show_human_skill_return.place(width=40, height=60, x='40', y='20')
        game_name_show_human_skill_return = tk.Button(text='绵绵', master=game_box_b_skill_humanskill, width=10, height=10, command=human_skill_c)
        game_name_show_human_skill_return.place(width=40, height=60, x='80', y='20')
        game_name_show_human_skill_return = tk.Button(text='金遁', master=game_box_b_skill_humanskill, width=10, height=10, command=human_skill_d)
        game_name_show_human_skill_return.place(width=40, height=60, x='120', y='20')
        game_name_show_human_skill_return = tk.Button(text='木遁', master=game_box_b_skill_humanskill, width=10, height=10, command=human_skill_e)
        game_name_show_human_skill_return.place(width=40, height=60, x='160', y='20')
        game_name_show_human_skill_return = tk.Button(text='水遁', master=game_box_b_skill_humanskill, width=10, height=10, command=human_skill_f)
        game_name_show_human_skill_return.place(width=40, height=60, x='0', y='80')
        game_name_show_human_skill_return = tk.Button(text='火遁', master=game_box_b_skill_humanskill, width=10, height=10, command=human_skill_g)
        game_name_show_human_skill_return.place(width=40, height=60, x='40', y='80')
        game_name_show_human_skill_return = tk.Button(text='土遁', master=game_box_b_skill_humanskill, width=10, height=10, command=human_skill_h)
        game_name_show_human_skill_return.place(width=40, height=60, x='80', y='80')
        game_name_show_human_skill_return = tk.Button(text='钻地\n土遁', master=game_box_b_skill_humanskill, width=10, height=10, command=human_skill_i)
        game_name_show_human_skill_return.place(width=40, height=60, x='120', y='80')
        game_name_show_human_skill_return = tk.Button(text='髌冰\n解锁', master=game_box_b_skill_humanskill, width=10, height=10, command=human_skill_j)
        game_name_show_human_skill_return.place(width=40, height=60, x='160', y='80')
        game_name_show_human_skill_return = tk.Button(text='吸气', master=game_box_b_skill_humanskill, width=10, height=10, command=human_skill_k)
        game_name_show_human_skill_return.place(width=200, height=60, x='0', y='140')

        # 风技能放置x=200,y=200
        game_name_show_feng_skill_return = tk.Label(text='风的技能', master=game_box_b_skill_fengskill, bg='LightYellow')
        game_name_show_feng_skill_return.place(width=200, height=20)
        game_name_show_feng_skill_return = tk.Button(text='风挡', master=game_box_b_skill_fengskill, bg='LightYellow', command=feng_skill_a)
        game_name_show_feng_skill_return.place(width=40, height=60, x=0, y=20)
        game_name_show_feng_skill_return = tk.Button(text='电风扇', master=game_box_b_skill_fengskill, bg='LightYellow', command=feng_skill_b)
        game_name_show_feng_skill_return.place(width=40, height=60, x=40, y=20)
        game_name_show_feng_skill_return = tk.Button(text='低级\n风波', master=game_box_b_skill_fengskill, bg='LightYellow', command=feng_skill_c)
        game_name_show_feng_skill_return.place(width=40, height=60, x=80, y=20)
        game_name_show_feng_skill_return = tk.Button(text='高级\n风波', master=game_box_b_skill_fengskill, bg='LightYellow', command=feng_skill_d)
        game_name_show_feng_skill_return.place(width=40, height=60, x=120, y=20)
        game_name_show_feng_skill_return = tk.Button(text='龙卷风', master=game_box_b_skill_fengskill, bg='LightYellow', command=feng_skill_e)
        game_name_show_feng_skill_return.place(width=40, height=60, x=160, y=20)
        game_name_show_feng_skill_return = tk.Button(text='低级风神下凡', master=game_box_b_skill_fengskill, bg='LightYellow', command=feng_skill_f)
        game_name_show_feng_skill_return.place(width=100, height=60, x=0, y=80)
        game_name_show_feng_skill_return = tk.Button(text='高级风神下凡', master=game_box_b_skill_fengskill, bg='LightYellow', command=feng_skill_g)
        game_name_show_feng_skill_return.place(width=100, height=60, x=100, y=80)

        # 雨的技能放置x=200,y=200
        game_name_show_yv_skill_return = tk.Label(text='雨的技能', master=game_box_b_skill_yvskill, bg='DeepSkyBlue')
        game_name_show_yv_skill_return.place(width=200, height=20)
        game_name_show_yv_skill_return = tk.Button(text='雨挡', master=game_box_b_skill_yvskill, bg='DeepSkyBlue', command=yv_skill_a)
        game_name_show_yv_skill_return.place(width=40, height=60, x=0, y=20)
        game_name_show_yv_skill_return = tk.Button(text='低级\n流星雨', master=game_box_b_skill_yvskill, bg='DeepSkyBlue', command=yv_skill_b)
        game_name_show_yv_skill_return.place(width=40, height=60, x=40, y=20)
        game_name_show_yv_skill_return = tk.Button(text='高级\n流星雨', master=game_box_b_skill_yvskill, bg='DeepSkyBlue', command=yv_skill_c)
        game_name_show_yv_skill_return.place(width=40, height=60, x=80, y=20)
        game_name_show_yv_skill_return = tk.Button(text='及时雨', master=game_box_b_skill_yvskill, bg='DeepSkyBlue', command=yv_skill_d)
        game_name_show_yv_skill_return.place(width=40, height=60, x=120, y=20)
        game_name_show_yv_skill_return = tk.Button(text='黑时雨', master=game_box_b_skill_yvskill, bg='DeepSkyBlue', command=yv_skill_e)
        game_name_show_yv_skill_return.place(width=40, height=60, x=160, y=20)
        game_name_show_yv_skill_return = tk.Button(text='低级雨神下凡', master=game_box_b_skill_yvskill, bg='DeepSkyBlue', command=yv_skill_f)
        game_name_show_yv_skill_return.place(width=100, height=60, x=0, y=80)
        game_name_show_yv_skill_return = tk.Button(text='高级雨神下凡', master=game_box_b_skill_yvskill, bg='DeepSkyBlue', command=yv_skill_g)
        game_name_show_yv_skill_return.place(width=100, height=60, x=100, y=80)

        # 雷的技能放置x=200,y=200
        game_name_show_lei_skill_return = tk.Label(text='雷的技能', master=game_box_b_skill_leiskill, bg='SlateBlue')
        game_name_show_lei_skill_return.place(width=200, height=20)
        game_name_show_lei_skill_return = tk.Button(text='雷挡', master=game_box_b_skill_leiskill, bg='SlateBlue', command=lei_skill_a)
        game_name_show_lei_skill_return.place(width=40, height=60, x=0, y=20)
        game_name_show_lei_skill_return = tk.Button(text='雷击', master=game_box_b_skill_leiskill, bg='SlateBlue', command=lei_skill_b)
        game_name_show_lei_skill_return.place(width=40, height=60, x=40, y=20)
        game_name_show_lei_skill_return = tk.Button(text='雷暴', master=game_box_b_skill_leiskill, bg='SlateBlue', command=lei_skill_c)
        game_name_show_lei_skill_return.place(width=40, height=60, x=80, y=20)
        game_name_show_lei_skill_return = tk.Button(text='低级\n五雷\n轰顶', master=game_box_b_skill_leiskill, bg='SlateBlue', command=lei_skill_d)
        game_name_show_lei_skill_return.place(width=40, height=60, x=120, y=20)
        game_name_show_lei_skill_return = tk.Button(text='高级\n五雷\n轰顶', master=game_box_b_skill_leiskill, bg='SlateBlue', command=lei_skill_e)
        game_name_show_lei_skill_return.place(width=40, height=60, x=160, y=20)
        game_name_show_lei_skill_return = tk.Button(text='低级\n雷神下凡', master=game_box_b_skill_leiskill, bg='SlateBlue', command=lei_skill_f)
        game_name_show_lei_skill_return.place(width=100, height=60, x=0, y=80)
        game_name_show_lei_skill_return = tk.Button(text='高级\n雷神下凡', master=game_box_b_skill_leiskill, bg='SlateBlue', command=lei_skill_g)
        game_name_show_lei_skill_return.place(width=100, height=60, x=100, y=80)

        # 电的技能放置x=200,y=200
        game_name_show_dian_skill_return = tk.Label(text='电的技能', master=game_box_b_skill_dianskill, bg='LightSteelBlue')
        game_name_show_dian_skill_return.place(width=200, height=20)
        game_name_show_dian_skill_return = tk.Button(text='电挡', master=game_box_b_skill_dianskill, bg='LightSteelBlue', command=dian_skill_a)
        game_name_show_dian_skill_return.place(width=50, height=60, x=0, y=20)
        game_name_show_dian_skill_return = tk.Button(text='放电', master=game_box_b_skill_dianskill, bg='LightSteelBlue', command=dian_skill_b)
        game_name_show_dian_skill_return.place(width=50, height=60, x=50, y=20)
        game_name_show_dian_skill_return = tk.Button(text='双重放电', master=game_box_b_skill_dianskill, bg='LightSteelBlue', command=dian_skill_c)
        game_name_show_dian_skill_return.place(width=50, height=60, x=100, y=20)
        game_name_show_dian_skill_return = tk.Button(text='电网', master=game_box_b_skill_dianskill, bg='LightSteelBlue', command=dian_skill_d)
        game_name_show_dian_skill_return.place(width=50, height=60, x=150, y=20)
        game_name_show_dian_skill_return = tk.Button(text='电神下凡', master=game_box_b_skill_dianskill, bg='LightSteelBlue', command=dian_skill_e)
        game_name_show_dian_skill_return.place(width=200, height=60, x=0, y=80)

        # 火的技能放置x=200,y=200
        game_name_show_huo_skill_return = tk.Label(text='火的技能', master=game_box_b_skill_huoskill, bg='OrangeRed')
        game_name_show_huo_skill_return.place(width=200, height=20)
        game_name_show_huo_skill_return = tk.Button(text='火挡', master=game_box_b_skill_huoskill, bg='OrangeRed', command=huo_skill_a)
        game_name_show_huo_skill_return.place(width=100, height=60, x=0, y=20)
        game_name_show_huo_skill_return = tk.Button(text='小火圈', master=game_box_b_skill_huoskill, bg='OrangeRed', command=huo_skill_b)
        game_name_show_huo_skill_return.place(width=100, height=60, x=100, y=20)
        game_name_show_huo_skill_return = tk.Button(text='大火圈', master=game_box_b_skill_huoskill, bg='OrangeRed', command=huo_skill_c)
        game_name_show_huo_skill_return.place(width=100, height=60, x=0, y=80)
        game_name_show_huo_skill_return = tk.Button(text='火神下凡', master=game_box_b_skill_huoskill, bg='OrangeRed', command=huo_skill_d)
        game_name_show_huo_skill_return.place(width=100, height=60, x=100, y=80)

        # 右侧栏容器
        global image_egg


        image_egg = tk.PhotoImage(file=photo_egg)
        game_box_b_skill_image_egg = tk.Label(master=game_box_b, image=image_egg)
        game_box_b_skill_image_egg.place(x=600, y=0)
        game_exit = tk.Button(text='退出游戏', master=game_box_b, command=game_exit)
        game_exit.place(width=100, height=40, x=600, y=560)
        # 彩蛋容器
        game_egg = tk.Label(text='这似乎是个小彩蛋（？', master=game_box_c)
        game_egg.pack(side='top')
        def game_egg_a():
            global qi
            qi += 100
            game_name_player = tk.Label(text=str(qi), master=game_box_a_b, bg='yellow', width=200, height=20)
            game_name_player.place(width=140, height=20, x='60', y='20')
        game_egg = tk.Button(text='无视回合自己获得100口气', master=game_box_c, command=game_egg_a)
        game_egg.pack(side='bottom')
        def game_egg_b():
            global xtqi
            xtqi += 100
            game_name_computer = tk.Label(text=str(xtqi), master=game_box_a_a, bg='yellow', width=200, height=20)
            game_name_computer.place(width=140, height=20, x='60', y='20')
        game_egg = tk.Button(text='无视回合对方获得100口气', master=game_box_c, command=game_egg_b)
        game_egg.pack(side='bottom')

        pass

    # 开始界面组件设置
    star_a_a = tk.Label(text='请熟悉游戏规则，如果已经熟知，点击开始')
    star_a_a.pack(side='top', padx='0.c', pady='1.c')
    star_b_a = tk.Button(text='开始游戏', command=elementary_game)
    star_b_a.pack(side='left', padx='2.c', pady='4.c')
    star_b_b = tk.Button(text='查看规则', command=elementary_rule)
    star_b_b.pack(side='right', padx='2.c', pady='4.c')
    star_b_c = tk.Button(text='退出游戏', command=elementary_exit)
    star_b_c.pack(side='bottom', padx='0.c', pady='1.c')

    window_elementary_main.mainloop()
    pass

# =======================================分割线=====================================
# 初级模式游戏运行主体

# =======================================分割线=====================================
# 游戏运行流程
def More_more_Clap():
    while True:

        # 测试代码
        print('游戏流程开始运行')

        # 窗口初始化
        MMC_A = tk.Tk()
        MMC_A.title('哆哆吸')
        MMC_A.geometry('800x600')
        txt_save.write('MMC_A窗口初始化成功')

        # 函数调用处理
        def MMC_end():
            txt_save.close()
            sys.exit(0)

        def MMC_star():
            # 结束MMC窗口进入另外一个窗口
            MMC_A.update()
            MMC_A.destroy()

            # 窗口初始化
            MMC_B = tk.Tk()
            MMC_B.title("哆哆吸")
            MMC_B.geometry('800x600')
            txt_save.write('MMC_B窗口初始化成功')

            # 函数调用处理

            def MMC_qixuanzhe_a():
                global MODE
                MODE = "普通人模式"
                MMC_qixuanzhe()
                pass

            def MMC_qixuanzhe_b():
                global MODE
                MODE = "初级模式"
                MMC_qixuanzhe()
                pass

            def MMC_qixuanzhe_c():
                global MODE
                MODE = "高级模式"
                MMC_qixuanzhe()
                pass

            def MMC_qixuanzhe_d():
                global MODE
                MODE = "完全模式"
                MMC_qixuanzhe()
                pass

            def MMC_qixuanzhe_e():
                global MODE
                MODE = "无尽模式"
                MMC_qixuanzhe()
                pass

            def MMC_qixuanzhe_f():
                global MODE
                MODE = "？？？"
                MMC_qixuanzhe()
                pass

            def MMC_qixuanzhe():

                # 结束上一个窗口
                MMC_B.update()
                MMC_B.destroy()

                # 初始化变量
                global MODE
                MODE = str(MODE)

                # 窗口初始化
                MMC_C = tk.Tk()
                MMC_C.title("哆哆吸")
                MMC_C.geometry('800x600')
                txt_save.write('MMC_C窗口初始化成功')

                # 函数调用处理

                def MMC_playerqueding_a():
                    global xiqi
                    xiqi = 1
                    MMC_playerqueding()
                    pass

                def MMC_playerqueding_b():
                    global xiqi
                    xiqi = 3
                    MMC_playerqueding()
                    pass

                def MMC_playerqueding_c():
                    global xiqi
                    xiqi = 5
                    MMC_playerqueding()
                    pass

                def MMC_playerqueding_d():
                    global xiqi
                    xiqi = 10
                    MMC_playerqueding()
                    pass

                def MMC_playerqueding_e():
                    global MMC_c_b_witer
                    global xiqi
                    xiqi = int(MMC_c_b_witer.get())
                    MMC_playerqueding()
                    pass

                def MMC_playerqueding():

                    # 结束上一个窗口
                    MMC_C.update()
                    MMC_C.destroy()

                    # 初始化使用变量
                    global xiqi
                    global MODE
                    xiqi = xiqi
                    MODE = MODE

                    # 窗口初始化
                    MMC_D = tk.Tk()
                    MMC_D.title("哆哆吸")
                    MMC_D.geometry('800x600')
                    txt_save.write('MMC_D窗口初始化成功')

                    # 函数调用处理
                    def MMC_D_a():

                        # 结束上一个窗口
                        MMC_D.update()
                        MMC_D.destroy()

                        # 初始化使用变量
                        global MODE

                        # 开始判断模式
                        if MODE == '普通人模式':
                            txt_save.write('普通人模式')
                            main()
                        elif MODE == '初级模式':
                            txt_save.write('初级模式')
                            elementary_main()
                        elif MODE == '高级模式':
                            # 其他模式还没写.jpg
                            pass
                        elif MODE == '完全模式':
                            # 其他模式还没写.jpg
                            pass
                        elif MODE == '无尽模式':
                            # 其他模式还没写.jpg
                            pass
                        elif MODE == '???':
                            # 其他模式还没写.jpg
                            pass

                    def MMC_D_b():
                        pass

                    def MMC_D_c():
                        txt_save.close()
                        sys.exit(0)

                    # 图片处理
                    pass

                    # 组件初始化

                    text__a = '你选着的模式是' + str(MODE) + '\n你选着一次吸' + str(xiqi) + '口气'

                    MMC_d_a_a = tk.Label(master=MMC_D, text=text__a)
                    MMC_d_a_a.pack(side='top', padx='0.c', pady='1.c')
                    MMC_d_b_a = tk.Button(master=MMC_D, text='确定开始游戏', command=MMC_D_a)
                    MMC_d_b_a.pack(side='bottom', padx='0.c', pady='1.c')
                    MMC_d_b_b = tk.Button(master=MMC_D, text='重新选着', command=MMC_D_b)
                    MMC_d_b_b.pack(side='bottom', padx='0.c', pady='1.c')
                    MMC_d_b_c = tk.Button(master=MMC_D, text='退出游戏', command=MMC_D_c)
                    MMC_d_b_c.pack(side='bottom', padx='0.c', pady='1.c')

                    MMC_D.mainloop()

                # 图片处理
                pass

                # 组件初始化
                global MMC_c_b_witer
                MMC_c_b_witer = 0
                MMC_c_a_a = tk.Label(master=MMC_C, text='请选择一次吸几口气？')
                MMC_c_a_a.pack(side='top', padx='0.c', pady='1.c')
                # MMC_c_a_b = tk.Label(master=MMC_C, image=SCP_XT_011, width=600, height=500)
                # MMC_c_a_b.pack()
                MMC_c_b_witer = tk.Entry(master=MMC_C, text='请输入您打算一次吸多少口气')
                MMC_c_b_witer.pack(side='top', padx='0.c', pady='1.c')
                MMC_c_b_a = tk.Button(master=MMC_C, text='一口气', command=MMC_playerqueding_a)
                MMC_c_b_a.pack(side='left', padx='1.c', pady='1.c')
                MMC_c_b_a = tk.Button(master=MMC_C, text='三口气（常用.jpg）', command=MMC_playerqueding_b)
                MMC_c_b_a.pack(side='left', padx='1.c', pady='1.c')
                MMC_c_b_a = tk.Button(master=MMC_C, text='五口气', command=MMC_playerqueding_c)
                MMC_c_b_a.pack(side='left', padx='1.c', pady='1.c')
                MMC_c_b_a = tk.Button(master=MMC_C, text='十口气', command=MMC_playerqueding_d)
                MMC_c_b_a.pack(side='left', padx='0.c', pady='1.c')
                MMC_c_b_a = tk.Button(master=MMC_C, text='确认使用你输入的一次吸气量', command=MMC_playerqueding_e)
                MMC_c_b_a.pack(side='left', padx='1.c', pady='1.c')

                MMC_C.mainloop()

            # 图片处理
            pass

            # 组件初始化
            MMC_b_a_a = tk.Label(master=MMC_B, text='请选择游戏模式')
            MMC_b_a_a.pack(side='top', padx='0.c', pady='1.c')
            # MMC_b_a_b = tk.Label(master=MMC_B, image=SCP_XT_011, width=600, height=500)
            # MMC_b_a_b.pack()
            MMC_b_b_a = tk.Button(master=MMC_B, text='普通人模式', command=MMC_qixuanzhe_a)
            MMC_b_b_a.pack(side='left', padx='1.c', pady='1.c')
            MMC_b_b_a = tk.Button(master=MMC_B, text='初级模式', command=MMC_qixuanzhe_b)
            MMC_b_b_a.pack(side='left', padx='1.c', pady='1.c')
            MMC_b_b_a = tk.Button(master=MMC_B, text='高级模式', command=MMC_qixuanzhe_c)
            MMC_b_b_a.pack(side='left', padx='1.c', pady='1.c')
            MMC_b_b_a = tk.Button(master=MMC_B, text='完全模式', command=MMC_qixuanzhe_d)
            MMC_b_b_a.pack(side='left', padx='1.c', pady='1.c')
            MMC_b_b_a = tk.Button(master=MMC_B, text='无尽模式', command=MMC_qixuanzhe_e)
            MMC_b_b_a.pack(side='left', padx='1.c', pady='1.c')
            MMC_b_b_a = tk.Button(master=MMC_B, text='敬请期待', command=MMC_qixuanzhe_f)
            MMC_b_b_a.pack(side='left', padx='0.c', pady='1.c')

            MMC_B.mainloop()

        # 图片处理
        # SCP_XT_011 = Image.open("SCP-XT-011.png")

        # 组件初始化
        MMC_a_a_a = tk.Label(master=MMC_A, text='欢迎进入游戏：哆哆吸')
        MMC_a_a_a.pack(side='top', padx='0.c', pady='1.c')
        # MMC_a_a_b = tk.Label(master=MMC_A ,image=SCP_XT_011, width=600, height=500)
        # MMC_a_a_b.pack()
        MMC_a_b = tk.Button(master=MMC_A, text='开始游戏', command=MMC_star)
        MMC_a_b.pack(side='left', padx='4.c', pady='1.c')
        MMC_a_c = tk.Button(master=MMC_A, text='关闭游戏', command=MMC_end)
        MMC_a_c.pack(side='left', padx='5.c', pady='1.c')

        MMC_A.mainloop()


if __name__ == '__main__':
    More_more_Clap()
