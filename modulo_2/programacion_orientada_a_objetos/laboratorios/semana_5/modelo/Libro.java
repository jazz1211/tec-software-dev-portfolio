package modelo;

import java.time.LocalDate;

public class Libro {
    private final int idLibro;
    private String titulo;
    private String autor;
    private int cantPaginas;
    private LocalDate fechaPublicacion;
    private boolean estado;

    public Libro() {
        this(0, null, null, 0, null, false);
    }

    public Libro(int idLibro, String titulo, String autor,
                 int cantPaginas, LocalDate fechaPublicacion,
                 boolean estado) {
        this.idLibro = idLibro;
        this.titulo = titulo;
        this.autor = autor;
        this.cantPaginas = cantPaginas;
        this.fechaPublicacion = fechaPublicacion;
        this.estado = estado;
    }

    public int getIdLibro() {
        return idLibro;
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
    public boolean equals(Object objeto) {
        if (this == objeto) {
            return true;
        }
        if (!(objeto instanceof Libro)) {
            return false;
        }
        Libro otro = (Libro) objeto;
        return idLibro == otro.idLibro;
    }

    @Override
    public int hashCode() {
        return Integer.hashCode(idLibro);
    }

    @Override
    public String toString() {
        return "Libro{"
                + "id=" + idLibro
                + ", titulo='" + titulo + '\''
                + ", autor='" + autor + '\''
                + ", paginas=" + cantPaginas
                + ", fechaPublicacion=" + fechaPublicacion
                + ", disponible=" + estado
                + '}';
    }
}
