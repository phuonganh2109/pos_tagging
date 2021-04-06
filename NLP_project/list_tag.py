import codecs
import numpy as np

file_name = ['./VLSP2013-POS-data/VLSP2013_POS_train_BI_POS_Column.txt.goldSeg',
             './VLSP2013-POS-data/VLSP2013_POS_test_BI_POS_Column.txt.goldSeg', './VLSP2013-POS-data/VLSP2013_POS_dev_BI_POS_Column.txt.goldSeg']
data = []
tag = []
dict_tag_treebank = {'N': 'N', 'Np': 'N', 'CH': 'PU', 'M': 'Q', 'R': 'R', 'A': 'A', 'Q': 'Q', 'O': 'N',
                     'P': 'P', 'V': 'V', 'Nc': 'L', 'E': 'E', 'L': 'L', 'C': 'C', 'Ny': 'N', 'T': 'I',
                     'Nb': 'N', 'Y': 'X', 'Nu': 'N', 'Cc': 'C', 'Vb': 'V', 'I': 'I', 'X': 'X', 'Z': 'Na', 'B': 'X', 'Eb': 'C', 'Vy': 'N', 'Ab': 'A', 'Cb': 'C', 'Mb': 'Q', 'Pb': 'C', 'Ni': 'X', 'Xy': 'X'}
freq = {}
freq_w = {}

tag_dict = {'Np': 'N', 'Nc': 'N', 'Ng': 'N', 'Nu': 'N', 'Na': 'N', 'Nl': 'N', 'Nt': 'L', 'Nn': 'Q',
            'Vt': 'V', 'Vit': 'V', 'Vim': 'V', 'Vo': 'V', 'Vs': 'V', 'Vb': 'V', 'Vv': 'V', 'Va': 'V', 'Vc': 'V', 'Vm': 'V', 'Vtim': 'V', 'Vta': 'V', 'Vtc': 'V', 'Vtb': 'V', 'Vto': 'V', 'Vts': 'V', 'Vtm': 'V', 'Vtv': 'V', 'Vitim': 'V', 'Vitb': 'V', 'Vits': 'V', 'Vitc': 'V', 'Vitm': 'V',
            'D': 'D', 'Vla': 'Z', 'Aa': 'A', 'An': 'A',
            'Pp': 'P', 'Pd': 'P', 'Pn': 'P', 'Pa': 'P', 'Pi': 'P',
            'Jt': 'R', 'Jd': 'R', 'Jr': 'R', 'Ja': 'R', 'Ji': 'R', 'Cm': 'C', 'Cc': 'C', 'I': 'M', 'E': 'E', 'X': 'X'}


def readFreq():
    data, tag = [], []
    freq, freq_w = {}, {}
    with codecs.open('./VLSP2013-POS-data/VLSP2013_POS_train_BI_POS_Column.txt.goldSeg', 'r', 'UTF-8') as f:
        lines = f.readlines()
        for l in range(len(lines)-1):
            if('\n' in lines[l] and '\t' in lines[l]):
                t = dict_tag_treebank[lines[l].split('\t')[1].split('\n')[0]]
                if t not in tag:
                    tag.append(t)
                data.append(t)
                w_s = lines[l].split('\n')[0].split('\t')
                if('_' in w_s[0]):
                    w_s[0] = ' '.join(w_s[0].split('_')).lower()
                else:
                    w_s[0] = w_s[0].lower()
                if w_s[0] not in freq_w.keys():
                    freq_w[w_s[0]] = {dict_tag_treebank[w_s[1]]: 1}
                else:
                    if w_s[1] in freq_w[w_s[0]]:
                        freq_w[w_s[0]][dict_tag_treebank[w_s[1]]] += 1
                    else:
                        freq_w[w_s[0]][dict_tag_treebank[w_s[1]]] = 1
        for j in range(0, len(data)-2, 1):
            t = tuple([data[j+k] for k in range(3)])
            if t in list(freq.keys()):
                freq[t] += 1
            else:
                freq[t] = 1
        freq = dict(sorted(freq.items(), key=lambda ans: ans[1], reverse=True))
    return freq, freq_w, tag, data


def readDictionary():
    data = {}
    with codecs.open('VDic_uni.txt', 'r', encoding='UTF-8-sig') as f:
        lines = f.readlines()
        for i, l in enumerate(lines):
            if i < len(lines)-11:
                t = l.split('\r\n')[0]
                k = t.split('\t')[0]
                t = l.split('\r\n')[0].replace(' ', '')
                tem = []
                te = ' '.join(t.split('\t')).replace(
                    '  ', ' ').split()
                if len(te) != 1:
                    tags = te[1].split(',')
                else:
                    tags = ['X']
                for tag in tags:
                    if tag_dict[tag] not in tem:
                        tem.append(tag_dict[tag])
                data[k] = tem
    return data


# thêm tag vào chữ đó, nếu chữ đó ko đủ tag so với từ điển, trả về dict mới
def initDic(data, fre_w):
    k = list(fre_w.keys())
    d_k = [list(data.keys())[i].lower() for i in range(len(list(data.keys())))]
    dic_k = [list(data.keys())[i] for i in range(len(list(data.keys())))]
    for i in range(len(k)):
        if k[i] in d_k:
            w = dic_k[d_k.index(k[i])]
            tag = list(fre_w[k[i]].keys())
            for t in data[w]:
                if t not in tag:
                    fre_w[k[i]][t] = 0
    return fre_w


# cập nhật: gọi hàm initDic trc khi viết file -> chỉ cần chạy 1 time
def write_fr(data, freq_w):
    freq_w = initDic(data, freq_w)
    for i in data:
        if i not in freq_w:
            freq_w[i] = {data[i][0]: 1}

    with codecs.open('model_fr.txt', 'w', 'UTF-8') as f:
        for key, val in freq_w.items():
            s = key + "_"
            for tag, fr in val.items():
                s += " " + tag + " " + str(fr)
            t = s.split('_')[1].strip()
            s = s.split('_')[0] + "_" + t
            f.write(s+'\n')


# tính xác suất của từng tag
def cal_P(fre_w):
    for key, val in fre_w.items():
        total = np.sum(np.array(list(val.values())))
        for k, v in val.items():
            fre_w[key][k] = (v*1.0)/total
    return fre_w


def writeM_3tag(freq):
    with codecs.open('model_new.txt', 'w', 'UTF-8') as f:
        k = list(freq.keys())
        for i in range(len(freq)):
            a = ' '.join(list(k[i]))
            a += ' '
            a += str(freq[k[i]])
            f.write(a + '\n')


# cập nhật tính xác suất cho từng bộ 3
def readM_3tag(filename):
    fre = {}
    total = 0
    with codecs.open(filename, 'r', 'UTF-8') as f:
        d = f.readlines()
        for l in d:
            da = l.split('\n')[0].split()
            k = tuple(da[0:3])
            fre[k] = int(da[-1])
            total += fre[k]
    proportion = {}
    for k, v in fre.items():
        proportion[k] = (v*1.0)/total
    return proportion, fre, total


def read_fr(filename):
    fre = {}
    total = 0
    with codecs.open(filename, 'r', 'UTF-8') as f:
        d = f.readlines()
        for l in d:
            ele = l.split('\n')[0].split('_')
            fre[ele[0]] = {}
            t = ele[1].split()
            i = 0
            while i < len(t):
                if t[i] in dict_tag_treebank.values():
                    PosTag_14 = t[i]
                else:
                    PosTag_14 = dict_tag_treebank[t[i]]
                if PosTag_14 in fre[ele[0]]:
                    fre[ele[0]][PosTag_14] = fre[ele[0]][PosTag_14]+int(t[i+1])
                else:
                    fre[ele[0]][PosTag_14] = int(t[i+1])
                total = total + fre[ele[0]][PosTag_14]
                i += 2
    return total, fre


def Build_P_word_tag(freq_w):
    freq_word_tag = {}
    for key in freq_w:
        for tag in freq_w[key]:
            if tag not in freq_word_tag:
                freq_word_tag[tag] = {key: freq_w[key][tag]}
            else:
                freq_word_tag[tag][key] = freq_w[key][tag]
    return freq_word_tag


def P_tag(freq_word_tag, total, tag):
    count = 0
    for i in freq_word_tag[tag]:
        count = count+freq_word_tag[tag][i]
    return (count*1.0)/total


def P_word_tag(freq_word_tag, word, tag):
    total = 0
    if word not in freq_word_tag[tag]:
        freq_word_tag[tag][word] = 1
    for i in freq_word_tag[tag]:
        total = total + freq_word_tag[tag][i]
    return (freq_word_tag[tag][word]*1.0)/total


# tính xác suất cho cặp tag
def countT_2(fre_w, t, total):
    k = list(fre_w.keys())
    v = list(fre_w.values())
    count = 0
    for i in range(len(k)):
        if list(k[i])[:2] == t:
            count += v[i]
    return count*1.0/total


# data = readDictionary()
# freq, freq_w, tag, da = readFreq()
# write_fr(data, freq_w)
# writeM_3tag(freq)
# total, freq_w = read_fr('model_fr.txt')
# write_fr(data, freq_w)
