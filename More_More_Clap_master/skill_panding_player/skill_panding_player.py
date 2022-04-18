"""
################################
普通人模式技能判定
################################
"""
import sys


def skillpanding(skill, xitongjileng):
    # 测试代码
    print('成功启动模块"技能判定"')

    # 初始化
    skillpanduanreturn_1 = '你防住了对方的攻击！'
    skillpanduanreturn_2 = '对方防住了你的攻击！'
    skillpanduanreturn_3 = '你没防住对方的攻击！'
    skillpanduanreturn_4 = '对方没防住你的攻击！'
    skillpanduanreturn_5 = '无事发生.jpg'
    skillpandingreturn_a = '双方存活'
    skillpandingreturn_b = '玩家胜利'
    skillpandingreturn_c = '系统胜利'

    # 初始化要用到的全局变量

    global skillpanduanreturn
    global skillpanduanreturn_number
    skillpanduanreturn = ''
    skillpanduanreturn_number = ''

    if skill == '挡':
        if xitongjileng == '挡':
            skillpanduanreturn = skillpandingreturn_a
            skillpanduanreturn_number = skillpanduanreturn_5
            different_a = 'None'
            return skillpanduanreturn, skillpanduanreturn_number, different_a
        elif xitongjileng == '穿山甲':
            skillpanduanreturn = skillpandingreturn_a
            skillpanduanreturn_number = skillpanduanreturn_5
            different_a = 'None'
            return skillpanduanreturn, skillpanduanreturn_number, different_a
        elif xitongjileng == '绵绵':
            skillpanduanreturn = skillpandingreturn_a
            skillpanduanreturn_number = skillpanduanreturn_5
            different_a = 'None'
            return skillpanduanreturn, skillpanduanreturn_number, different_a
        elif xitongjileng == '金遁':
            skillpanduanreturn = skillpandingreturn_a
            skillpanduanreturn_number = skillpanduanreturn_1
            different_a = 'None'
            return skillpanduanreturn, skillpanduanreturn_number, different_a
        elif xitongjileng == '木遁':
            skillpanduanreturn = skillpandingreturn_a
            skillpanduanreturn_number = skillpanduanreturn_1
            different_a = 'None'
            return skillpanduanreturn, skillpanduanreturn_number, different_a
        elif xitongjileng == '水遁':
            skillpanduanreturn = skillpandingreturn_c
            skillpanduanreturn_number = skillpanduanreturn_3
            different_a = 'None'
            return skillpanduanreturn, skillpanduanreturn_number, different_a
        elif xitongjileng == '火遁':
            skillpanduanreturn = skillpandingreturn_c
            skillpanduanreturn_number = skillpanduanreturn_3
            different_a = 'None'
            return skillpanduanreturn, skillpanduanreturn_number, different_a
        elif xitongjileng == '土遁':
            skillpanduanreturn = skillpandingreturn_c
            skillpanduanreturn_number = skillpanduanreturn_3
            different_a = 'None'
            return skillpanduanreturn, skillpanduanreturn_number, different_a
        elif xitongjileng == '钻地土遁':
            skillpanduanreturn = skillpandingreturn_a
            skillpanduanreturn_number = skillpanduanreturn_5
            different_a = 'None'
            return skillpanduanreturn, skillpanduanreturn_number, different_a
        elif xitongjileng == '髌冰解锁':
            skillpanduanreturn = skillpandingreturn_a
            skillpanduanreturn_number = skillpanduanreturn_5
            different_a = 'None'
            return skillpanduanreturn, skillpanduanreturn_number, different_a
        elif xitongjileng == '吸气':
            skillpanduanreturn = skillpandingreturn_a
            skillpanduanreturn_number = skillpanduanreturn_5
            different_a = 'None'
            return skillpanduanreturn, skillpanduanreturn_number, different_a
        else:
            print('你特么干了啥？？？')
            pass
    elif skill == '穿山甲':
        if xitongjileng == '挡':
            skillpanduanreturn = skillpandingreturn_a
            skillpanduanreturn_number = skillpanduanreturn_5
            different_a = 'None'
            return skillpanduanreturn, skillpanduanreturn_number, different_a
        elif xitongjileng == '穿山甲':
            skillpanduanreturn = skillpandingreturn_a
            skillpanduanreturn_number = skillpanduanreturn_5
            different_a = 'None'
            return skillpanduanreturn, skillpanduanreturn_number, different_a
        elif xitongjileng == '绵绵':
            skillpanduanreturn = skillpandingreturn_a
            skillpanduanreturn_number = skillpanduanreturn_5
            different_a = 'None'
            return skillpanduanreturn, skillpanduanreturn_number, different_a
        elif xitongjileng == '金遁':
            skillpanduanreturn = skillpandingreturn_a
            skillpanduanreturn_number = skillpanduanreturn_1
            different_a = 'None'
            return skillpanduanreturn, skillpanduanreturn_number, different_a
        elif xitongjileng == '木遁':
            skillpanduanreturn = skillpandingreturn_a
            skillpanduanreturn_number = skillpanduanreturn_1
            different_a = 'None'
            return skillpanduanreturn, skillpanduanreturn_number, different_a
        elif xitongjileng == '水遁':
            skillpanduanreturn = skillpandingreturn_a
            skillpanduanreturn_number = skillpanduanreturn_2
            different_a = 'None'
            return skillpanduanreturn, skillpanduanreturn_number, different_a
        elif xitongjileng == '火遁':
            skillpanduanreturn = skillpandingreturn_a
            skillpanduanreturn_number = skillpanduanreturn_2
            different_a = 'None'
            return skillpanduanreturn, skillpanduanreturn_number, different_a
        elif xitongjileng == '土遁':
            skillpanduanreturn = skillpandingreturn_c
            skillpanduanreturn_number = skillpanduanreturn_3
            different_a = 'None'
            return skillpanduanreturn, skillpanduanreturn_number, different_a
        elif xitongjileng == '钻地土遁':
            skillpanduanreturn = skillpandingreturn_a
            skillpanduanreturn_number = skillpanduanreturn_5
            different_a = 'None'
            return skillpanduanreturn, skillpanduanreturn_number, different_a
        elif xitongjileng == '髌冰解锁':
            skillpanduanreturn = skillpandingreturn_a
            skillpanduanreturn_number = skillpanduanreturn_5
            different_a = 'None'
            return skillpanduanreturn, skillpanduanreturn_number, different_a
        elif xitongjileng == '吸气':
            skillpanduanreturn = skillpandingreturn_a
            skillpanduanreturn_number = skillpanduanreturn_5
            different_a = 'None'
            return skillpanduanreturn, skillpanduanreturn_number, different_a
        else:
            print('你特么干了啥？？？')
            pass
    elif skill == '绵绵':
        if xitongjileng == '挡':
            skillpanduanreturn = skillpandingreturn_a
            skillpanduanreturn_number = skillpanduanreturn_5
            different_a = 'None'
            return skillpanduanreturn, skillpanduanreturn_number, different_a
        elif xitongjileng == '穿山甲':
            skillpanduanreturn = skillpandingreturn_a
            skillpanduanreturn_number = skillpanduanreturn_5
            different_a = 'None'
            return skillpanduanreturn, skillpanduanreturn_number, different_a
        elif xitongjileng == '绵绵':
            skillpanduanreturn = skillpandingreturn_a
            skillpanduanreturn_number = skillpanduanreturn_5
            different_a = 'None'
            return skillpanduanreturn, skillpanduanreturn_number, different_a
        elif xitongjileng == '金遁':
            skillpanduanreturn = skillpandingreturn_a
            skillpanduanreturn_number = skillpanduanreturn_1
            different_a = 'None'
            return skillpanduanreturn, skillpanduanreturn_number, different_a
        elif xitongjileng == '木遁':
            skillpanduanreturn = skillpandingreturn_a
            skillpanduanreturn_number = skillpanduanreturn_1
            different_a = 'None'
            return skillpanduanreturn, skillpanduanreturn_number, different_a
        elif xitongjileng == '水遁':
            skillpanduanreturn = skillpandingreturn_a
            skillpanduanreturn_number = skillpanduanreturn_1
            different_a = 'None'
            return skillpanduanreturn, skillpanduanreturn_number, different_a
        elif xitongjileng == '火遁':
            skillpanduanreturn = skillpandingreturn_c
            skillpanduanreturn_number = skillpanduanreturn_3
            different_a = 'None'
            return skillpanduanreturn, skillpanduanreturn_number, different_a
        elif xitongjileng == '土遁':
            skillpanduanreturn = skillpandingreturn_a
            skillpanduanreturn_number = skillpanduanreturn_1
            different_a = 'None'
            return skillpanduanreturn, skillpanduanreturn_number, different_a
        elif xitongjileng == '钻地土遁':
            skillpanduanreturn = skillpandingreturn_a
            skillpanduanreturn_number = skillpanduanreturn_5
            different_a = 'None'
            return skillpanduanreturn, skillpanduanreturn_number, different_a
        elif xitongjileng == '髌冰解锁':
            skillpanduanreturn = skillpandingreturn_a
            skillpanduanreturn_number = skillpanduanreturn_5
            different_a = 'None'
            return skillpanduanreturn, skillpanduanreturn_number, different_a
        elif xitongjileng == '吸气':
            skillpanduanreturn = skillpandingreturn_a
            skillpanduanreturn_number = skillpanduanreturn_5
            different_a = 'None'
            return skillpanduanreturn, skillpanduanreturn_number, different_a
        else:
            print('你特么干了啥？？？')
            pass
    elif skill == '金遁':
        if xitongjileng == '挡':
            skillpanduanreturn = skillpandingreturn_a
            skillpanduanreturn_number = skillpanduanreturn_2
            different_a = 'None'
            return skillpanduanreturn, skillpanduanreturn_number, different_a
        elif xitongjileng == '穿山甲':
            skillpanduanreturn = skillpandingreturn_a
            skillpanduanreturn_number = skillpanduanreturn_2
            different_a = 'None'
            return skillpanduanreturn, skillpanduanreturn_number, different_a
        elif xitongjileng == '绵绵':
            skillpanduanreturn = skillpandingreturn_a
            skillpanduanreturn_number = skillpanduanreturn_2
            different_a = 'None'
            return skillpanduanreturn, skillpanduanreturn_number, different_a
        elif xitongjileng == '金遁':
            skillpanduanreturn = skillpandingreturn_a
            skillpanduanreturn_number = skillpanduanreturn_5
            different_a = 'None'
            return skillpanduanreturn, skillpanduanreturn_number, different_a
        elif xitongjileng == '木遁':
            skillpanduanreturn = skillpandingreturn_a
            skillpanduanreturn_number = skillpanduanreturn_5
            different_a = 'None'
            return skillpanduanreturn, skillpanduanreturn_number, different_a
        elif xitongjileng == '水遁':
            skillpanduanreturn = skillpandingreturn_c
            skillpanduanreturn_number = skillpanduanreturn_3
            different_a = 'None'
            return skillpanduanreturn, skillpanduanreturn_number, different_a
        elif xitongjileng == '火遁':
            skillpanduanreturn = skillpandingreturn_c
            skillpanduanreturn_number = skillpanduanreturn_3
            different_a = 'None'
            return skillpanduanreturn, skillpanduanreturn_number, different_a
        elif xitongjileng == '土遁':
            skillpanduanreturn = skillpandingreturn_c
            skillpanduanreturn_number = skillpanduanreturn_3
            different_a = 'None'
            return skillpanduanreturn, skillpanduanreturn_number, different_a
        elif xitongjileng == '钻地土遁':
            skillpanduanreturn = skillpandingreturn_a
            skillpanduanreturn_number = skillpanduanreturn_5
            different_a = 'None'
            return skillpanduanreturn, skillpanduanreturn_number, different_a
        elif xitongjileng == '髌冰解锁':
            skillpanduanreturn = skillpandingreturn_a
            skillpanduanreturn_number = skillpanduanreturn_2
            different_a = 'a'
            return skillpanduanreturn, skillpanduanreturn_number, different_a
        elif xitongjileng == '吸气':
            skillpanduanreturn = skillpandingreturn_b
            skillpanduanreturn_number = skillpanduanreturn_4
            different_a = 'None'
            return skillpanduanreturn, skillpanduanreturn_number, different_a
        else:
            print('你特么干了啥？？？')
            pass
    elif skill == '木遁':
        if xitongjileng == '挡':
            skillpanduanreturn = skillpandingreturn_a
            skillpanduanreturn_number = skillpanduanreturn_2
            different_a = 'None'
            return skillpanduanreturn, skillpanduanreturn_number, different_a
        elif xitongjileng == '穿山甲':
            skillpanduanreturn = skillpandingreturn_a
            skillpanduanreturn_number = skillpanduanreturn_2
            different_a = 'None'
            return skillpanduanreturn, skillpanduanreturn_number, different_a
        elif xitongjileng == '绵绵':
            skillpanduanreturn = skillpandingreturn_a
            skillpanduanreturn_number = skillpanduanreturn_2
            different_a = 'None'
            return skillpanduanreturn, skillpanduanreturn_number, different_a
        elif xitongjileng == '金遁':
            skillpanduanreturn = skillpandingreturn_a
            skillpanduanreturn_number = skillpanduanreturn_5
            different_a = 'None'
            return skillpanduanreturn, skillpanduanreturn_number, different_a
        elif xitongjileng == '木遁':
            skillpanduanreturn = skillpandingreturn_a
            skillpanduanreturn_number = skillpanduanreturn_5
            different_a = 'None'
            return skillpanduanreturn, skillpanduanreturn_number, different_a
        elif xitongjileng == '水遁':
            skillpanduanreturn = skillpandingreturn_c
            skillpanduanreturn_number = skillpanduanreturn_3
            different_a = 'None'
            return skillpanduanreturn, skillpanduanreturn_number, different_a
        elif xitongjileng == '火遁':
            skillpanduanreturn = skillpandingreturn_c
            skillpanduanreturn_number = skillpanduanreturn_3
            different_a = 'None'
            return skillpanduanreturn, skillpanduanreturn_number, different_a
        elif xitongjileng == '土遁':
            skillpanduanreturn = skillpandingreturn_c
            skillpanduanreturn_number = skillpanduanreturn_3
            different_a = 'None'
            return skillpanduanreturn, skillpanduanreturn_number, different_a
        elif xitongjileng == '钻地土遁':
            skillpanduanreturn = skillpandingreturn_a
            skillpanduanreturn_number = skillpanduanreturn_5
            different_a = 'None'
            return skillpanduanreturn, skillpanduanreturn_number, different_a
        elif xitongjileng == '髌冰解锁':
            skillpanduanreturn = skillpandingreturn_a
            skillpanduanreturn_number = skillpanduanreturn_2
            different_a = 'a'
            return skillpanduanreturn, skillpanduanreturn_number, different_a
        elif xitongjileng == '吸气':
            skillpanduanreturn = skillpandingreturn_b
            skillpanduanreturn_number = skillpanduanreturn_4
            different_a = 'None'
            return skillpanduanreturn, skillpanduanreturn_number, different_a
        else:
            print('你特么干了啥？？？')
            pass
    elif skill == '水遁':
        if xitongjileng == '挡':
            skillpanduanreturn = skillpandingreturn_b
            skillpanduanreturn_number = skillpanduanreturn_4
            different_a = 'None'
            return skillpanduanreturn, skillpanduanreturn_number, different_a
        elif xitongjileng == '穿山甲':
            skillpanduanreturn = skillpandingreturn_a
            skillpanduanreturn_number = skillpanduanreturn_5
            different_a = 'None'
            return skillpanduanreturn, skillpanduanreturn_number, different_a
        elif xitongjileng == '绵绵':
            skillpanduanreturn = skillpandingreturn_a
            skillpanduanreturn_number = skillpanduanreturn_5
            different_a = 'None'
            return skillpanduanreturn, skillpanduanreturn_number, different_a
        elif xitongjileng == '金遁':
            skillpanduanreturn = skillpandingreturn_b
            skillpanduanreturn_number = skillpanduanreturn_4
            different_a = 'None'
            return skillpanduanreturn, skillpanduanreturn_number, different_a
        elif xitongjileng == '木遁':
            skillpanduanreturn = skillpandingreturn_b
            skillpanduanreturn_number = skillpanduanreturn_4
            different_a = 'None'
            return skillpanduanreturn, skillpanduanreturn_number, different_a
        elif xitongjileng == '水遁':
            skillpanduanreturn = skillpandingreturn_a
            skillpanduanreturn_number = skillpanduanreturn_5
            different_a = 'None'
            return skillpanduanreturn, skillpanduanreturn_number, different_a
        elif xitongjileng == '火遁':
            skillpanduanreturn = skillpandingreturn_c
            skillpanduanreturn_number = skillpanduanreturn_3
            different_a = 'None'
            return skillpanduanreturn, skillpanduanreturn_number, different_a
        elif xitongjileng == '土遁':
            skillpanduanreturn = skillpandingreturn_c
            skillpanduanreturn_number = skillpanduanreturn_3
            different_a = 'None'
            return skillpanduanreturn, skillpanduanreturn_number, different_a
        elif xitongjileng == '钻地土遁':
            skillpanduanreturn = skillpandingreturn_a
            skillpanduanreturn_number = skillpanduanreturn_5
            different_a = 'None'
            return skillpanduanreturn, skillpanduanreturn_number, different_a
        elif xitongjileng == '髌冰解锁':
            skillpanduanreturn = skillpandingreturn_b
            skillpanduanreturn_number = skillpanduanreturn_4
            different_a = 'None'
            return skillpanduanreturn, skillpanduanreturn_number, different_a
        elif xitongjileng == '吸气':
            skillpanduanreturn = skillpandingreturn_b
            skillpanduanreturn_number = skillpanduanreturn_4
            different_a = 'None'
            return skillpanduanreturn, skillpanduanreturn_number, different_a
        else:
            print('你特么干了啥？？？')
            pass
    elif skill == '火遁':
        if xitongjileng == '挡':
            skillpanduanreturn = skillpandingreturn_b
            skillpanduanreturn_number = skillpanduanreturn_4
            different_a = 'None'
            return skillpanduanreturn, skillpanduanreturn_number, different_a
        elif xitongjileng == '穿山甲':
            skillpanduanreturn = skillpandingreturn_a
            skillpanduanreturn_number = skillpanduanreturn_5
            different_a = 'None'
            return skillpanduanreturn, skillpanduanreturn_number, different_a
        elif xitongjileng == '绵绵':
            skillpanduanreturn = skillpandingreturn_b
            skillpanduanreturn_number = skillpanduanreturn_4
            different_a = 'None'
            return skillpanduanreturn, skillpanduanreturn_number, different_a
        elif xitongjileng == '金遁':
            skillpanduanreturn = skillpandingreturn_b
            skillpanduanreturn_number = skillpanduanreturn_4
            different_a = 'None'
            return skillpanduanreturn, skillpanduanreturn_number, different_a
        elif xitongjileng == '木遁':
            skillpanduanreturn = skillpandingreturn_b
            skillpanduanreturn_number = skillpanduanreturn_4
            different_a = 'None'
            return skillpanduanreturn, skillpanduanreturn_number, different_a
        elif xitongjileng == '水遁':
            skillpanduanreturn = skillpandingreturn_b
            skillpanduanreturn_number = skillpanduanreturn_4
            different_a = 'None'
            return skillpanduanreturn, skillpanduanreturn_number, different_a
        elif xitongjileng == '火遁':
            skillpanduanreturn = skillpandingreturn_a
            skillpanduanreturn_number = skillpanduanreturn_5
            different_a = 'None'
            return skillpanduanreturn, skillpanduanreturn_number, different_a
        elif xitongjileng == '土遁':
            skillpanduanreturn = skillpandingreturn_c
            skillpanduanreturn_number = skillpanduanreturn_3
            different_a = 'None'
            return skillpanduanreturn, skillpanduanreturn_number, different_a
        elif xitongjileng == '钻地土遁':
            skillpanduanreturn = skillpandingreturn_a
            skillpanduanreturn_number = skillpanduanreturn_5
            different_a = 'None'
            return skillpanduanreturn, skillpanduanreturn_number, different_a
        elif xitongjileng == '髌冰解锁':
            skillpanduanreturn = skillpandingreturn_a
            skillpanduanreturn_number = skillpanduanreturn_5
            different_a = 'None'
            return skillpanduanreturn, skillpanduanreturn_number, different_a
        elif xitongjileng == '吸气':
            skillpanduanreturn = skillpandingreturn_b
            skillpanduanreturn_number = skillpanduanreturn_4
            different_a = 'None'
            return skillpanduanreturn, skillpanduanreturn_number, different_a
        else:
            print('你特么干了啥？？？')
            pass
    elif skill == '土遁':
        if xitongjileng == '挡':
            skillpanduanreturn = skillpandingreturn_b
            skillpanduanreturn_number = skillpanduanreturn_4
            different_a = 'None'
            return skillpanduanreturn, skillpanduanreturn_number, different_a
        elif xitongjileng == '穿山甲':
            skillpanduanreturn = skillpandingreturn_b
            skillpanduanreturn_number = skillpanduanreturn_4
            different_a = 'None'
            return skillpanduanreturn, skillpanduanreturn_number, different_a
        elif xitongjileng == '绵绵':
            skillpanduanreturn = skillpandingreturn_a
            skillpanduanreturn_number = skillpanduanreturn_5
            different_a = 'None'
            return skillpanduanreturn, skillpanduanreturn_number, different_a
        elif xitongjileng == '金遁':
            skillpanduanreturn = skillpandingreturn_b
            skillpanduanreturn_number = skillpanduanreturn_4
            different_a = 'None'
            return skillpanduanreturn, skillpanduanreturn_number, different_a
        elif xitongjileng == '木遁':
            skillpanduanreturn = skillpandingreturn_b
            skillpanduanreturn_number = skillpanduanreturn_4
            different_a = 'None'
            return skillpanduanreturn, skillpanduanreturn_number, different_a
        elif xitongjileng == '水遁':
            skillpanduanreturn = skillpandingreturn_b
            skillpanduanreturn_number = skillpanduanreturn_4
            different_a = 'None'
            return skillpanduanreturn, skillpanduanreturn_number, different_a
        elif xitongjileng == '火遁':
            skillpanduanreturn = skillpandingreturn_b
            skillpanduanreturn_number = skillpanduanreturn_4
            different_a = 'None'
            return skillpanduanreturn, skillpanduanreturn_number, different_a
        elif xitongjileng == '土遁':
            skillpanduanreturn = skillpandingreturn_a
            skillpanduanreturn_number = skillpanduanreturn_5
            different_a = 'None'
            return skillpanduanreturn, skillpanduanreturn_number, different_a
        elif xitongjileng == '钻地土遁':
            skillpanduanreturn = skillpandingreturn_b
            skillpanduanreturn_number = skillpanduanreturn_4
            different_a = 'None'
            return skillpanduanreturn, skillpanduanreturn_number, different_a
        elif xitongjileng == '髌冰解锁':
            skillpanduanreturn = skillpandingreturn_b
            skillpanduanreturn_number = skillpanduanreturn_4
            different_a = 'None'
            return skillpanduanreturn, skillpanduanreturn_number, different_a
        elif xitongjileng == '吸气':
            skillpanduanreturn = skillpandingreturn_b
            skillpanduanreturn_number = skillpanduanreturn_4
            different_a = 'None'
            return skillpanduanreturn, skillpanduanreturn_number, different_a
        else:
            print('你特么干了啥？？？')
            pass
    elif skill == '钻地土遁':
        if xitongjileng == '挡':
            skillpanduanreturn = skillpandingreturn_a
            skillpanduanreturn_number = skillpanduanreturn_5
            different_a = 'None'
            return skillpanduanreturn, skillpanduanreturn_number, different_a
        elif xitongjileng == '穿山甲':
            skillpanduanreturn = skillpandingreturn_b
            skillpanduanreturn_number = skillpanduanreturn_4
            different_a = 'None'
            return skillpanduanreturn, skillpanduanreturn_number, different_a
        elif xitongjileng == '绵绵':
            skillpanduanreturn = skillpandingreturn_a
            skillpanduanreturn_number = skillpanduanreturn_5
            different_a = 'None'
            return skillpanduanreturn, skillpanduanreturn_number, different_a
        elif xitongjileng == '金遁':
            skillpanduanreturn = skillpandingreturn_a
            skillpanduanreturn_number = skillpanduanreturn_5
            different_a = 'None'
            return skillpanduanreturn, skillpanduanreturn_number, different_a
        elif xitongjileng == '木遁':
            skillpanduanreturn = skillpandingreturn_a
            skillpanduanreturn_number = skillpanduanreturn_5
            different_a = 'None'
            return skillpanduanreturn, skillpanduanreturn_number, different_a
        elif xitongjileng == '水遁':
            skillpanduanreturn = skillpandingreturn_a
            skillpanduanreturn_number = skillpanduanreturn_5
            different_a = 'None'
            return skillpanduanreturn, skillpanduanreturn_number, different_a
        elif xitongjileng == '火遁':
            skillpanduanreturn = skillpandingreturn_a
            skillpanduanreturn_number = skillpanduanreturn_5
            different_a = 'None'
            return skillpanduanreturn, skillpanduanreturn_number, different_a
        elif xitongjileng == '土遁':
            skillpanduanreturn = skillpandingreturn_c
            skillpanduanreturn_number = skillpanduanreturn_3
            different_a = 'None'
            return skillpanduanreturn, skillpanduanreturn_number, different_a
        elif xitongjileng == '钻地土遁':
            skillpanduanreturn = skillpandingreturn_a
            skillpanduanreturn_number = skillpanduanreturn_5
            different_a = 'None'
            return skillpanduanreturn, skillpanduanreturn_number, different_a
        elif xitongjileng == '髌冰解锁':
            skillpanduanreturn = skillpandingreturn_a
            skillpanduanreturn_number = skillpanduanreturn_5
            different_a = 'None'
            return skillpanduanreturn, skillpanduanreturn_number, different_a
        elif xitongjileng == '吸气':
            skillpanduanreturn = skillpandingreturn_a
            skillpanduanreturn_number = skillpanduanreturn_5
            different_a = 'None'
            return skillpanduanreturn, skillpanduanreturn_number, different_a
        else:
            print('你特么干了啥？？？')
            pass
    elif skill == '髌冰解锁':
        if xitongjileng == '挡':
            skillpanduanreturn = skillpandingreturn_a
            skillpanduanreturn_number = skillpanduanreturn_5
            different_a = 'None'
            return skillpanduanreturn, skillpanduanreturn_number, different_a
        elif xitongjileng == '穿山甲':
            skillpanduanreturn = skillpandingreturn_a
            skillpanduanreturn_number = skillpanduanreturn_5
            different_a = 'None'
            return skillpanduanreturn, skillpanduanreturn_number, different_a
        elif xitongjileng == '绵绵':
            skillpanduanreturn = skillpandingreturn_a
            skillpanduanreturn_number = skillpanduanreturn_5
            different_a = 'None'
            return skillpanduanreturn, skillpanduanreturn_number, different_a
        elif xitongjileng == '金遁':
            skillpanduanreturn = skillpandingreturn_a
            skillpanduanreturn_number = skillpanduanreturn_5
            different_a = 'a'
            return skillpanduanreturn, skillpanduanreturn_number, different_a
        elif xitongjileng == '木遁':
            skillpanduanreturn = skillpandingreturn_a
            skillpanduanreturn_number = skillpanduanreturn_5
            different_a = 'a'
            return skillpanduanreturn, skillpanduanreturn_number, different_a
        elif xitongjileng == '水遁':
            skillpanduanreturn = skillpandingreturn_c
            skillpanduanreturn_number = skillpanduanreturn_3
            different_a = 'None'
            return skillpanduanreturn, skillpanduanreturn_number, different_a
        elif xitongjileng == '火遁':
            skillpanduanreturn = skillpandingreturn_c
            skillpanduanreturn_number = skillpanduanreturn_3
            different_a = 'None'
            return skillpanduanreturn, skillpanduanreturn_number, different_a
        elif xitongjileng == '土遁':
            skillpanduanreturn = skillpandingreturn_c
            skillpanduanreturn_number = skillpanduanreturn_3
            different_a = 'None'
            return skillpanduanreturn, skillpanduanreturn_number, different_a
        elif xitongjileng == '钻地土遁':
            skillpanduanreturn = skillpandingreturn_a
            skillpanduanreturn_number = skillpanduanreturn_5
            different_a = 'None'
            return skillpanduanreturn, skillpanduanreturn_number, different_a
        elif xitongjileng == '髌冰解锁':
            skillpanduanreturn = skillpandingreturn_a
            skillpanduanreturn_number = skillpanduanreturn_5
            different_a = 'None'
            return skillpanduanreturn, skillpanduanreturn_number, different_a
        elif xitongjileng == '吸气':
            skillpanduanreturn = skillpandingreturn_a
            skillpanduanreturn_number = skillpanduanreturn_5
            different_a = 'None'
            return skillpanduanreturn, skillpanduanreturn_number, different_a
        else:
            print("髌冰解锁技能出了bug")
            print('你特么干了啥？？？')
            pass
    elif skill == '吸气':
        if xitongjileng == '挡':
            skillpanduanreturn = skillpandingreturn_a
            skillpanduanreturn_number = skillpanduanreturn_5
            different_a = 'None'
            return skillpanduanreturn, skillpanduanreturn_number, different_a
        elif xitongjileng == '穿山甲':
            skillpanduanreturn = skillpandingreturn_a
            skillpanduanreturn_number = skillpanduanreturn_5
            different_a = 'None'
            return skillpanduanreturn, skillpanduanreturn_number, different_a
        elif xitongjileng == '绵绵':
            skillpanduanreturn = skillpandingreturn_a
            skillpanduanreturn_number = skillpanduanreturn_5
            different_a = 'None'
            return skillpanduanreturn, skillpanduanreturn_number, different_a
        elif xitongjileng == '金遁':
            skillpanduanreturn = skillpandingreturn_c
            skillpanduanreturn_number = skillpanduanreturn_3
            different_a = 'None'
            return skillpanduanreturn, skillpanduanreturn_number, different_a
        elif xitongjileng == '木遁':
            skillpanduanreturn = skillpandingreturn_c
            skillpanduanreturn_number = skillpanduanreturn_3
            different_a = 'None'
            return skillpanduanreturn, skillpanduanreturn_number, different_a
        elif xitongjileng == '水遁':
            skillpanduanreturn = skillpandingreturn_c
            skillpanduanreturn_number = skillpanduanreturn_3
            different_a = 'None'
            return skillpanduanreturn, skillpanduanreturn_number, different_a
        elif xitongjileng == '火遁':
            skillpanduanreturn = skillpandingreturn_c
            skillpanduanreturn_number = skillpanduanreturn_3
            different_a = 'None'
            return skillpanduanreturn, skillpanduanreturn_number, different_a
        elif xitongjileng == '土遁':
            skillpanduanreturn = skillpandingreturn_c
            skillpanduanreturn_number = skillpanduanreturn_3
            different_a = 'None'
            return skillpanduanreturn, skillpanduanreturn_number, different_a
        elif xitongjileng == '钻地土遁':
            skillpanduanreturn = skillpandingreturn_a
            skillpanduanreturn_number = skillpanduanreturn_5
            different_a = 'None'
            return skillpanduanreturn, skillpanduanreturn_number, different_a
        elif xitongjileng == '髌冰解锁':
            skillpanduanreturn = skillpandingreturn_a
            skillpanduanreturn_number = skillpanduanreturn_5
            different_a = 'None'
            return skillpanduanreturn, skillpanduanreturn_number, different_a
        elif xitongjileng == '吸气':
            skillpanduanreturn = skillpandingreturn_a
            skillpanduanreturn_number = skillpanduanreturn_5
            different_a = 'None'
            return skillpanduanreturn, skillpanduanreturn_number, different_a
        else:
            print('你特么干了啥？？？')
            pass
    else:
        print('你特么的干了啥？？？')
        sys.exit(0)
        pass
    pass


def skillpanding_a(skill, xitongjilen):
    # 测试代码
    print('成功启动模块"技能判定-特殊a"')

    # 初始化
    skillpanduanreturn_5 = '无事发生.jpg'
    skillpandingreturn_a = '双方存活'
    skillpandingreturn_c = '系统胜利'

    # 初始化要用到的全局变量

    global skillpanduanreturn
    global skillpanduanreturn_number
    skillpanduanreturn = ''
    skillpanduanreturn_number = ''

    if skill == '吸气':
        if xitongjilen == '吸气':
            skillpanduanreturn = skillpandingreturn_a
            skillpanduanreturn_number = skillpanduanreturn_5
            return skillpanduanreturn, skillpanduanreturn_number
        else:
            print('出bug拉！')
            pass
    else:
        if xitongjilen == '吸气':
            skillpanduanreturn = skillpandingreturn_c
            skillpanduanreturn_number = "你暴死了！"
            return skillpanduanreturn, skillpanduanreturn_number
        else:
            print('出bug拉！')
            pass


"""
################################
初级模式技能判定
################################
"""


def elementary_skillpanding(user_skill, xitong_skill, hui):

    #测试代码
    print("初级技能判定运行成功")
    print(hui)

    #初始化
    global bbjs_xiqi
    #bbjs_xiqi如果等于0，下回合不用吸气，如果等于1就表示用了召唤技能，下回合要吸气。
    bbjs_xiqi = 0

    #初级模式技能DSKI定数
    elementary_commonHuman_D = \
        {
            # 普通人
            # 防御
            '挡': -10, '穿山甲': -1000, '绵绵': -1000, '钻地土遁': -1000,
            # 风
            '风挡': -30,
            # 雨
            '雨挡': -31,
            # 雷
            '雷挡': -31, '雷击': -96,
            # 电
            '电挡': -36,
            # 火
            '火挡': -40,
        }

    elementary_commonHuman_S = \
        {
            # 普通人
            # 攻击
            '金遁': 10, '木遁': 12, '水遁': 30, '火遁': 50, '土遁': 80,
            # 风
            '电风扇': 10, '低级风波': 12, '高级风波': 20, '龙卷风': 32, '低级风神下凡': 40, '高级风神下凡': 50,
            # 雨
            '低级流星雨': 20, '高级流星雨': 30, '及时雨': 38, '黑时雨': 50, '低级雨神下凡': 47, '高级雨神下凡': 80,
            # 雷
            '雷暴': 30, '低级五雷轰顶': 41, '高级五雷轰顶': 50, '低级雷神下凡': 48, '高级雷神下凡': 90,
            # 电
            '放电': 30, '双重放电': 46, '电神下凡': 80,
            # 火
            '小火圈': 32, '大火圈': 48, '火神下凡': 90
        }

    elementary_commonHuman_I = \
        {
            # 电
            '电网': 1
        }

    elementary_commonHuman_bbjs = {'水遁': 1, '火遁': 1, '土遁': 1}

    #########特殊判定
    #小火球烧死绵绵处理
    if str(user_skill) == "小火圈":
        if str(xitong_skill) == "绵绵":
            show_return = "对方被你烧死了！"
            zhuangtai = "你胜利了"
            return show_return, zhuangtai, bbjs_xiqi
    elif str(xitong_skill) == "小火圈":
        if str(user_skill) == "绵绵":
            show_return = "你被对方烧死了！"
            zhuangtai = "对方胜利"
            return show_return, zhuangtai, bbjs_xiqi
    # 钻地土遁打死穿山甲处理
    if str(user_skill) == "钻地土遁":
        if str(xitong_skill) == "穿山甲":
            show_return = "对方被你钻死了！"
            zhuangtai = "你胜利了"
            return show_return, zhuangtai, bbjs_xiqi
    elif str(xitong_skill) == "钻地土遁":
        if str(user_skill) == "穿山甲":
            show_return = "你被对方钻死了！"
            zhuangtai = "对方胜利"
            return show_return, zhuangtai, bbjs_xiqi
    # 雷击打死穿山甲处理
    if str(user_skill) == "雷击":
        if str(xitong_skill) == "穿山甲":
            show_return = "对方被你劈死了！"
            zhuangtai = "你胜利了"
            return show_return, zhuangtai, bbjs_xiqi
    elif str(xitong_skill) == "雷击":
        if str(user_skill) == "穿山甲":
            show_return = "你被对方劈死了！"
            zhuangtai = "对方胜利"
            return show_return, zhuangtai, bbjs_xiqi
    # 普通挡挡住小火圈处理
    if str(user_skill) == "小火圈":
        if str(xitong_skill) == "挡":
            show_return = "对方防住了你的攻击！"
            zhuangtai = "双方存活"
            return show_return, zhuangtai, bbjs_xiqi
    elif str(xitong_skill) == "小火圈":
        if str(user_skill) == "挡":
            show_return = "你防住了对方的攻击！"
            zhuangtai = "双方存活"
            return show_return, zhuangtai, bbjs_xiqi
    #风挡挡不住水遁处理
    if str(user_skill) == "风挡":
        if str(xitong_skill) == "水遁":
            show_return = "你没防住对方的攻击！"
            zhuangtai = "对方胜利"
            return show_return, zhuangtai, bbjs_xiqi
    elif str(xitong_skill) == "风挡":
        if str(user_skill) == "水遁":
            show_return = "对方没防住你的攻击！"
            zhuangtai = "你胜利了"
            return show_return, zhuangtai, bbjs_xiqi
    #穿山甲特殊判定
    if str(user_skill) in ["土遁", "钻地土遁"]:
        if str(xitong_skill) == "穿山甲":
            show_return = "你的攻击钻死了对方的穿山甲"
            zhuangtai = "你胜利了"
            return show_return, zhuangtai, bbjs_xiqi
    if str(xitong_skill) in ["土遁", "钻地土遁"]:
        if str(user_skill) == "穿山甲":
            show_return = "对方的攻击钻死了你的穿山甲"
            zhuangtai = "对方胜利"
            return show_return, zhuangtai, bbjs_xiqi
    #开局玩家不吸气特殊判定
    if hui == 0:
        if str(user_skill) != "吸气":
            show_return = "你开局没吸气！"
            zhuangtai = "对方胜利"
            return show_return, zhuangtai, bbjs_xiqi
        elif str(user_skill) == "吸气":
            show_return = "无事发生.jpg"
            zhuangtai = "双方存活"
            return show_return, zhuangtai, bbjs_xiqi
    elif hui != 0:
        pass
    else:
        print('出错啦！')


    print('user_skill=' + user_skill + 'xitong_skill=' + xitong_skill)
    #正常判定
    if str(user_skill) == "吸气":

        print("玩家使用的集气技能！")
        if str(xitong_skill) == "吸气":
            show_return = "无事发生.jpg"
            zhuangtai = "双方存活"
            print("双方使用了吸气")
            return show_return, zhuangtai, bbjs_xiqi
        elif str(elementary_commonHuman_D.get(xitong_skill, None)) != "None":
            show_return = "无事发生.jpg"
            zhuangtai = "双方存活"
            return show_return, zhuangtai, bbjs_xiqi
        elif str(elementary_commonHuman_S.get(xitong_skill, None)) != "None":
            show_return = "你被对方打死了！"
            zhuangtai = "对方胜利"
            return show_return, zhuangtai, bbjs_xiqi
        elif str(elementary_commonHuman_I.get(xitong_skill, None)) != "None":
            show_return = "无事发生.jpg"
            zhuangtai = "双方存活"
            return show_return, zhuangtai, bbjs_xiqi
        elif str(elementary_commonHuman_I.get(xitong_skill, None)) != "髌冰解锁":
            show_return = "无事发生.jpg"
            zhuangtai = "双方存活"
            return show_return, zhuangtai, bbjs_xiqi
        else:
            print("吔？！")
            sys.exit(0)
    elif str(elementary_commonHuman_D.get(user_skill, None)) != "None":
        print("玩家使用的防御技能！")
        if str(xitong_skill) == "吸气":
            print(user_skill + str(elementary_commonHuman_D.get(user_skill)))
            show_return = "无事发生.jpg"
            zhuangtai = "双方存活"
            return show_return, zhuangtai, bbjs_xiqi
        elif str(elementary_commonHuman_D.get(xitong_skill, None)) != "None":
            show_return = "无事发生.jpg"
            zhuangtai = "双方存活"
            return show_return, zhuangtai, bbjs_xiqi
        elif str(elementary_commonHuman_S.get(xitong_skill, None)) != "None":
            skill_add = elementary_commonHuman_D.get(user_skill) + elementary_commonHuman_S.get(xitong_skill)
            if skill_add < 0:
                show_return = "你防住了对方的攻击！"
                zhuangtai = "双方存活"
                return show_return, zhuangtai, bbjs_xiqi
            elif skill_add == 0:
                show_return = "你防住了对方的攻击！"
                zhuangtai = "双方存活"
                return show_return, zhuangtai, bbjs_xiqi
            elif skill_add > 0:
                show_return = "你没防住对方的攻击！"
                zhuangtai = "对方胜利"
                return show_return, zhuangtai, bbjs_xiqi
            else:
                print("吔？！")
                sys.exit(0)
        elif str(elementary_commonHuman_I.get(xitong_skill, None)) != "None":
            show_return = "无事发生.jpg"
            zhuangtai = "双方存活"
            return show_return, zhuangtai, bbjs_xiqi
        elif str(elementary_commonHuman_I.get(xitong_skill, None)) != "髌冰解锁":
            show_return = "无事发生.jpg"
            zhuangtai = "双方存活"
            return show_return, zhuangtai, bbjs_xiqi
        else:
            print("吔？！")
            sys.exit(0)


    elif str(elementary_commonHuman_S.get(user_skill, None)) != "None":
        print("玩家使用了攻击技能！")
        if str(xitong_skill) == "吸气":
            show_return = "对方没防住你的攻击！"
            zhuangtai = "你胜利了"
            print(show_return + zhuangtai)
            return show_return, zhuangtai, bbjs_xiqi
        elif xitong_skill == "髌冰解锁":
            if user_skill in elementary_commonHuman_bbjs:
                show_return = "对方没防住了你的攻击！"
                zhuangtai = "你胜利了"
                return show_return, zhuangtai, bbjs_xiqi
            else:
                show_return = "对方的召唤防住了你的攻击！"
                zhuangtai = "双方存活"
                return show_return, zhuangtai, bbjs_xiqi
            pass
        elif str(elementary_commonHuman_D.get(xitong_skill, None)) != "None":
            skill_add = elementary_commonHuman_S.get(user_skill) + elementary_commonHuman_D.get(xitong_skill)
            if skill_add < 0:
                show_return = "对方防住了你的攻击！"
                zhuangtai = "双方存活"
                return show_return, zhuangtai, bbjs_xiqi
            elif skill_add == 0:
                show_return = "对方防住了你的攻击！"
                zhuangtai = "双方存活"
                return show_return, zhuangtai, bbjs_xiqi
            elif skill_add > 0:
                show_return = "对方没防住你的攻击！"
                zhuangtai = "你胜利了"
                return show_return, zhuangtai, bbjs_xiqi
            else:
                print("吔？！")
                sys.exit(0)

        elif str(elementary_commonHuman_S.get(xitong_skill, None)) != "None":
            if elementary_commonHuman_S.get(user_skill) < elementary_commonHuman_S.get(xitong_skill):
                show_return = "对方的攻击比你强！"
                zhuangtai = "对方胜利"
                return show_return, zhuangtai, bbjs_xiqi
            elif elementary_commonHuman_S.get(user_skill) == elementary_commonHuman_S.get(xitong_skill):
                show_return = "双方攻击打平！"
                zhuangtai = "双方存活"
                return show_return, zhuangtai, bbjs_xiqi
            elif elementary_commonHuman_S.get(user_skill) > elementary_commonHuman_S.get(xitong_skill):
                show_return = "你的攻击比对方强！"
                zhuangtai = "你胜利了"
                return show_return, zhuangtai, bbjs_xiqi
            else:
                print("吔？！")
                sys.exit(0)

        elif str(elementary_commonHuman_I.get(xitong_skill, None)) != "None":
            show_return = "对方是反弹技能！\n你被你自己的攻击打死了！"
            zhuangtai = "对方胜利"
            return show_return, zhuangtai, bbjs_xiqi

        elif str(elementary_commonHuman_I.get(xitong_skill, None)) != "髌冰解锁":
            if str(elementary_commonHuman_bbjs.get(user_skill, None)) != "None":
                show_return = "你的攻击打死了对方的召唤！"
                zhuangtai = "你胜利了"
                return show_return, zhuangtai, bbjs_xiqi
            elif str(elementary_commonHuman_S.get(user_skill, None)) == "None":
                show_return = "你的攻击被对方的召唤解掉了！"
                zhuangtai = "双方存活"
                return show_return, zhuangtai, bbjs_xiqi
            else:
                print("吔？！未知错误！！")
                sys.exit(0)
        else:
            print("吔？！未知错误！！")
            sys.exit(0)

    elif str(elementary_commonHuman_I.get(user_skill, None)) != "None":
        if str(xitong_skill) == "吸气":
            show_return = "无事发生.jpg"
            zhuangtai = "双方存活"
            return show_return, zhuangtai, bbjs_xiqi
        elif str(elementary_commonHuman_D.get(xitong_skill, None)) != "None":
            show_return = "无事发生.jpg"
            zhuangtai = "双方存活"
            return show_return, zhuangtai, bbjs_xiqi
        elif str(elementary_commonHuman_S.get(xitong_skill, None)) != "None":
            show_return = "你使用了反弹技能！\n对方被对方自己的攻击打死了！"
            zhuangtai = "你胜利了"
            return show_return, zhuangtai, bbjs_xiqi
        elif str(elementary_commonHuman_I.get(xitong_skill, None)) != "None":
            show_return = "无事发生.jpg"
            zhuangtai = "双方存活"
            return show_return, zhuangtai, bbjs_xiqi
        elif str(elementary_commonHuman_I.get(xitong_skill, None)) != "髌冰解锁":
            show_return = "无事发生.jpg"
            zhuangtai = "双方存活"
            return show_return, zhuangtai, bbjs_xiqi
        else:
            print("吔？！未知错误！！！")
            sys.exit(0)
    elif str(user_skill) == "髌冰解锁":
        if str(xitong_skill) == "吸气":
            show_return = "无事发生.jpg"
            zhuangtai = "双方存活"
            return show_return, zhuangtai, bbjs_xiqi
        elif str(elementary_commonHuman_D.get(xitong_skill, None)) != "None":
            show_return = "无事发生.jpg"
            zhuangtai = "双方存活"
            return show_return, zhuangtai, bbjs_xiqi
        elif str(elementary_commonHuman_S.get(xitong_skill, None)) != "None":
            if str(elementary_commonHuman_bbjs.get(xitong_skill, None)) != "None":
                show_return = "你的召唤被对方的攻击打死了！"
                zhuangtai = "对方胜利"
                return show_return, zhuangtai, bbjs_xiqi
            elif str(elementary_commonHuman_S.get(xitong_skill, None)) != "None":
                show_return = "你的召唤解掉了对方的攻击！"
                zhuangtai = "双方存活"
                bbjs_xiqi = 1
                return show_return, zhuangtai, bbjs_xiqi
            else:
                print("吔？！髌冰解锁错误！玩家使用，系统攻击！")
                sys.exit(0)
        elif str(elementary_commonHuman_I.get(xitong_skill, None)) != "None":
            show_return = "无事发生.jpg"
            zhuangtai = "双方存活"
            return show_return, zhuangtai, bbjs_xiqi
        elif str(elementary_commonHuman_I.get(xitong_skill, None)) != "髌冰解锁":
            show_return = "无事发生.jpg"
            zhuangtai = "双方存活"
            return show_return, zhuangtai, bbjs_xiqi
        else:
            print("吔？！未知错误！！！")
            sys.exit(0)
    else:
        print("吔？！玩家技能识别判定出错！")
        sys.exit(0)


def elementary_renwu_skillpanding(skill):
    # 定义人物列表
    # 普通人
    human = ['金遁', '木遁', '水遁', '火遁', '土遁', '挡', '穿山甲', '绵绵', '钻地土遁', '吸气', '髌冰解锁']
    # 风
    feng = ['电风扇', '低级风波', '高级风波', '龙卷风', '低级风神下凡', '高级风神下凡', '风挡']
    # 雨
    yv = ['低级流星雨', '高级流星雨', '及时雨', '黑时雨', '低级雨神下凡', '高级雨神下凡', '雨挡']
    # 雷
    lei = ['雷暴', '低级五雷轰顶', '高级五雷轰顶', '低级雷神下凡', '高级雷神下凡', '雷挡', '雷击']
    # 电
    dian = ['放电', '双重放电', '电神下凡', '电挡', '电网']
    # 火
    huo = ['小火圈', '大火圈', '火神下凡', '火挡']

    if skill in human:
        return "普通人"
    elif skill in feng:
        return "风"
    elif skill in yv:
        return "雨"
    elif skill in lei:
        return "雷"
    elif skill in dian:
        return "电"
    elif skill in huo:
        return "火"
    else:
        print("出错了")
        print("skill=" + str(skill))
        #sys.exit(0)
