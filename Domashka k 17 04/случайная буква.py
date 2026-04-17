from collections import deque


class Node:
    def __init__(self):
        self.children = {}
        self.to = {}
        self.sufflink = None
        self.compressed_sufflink = None
        self.output = None


class AhoCorasick:
    def __init__(self):
        self.root = Node()

    def add(self, s):
        v = self.root
        for c in s:
            if c in v.children:
                v = v.children[c]
            else:
                new_v = Node()
                v.children[c] = new_v
                v = new_v
        v.output = s

    def build_trie(self, words):
        for word in words:
            self.add(word)
        self.build_links()

    def build_links(self):
        queue = deque()
        self.root.sufflink = self.root
        self.root.compressed_sufflink = self.root
        for char in alphabet:
            if char in self.root.children:
                self.root.to[char] = self.root.children[char]
            else:
                self.root.to[char] = self.root
        for i in self.root.children:
            cur = self.root.children[i]
            cur.sufflink = self.root
            cur.compressed_sufflink = self.root
            queue.append(cur)
        while queue:
            current = queue.popleft()
            for char in alphabet:
                if char in current.children:
                    current.to[char] = current.children[char]
                else:
                    current.to[char] = current.sufflink.to[char]
            for i in current.children:
                current_child = current.children[i]
                current_child.sufflink = current.sufflink.to[i]
                queue.append(current_child)
                if current_child.sufflink.output:
                    current_child.compressed_sufflink = current_child.sufflink
                else:
                    current_child.compressed_sufflink = current_child.sufflink.compressed_sufflink

    def find(self, text):
        cur_node = self.root
        result = {}

        for i, char in enumerate(text):
            cur_node = cur_node.to[char]
            temp = cur_node
            while temp != self.root:
                if temp.output:
                    if temp.output in result:
                        result[temp.output].add(i)
                    else:
                        result[temp.output] = {i}
                temp = temp.compressed_sufflink
        return result


S = AhoCorasick()
inp = list(input().split("?"))
s = str()
for i in inp:
    s += i
alphabet = sorted(set(s))
S.build_trie(inp)
T = input()
right_Index = S.find(T)

marks = []
for w in right_Index:
    for r in right_Index[w]:
        l = r - len(w) + 1
        marks.append((l, r, w))
marks.sort()
left, right = 0,0
count = 0
while right < len(T)+1:
    counted = []
    counted1 = []
    flag = True
    for i in range(len(marks)):
        if left<=marks[i][0] and marks[i][1] <= right:
            if counted == []:
                counted.append(marks[i])
                counted1.append(marks[i][2])
            else:
                if marks[i][0] - counted[-1][1] == 2:
                    counted.append(marks[i])
                    counted1.append(marks[i][2])
    if inp != counted1:
        flag = False
    if flag or set(inp).issubset(set(counted1)):
        left += 1
    if flag:
        count += 1
    else:
        right += 1
print(count)
