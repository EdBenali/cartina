from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0 for i in temperatures]

        for i, t in enumerate(temperatures):
            count = 1
            while i + count < len(temperatures):
                if t < temperatures[i + count]:
                    answer[i] = count
                    break

                count += 1

        return answer


if __name__ == "__main__":
    Solution().dailyTemperatures([73,74,75,71,69,72,76,73])
