from typing import List


# class Solution:
#     def findRelativeRanks(self, score: List[int]) -> List[str]:
#         topscores = sorted(score, reverse=True)
#         places = {topscores[0]: "Gold Medal"}
#         for i in range(0, len(topscores)):
#             if i == 1:
#                 places.setdefault(topscores[i], "Silver Medal")
#             elif i == 2:
#                 places.setdefault(topscores[i], "Bronze Medal")
#             else:
#                 places.setdefault(topscores[i], str(i+1))
        
#         return [places[x] for x in score]

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        i = 0
        places = {}
        for x in sorted(score, reverse=True):
            if i == 0:
                places[x] = "Gold Medal"
            elif i == 1:
                places[x] = "Silver Medal"
            elif i == 2:
                places[x] = "Bronze Medal"
            else:
                places[x] = str(i+1)
            i +=1
        
        return [places[x] for x in score]


        

a = Solution()
print(a.findRelativeRanks([10,3,8,9,4]))