from collections import deque
alphabet = "ab"

class Node:
    def __init__(self):
        self.children = {}
        self.to = {}
        self.sufflink = None
        self.compressed_sufflink = None
        self.output = None

class AhoCorasick:
    def __init__(self):
        self.root  = Node()


    def add(self,s):
        v = self.root
        for c in s:
            if c in v.children:
                v = v.children[c]
            else:
                new_v = Node()
                v.children[c] = new_v
                v = new_v

        v.output = s

    def delete(self,s):
        v = self.root
        for c in s:
            if c not in v.children:
                print("Этого слова итак нет в словаре")
                return False
            v = v.children[c]
        v.output = None
        return True


    def build_trie(self,words):
        for word in words:
            self.add(word)
        self.build_links()

    def build_links(self):
        queue = deque()
        self.root.sufflink = self.root
        self.root.compressed_sufflink = self.root
        for char in alphabet:
            if char  in self.root.children:
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
                if current_child.sufflink.output is not None:
                    current_child.compressed_sufflink = current_child.sufflink
                else:
                    current_child.compressed_sufflink = current_child.sufflink.compressed_sufflink

    def find(self,text):
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

    def find_min(self,words,L):
        for word in words:
            self.add(word)
        self.build_links()
        def dfs(start,word,L):
            if len(word) == L:
                return word
            for i in alphabet:
                if not start.to[i].output and not start.to[i].compressed_sufflink.output:
                    res = dfs(start.to[i],word+i,L)
                    if res:
                        return res
                return False
            return dfs(self.root,"",L)