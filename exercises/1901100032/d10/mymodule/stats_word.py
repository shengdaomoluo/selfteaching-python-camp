from collections import Counter
import jieba

def stats_text_en(text, count):
    elements = text.split()
    words = []
    symbols = ',.*-!'
    for element in elements:
        for symbol in symbols:
            element = element.replace(symbol,'')
        if len(element) and element.isascii():
            words.append(element)
    return Counter(words).most_common(count)


def stats_text_cn(text, count):
    words = jieba.cut(text)
    tmp = []
    for i in words:
        if len(i) > 1:
            tmp.append(i)
    return Counter(tmp).most_common(count)


def stats_text(text, count):
    '''
    '''
    if not isinstance(text,str):
        raise ValueError('参数必须是 str 类型，输入类型 %s' % type(text))
    return stats_text_en(text,count) + stats_text_cn(text, count)
