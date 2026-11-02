import java.time.LocalDate;

public class Libro {
    private int idLibro;
    private String titulo;
    private String autor;
    private int cantPaginas;
    private LocalDate fechaPublicacion;
    private boolean estado;

    public Libro() {
    }

    public int getIdLibro() {
        return idLibro;
    }

    public void setIdLibro(int idLibro) {
        this.idLibro = idLibro;
    }

    public String getTitulo() {
        return titulo;
    }

    public void setTitulo(String titulo) {
        this.titulo = titulo;
    }

    public String getAutor() {
        return autor;
    }

    public void setAutor(String autor) {
        this.autor = autor;
    }

    public int getCantPaginas() {
        return cantPaginas;
    }

    public void setCantPaginas(int cantPaginas) {
        this.cantPaginas = cantPaginas;
    }

    public LocalDate getFechaPublicacion() {
        return fechaPublicacion;
    }

    public void setFechaPublicacion(LocalDate fechaPublicacion) {
        this.fechaPublicacion = fechaPublicacion;
    }

    public boolean getEstado() {
        return estado;
    }

    public void setEstado(boolean estado) {
        this.estado = estado;
    }

    public boolean consultarDisponibilidad() {
        return estado;
    }

    @Override
    public String toString() {
        return "Libro{" +
                "idLibro=" + idLibro +
                ", titulo='" + titulo + '\'' +
                ", autor='" + autor + '\'' +
                ", cantPaginas=" + cantPaginas +
                ", fechaPublicacion=" + fechaPublicacion +
                ", estado=" + estado +
                '}';
    }
}
