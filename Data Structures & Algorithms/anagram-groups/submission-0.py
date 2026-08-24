class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        htable = defaultdict(list) #makes default value a list
    
        for word in strs:
            count = [0] * 26 #create empty list that can count the number of letters in word

            for c in word:
                count[ord(c)-ord("a")] +=1 #adds count of letter for every letter in count

            htable[tuple(count)].append(word) #add word to list of values of a certain count
        
        return htable.values()