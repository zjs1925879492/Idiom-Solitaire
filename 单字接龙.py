import random

def chinese_to_pinyin(x):
    """参数为字符串，返回为该字符串对应的汉语拼音"""
    y = ''
    dic = {}
    with open("unicode_py.txt") as f:
        for i in f.readlines():
            dic[i.split()[0]] = i.split()[1]
    for i in x:
        i = str(i.encode('unicode_escape'))[-5:-1].upper()
        try:
            y += dic[i] + ' '
            waring=0
        except:
            y += 'XXXX ' #非法字符我们用XXXX代替
            return 'waring'
    return y

def idiom_select(x):
    """核心代码部分，参数x为成语，返回该成语的接龙匹配成语"""
    with open('idiom.txt','r') as f:
        #以下六行代码，通过索引排除无效循环，显著提升运行效率
        pinyin = chinese_to_pinyin(x[-1])
        if pinyin=='waring':
            return '警告，该字符非汉语文字！！！'
        base = f.readlines()
        if pinyin[0] != 'Z':
            base = base[base.index(pinyin[0]+'\n'):base.index(chr(ord(pinyin[0])+1)+'\n')]
        else:
            base = base[base.index(pinyin[0]+'\n'):]
        random.shuffle(base)
        for i in base:
            if i[:-1] == x or len(i) != 5:
                continue
            if i[0] == x[-1]:
                return i[:-1]
            if chinese_to_pinyin(i[0]) == pinyin:
                return i[:-1]
            if chinese_to_pinyin(i[0])[:-2] == pinyin[:-2]:
                return i[:-1]
            

while True:
    x= input('请输入任何一字！')
    if x in ['退出','不玩了']:
        break
    else:
        cy=idiom_select(x)
        print(cy)        
    
