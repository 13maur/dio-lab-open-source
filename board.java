import java.util.*;

// Modelo (Task)
class Task {
    private int id;
    private String title;
    private String description;
    private String status;

    // Construtor
    public Task(int id, String title, String description, String status) {
        this.id = id;
        this.title = title;
        this.description = description;
        this.status = status;
    }

    // Getters e Setters
    public int getId() { return id; }
    public String getTitle() { return title; }
    public String getDescription() { return description; }
    public String getStatus() { return status; }

    public void setStatus(String status) { this.status = status; }

    @Override
    public String toString() {
        return "ID: " + id + ", Title: " + title + ", Status: " + status;
    }
}

// Repositório (TaskRepository)
class TaskRepository {
    private List<Task> tasks = new ArrayList<>();
    private int nextId = 1;

    // Método para salvar uma tarefa
    public void save(Task task) {
        task = new Task(nextId++, task.getTitle(), task.getDescription(), task.getStatus());
        tasks.add(task);
    }

    // Método para excluir uma tarefa
    public void delete(int id) {
        tasks.removeIf(task -> task.getId() == id);
    }

    // Método para encontrar todas as tarefas
    public List<Task> findAll() {
        return tasks;
    }

    // Método para encontrar tarefa por ID
    public Task findById(int id) {
        return tasks.stream().filter(task -> task.getId() == id).findFirst().orElse(null);
    }
}

// Serviço (TaskService)
class TaskService {
    private TaskRepository repository;

    public TaskService(TaskRepository repository) {
        this.repository = repository;
    }

    // Método para adicionar uma tarefa
    public void addTask(String title, String description, String status) {
        Task task = new Task(0, title, description, status);  // O ID será gerado no repository
        repository.save(task);
    }

    // Método para listar todas as tarefas
    public List<Task> listTasks() {
        return repository.findAll();
    }

    // Método para excluir tarefa
    public void removeTask(int id) {
        repository.delete(id);
    }

    // Método para atualizar o status de uma tarefa
    public void updateTaskStatus(int id, String newStatus) {
        Task task = repository.findById(id);
        if (task != null) {
            task.setStatus(newStatus);
        }
    }
}

// Controlador (TaskController)
class TaskController {
    private TaskService service;

    public TaskController(TaskService service) {
        this.service = service;
    }

    // Exibir as tarefas
    public void listTasks() {
        List<Task> tasks = service.listTasks();
        if (tasks.isEmpty()) {
            System.out.println("Nenhuma tarefa encontrada.");
        } else {
            tasks.forEach(System.out::println);
        }
    }

    // Criar nova tarefa
    public void createTask(String title, String description, String status) {
        service.addTask(title, description, status);
        System.out.println("Tarefa criada com sucesso!");
    }

    // Excluir tarefa
    public void deleteTask(int id) {
        service.removeTask(id);
        System.out.println("Tarefa excluída com sucesso!");
    }

    // Atualizar o status de uma tarefa
    public void updateTaskStatus(int id, String newStatus) {
        service.updateTaskStatus(id, newStatus);
        System.out.println("Status da tarefa atualizado!");
    }
}

// Classe Principal (UI)
public class Main {
    public static void main(String[] args) {
        // Inicializando as camadas
        TaskRepository repository = new TaskRepository();
        TaskService service = new TaskService(repository);
        TaskController controller = new TaskController(service);

        Scanner scanner = new Scanner(System.in);

        while (true) {
            System.out.println("\n--- Board de Tarefas ---");
            System.out.println("1. Criar Tarefa");
            System.out.println("2. Listar Tarefas");
            System.out.println("3. Excluir Tarefa");
            System.out.println("4. Atualizar Status");
            System.out.println("5. Sair");
            System.out.print("Escolha uma opção: ");
            int option = scanner.nextInt();
            scanner.nextLine();  // Consumir a linha após o número

            switch (option) {
                case 1:
                    System.out.print("Título da tarefa: ");
                    String title = scanner.nextLine();
                    System.out.print("Descrição da tarefa: ");
                    String description = scanner.nextLine();
                    System.out.print("Status da tarefa: ");
                    String status = scanner.nextLine();
                    controller.createTask(title, description, status);
                    break;

                case 2:
                    controller.listTasks();
                    break;

                case 3:
                    System.out.print("ID da tarefa a ser excluída: ");
                    int deleteId = scanner.nextInt();
                    controller.deleteTask(deleteId);
                    break;

                case 4:
                    System.out.print("ID da tarefa a ser atualizada: ");
                    int updateId = scanner.nextInt();
                    scanner.nextLine();  // Consumir a linha
                    System.out.print("Novo status da tarefa: ");
                    String newStatus = scanner.nextLine();
                    controller.updateTaskStatus(updateId, newStatus);
                    break;

                case 5:
                    System.out.println("Saindo...");
                    scanner.close();
                    return;

                default:
                    System.out.println("Opção inválida!");
            }
        }
    }
}
