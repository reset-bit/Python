import pymongo
# import jieba
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

# # 加在包引用的后面，开启paddle模式
# jieba.enable_paddle()
# # 分词
# def getCutWord():
#     # 获取集合
#     client = pymongo.MongoClient(host='localhost', port=27017)
#     db = client.leipin
#     collection = db['java']
#     # 通过[0]来只取出第一条数据
#     douban = collection.find()[0]
#     # word_total = ''
#     # 获取短评
#     context = douban['job']
#     list_paddle = jieba.cut(context, use_paddle=True)
#     # 通过join()通过空格来连接list_paddle来生成一段文本
#     word = " ".join(list_paddle)
#     return word
    

if __name__ == '__main__':
    # 调用分词方法
    # text = getCutWord()
    # print(text)

    # 从数据库中提取数据并格式化为词云指定格式
    client = pymongo.MongoClient(host='localhost', port=27017)
    db = client.leipin
    collection = db['java']
    result = collection.find({}, {'_id': 0, 'place': 1})
    text = ''
    for i in result:
        text += (i['place'] + ' ')
    print(text)

    # 添加词云屏蔽词
    word = {}
    stopwords = STOPWORDS.update(word)
    # 背景白，要加font_path字体（识别中文需要设置字体）
    wordcloud = WordCloud(background_color='white', font_path="msyh.ttc", stopwords=stopwords, max_words=300)
    # mask设置词云背景
    # mask = np.array(Image.open('img5.jpg'))
    # wordcloud = WordCloud(background_color='white', font_path="msyh.ttc",mask=mask, stopwords=stopwords, max_words=300)
    # 以text生成词云
    wordcloud.generate(text=text)

    # 显示词云
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off') # 关闭坐标轴
    plt.show()
    # 保存词云为图片
    # wordcloud.to_file('cloud.png')

