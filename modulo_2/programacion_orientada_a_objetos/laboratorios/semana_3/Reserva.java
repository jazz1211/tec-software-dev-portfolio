import java.time.LocalDate;

public class Reserva {
    private int idReserva;
    private LocalDate fechaReserva;
    private LocalDate fechaVencimiento;
    private String estadoReserva;
    private int idLibro;
    private int idUsuario;

    public Reserva() {
    }

    public boolean crearReserva() {
        if (idReserva <= 0 || idLibro <= 0 || idUsuario <= 0 || fechaReserva == null || fechaVencimiento == null) {
            return false;
        }

        estadoReserva = "Pendiente";
        return true;
    }

    public boolean confirmarReserva() {
        if (!"Pendiente".equals(estadoReserva)) {
            return false;
        }

        estadoReserva = "Confirmada";
        return true;
    }

    public boolean cancelarReserva() {
        if ("Cancelada".equals(estadoReserva)) {
            return false;
        }

        estadoReserva = "Cancelada";
        return true;
    }

    public int getIdReserva() {
        return idReserva;
    }

    public void setIdReserva(int idReserva) {
        this.idReserva = idReserva;
    }

    public LocalDate getFechaReserva() {
        return fechaReserva;
    }

    public void setFechaReserva(LocalDate fechaReserva) {
        this.fechaReserva = fechaReserva;
    }

    public LocalDate getFechaVencimiento() {
        return fechaVencimiento;
    }

    public void setFechaVencimiento(LocalDate fechaVencimiento) {
        this.fechaVencimiento = fechaVencimiento;
    }

    public String getEstadoReserva() {
        return estadoReserva;
    }

    public void setEstadoReserva(String estadoReserva) {
        this.estadoReserva = estadoReserva;
    }

    public int getIdLibro() {
        return idLibro;
    }

    public void setIdLibro(int idLibro) {
        this.idLibro = idLibro;
    }

    public int getIdUsuario() {
        return idUsuario;
    }

    public void setIdUsuario(int idUsuario) {
        this.idUsuario = idUsuario;
    }

    @Override
    public String toString() {
        return "Reserva{" +
                "idReserva=" + idReserva +
                ", fechaReserva=" + fechaReserva +
                ", fechaVencimiento=" + fechaVencimiento +
                ", estadoReserva='" + estadoReserva + '\'' +
                ", idLibro=" + idLibro +
                ", idUsuario=" + idUsuario +
                '}';
    }
}
