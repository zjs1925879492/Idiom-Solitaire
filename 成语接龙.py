import random

def chinese_to_pinyin(x):
    y = ''
    dic = {}
    with open("unicode_py.txt") as f:
        for i in f.readlines():
            dic[i.split()[0]] = i.split()[1]
    for i in x:
        i = str(i.encode('unicode_escape'))[-5:-1].upper()
        try:
            y += dic[i] + ' '
        except:
            y += 'XXXX ' #非法字符以XXXX代替
    return y

def idiom_exists(x):           #判断输入是否在成语库中
    with open('idiom.txt','r') as f:
        for i in set(f.readlines()):
            if x == i.strip():
                return True
        return False

def idiom_test(idiom1, idiom2, mode, opt):      #判断首尾是否接上
    if mode == 0 and idiom2[0] != idiom1[-1]:
        return False
    if mode == 1 and chinese_to_pinyin(idiom2[0]) != chinese_to_pinyin(idiom1[-1]):
        return False
    if mode ==2 and chinese_to_pinyin(idiom2[0])[:-2] != chinese_to_pinyin(idiom1[-1])[:-2]:
        return False
    if opt == 0 and len(idiom2) != 4:
        return False
    return True

def idiom_select(x, mode, opt):
    if x == None:
        with open('idiom.txt','r') as f:
            return random.choice(f.readlines())[:-1]
    else:
        with open('idiom.txt','r') as f:
            pinyin = chinese_to_pinyin(x[-1])
            base = f.readlines()
            if pinyin[0] != 'Z':
                base = base[base.index(pinyin[0]+'\n'):base.index(chr(ord(pinyin[0])+1)+'\n')]
            else:
                base = base[base.index(pinyin[0]+'\n'):]
            random.shuffle(base)
            for i in base:
                if i[:-1] == x or (opt == 0 and len(i) != 5):
                    continue
                if mode == 0 and i[0] == x[-1]:
                    return i[:-1]
                if mode == 1 and chinese_to_pinyin(i[0]) == pinyin:
                    return i[:-1]
                if mode == 2 and chinese_to_pinyin(i[0])[:-2] == pinyin[:-2]:
                    return i[:-1]
        return None

def idiom_start(start = 0, mode = 0, opt = 0):
    memory = set()  #防止重复使用同样成语
    if start == 0:
        while True:
            t = idiom_select(None, mode, opt)
            if idiom_select(t, mode, opt) != None:
                break
        print(t)
    else:
        p = input("请输入成语:")
        if p.strip() == '':
            print("游戏结束！你输了")
            return 0
        if idiom_exists(p) == False:
            print("游戏结束！该成语不存在")
            return 0
        memory.add(p)
        cycle_flag = 0  #控制循环次数
        while True:
            t = idiom_select(p, mode, opt)
            if t not in memory:
                break
        if t == None:
            print("恭喜你，你赢了！")
            return 1
        else:
            print(t)
            memory.add(t)        
    while True:
        p = input("请输入成语:")
        if p.strip() == '':
            print("游戏结束！你输了")
        if idiom_exists(p) == False:
            print("游戏结束！该成语不存在")
            return 0
        memory.add(p)
        cycle_flag = 0
        while True:
            t = idiom_select(p, mode, opt)
            cycle_flag += 1
            if t not in memory:
                break
            if cycle_flag == 10:
                t = None
                break
        if t == None:
            print("恭喜你，你赢了！")
            return 1
        else:
            print(t)
            memory.add(t)

idiom_start(start=1, mode=2, opt=1)
