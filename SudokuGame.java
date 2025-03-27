import java.util.Scanner;

public class SudokuGame {

    public static void main(String[] args) {
        SudokuGame game = new SudokuGame();
        game.startGame();
    }

    // Classe Cell representa uma célula do Sudoku
    static class Cell {
        private int value; // valor da célula (0 indica célula vazia)
        private boolean isFixed; // indica se a célula tem valor fixo ou não

        public Cell(int value, boolean isFixed) {
            this.value = value;
            this.isFixed = isFixed;
        }

        public int getValue() {
            return value;
        }

        public void setValue(int value) {
            if (!isFixed) {
                this.value = value;
            } else {
                System.out.println("Esta célula é fixa e não pode ser alterada!");
            }
        }

        public boolean isFixed() {
            return isFixed;
        }

        public void setFixed(boolean fixed) {
            isFixed = fixed;
        }

        @Override
        public String toString() {
            return value == 0 ? "." : String.valueOf(value); // Exibe "." para células vazias
        }
    }

    // Classe Board representa o tabuleiro do Sudoku
    static class Board {
        private Cell[][] board;

        public Board() {
            board = new Cell[9][9];
            initializeBoard();
        }

        private void initializeBoard() {
            for (int row = 0; row < 9; row++) {
                for (int col = 0; col < 9; col++) {
                    board[row][col] = new Cell(0, false); // Inicializa todas as células como vazias
                }
            }
        }

        // Configura o valor de uma célula, se a jogada for válida
        public void setCell(int row, int col, int value) {
            if (isValidMove(row, col, value)) {
                board[row][col].setValue(value);
            } else {
                System.out.println("Jogada inválida!");
            }
        }

        // Verifica se a jogada é válida
        public boolean isValidMove(int row, int col, int value) {
            return !isInRow(row, value) && !isInCol(col, value) && !isInSubgrid(row, col, value);
        }

        // Verifica se o valor já está na linha
        private boolean isInRow(int row, int value) {
            for (int col = 0; col < 9; col++) {
                if (board[row][col].getValue() == value) {
                    return true;
                }
            }
            return false;
        }

        // Verifica se o valor já está na coluna
        private boolean isInCol(int col, int value) {
            for (int row = 0; row < 9; row++) {
                if (board[row][col].getValue() == value) {
                    return true;
                }
            }
            return false;
        }

        // Verifica se o valor já está no subgrid 3x3
        private boolean isInSubgrid(int row, int col, int value) {
            int startRow = row / 3 * 3;
            int startCol = col / 3 * 3;
            for (int i = startRow; i < startRow + 3; i++) {
                for (int j = startCol; j < startCol + 3; j++) {
                    if (board[i][j].getValue() == value) {
                        return true;
                    }
                }
            }
            return false;
        }

        // Imprime o tabuleiro
        public void printBoard() {
            for (int row = 0; row < 9; row++) {
                for (int col = 0; col < 9; col++) {
                    System.out.print(board[row][col] + " ");
                }
                System.out.println();
            }
        }

        // Verifica se o tabuleiro está completo
        public boolean isBoardFull() {
            for (int row = 0; row < 9; row++) {
                for (int col = 0; col < 9; col++) {
                    if (board[row][col].getValue() == 0) {
                        return false;
                    }
                }
            }
            return true;
        }
    }

    // Classe principal que controla o jogo
    private Board board;
    private Scanner scanner;

    public SudokuGame() {
        board = new Board();
        scanner = new Scanner(System.in);
    }

    // Inicia o jogo
    public void startGame() {
        System.out.println("Bem-vindo ao Sudoku!");
        while (true) {
            board.printBoard();
            if (board.isBoardFull()) {
                System.out.println("Parabéns! Você resolveu o Sudoku!");
                break;
            }
            System.out.println("Digite a linha (0-8), coluna (0-8) e valor (1-9) separados por espaços:");
            int row = scanner.nextInt();
            int col = scanner.nextInt();
            int value = scanner.nextInt();

            board.setCell(row, col, value);
        }
    }
}
