# tests/test_game.py
# [...]
    def test_unknown_word_is_invalid(self):
      new_game = Game()
      new_game.grid = list('KWIENFUQW') # Forcer la grille à un scénario de test :
      self.assertIs(new_game.is_valid('FEUN'), False)