import unittest
import go_solver

class GoSolverTests(unittest.TestCase):

    def setUp(self):
        self.board = go_solver.build_empty_board() # generate an empty board for each test
        go_solver.memory = {} # reset memory before each test

    
    def test_Out_Of_Range_Positions_Are_Dead(self):
        
        self.assertTrue(go_solver.is_dead(self.board, (-1, 0)))
        self.assertTrue(go_solver.is_dead(self.board, (0, -1)))
        self.assertTrue(go_solver.is_dead(self.board, (19, 0)))
        self.assertTrue(go_solver.is_dead(self.board, (0, 19)))
        
    def test_Empty_Positions_Are_Dead(self):
        self.assertTrue(go_solver.is_dead(self.board, (3,3)))

    def test_Stone_With_No_Surrounding_Stones_Are_Alive(self):
        self.board[3][3] = "b"
        position = (3,3)

        result = go_solver.is_dead(self.board, position)

        self.assertFalse(result)

    def test_Stone_Surrounded_With_Enemies_Is_Dead(self):
        self.board[3][3] = "b" # surrounded by 4 enemies
        self.board[2][3] = "w"
        self.board[3][2] = "w"
        self.board[4][3] = "w"
        self.board[3][4] = "w" # no surrounding enemies; neighboring friend
        position = (3,3)

        result = go_solver.is_dead(self.board, position)

        self.assertTrue(result)

    def test_Stone_Group_Nearly_Surrounded_With_Enemies_Is_Alive(self):
        self.board[3][3] = "b" # surrounded by 3 enemies
        self.board[2][3] = "w"
        self.board[3][2] = "w"
        self.board[4][3] = "w"
        self.board[3][4] = "b" # no surrounding enemies; neighboring friend
        position = (3,3)

        result = go_solver.is_dead(self.board, position)

        self.assertFalse(result)

    def test_Stone_Large_Group_Nearly_Surrounded_With_Enemies_Is_Alive(self):
        self.board[3][3] = "b" # surrounded by 3 enemies
        self.board[2][3] = "w"
        self.board[3][2] = "w"
        self.board[4][3] = "w"
        self.board[3][4] = "b" # 1 surrounding enemy; 3 neighboring friends
        self.board[3][5] = "w"
        self.board[2][4] = "b" # 1 friend; 1 ememy
        self.board[4][4] = "b" # 1 friend; 1 enemy

        position = (3,3)

        result = go_solver.is_dead(self.board, position)

        self.assertFalse(result)


# if __name__ == '__main__':
#     unittest.main()