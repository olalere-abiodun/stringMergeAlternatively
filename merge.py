class Solution:
    def __init__(self, word1: str, word2: str) -> None:
        self.word1 = word1
        self.word2 = word2

    def mergeAlternately(self) -> str:
        merged = ''
        min_len = min(len(self.word1), len(self.word2))

        for i in range(min_len):
            merged += self.word1[i] + " " + self.word2[i] + " "

        if len(self.word1) > min_len:
            merged += " ".join(self.word1[min_len:])
        elif len(self.word2) > min_len:
            merged += " ".join(self.word2[min_len:])

        return merged


word1 = "class"
word2 = "pq"
merger = Solution(word1, word2)
merged_result = merger.mergeAlternately()
print(merged_result)

word1 = "ab"
word2 = "pqrs"
merger = Solution(word1, word2)
merged_result2 = merger.mergeAlternately()
print(merged_result2)

# class Solution:
#     def mergeAlternately(self, word1, word2):
           
#         merged = ''
#         min_len = min(len(word1), len(word2))

#         for i in range(min_len):
#             merged += word1[i] + word2[i]

#         if len(word1) > min_len:
#             merged += "".join(word1[min_len:])
#         elif len(word2) > min_len:
#             merged += "".join(word2[min_len:])

#         return merged

# word1 = "ab"
# word2 = "pqrs"
# solution = Solution()
# merged_result = solution.mergeAlternately(word1, word2)
# print(merged_result)
