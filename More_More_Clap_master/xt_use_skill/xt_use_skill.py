"""
#########################################
本模块用来专门处理系统技能使用
#########################################
"""
import sys
import random

"""
################################
初级模式系统技能处理
################################
"""


def xt_use_skill_elementary(xtqi, hui, b):
    # 利用解包思想，合并两个字典
    def Merge(dict1, dict2):
        res = dict1 + dict2
        # res = {**dict1, **dict2}
        return res

    # 耗气预处理
    elementary_commonHuman = []

    # 预处理
    xt_use_skill_elementary_box_a = \
        [
            # 普通人
            '金遁', '木遁', '水遁', '火遁', '土遁', '挡', '穿山甲', '绵绵', '钻地土遁', '髌冰解锁',
            # 风
            '电风扇', '低级风波', '高级风波', '龙卷风', '低级风神下凡', '高级风神下凡', '风挡',
            # 雨
            '低级流星雨', '高级流星雨', '及时雨', '黑时雨', '低级雨神下凡', '高级雨神下凡', '雨挡',
            # 雷
            '雷暴', '低级五雷轰顶', '高级五雷轰顶', '低级雷神下凡', '高级雷神下凡', '雷挡', '雷击',
            # 电
            '放电', '双重放电', '电神下凡', '电挡', '电网',
            # 火
            '小火圈', '大火圈', '火神下凡', '火挡'
        ]

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

    # 全部技能耗气，迭代预处理
    elementary_commonHuman_all = \
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

    # 过渡
    elementary_commonHuman_guodu = {}

    # 输出结果预处理
    xt_use_skill_elementary_box_b = ["吸气"]

    # 系统可用人物技能处理
    print("系统使用技能判定时，系统人物：" + str(b))
    for i in b:
        if "普通人" == i:
            elementary_commonHuman = Merge(human, elementary_commonHuman)
        elif "风" == i:
            elementary_commonHuman = Merge(feng, elementary_commonHuman)
        elif "雨" == i:
            elementary_commonHuman = Merge(yv, elementary_commonHuman)
        elif "雷" == i:
            elementary_commonHuman = Merge(lei, elementary_commonHuman)
        elif "电" == i:
            elementary_commonHuman = Merge(dian, elementary_commonHuman)
        elif "火" == i:
            elementary_commonHuman = Merge(huo, elementary_commonHuman)
        else:
            print("系统可用人物处理出问题啦！")
            sys.exit(0)

    # 处理列表中重复的元素
    elementary_commonHuman = list(set(elementary_commonHuman))
    print("成功处理重复的元素，处理后为：" + str(elementary_commonHuman))

    # 技能优化，处理系统重复用各种等级的挡的问题
    for i in b:
        if i == "电":
            a = 4
            while a != 0:
                a -= 1
                for ii in ["挡", "风挡", "雨挡", "雷挡"]:
                    if ii in elementary_commonHuman:
                        elementary_commonHuman.remove(ii)
                    else:
                        pass
        if i == "雷":
            a = 3
            while a != 0:
                a -= 1
                for ii in ["挡", "风挡", "雨挡"]:
                    if ii in elementary_commonHuman:
                        elementary_commonHuman.remove(ii)
                    else:
                        pass
        if i == "雨":
            a = 2
            while a != 0:
                a -= 1
                for ii in ["挡", "风挡"]:
                    if ii in elementary_commonHuman:
                        elementary_commonHuman.remove(ii)
                    else:
                        pass
        if i == "风":
            a = 1
            while a != 0:
                a -= 1
                for ii in ["挡"]:
                    if ii in elementary_commonHuman:
                        elementary_commonHuman.remove(ii)
                    else:
                        pass
        else:
            pass

    for i in elementary_commonHuman:
        if i in elementary_commonHuman_all:
            elementary_commonHuman_guodu[i] = elementary_commonHuman_all.get(str(i))
        else:
            pass

    # 系统可用技能反馈处理
    print("系统使用技能判定时，系统人物：" + str(b))
    if hui == 0:
        return_skill = "吸气"
        return return_skill
    elif hui > 0:

        # 测试代码
        print(elementary_commonHuman)

        number = len(elementary_commonHuman)
        while number > 0:
            number -= 1
            for i in xt_use_skill_elementary_box_a:
                if i in elementary_commonHuman:
                    ii = float(elementary_commonHuman_guodu.get(i))
                    if ii > xtqi:
                        pass
                    elif ii <= xtqi:
                        xt_use_skill_elementary_box_b.append(str(i))
                    else:
                        print("系统随机技能处理出错")
                        sys.exit(0)
                else:
                    pass
        xt_use_skill_elementary_box_b = list(set(xt_use_skill_elementary_box_b))
        print("根据系统气筛选后，系统可使用技能:" + str(xt_use_skill_elementary_box_b))

        return_skill = random.choice(xt_use_skill_elementary_box_b)
        return return_skill
    else:
        print("xt_use_skill模块，jv处理出错")
        sys.exit(0)
