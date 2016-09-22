from wordcloud import WordCloud
import jieba
import PIL
import matplotlib.pyplot as plt
import numpy as np
def wordcloudplot(txt):
    #path='D:/workspace/python/wordcloud/msyh.ttf'
    #path= unicode(path, 'utf8').encode('gb18030')
    alice_mask = np.array(PIL.Image.open('D:/workspace/python/wordcloud/meiniu.jpg'))
    wordcloud = WordCloud(font_path="D:/workspace/python/wordcloud/msyh.ttf",background_color="white",margin=5, width=800, height=1080,mask=alice_mask,max_words=2000,max_font_size=60,random_state=42)
    wordcloud = wordcloud.generate(txt)
    wordcloud.to_file('D:/workspace/python/wordcloud/meiniu2.jpg')
    plt.imshow(wordcloud)
    plt.axis("off")
    #plt.show()
def main():
    a=[]
    f=open(r'D:/workspace/python/wordcloud/a.txt','r').read()
    words=list(jieba.cut(f))
    for word in words:
        if len(word)>1:
            a.append(word)
            txt=r' '.join(a)
            wordcloudplot(txt)
if __name__=='__main__':
    main()