import codecs
import random
import nltk
from nltk.tokenize import word_tokenize
import list_tag as tag_counting
import numpy as np

punc = '''!()[]{};:'"\, <>./?@#$%^&*_~-”“'''


class POS_tag():
    tag_dict = {'Np': 'N', 'Nc': 'N', 'Ng': 'N', 'Nu': 'N', 'Na': 'N', 'Nl': 'N', 'Nt': 'L', 'Nn': 'Q',
                'Vt': 'V', 'Vit': 'V', 'Vim': 'V', 'Vo': 'V', 'Vs': 'V', 'Vb': 'V', 'Vv': 'V', 'Va': 'V', 'Vc': 'V', 'Vm': 'V', 'Vtim': 'V', 'Vta': 'V', 'Vtc': 'V', 'Vtb': 'V', 'Vto': 'V', 'Vts': 'V', 'Vtm': 'V', 'Vtv': 'V', 'Vitim': 'V', 'Vitb': 'V', 'Vits': 'V', 'Vitc': 'V', 'Vitm': 'V',
                'D': 'D', 'Vla': 'Z', 'Aa': 'A', 'An': 'A',
                'Pp': 'P', 'Pd': 'P', 'Pn': 'P', 'Pa': 'P', 'Pi': 'P',
                'Jt': 'R', 'Jd': 'R', 'Jr': 'R', 'Ja': 'R', 'Ji': 'R', 'Cm': 'C', 'Cc': 'C', 'I': 'M', 'E': 'E', 'X': 'X'}

    def __init__(self, text, punc):
        self.data = {}
        self.sentences = [x.lower() for x in word_tokenize(text)]
        self.text = text
        self.punc = punc
        self.total_tag, self.data = tag_counting.read_fr('model_fr.txt')
        self.proportion, self.freq_3t, self.total_3t = tag_counting.readM_3tag(
            'model_new.txt')

    def readDictionary(self):
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
                        if self.tag_dict[tag] not in tem:
                            tem.append(self.tag_dict[tag])
                    self.data[k] = tem
        for i in self.punc:
            self.data[i] = ['PU']
        self.data['...'] = ['PU']

    def assignLabel_basic(self):
        self.preprocess_s = []
        for i in self.text:
            if '-' not in i:
                self.preprocess_s.extend(word_tokenize(i))
            else:
                self.preprocess_s.append(i)
        self.s_label = {}
        i = 0
        output_text = ""
        while i < len(self.preprocess_s):
            j = i+1
            temp_s = self.preprocess_s[i]
            check = False
            while (j < len(self.preprocess_s)) and (self.preprocess_s[j] not in self.punc):
                temp_s = temp_s+" "+self.preprocess_s[j]
                lower_s = temp_s.lower()
                if lower_s in self.data:
                    output_text = output_text + temp_s.replace(" ", "_") + " "
                    i = j
                    check = True
                    break
                j = j+1
            if not check:
                if self.preprocess_s[i] not in self.punc:
                    if self.preprocess_s[i].lower() in self.data:
                        self.s_label[self.preprocess_s[i]
                                     ] = self.data[self.preprocess_s[i].lower()][0]
                    else:
                        self.s_label[self.preprocess_s[i]] = 'X'
            else:
                self.s_label[temp_s] = self.data[lower_s][0]
            i += 1
        return self.s_label

    def automat_word(self):
        self.Tree = {0: []}
        continue_p = 0
        end_pos = 0
        for i in self.data:
            p = 0
            am_tiet = i.split()
            index = 0
            while (index < len(am_tiet)) and (p in self.Tree):
                temp_dict = self.Tree[p]
                exist_p = [item for item in temp_dict if item[0]
                           == am_tiet[index]]
                if not exist_p:
                    break
                else:
                    p = exist_p[0][1]
                    index = index+1
            while index < len(am_tiet)-1:
                if p in self.Tree:
                    self.Tree[p].append((am_tiet[index], continue_p+1))
                    continue_p = continue_p+1
                else:
                    self.Tree[continue_p] = [(am_tiet[index], continue_p+1)]
                    continue_p = continue_p+1
                index = index+1
                p = continue_p
            if index == len(am_tiet)-1:
                if p in self.Tree:
                    self.Tree[p].append((am_tiet[index], 'end'+str(end_pos)))
                else:
                    self.Tree[p] = [(am_tiet[index], 'end'+str(end_pos))]
            end_pos = end_pos+1

    def findWord(self, start_pos, sentence):
        p = 0
        for i in range(start_pos, len(sentence)):
            if p not in self.Tree:
                if i-start_pos > 1:
                    return i
                else:
                    return -1
            temp_dict = self.Tree[p]
            exist_p = [item for item in temp_dict if item[0]
                       == sentence[i].lower()]
            if exist_p:
                p = exist_p[0][1]
            else:
                if i-start_pos > 1:
                    return i
                else:
                    return -1
        if (i-start_pos > 0) and ('end' in p):
            return i+1
        return -1

    def write_automate_File(self):
        self.automat_word()
        with codecs.open('automat.txt', 'w', 'UTF-8') as f:
            for key, value in self.Tree.items():
                if isinstance(key, int):
                    f.write(str(key)+'\n')
                else:
                    f.write(key+'\n')
                line = ""
                for qi in value:
                    if isinstance(qi[1], int):
                        tuple_temp = qi[0]+' '+str(qi[1])
                    else:
                        tuple_temp = qi[0]+' '+qi[1]

                    line = line+tuple_temp+"_"
                line = line.rstrip('_')
                f.write(line+'\n')

    def read_automate_File(self):
        self.Tree = {}
        count = 0
        with codecs.open('automat.txt', 'r', 'UTF-8') as f:
            d = f.readlines()
            for l in d:
                l = l.strip('\n')
                if count % 2 == 0:
                    if l.isnumeric():
                        self.Tree[int(l)] = {}
                        key = int(l)
                    else:
                        self.Tree[str(l)] = {}
                        key = l
                else:
                    tuples = l.split('_')
                    temp_list = []
                    for i in tuples:
                        temp_tuple = i.split(" ")
                        if temp_tuple[1].isnumeric():
                            temp_tuple[1] = int(temp_tuple[1])
                        temp_tuple = tuple(temp_tuple)
                        temp_list.append(temp_tuple)
                    self.Tree[key] = temp_list
                count = count+1

    def BFS_SP(self, graph, start, goal):
        explored = []
        queue = [[start]]
        result_path = []
        if start == goal:
            return
        level_shortest_path = len(graph)
        while queue:
            path = queue.pop(0)
            node = path[-1]
            neighbours = graph[node]
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
                if (neighbour == goal) and (level_shortest_path >= len(queue[-1])):
                    level_shortest_path = len(queue[-1])
                    result_path.append(new_path)
                if level_shortest_path < len(queue[-1]):
                    return result_path
            explored.append(node)
        return result_path

    def generate_2(self, a, b):
        result = []
        for i in a:
            for j in b:
                result.append([i, j])
        return result

    def count_confident(self, freq_word_tag, text_input, solution):
        P_w_t = tag_counting.P_word_tag(
            freq_word_tag, text_input[0], solution[0])
        P_w_t = P_w_t * \
            tag_counting.P_word_tag(freq_word_tag, text_input[1], solution[1])

        P_t1 = tag_counting.P_tag(freq_word_tag, self.total_tag, solution[0])
        P_t1_t2 = tag_counting.countT_2(self.freq_3t, [
                                        solution[0], solution[1]], self.total_3t)/tag_counting.P_tag(freq_word_tag, self.total_tag, solution[1])
        P_ti_t1_t2 = P_t1*P_t1_t2

        for i in range(2, len(text_input)):
            P_w_t = P_w_t * \
                tag_counting.P_word_tag(
                    freq_word_tag, text_input[i], solution[i])
            P_ti_t1_t2 = P_ti_t1_t2*(self.proportion[(solution[i-2], solution[i-1], solution[i])]/tag_counting.countT_2(
                self.freq_3t, [solution[i-2], solution[i-1]], self.total_3t))
        return P_ti_t1_t2*P_w_t

    def buildG(self):
        self.G = {}
        self.freq_w = tag_counting.cal_P(self.data)
        for i in range(len(self.sentences)):
            self.G[i] = [i+1]
        self.G[len(self.sentences)] = []
        for i in range(len(self.sentences)):
            pos_word = self.findWord(i, self.sentences)
            if pos_word > i:
                self.G[i].append(pos_word)
        result_path = self.BFS_SP(self.G, 0, len(self.sentences))
        freq_word_tag = tag_counting.Build_P_word_tag(self.data)
        final_solution = -1
        max_confident = -1
        text_input = ''
        if result_path[0][0] == 0 and result_path[0][1] == len(self.sentences):
            text_input = ' '.join(self.sentences)
            if text_input not in self.data:
                final_solution = 'X'
            else:
                final_solution = list(self.freq_w[text_input].keys())[
                    np.argmax(np.array(list(self.freq_w[text_input].values())))]
            ans = [(text_input, final_solution)]
            return ans
        else:
            for i in result_path:
                text_inp, result_assign_tag = self.Algorithm(i)
                confident = self.count_confident(
                    freq_word_tag, text_inp, result_assign_tag)
                if confident > max_confident:
                    max_confident = confident
                    final_solution = result_assign_tag
                    text_input = text_inp
            if final_solution != -1:
                ans = []
                for i, t in enumerate(final_solution):
                    ans.append((text_input[i], t))
                return ans

    def Algorithm(self, word_segment):
        self.s_label = {}

        # freq_w = tag_counting.cal_P(self.data)
        text_input = []

        for i in range(len(word_segment)-1):
            word = ""
            for j in range(word_segment[i], word_segment[i+1]):
                word = word + self.sentences[j] + " "
            text_input.append(word.rstrip(" "))

        text_input = ['anh', 'anh']+text_input+['anh', 'anh']

        start = 2
        end = len(text_input)

        window = ['anh', 'anh']

        result_tag = []

        P_t1 = {'N': {(None, 'N'): 1}}
        P_t2 = {'N': {(None, None): 1}}

        for i in range(start, end):
            window.append(text_input[i])
            if i-3 < 0:
                assigned_tag_1 = None
            else:
                assigned_tag_1 = result_tag[i-3]

            if i-4 < 0:
                assigned_tag_2 = None
            else:
                assigned_tag_2 = result_tag[i-4]

            P_tag = {}
            Three_tag = []
            Pair_tag = self.generate_2(list(P_t2.keys()), list(P_t1.keys()))

            if window[2] not in self.data:
                self.data[window[2]] = {'X': 1}
                self.freq_w[window[2]]['X'] = 1.0
            for tag in self.data[window[2]]:
                if tag in self.freq_w[window[2]] and self.freq_w[window[2]][tag] != 0:
                    P_w = self.freq_w[window[2]][tag]

                    P_tag[tag] = {}
                    for pair in Pair_tag:
                        if (pair[0], pair[1], tag) in self.proportion:
                            P_c = self.proportion[(
                                pair[0], pair[1], tag)]/tag_counting.countT_2(self.freq_3t, pair, self.total_3t)
                            P_tag[tag][tuple(pair)] = P_w*P_c
                            Three_tag.append(list(pair)+[tag])
                        else:
                            P_tag[tag][tuple(pair)] = 0

            max_P = -1
            for ele in Three_tag:
                t1_t2 = (ele[0], ele[1])
                P1 = P_tag[ele[2]][t1_t2]
                P2 = P_t1[ele[1]][(assigned_tag_1, ele[0])]
                P3 = P_t2[ele[0]][(assigned_tag_2, assigned_tag_1)]
                P_kethop = P1*P2*P3
                if max_P < P_kethop:
                    max_P = P_kethop
                    tag_result = ele[0]

            result_tag.append(tag_result)

            window.pop(0)

            P_t2 = P_t1.copy()
            P_t1 = P_tag.copy()

        text_input.pop(-1)
        text_input.pop(-1)

        return text_input[2:], result_tag[2:]
