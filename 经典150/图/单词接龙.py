from collections import deque


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set=set(wordList)
        if endWord not in word_set:
            return 0
        queue=deque()
        queue.append((beginWord,1))

        visited=set()
        visited.add(beginWord)

        word_len=len(beginWord)

        while queue:
            word,step=queue.popleft()
            for i in range(word_len):
                for x in 'abcdefghijklmnopqrstuvwxyz':
                    if word[i]==x:
                        continue
                    new_word=word[:i]+x+word[i+1:]
                    if new_word==endWord:
                        return step+1
                    if new_word in word_set and new_word not in visited:
                        queue.append((new_word,step+1))
                        visited.add(new_word)
        return 0