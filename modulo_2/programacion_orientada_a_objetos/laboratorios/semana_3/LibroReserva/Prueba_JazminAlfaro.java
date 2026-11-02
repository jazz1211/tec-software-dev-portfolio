import java.time.LocalDate;

public class Prueba_JazminAlfaro {
    public static void main(String[] args) {
        Libro libro = new Libro();
        Reserva reserva = new Reserva();

        libro.setIdLibro(1);
        libro.setTitulo("1984");
        libro.setAutor("George Orwell");
        libro.setCantPaginas(328);
        libro.setFechaPublicacion(LocalDate.of(1949, 6, 8));
        libro.setEstado(true);

        reserva.setIdReserva(1);
        reserva.setFechaReserva(LocalDate.of(2026, 11, 1));
        reserva.setFechaVencimiento(LocalDate.of(2026, 11, 8));
        reserva.setIdLibro(libro.getIdLibro());
        reserva.setIdUsuario(100);

        if (!reserva.crearReserva()) {
            System.out.println("No se pudo crear la reserva.");
        }

        System.out.println("Datos del libro:");
        System.out.println(libro);

        System.out.println("\nDatos de la reserva:");
        System.out.println(reserva);
    }
}
