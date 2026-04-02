class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def checkContain(nums):
            seen = set()
            for num in nums:
                if num != '.':
                    if num in seen:
                        return False
                    seen.add(num)
            return True
        columns = [[] for _ in range(9)]
        boxs = [[] for _ in range(9)]
        for i in range(9):
            # check row
            if not checkContain(board[i]): return False
            for j in range(9):
                # check column
                columns[j].append(board[i][j])
                boxs[i//3*3 + j//3].append(board[i][j])
        # check box
        for col in columns:
            if not checkContain(col): return False
        for box in boxs:
            if not checkContain(box): return False
        return True