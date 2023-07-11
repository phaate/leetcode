class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        if k == 0 or k*'B' in blocks:
            return 0
        else:
            i = 0
            min = k
            for i in range(len(blocks)-(i+k-1)):

                curr = 0
                for letter in blocks[i:i + k]:
                    if letter == 'W':
                        curr += 1
                if curr < min:
                    min=curr
                i+=1
        return min


        




if __name__ == '__main__':
    s = Solution()
    print(s.minimumRecolors("WBBWWBBWBW", 7))
