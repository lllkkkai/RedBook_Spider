import csv
from collections import Counter
import jieba
class Deal:
    def main(self):
        x = ['出现','可以','情况','10','30','20','12','地方','地点','看到','10','20','30','00','12','分钟','11','21','22','19','真的','关注','']
        with open("./datas_search/stopwords.dat", "r", encoding='utf-8') as stopwords:
            for line in stopwords:
                x.append(line.strip())
        baidu_stopwords = {}.fromkeys(x)  # 导入停用词表
        jieba.load_userdict("./datas_search/dict.txt")
        seg_list = jieba.cut("蓝眼泪景观十分有名")
        print("Full Mode: " + "/ ".join(seg_list))
        # result = Counter()
        with open("./datas_search/desc.txt", "r", encoding='utf-8') as f:
            text = f.read()
        ls = jieba.lcut(text)
        counts = {}
        for i in ls:
            if len(i) > 1:
                if not i.isdigit():
                    counts[i] = counts.get(i, 0) + 1
        for word in baidu_stopwords:  # 去掉停用词
            counts.pop(word, 0)

        ls1 = sorted(counts.items(), key=lambda x: x[1], reverse=True)  # 词频排序
        print(ls1[:100])
        with open("./datas_search/frequency.csv", "w", encoding='utf-8', newline='') as csvfile:
            write = csv.writer(csvfile)
            write.writerow(['访问来源','数值'])
            for i in range(100):
                write.writerow(ls1[i])
            # f.writerow(['链接','类型','标题','点赞','收藏','评论','分享','上传时间','标签','IP归属地'])
            #
        #     while True:
        #         lines = f.read(1024).splitlines()
        #         if lines == []:
        #             break
        #         lines = [lines[i].split(" ") for i in range(len(lines))]
        #         words = []
        #         for line in lines:
        #             words.extend(line)
        #         tmp = Counter(words)
        #         result += tmp
        #
        # print(result.most_common(100))

if __name__ == '__main__':
    deal = Deal()
    deal.main()
