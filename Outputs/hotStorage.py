class Store:
    def __init__(self):
        self.boards = []

    def add(self, board, score):
        """
        Add a board to the store.
        
        Args:
            board: The board to add.
        """
        self.boards.append((board, score))
    
    def checkMatch(self, board):
        """
        Check if a board is already in the store.
        
        Args:
            board: The board to check.
        
        Returns:
            bool: True if the board is in the store, False otherwise.
        """
        for stored_board in self.boards:
            if stored_board[0] == board:
                return True
        return False
    
    def getBoards(self):
        """
        Get all boards in the store.
        
        Returns:
            list: A list of boards in the store.
        """
        return self.boards