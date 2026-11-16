package vista;

import control.AdminBiblioteca;
import java.time.LocalDate;
import java.util.Collection;
import modelo.Libro;

public class Lab5_JazminAlfaro {

    public static void main(String[] args) {
        AdminBiblioteca admin = new AdminBiblioteca();

        Libro libro1 = new Libro(
                1, "Pedro Páramo", "Juan Rulfo", 128,
                LocalDate.of(1955, 1, 1), true);

        Libro libro2 = new Libro(
                2, "Ensayo sobre la ceguera", "José Saramago", 352,
                LocalDate.of(1995, 1, 1), false);

        // Autor y fecha ilustrativos: ajustarlos según la edición utilizada.
        Libro libro3 = new Libro(
                3, "El cielo de la selva", "Autor por confirmar", 200,
                LocalDate.of(2020, 1, 1), true);

        Libro duplicado = new Libro(
                1, "Libro duplicado", "Autor de prueba", 100,
                LocalDate.of(2020, 1, 1), true);

        System.out.println("=== AGREGAR ===");
        mostrarAgregar(admin, libro1);
        mostrarAgregar(admin, libro2);
        mostrarAgregar(admin, libro3);
        mostrarAgregar(admin, duplicado);
        mostrarAgregar(admin, null);

        System.out.println("\n=== CONSULTAR ===");
        mostrarLibro(admin, 1);
        mostrarLibro(admin, 99);

        System.out.println("\n=== CONSULTAR EXISTENCIA ===");
        mostrarExistencia(admin, 1);
        mostrarExistencia(admin, 99);

        System.out.println("\n=== MODIFICAR ===");
        Libro actualizado = new Libro(
                1, "Pedro Páramo", "Juan Rulfo", 150,
                LocalDate.of(1955, 1, 1), false);

        Libro inexistente = new Libro(
                99, "No registrado", "Autor de prueba", 50,
                LocalDate.of(2020, 1, 1), true);

        mostrarModificar(admin, actualizado);
        mostrarLibro(admin, 1);
        mostrarModificar(admin, inexistente);
        mostrarModificar(admin, null);

        System.out.println("\n=== BUSCAR POR TÍTULO ===");
        buscarTitulo(admin, "PEDRO PÁRAMO");
        buscarTitulo(admin, "Título inexistente");
        buscarTitulo(admin, null);

        System.out.println("\n=== BUSCAR POR AUTOR ===");
        buscarAutor(admin, "JOSÉ SARAMAGO");
        buscarAutor(admin, "Autor inexistente");
        buscarAutor(admin, null);

        System.out.println("\n=== DISPONIBILIDAD ===");
        mostrarDisponibilidad(admin, 1);
        mostrarDisponibilidad(admin, 3);
        mostrarDisponibilidad(admin, 99);

        System.out.println("\n=== ELIMINAR ===");
        mostrarEliminar(admin, 2);
        mostrarEliminar(admin, 2);

        System.out.println("\n=== RESULTADO FINAL ===");
        System.out.println("Total de libros restantes: " + admin.retornarTotal());
        System.out.println("Contenido final: " + admin);
    }

    private static void mostrarAgregar(AdminBiblioteca admin, Libro libro) {
        boolean resultado = admin.agregar(libro);

        if (resultado) {
            System.out.println("- Libro agregado: " + libro.getTitulo());
        } else if (libro == null) {
            System.out.println("- No se agregó el libro porque es nulo.");
        } else {
            System.out.println("- No se agregó el libro: el ID " + libro.getIdLibro() + " ya existe.");
        }
    }

    private static void mostrarLibro(AdminBiblioteca admin, int id) {
        Libro libro = admin.consultar(id);

        if (libro != null) {
            System.out.println("- Libro encontrado: " + libro);
        } else {
            System.out.println("- No existe un libro con ID " + id + ".");
        }
    }

    private static void mostrarExistencia(AdminBiblioteca admin, int id) {
        if (admin.consultarExistencia(id)) {
            System.out.println("- Sí existe un libro con ID " + id + ".");
        } else {
            System.out.println("- No existe un libro con ID " + id + ".");
        }
    }

    private static void mostrarModificar(AdminBiblioteca admin, Libro libro) {
        boolean resultado = admin.modificar(libro);

        if (resultado) {
            System.out.println("- Libro modificado: ID " + libro.getIdLibro() + ".");
        } else if (libro == null) {
            System.out.println("- No se modificó el libro porque es nulo.");
        } else {
            System.out.println("- No se modificó el libro: no existe el ID " + libro.getIdLibro() + ".");
        }
    }

    private static void buscarTitulo(AdminBiblioteca admin, String titulo) {
        Collection<Libro> resultados = admin.buscarPorTitulo(titulo);

        if (titulo == null) {
            System.out.println("- No se puede buscar: el título es nulo.");
        } else {
            mostrarResultados("título", titulo, resultados);
        }
    }

    private static void buscarAutor(AdminBiblioteca admin, String autor) {
        Collection<Libro> resultados = admin.buscarPorAutor(autor);

        if (autor == null) {
            System.out.println("- No se puede buscar: el autor es nulo.");
        } else {
            mostrarResultados("autor", autor, resultados);
        }
    }

    private static void mostrarResultados(
            String tipo, String valor, Collection<Libro> libros) {
        if (libros.isEmpty()) {
            System.out.println("- No se encontraron libros con "
                    + tipo + " \"" + valor + "\".");
        } else {
            for (Libro libro : libros) {
                System.out.println("- Encontrado por " + tipo + ": " + libro);
            }
        }
    }

    private static void mostrarDisponibilidad(AdminBiblioteca admin, int id) {
        if (!admin.consultarExistencia(id)) {
            System.out.println("- No existe un libro con ID " + id + ".");
        } else if (admin.consultarDisponibilidad(id)) {
            System.out.println("- El libro con ID " + id + " está disponible.");
        } else {
            System.out.println("- El libro con ID " + id + " no está disponible.");
        }
    }

    private static void mostrarEliminar(AdminBiblioteca admin, int id) {
        if (admin.eliminar(id)) {
            System.out.println("- Se eliminó el libro con ID " + id + ".");
        } else {
            System.out.println("- No se eliminó el libro: no existe el ID "+ id + ".");
        }
    }
}
