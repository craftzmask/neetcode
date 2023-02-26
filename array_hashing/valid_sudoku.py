class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        for r in range(len(board)):
            for c in range(len(board)):
                cell = board[r][c]

                if cell == '.':
                    continue
                elif cell in rows[r]:
                    return False
                elif cell in cols[c]:
                    return False
                elif cell in boxes[(r // 3, c // 3)]:
                    return False

                rows[r].add(cell)
                cols[c].add(cell)
                boxes[(r // 3, c // 3)].add(cell)

        return True