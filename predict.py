import operator

class DataSetFile:
    def __init__(self, dataPath):
        self.path = dataPath
        self.file = open(self.path, "r")

    def buildDataSet(self):
        return self.file.read()


class Solution:
    def __init__(self):
        self.preWordMap = {}
        self.nextWordMap = {}

    def __getSortedWords(self, wordMap: dict):
        # return {k: v for k, v in sorted(wordMap.items(), key=lambda item: item[1], reverse=True)}
        return {k: v for k, v in sorted(wordMap.items(), key=operator.itemgetter(1), reverse=True)}

    def __clarifyWord(self, data: str, index: int):
        return data[index] if 0 <= index < len(data) else '\n'

    def __cleanUselessWord(self, wordMap: dict):
        if '\t' in wordMap:
            wordMap.pop('\t')
        if '\n' in wordMap:
            wordMap.pop('\n')

    def findMostPossibleWord(self, data: str, target: str):
        index = data.find(target)
        dataSize = len(data)

        # Count the words
        while index != -1:
            # Get the index of words
            preIndex = index - 1
            nextIndex = index + len(target)

            # Get the words
            preWord = self.__clarifyWord(data, preIndex)
            nextWord = self.__clarifyWord(data, nextIndex)

            # Accumulate the counter
            if preWord not in self.preWordMap:
                self.preWordMap[preWord] = 0
            self.preWordMap[preWord] += 1
            if nextWord not in self.nextWordMap:
                self.nextWordMap[nextWord] = 0
            self.nextWordMap[nextWord] += 1

            # Find next target
            index = data.find(target, nextIndex, dataSize - 1)

        # Clear useless word
        self.__cleanUselessWord(self.preWordMap)
        self.__cleanUselessWord(self.nextWordMap)

        famousPreWords = self.__getSortedWords(self.preWordMap)
        famousNextWords = self.__getSortedWords(self.nextWordMap)

        return famousPreWords, famousNextWords


# path = input()
target = input()

dataFile = DataSetFile('Gossiping-QA-Dataset.txt')
# dataFile = DataSetFile(path)
data = dataFile.buildDataSet()
solution = Solution()
preWords, nextWords = solution.findMostPossibleWord(data, target)

# print(preWords)
# print(nextWords)

print('熱門前一個字:')

i = 0
for k, v in preWords.items():
    if i >= 10:
        break
    print("{}---{}".format(k, target))
    i += 1

print("熱門下一個字:")

i = 0
for k, v in nextWords.items():
    if i >= 10:
        break
    print("{}---{}".format(target, k))
    i += 1
