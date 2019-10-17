import jieba.posseg as pseg
for line in open("train_words.txt", "r"):
    words = pseg.cut(line)   #词性标注
    with open("train_pseg.txt", "a") as f:
        for word, flag in words:
            if flag != 'x':
                f.write(flag + ' ')
        f.write('\n')
    f.close()