﻿from math import *
from PublicReference.base import *
    

class 知源·元素师主动技能(主动技能):
    def 等效CD(self, 武器类型):
        if 武器类型 == '法杖':
            return round(self.CD / self.恢复 * 1.1, 1)
        if 武器类型 == '魔杖':
            return round(self.CD / self.恢复 * 1, 1)

    def 实际技能次数(self, 输出时间,武器类型):
        
        技能CD = self.等效CD(武器类型)
        # 能够打满的技能次数计算
        技能次数 = int((输出时间 - self.演出时间) / self.等效CD(武器类型) + 1 + self.基础释放次数)
        剩余时间 = 输出时间 - (技能次数 - 1 - self.基础释放次数)*self.等效CD(武器类型) - 技能CD - (技能次数-1)*0.5
        # 最后一次技能小数点技能次数计算
        if 剩余时间 > 0 and 剩余时间 <  self.演出时间:
            技能次数 += self.最后一次伤害估算(剩余时间)
        return round(技能次数,2)

    def 最后一次伤害估算(self,剩余时间):     
        return 0

class 知源·元素师技能0(知源·元素师主动技能):
    名称 = '烈焰冲击'
    所在等级 = 15
    等级上限 = 60
    基础等级 = 46
    数据 = [0, 2742, 3021, 3301, 3578, 3857, 4135, 4413, 4691, 4969, 5247, 5526, 5806, 6083, 6362, 6640, 6918, 7196, 7475, 7753, 8031, 8308, 8588, 8866, 9145, 9424, 9701, 9980, 10258, 10536, 10813, 11093, 11370, 11651, 11928, 12206, 12485, 12763, 13040, 13320, 13598, 13875, 14155, 14433, 14713, 14990, 15268, 15547, 15825, 16102, 16381, 16659, 16937, 17215, 17495, 17773, 18052, 18330, 18608, 18886, 19164, 19443, 19720, 19999, 20279, 20557, 20835, 21113, 21392, 21669, 21948]
    攻击次数 = 1
    CD = 7.0
    TP成长 = 0.1
    TP上限 = 5
    演出时间 = 0.4
    def 等效百分比(self, 武器类型):
        return self.数据[self.等级] * self.攻击次数 * (1 + self.TP成长 * self.TP等级) * self.倍率

class 知源·元素师技能1(被动技能):
    名称 = '属性精通'
    所在等级 = 30
    等级上限 = 15
    基础等级 = 5
    圣灵符文倍率 = 1.0
    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1 + (0.30 + 0.02 * self.等级) * self.圣灵符文倍率, 5)

class 知源·元素师技能2(知源·元素师主动技能):
    名称 = '虚无之球'
    所在等级 = 20
    等级上限 = 60
    基础等级 = 43
    数据 = [0, 379, 416, 457, 494, 532, 569, 609, 646, 685, 723, 762, 799, 839, 877, 916, 953, 993, 1031, 1068, 1109, 1145, 1185, 1222, 1262, 1299, 1338, 1376, 1416, 1452, 1490, 1530, 1568, 1605, 1645, 1682, 1721, 1758, 1799, 1837, 1875, 1914, 1952, 1990, 2027, 2067, 2104, 2143, 2182, 2221, 2258, 2297, 2335, 2374, 2411, 2452, 2488, 2526, 2567, 2604, 2643, 2680, 2720, 2757, 2795, 2835, 2873, 2911, 2949, 2988, 3027]
    攻击次数 = 8
    CD = 6.0
    TP成长 = 0.10
    TP上限 = 5
    演出时间 = 8.0
    def 等效百分比(self, 武器类型):
        return self.数据[self.等级] * self.攻击次数 * (1 + self.TP成长 * self.TP等级) * self.倍率

class 知源·元素师技能3(知源·元素师主动技能):
    名称 = '冰墙'
    学习间隔 = 2
    sp消耗 = 25
    所在等级 = 25
    等级上限 = 60
    基础等级 = 41
    数据 = [0, 5858, 6451, 7042, 7635, 8234, 8825, 9418, 10011, 10609, 11202, 11795, 12388, 12981, 13577, 14170, 14762, 15355, 15954, 16546, 17139, 17732, 18328, 18921, 19514, 20107, 20705, 21298, 21891, 22484, 23081, 23674, 24265, 24858, 25458, 26048, 26641, 27234, 27832, 28425, 29018, 29611, 30207, 30800, 31393, 31985, 32584, 33177, 33769, 34362, 34959, 35551, 36144, 36737, 37335, 37928, 38521, 39114, 39711, 40304, 40897, 41489, 42084, 42678, 43271, 43864, 44461, 45055, 45648, 46243, 46835]
    攻击次数 = 1
    CD = 15.0
    TP成长 = 0.10
    TP上限 = 5
    演出时间 = 1.0
    def 等效百分比(self, 武器类型):
        return self.数据[self.等级] * self.攻击次数 * (1 + self.TP成长 * self.TP等级) * self.倍率

class 知源·元素师技能4(知源·元素师主动技能):
    名称 = '雷旋'
    所在等级 = 25
    等级上限 = 60
    基础等级 = 41
    数据 = [0, 2808, 3093, 3380, 3668, 3953, 4237, 4522, 4808, 5091, 5377, 5664, 5948, 6232, 6518, 6804, 7089, 7375, 7658, 7944, 8229, 8513, 8800, 9085, 9370, 9655, 9941, 10225, 10511, 10795, 11080, 11365, 11651, 11934, 12221, 12507, 12794, 13078, 13364, 13648, 13934, 14220, 14503, 14789, 15075, 15358, 15644, 15931, 16215, 16500, 16785, 17070, 17355, 17641, 17925, 18211, 18497, 18780, 19068, 19353, 19640, 19922, 20209, 20494, 20779, 21064, 21348, 21634, 21921, 22205, 22489]
    攻击次数 = 1
    CD = 5.0
    TP成长 = 0.10
    TP上限 = 5
    演出时间 = 1.5
    def 等效百分比(self, 武器类型):
        return self.数据[self.等级] * self.攻击次数 * (1 + self.TP成长 * self.TP等级) * self.倍率

class 知源·元素师技能5(知源·元素师主动技能):
    名称 = '天雷冲击'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 36
    数据 = [0, 2680, 2953, 3224, 3497, 3768, 4040, 4312, 4584, 4856, 5127, 5399, 5672, 5943, 6216, 6488, 6760, 7031, 7303, 7576, 7847, 8119, 8392, 8663, 8935, 9207, 9479, 9751, 10022, 10295, 10567, 10838, 11111, 11383, 11655, 11926, 12198, 12471, 12742, 13015, 13287, 13558, 13830, 14102, 14375, 14646, 14917, 15190, 15462, 15734, 16006, 16278, 16550, 16821, 17094, 17365, 17637, 17910, 18182, 18453, 18725, 18997, 19269, 19541, 19814, 20085, 20356, 20629, 20901, 21173, 21445]
    攻击次数 = 3
    天雷攻击力增加率 = 1.55
    CD = 20.0
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    演出时间 = 1.5
    护石选项 = ['魔界', '圣痕']
    def 等效百分比(self, 武器类型):
        return self.数据[self.等级] * self.攻击次数 * (1 + self.TP成长 * self.TP等级) * self.天雷攻击力增加率 * self.倍率

    def 装备护石(self, x):
        if x == 0:
            self.攻击次数 = 1
            self.天雷攻击力增加率 = 5.51
        elif x == 1:
            self.攻击次数 = 1
            self.天雷攻击力增加率 = 5.93

class 知源·元素师技能6(知源·元素师主动技能):
    名称 = '极冰盛宴'
    所在等级 = 40
    等级上限 = 60
    基础等级 = 33
    数据 = [0, 1307, 1439, 1572, 1705, 1836, 1969, 2101, 2234, 2367, 2499, 2632, 2765, 2897, 3030, 3162, 3294, 3427, 3560, 3692, 3825, 3958, 4090, 4223, 4356, 4487, 4620, 4753, 4885, 5018, 5151, 5283, 5416, 5549, 5681, 5814, 5947, 6078, 6211, 6344, 6476, 6609, 6742, 6874, 7007, 7140, 7272, 7404, 7537, 7669, 7802, 7935, 8067, 8200, 8333, 8465, 8598, 8731, 8862, 8995, 9128, 9260, 9393, 9526, 9658, 9791, 9924, 10056, 10189, 10321, 10453]
    攻击次数 = 8
    CD = 19.0
    TP成长 = 0.10
    TP上限 = 5
    演出时间 = 4.7
    def 等效百分比(self, 武器类型):
        return self.数据[self.等级] * self.攻击次数 * (1 + self.TP成长 * self.TP等级) * self.倍率

    def 最后一次伤害估算(self,剩余时间):
        实际攻击次数 = int(剩余时间/self.演出时间*self.攻击次数)
        实际百分比 = ((self.数据[self.等级] * 实际攻击次数 * (1 + self.TP成长 * self.TP等级))) * self.倍率   
        return round(实际百分比/self.等效百分比(''),2)


class 知源·元素师技能7(知源·元素师主动技能):
    名称 = '湮灭黑洞'
    所在等级 = 40
    等级上限 = 60
    基础等级 = 33
    数据1 = [0, 854, 942, 1028, 1115, 1201, 1288, 1374, 1463, 1549, 1636, 1722, 1809, 1895, 1983, 2069, 2156, 2242, 2329, 2415, 2504, 2590, 2677, 2763, 2850, 2936, 3023, 3109, 3197, 3283, 3370, 3456, 3544, 3630, 3718, 3804, 3891, 3977, 4064, 4150, 4237, 4324, 4411, 4497, 4585, 4671, 4758, 4845, 4932, 5018, 5105, 5191, 5278, 5364, 5452, 5538, 5626, 5712, 5799, 5885, 5973, 6059, 6146, 6232, 6319, 6405, 6492, 6578, 6667, 6753, 6840]
    攻击次数1 = 15
    数据2 = [0, 4279, 4714, 5147, 5581, 6016, 6449, 6884, 7318, 7753, 8187, 8621, 9055, 9489, 9923, 10357, 10792, 11226, 11661, 12093, 12528, 12962, 13397, 13831, 14266, 14700, 15133, 15567, 16001, 16436, 16870, 17305, 17739, 18174, 18607, 19040, 19475, 19909, 20344, 20777, 21212, 21646, 22081, 22514, 22948, 23383, 23816, 24251, 24685, 25120, 25554, 25988, 26421, 26856, 27290, 27724, 28159, 28593, 29028, 29460, 29895, 30329, 30764, 31198, 31633, 32067, 32500, 32934, 33368, 33803, 34237]
    攻击次数2 = 1
    CD = 35.0
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    演出时间 = 6.2
    护石选项 = ['魔界', '圣痕']
    def 等效百分比(self, 武器类型):
        return ((self.数据1[self.等级] * self.攻击次数1 * (1 + self.TP成长 * self.TP等级))+(self.数据2[self.等级] * self.攻击次数2 * (1 + self.TP成长 * self.TP等级))) * self.倍率

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.28
            self.演出时间 *= 0.6
        elif x == 1:
            self.倍率 *= 1.37
            self.演出时间 *= 0.6

    def 最后一次伤害估算(self,剩余时间):
        实际攻击次数1 = int(剩余时间/self.演出时间*self.攻击次数1)
        实际攻击次数2 = 1
        实际百分比 = ((self.数据1[self.等级] * 实际攻击次数1 * (1 + self.TP成长 * self.TP等级))+(self.数据2[self.等级] * 实际攻击次数2 * (1 + self.TP成长 * self.TP等级))) * self.倍率   
        return round(实际百分比/self.等效百分比(''),2)



class 知源·元素师技能8(知源·元素师主动技能):
    名称 = '杰克降临'
    所在等级 = 45
    等级上限 = 60
    基础等级 = 31
    数据1 = [0, 3998, 4406, 4811, 5217, 5621, 6027, 6433, 6840, 7246, 7651, 8055, 8462, 8867, 9275, 9680, 10084, 10491, 10896, 11304, 11709, 12115, 12519, 12925, 13331, 13738, 14144, 14549, 14953, 15360, 15766, 16173, 16578, 16982, 17389, 17794, 18201, 18607, 19012, 19420, 19823, 20230, 20635, 21041, 21447, 21851, 22259, 22664, 23071, 23476, 23881, 24288, 24693, 25099, 25505, 25910, 26318, 26722, 27128, 27533, 27939, 28345, 28749, 29157, 29562, 29967, 30374, 30779, 31187, 31591, 31996]
    攻击次数1 = 1
    数据2 = [0, 15999, 17622, 19244, 20867, 22490, 24113, 25736, 27360, 28982, 30606, 32229, 33852, 35475, 37098, 38722, 40343, 41966, 43591, 45213, 46836, 48460, 50082, 51706, 53328, 54952, 56575, 58198, 59821, 61444, 63066, 64691, 66312, 67936, 69560, 71183, 72805, 74430, 76052, 77674, 79300, 80921, 82544, 84166, 85790, 87414, 89036, 90661, 92283, 93905, 95530, 97151, 98774, 100399, 102021, 103644, 105268, 106890, 108514, 110135, 111760, 113383, 115004, 116629, 118252, 119874, 121499, 123120, 124744, 126368, 127991]
    攻击次数2 = 1
    CD = 45.0
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    演出时间 = 1.6
    护石选项 = ['魔界', '圣痕']
    def 等效百分比(self, 武器类型):
        return ((self.数据1[self.等级] * self.攻击次数1 * (1 + self.TP成长 * self.TP等级))+(self.数据2[self.等级] * self.攻击次数2 * (1 + self.TP成长 * self.TP等级))) * self.倍率

    def 装备护石(self, x):
        if x == 0:
            self.攻击次数1 *= 0.1 * 4
            self.攻击次数2 *= 1.44
        elif x == 1:
            self.攻击次数1 *= 0.1 * 4
            self.攻击次数2 *= 1.54

        
class 知源·元素师技能9(知源·元素师主动技能):
    名称 = '元素之幕'
    所在等级 = 60
    等级上限 = 40
    基础等级 = 23
    数据1 = [0, 370, 406, 444, 483, 519, 557, 595, 632, 669, 708, 745, 782, 819, 857, 895, 931, 970, 1008, 1044, 1082, 1120, 1156, 1195, 1233, 1270, 1307, 1345, 1384, 1420, 1458, 1495, 1533, 1568, 1608, 1646, 1683, 1720, 1758, 1796, 1833, 1871, 1909, 1944, 1982, 2021, 2059, 2096, 2134, 2170, 2207, 2244, 2283, 2322, 2358, 2395, 2433, 2469, 2508, 2546, 2585, 2620, 2658, 2698, 2733, 2771, 2809, 2846, 2883, 2920, 2959]
    攻击次数1 = 20
    数据2 = [0, 11098, 12225, 13350, 14475, 15602, 16727, 17854, 18980, 20105, 21232, 22356, 23482, 24610, 25734, 26862, 27988, 29112, 30239, 31365, 32491, 33617, 34743, 35869, 36994, 38119, 39246, 40372, 41500, 42625, 43751, 44878, 46002, 47129, 48254, 49380, 50507, 51632, 52757, 53884, 55009, 56136, 57262, 58386, 59515, 60639, 61766, 62892, 64017, 65144, 66270, 67394, 68521, 69647, 70773, 71899, 73025, 74151, 75276, 76405, 77529, 78655, 79782, 80907, 82033, 83158, 84284, 85411, 86536, 87662, 88789]
    攻击次数2 = 1
    CD = 30.0
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    演出时间 = 3.0
    护石选项 = ['魔界', '圣痕']
    def 等效百分比(self, 武器类型):
        return ((self.数据1[self.等级] * self.攻击次数1 * (1 + self.TP成长 * self.TP等级))+(self.数据2[self.等级] * self.攻击次数2 * (1 + self.TP成长 * self.TP等级))) * self.倍率

    def 装备护石(self, x):
        if x == 0:
            self.CD *= 0.95
            self.攻击次数1 *= 1 + 0.45
            self.攻击次数2 *= 1.17
        if x == 1:
            self.CD *= 0.95
            self.攻击次数1 *= 1 + 0.45
            self.攻击次数2 *= 1.32

    def 最后一次伤害估算(self,剩余时间):
        实际攻击次数1 = int(剩余时间/self.演出时间*self.攻击次数1)
        实际攻击次数2 = 1
        实际百分比 = ((self.数据1[self.等级] * 实际攻击次数1 * (1 + self.TP成长 * self.TP等级))+(self.数据2[self.等级] * 实际攻击次数2 * (1 + self.TP成长 * self.TP等级))) * self.倍率   
        return round(实际百分比/self.等效百分比(''),2)

class 知源·元素师技能10(被动技能):
    名称 = '魔力增幅'
    所在等级 = 48
    等级上限 = 40
    基础等级 = 20

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.075 + 0.015 * self.等级, 5)

    def 魔法攻击力倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.075 + 0.015 * self.等级, 5)

class 知源·元素师技能11(知源·元素师主动技能):
    名称 = '陨星幻灭'
    所在等级 = 50
    等级上限 = 40
    基础等级 = 12
    数据1 = [0, 159, 197, 233, 270, 307, 343, 380, 418, 540, 575, 611, 646, 682, 718, 754, 789, 825, 861, 896, 932, 968, 1003, 1039, 1075, 1110, 1146, 1182, 1217, 1253, 1289, 1324, 1360, 1396, 1432, 1467, 1503, 1538, 1574, 1610, 1645, 1681, 1717, 1754, 1788, 1825, 1861, 1896, 1932, 1968, 2003, 2039, 2075, 2110, 2146, 2182, 2217, 2253, 2289, 2324, 2360, 2396, 2431, 2467, 2503, 2539, 2574, 2610, 2645, 2681, 2717]
    攻击次数1 = 40
    数据2 = [0, 638, 785, 932, 1080, 1228, 1375, 1523, 1672, 2162, 2300, 2441, 2584, 2727, 2871, 3014, 3156, 3301, 3443, 3584, 3728, 3871, 4014, 4156, 4301, 4443, 4585, 4728, 4871, 5014, 5156, 5298, 5441, 5584, 5728, 5870, 6011, 6154, 6297, 6439, 6584, 6728, 6870, 7012, 7154, 7298, 7441, 7583, 7727, 7869, 8013, 8155, 8298, 8441, 8582, 8727, 8869, 9012, 9155, 9296, 9439, 9581, 9725, 9868, 10010, 10155, 10296, 10439, 10582, 10725, 10868]
    攻击次数2 = 40
    数据3 = [0, 1275, 1570, 1865, 2160, 2455, 2750, 3046, 3345, 4324, 4600, 4884, 5169, 5454, 5742, 6027, 6311, 6601, 6885, 7168, 7458, 7741, 8028, 8314, 8600, 8884, 9168, 9454, 9742, 10029, 10312, 10595, 10881, 11168, 11457, 11740, 12023, 12309, 12596, 12880, 13166, 13455, 13740, 14024, 14309, 14596, 14881, 15166, 15454, 15739, 16025, 16310, 16595, 16882, 17164, 17453, 17737, 18023, 18309, 18592, 18879, 19163, 19450, 19737, 20021, 20308, 20590, 20878, 21164, 21450, 21737]
    攻击次数3 = 5
    数据4 = [0, 5101, 6279, 7459, 8639, 9822, 11000, 12185, 13379, 17295, 18400, 19533, 20676, 21816, 22968, 24112, 25245, 26404, 27542, 28670, 29829, 30967, 32112, 33253, 34402, 35538, 36673, 37817, 38967, 40115, 41247, 42381, 43524, 44672, 45825, 46959, 48093, 49235, 50383, 51518, 52665, 53819, 54958, 56096, 57234, 58387, 59526, 60664, 61817, 62957, 64099, 65238, 66380, 67525, 68656, 69813, 70948, 72094, 73237, 74368, 75516, 76651, 77799, 78947, 80081, 81236, 82361, 83512, 84654, 85799, 86947]
    攻击次数4 = 5
    CD = 145.0

    def 等效百分比(self, 武器类型):
        return ((self.数据1[self.等级] * self.攻击次数1 * (1 + self.TP成长 * self.TP等级))+(self.数据2[self.等级] * self.攻击次数2 * (1 + self.TP成长 * self.TP等级))+(self.数据3[self.等级] * self.攻击次数3 * (1 + self.TP成长 * self.TP等级))+(self.数据4[self.等级] * self.攻击次数4 * (1 + self.TP成长 * self.TP等级))) * self.倍率


class 知源·元素师技能12(知源·元素师主动技能):
    名称 = '元素震荡'
    所在等级 = 70
    等级上限 = 40
    基础等级 = 18
    数据1 = [0, 4673, 5150, 5623, 6097, 6572, 7046, 7519, 7996, 8469, 8943, 9417, 9892, 10365, 10842, 11315, 11789, 12263, 12738, 13211, 13688, 14161, 14636, 15109, 15584, 16057, 16533, 17007, 17482, 17955, 18432, 18904, 19379, 19853, 20328, 20801, 21278, 21750, 22223, 22700, 23173, 23647, 24120, 24597, 25069, 25546, 26019, 26493, 26966, 27443, 27916, 28391, 28865, 29339, 29812, 30289, 30762, 31237, 31711, 32185, 32659, 33135, 33608, 34083, 34557, 35032, 35505, 35981, 36455, 36929, 37402]
    攻击次数1 = 3
    数据2 = [0, 21039, 23173, 25307, 27443, 29577, 31711, 33845, 35981, 38114, 40248, 42383, 44516, 46653, 48787, 50920, 53054, 55191, 57325, 59458, 61594, 63728, 65862, 67996, 70132, 72265, 74400, 76534, 78671, 80803, 82937, 85073, 87205, 89342, 91476, 93610, 95744, 97880, 100013, 102147, 104283, 106417, 108551, 110685, 112822, 114954, 117088, 119224, 121356, 123493, 125627, 127761, 129895, 132031, 134165, 136298, 138434, 140568, 142702, 144836, 146972, 149105, 151240, 153374, 155507, 157644, 159778, 161913, 164046, 166182, 168316]
    攻击次数2 = 1
    数据3 = 0
    攻击次数3 = 0
    CD = 50.0
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    演出时间 = 4.0
    护石选项 = ['魔界', '圣痕']
    def 等效百分比(self, 武器类型):
        return ((self.数据1[self.等级] * self.攻击次数1 * (1 + self.TP成长 * self.TP等级))+(self.数据2[self.等级] * self.攻击次数2 * (1 + self.TP成长 * self.TP等级))) * self.倍率

    def 装备护石(self, x):
        if x == 0:
            self.攻击次数1 += 0.11 * 16
        elif x == 1:
            self.攻击次数1 += 0.14 * 17
        

class 知源·元素师技能13(知源·元素师主动技能):
    名称 = '圣灵水晶'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 16
    数据 = [0, 51419, 56634, 61850, 67067, 72284, 77501, 82716, 87932, 93148, 98366, 103582, 108799, 114014, 119233, 124447, 129663, 134880, 140096, 145312, 150530, 155746, 160963, 166179, 171393, 176612, 181827, 187044, 192260, 197478, 202694, 207910, 213125, 218342, 223559, 228776, 233992, 239207, 244426, 249641, 254857, 260073, 265289, 270506, 275723, 280940, 286156, 291372, 296590, 301805, 307020, 312237, 317453, 322671, 327887, 333104, 338320, 343535, 348753, 353969, 359185, 364402, 369619, 374836, 380051, 385266, 390483, 395700, 400916, 406133, 411349]
    攻击次数 = 1
    CD = 40.0
    演出时间 = 1.6
    是否有护石 = 1
    def 等效百分比(self, 武器类型):
        return self.数据[self.等级] * self.攻击次数 * (1 + self.TP成长 * self.TP等级) * self.倍率
    护石选项 = ['圣痕']
    def 装备护石(self, x):
        self.倍率 *= 1.25
        self.演出时间 -= 4.2



class 知源·元素师技能14(被动技能):
    名称 = '元素奥义'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 11

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18 + 0.02 * self.等级, 5)

class 知源·元素师技能15(知源·元素师主动技能):
    名称 = '元素之门'
    所在等级 = 80
    等级上限 = 40
    基础等级 = 13
    数据 = [0, 5398, 5946, 6493, 7042, 7589, 8142, 8682, 9230, 9777, 10326, 10878, 11420, 11972, 12519, 13069, 13616, 14162, 14709, 15258, 15799, 16350, 16899, 17446, 17997, 18544, 19094, 19638, 20188, 20735, 21284, 21834, 22374, 22925, 23472, 24022, 24570, 25118, 25664, 26212, 26759, 27309, 27860, 28407, 28951, 29496, 30048, 30589, 31142, 31689, 32238, 32787, 33334, 33886, 34428, 34980, 35522, 36070, 36616, 37164, 37711, 38263, 38813, 39360, 39908, 40454, 41002, 41542, 42096, 42642, 43190]
    攻击次数 = 10
    CD = 45.0
    演出时间 = 2.2
    是否有护石 = 1
    def 等效百分比(self, 武器类型):
        # 根据外门数量的攻击力最大增幅率110%
        return self.数据[self.等级] * self.攻击次数 * (1 + self.TP成长 * self.TP等级) * self.倍率 * 1.1
    护石选项 = ['圣痕']
    def 装备护石(self, x):
        self.攻击次数 = 1 * 13.25
        self.演出时间 *= 0.8
    def 最后一次伤害估算(self,剩余时间):
        实际攻击次数 = int((剩余时间-1)/(self.演出时间-1)*self.攻击次数)
        实际百分比 = ((self.数据[self.等级] * 实际攻击次数 * (1 + self.TP成长 * self.TP等级))) * self.倍率   
        return round(实际百分比/self.等效百分比(''),2)

class 知源·元素师技能17(知源·元素师主动技能):
    名称 = '第六元素'
    所在等级 = 85
    等级上限 = 40
    基础等级 = 5
    数据1 = [0, 2458, 3030, 3597, 4167, 4735, 5309, 5876, 6447, 7017, 7587, 8155, 8726, 9295, 9865, 10431, 11006, 11571, 12144, 12713, 13283, 13858, 14426, 14996, 15563, 16138, 16705, 17275, 17844, 18414, 18983, 19554, 20123, 20693, 21260, 21834, 22400, 22970, 23541, 24112, 24680, 25254, 25822, 26391, 26961, 27531, 28100, 28673, 29241, 29812, 30378, 30952, 31518, 32088, 32658, 33229, 33799, 34370, 34940, 35508, 36079, 36649, 37220, 37790, 38360, 38928, 39501, 40070, 40640, 41207, 41779]
    攻击次数1 = 20
    数据2 = [0, 114682, 141273, 167868, 194459, 221054, 247648, 274238, 300833, 327427, 354018, 380613, 407205, 433801, 460395, 486988, 513579, 540174, 566767, 593362, 619952, 646545, 673139, 699732, 726327, 752921, 779513, 806108, 832703, 859294, 885887, 912481, 939074, 965670, 992257, 1018852, 1045448, 1072039, 1098635, 1125227, 1151819, 1178414, 1205007, 1231602, 1258195, 1284789, 1311383, 1337972, 1364567, 1391160, 1417752, 1444348, 1470943, 1497533, 1524127, 1550722, 1577314, 1603909, 1630499, 1657093, 1683689, 1710279, 1736874, 1763468, 1790058, 1816654, 1843246, 1869840, 1896434, 1923028, 1949622] 
    攻击次数2 = 1
    CD = 180.0
    def 等效百分比(self, 武器类型):
        return ((self.数据1[self.等级] * self.攻击次数1 * (1 + self.TP成长 * self.TP等级))+(self.数据2[self.等级] * self.攻击次数2 * (1 + self.TP成长 * self.TP等级))) * self.倍率

class 知源·元素师技能16(知源·元素师主动技能):
    名称 = '圣灵符文'
    所在等级 = 75
    等级上限 = 11
    基础等级 = 1
    是否有伤害 = 0
    是否主动 = 1
    data1 = [0, 131, 144, 156, 169, 181, 194, 206, 219, 231, 244, 256, 269, 281, 294, 306, 319, 331, 344, 356, 369]
    data2 = [0, 160, 174, 188, 201, 216, 229, 244, 257, 272, 285, 299, 313, 327, 341, 355, 369, 383, 397, 411, 424]

    自定义描述 = 1
    def 技能描述(self, 武器类型):
        temp = ''
        temp += '属性精通增幅：%.1f%%' % (self.data1[self.等级] / 10) + '<br>'
        temp += '魔法秀增幅：%.1f%%' % (self.data2[self.等级] / 10)
        return temp    

class 知源·元素师技能18(知源·元素师主动技能):
    名称 = '魔法秀'
    所在等级 = 20
    等级上限 = 15
    基础等级 = 10
    魔法秀数值 = [0, 22, 43, 65, 86, 108, 130, 151, 173, 194, 216, 238, 259, 281, 302, 324, 346, 367, 389, 410, 432]
    是否有伤害 = 0
    冷却关联技能 = ['冰墙','元素之门','元素之幕','元素震荡','圣灵水晶','烈焰冲击','天雷冲击','雷旋','杰克降临','湮灭黑洞','极冰盛宴','虚无之球','光与暗的交响']
    
    圣灵符文倍率 = 1.0
    def CD缩减倍率(self, 武器类型):
        return round(1 - 0.001 * self.魔法秀数值[self.等级] * self.圣灵符文倍率, 3)

class 知源·元素师技能19(被动技能):
    名称 = '元素之源'
    所在等级 = 95
    等级上限 = 40
    基础等级 = 4

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18 + 0.02 * self.等级, 5)

class 知源·元素师技能20(知源·元素师主动技能):
    名称 = '光与暗的交响'
    所在等级 = 95
    等级上限 = 40
    基础等级 = 6
    数据1 = [0,7853, 8650, 9447, 10244, 11041, 11838, 12635, 13432, 14229, 15026, 15823, 16620, 17417, 18214, 19011, 19808, 20605, 21402, 22199, 22996, 23793, 24590, 25387, 26184, 26981, 27778, 28575, 29372, 30169, 30966, 31763, 32560, 33357, 34154, 34951, 35748, 36545, 37342, 38139, 38936]
    攻击次数1 = 15
    CD = 60.0
    演出时间 = 3.0

    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1)* self.倍率

class 知源·元素师技能21(知源·元素师主动技能):
    名称 = '宇宙寂灭-冰火之歌'
    所在等级 = 100
    等级上限 = 40
    基础等级 = 2
    数据1 = [0,263047, 324042, 385040, 446032, 507027, 568022, 629017, 690012, 751007, 812002, 872997, 933992, 994987, 1055982, 1116977, 1177972, 1238967, 1299962, 1360957, 1421952, 1482947, 1543942, 1604937, 1665932, 1726927, 1787922, 1848917, 1909912, 1970907, 2031902, 2092897, 2153892, 2214887, 2275882, 2336877, 2397872, 2458867, 2519862, 2580857, 2641852]    
    攻击次数1 = 1
    数据2 = [0,25052, 30861, 36670, 42479, 48288, 54097, 59906, 65715, 71524, 77333, 83142, 88951, 94760, 100569, 106378, 112187, 117996, 123805, 129614, 135423, 141232, 147041, 152850, 158659, 164468, 170277, 176086, 181895, 187704, 193513, 199322, 205131, 210940, 216749, 222558, 228367, 234176, 239985, 245794, 251603]
    攻击次数2 = 7
    关联技能 = ['无']
    CD = 290.0

    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1 + self.数据2[self.等级] * self.攻击次数2 )* self.倍率

    def 加成倍率(self, 武器类型):
         return 0.0

知源·元素师技能列表 = []
i = 0
while i >= 0:
    try:
        exec('知源·元素师技能列表.append(知源·元素师技能'+str(i)+'())')
        i += 1
    except:
        i = -1

知源·元素师技能序号 = dict()
for i in range(len(知源·元素师技能列表)):
    知源·元素师技能序号[知源·元素师技能列表[i].名称] = i

知源·元素师一觉序号 = 0
知源·元素师二觉序号 = 0
知源·元素师三觉序号 = 0
for i in 知源·元素师技能列表:
    if i.所在等级 == 50:
        知源·元素师一觉序号 = 知源·元素师技能序号[i.名称]
    if i.所在等级 == 85:
        知源·元素师二觉序号 = 知源·元素师技能序号[i.名称]
    if i.所在等级 == 100:
        知源·元素师三觉序号 = 知源·元素师技能序号[i.名称]

知源·元素师护石选项 = ['无']
for i in 知源·元素师技能列表:
    if i.是否有伤害 == 1 and i.是否有护石 == 1:
        知源·元素师护石选项.append(i.名称)

知源·元素师符文选项 = ['无']
for i in 知源·元素师技能列表:
    if i.所在等级 >= 20 and i.所在等级 <= 80 and i.所在等级 != 50 and i.是否有伤害 == 1:
        知源·元素师符文选项.append(i.名称)

class 知源·元素师角色属性(角色属性):

    实际名称 = '知源·元素师'
    角色 = '魔法师(女)'
    职业 = '元素师'

    武器选项 = ['魔杖','法杖']
    
    伤害类型选择 = ['魔法百分比']
    
    伤害类型 = '魔法百分比'
    防具类型 = '布甲'
    防具精通属性 = ['智力']

    主BUFF = 1.85
   
    远古记忆 = 0
  
    def __init__(self):
        基础属性输入(self)
        self.技能栏= deepcopy(知源·元素师技能列表)
        self.技能序号= deepcopy(知源·元素师技能序号)
   
    def CD倍率计算(self):
        圣灵符文 = self.技能栏[self.技能序号['圣灵符文']]
        self.技能栏[self.技能序号['属性精通']].圣灵符文倍率 = 1 + 圣灵符文.data1[圣灵符文.等级] / 1000
        self.技能栏[self.技能序号['魔法秀']].圣灵符文倍率 = 1 + 圣灵符文.data2[圣灵符文.等级] / 1000
        super().CD倍率计算()

    def 技能释放次数计算(self):
        技能释放次数 = []
        for i in self.技能栏:
            if i.是否有伤害 == 1:
                if self.次数输入[self.技能序号[i.名称]] == '/CD':
                    技能释放次数.append(i.实际技能次数(self.时间输入,self.武器类型))
                elif self.次数输入[self.技能序号[i.名称]] != '0':
                    技能释放次数.append(int(self.次数输入[self.技能序号[i.名称]]))
                else:
                    技能释放次数.append(0)
            else:
                技能释放次数.append(0)
        return 技能释放次数    

class 知源·元素师(角色窗口):
    def 窗口属性输入(self):
        self.初始属性 = 知源·元素师角色属性()
        self.角色属性A = 知源·元素师角色属性()
        self.角色属性B = 知源·元素师角色属性()
        self.一觉序号 = 知源·元素师一觉序号
        self.二觉序号 = 知源·元素师二觉序号
        self.三觉序号 = 知源·元素师三觉序号
        self.护石选项 = deepcopy(知源·元素师护石选项)
        self.符文选项 = deepcopy(知源·元素师符文选项)
 
