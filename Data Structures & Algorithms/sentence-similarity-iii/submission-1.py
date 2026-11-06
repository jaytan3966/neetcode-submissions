class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        words1 = sentence1.split()
        words2 = sentence2.split()

        if len(words1)<len(words2):
            words1, words2 = words2, words1
        
        if len(words1) == len(words2):
            return words1 == words2
        indices1 = {word: i for i, word in enumerate(words1)}
        indices2 = {word: i for i, word in enumerate(words2)}

        started = False
        ended = False
        for word in indices1:
            if word not in indices2:
                if ended: return False
                started = True
            else:
                if started:
                    ended = True
        
        for word in indices2:
            if word not in indices1:
                return False
        return True