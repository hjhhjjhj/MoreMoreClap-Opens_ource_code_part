"""
################################
普通人模式气判断
################################
"""


# 系统使用技能时气的判断
def xitongqipanduan(xitongjileng, xtqi, xiqi):
    if xitongjileng == '吸气':
        xtqi += xiqi
        return xtqi
    elif xitongjileng == '挡':
        xtqi += 0
        return xtqi
    elif xitongjileng == '髌冰解锁':
        xtqi += 0
        return xtqi
    elif xitongjileng == '穿山甲':
        xtqi -= 0.5
        return xtqi
    elif xitongjileng == '绵绵':
        xtqi -= 1
        return xtqi
    elif xitongjileng == '金遁':
        xtqi -= 1
        return xtqi
    elif xitongjileng == '木遁':
        xtqi -= 2
        return xtqi
    elif xitongjileng == '水遁':
        xtqi -= 3
        return xtqi
    elif xitongjileng == '火遁':
        xtqi -= 4
        return xtqi
    elif xitongjileng == '土遁':
        xtqi -= 5
        return xtqi
    elif xitongjileng == '钻地土遁':
        xtqi -= 4
        return xiqi
    else:
        return xtqi


# 玩家使用技能时气的判断
def playerqipanduan(skill, qi, xiqi):
    if skill == '吸气':
        qi += xiqi
        return qi
    elif skill == '挡':
        qi += 0
        return qi
    elif skill == '髌冰解锁':
        qi += 0
        return qi
    elif skill == '穿山甲':
        qi -= 0.5
        return qi
    elif skill == '绵绵':
        qi -= 1
        return qi
    elif skill == '金遁':
        qi -= 1
        return qi
    elif skill == '木遁':
        qi -= 2
        return qi
    elif skill == '水遁':
        qi -= 3
        return qi
    elif skill == '火遁':
        qi -= 4
        return qi
    elif skill == '土遁':
        qi -= 5
        return qi
    elif skill == '钻地土遁':
        qi -= 4
        return qi
    else:
        return qi


"""
################################
初级模式气判断
################################
"""


#初级模式耗气判定
def elementary_qi_panding(skill, qi, xiqi):

    #初始化

    #耗气
    elementary_commonHuman = \
        {
            # 普通人
            '金遁': 1, '木遁': 2, '水遁': 3, '火遁': 4, '土遁': 5, '挡': 0, '穿山甲': 0.5, '绵绵': 1, '钻地土遁': 4, '髌冰解锁': 0,
            # 风
            '电风扇': 0.5, '低级风波': 1, '高级风波': 2, '龙卷风': 3, '低级风神下凡': 4, '高级风神下凡': 8, '风挡': 0,
            # 雨
            '低级流星雨': 1, '高级流星雨': 2, '及时雨': 3, '黑时雨': 6, '低级雨神下凡': 4, '高级雨神下凡': 8, '雨挡': 0,
            # 雷
            '雷暴': 1, '低级五雷轰顶': 3, '高级五雷轰顶': 5, '低级雷神下凡': 4, '高级雷神下凡': 8, '雷挡': 0, '雷击': 1,
            # 电
            '放电': 0.5, '双重放电': 3, '电神下凡': 5, '电挡': 0, '电网': 1,
            # 火
            '小火圈': 0.5, '大火圈': 3, '火神下凡': 5, '火挡': 0
        }

    #判定程序
    if skill == "吸气":

        #测试代码
        print("初级模式吸气气判定成功运行")

        qi += xiqi

        #测试代码
        print(qi)

        return qi
    elif elementary_commonHuman.get(skill, None) != "None":

        #测试代码
        print(skill)

        qi -= elementary_commonHuman.get(skill, None)
        return qi
    else:
        print("初级模式气判定出问题\n请反馈bug")
        pass
