package control;

import java.util.ArrayList;
import java.util.Collection;
import java.util.List;
import modelo.Libro;

public class AdminBiblioteca {
    private final List<Libro> listaLibros;

    public AdminBiblioteca() {
        listaLibros = new ArrayList<>();
    }

    public boolean agregar(Libro libro) {
        if (libro == null || consultarExistencia(libro.getIdLibro())) {
            return false;
        }
        return listaLibros.add(libro);
    }

    public Libro consultar(int id) {
        for (Libro libro : listaLibros) {
            if (libro.getIdLibro() == id) {
                return libro;
            }
        }
        return null;
    }

    public boolean consultarExistencia(int id) {
        return consultar(id) != null;
    }

    public boolean modificar(Libro libro) {
        if (libro == null) {
            return false;
        }

        for (int i = 0; i < listaLibros.size(); i++) {
            if (listaLibros.get(i).getIdLibro() == libro.getIdLibro()) {
                listaLibros.set(i, libro);
                return true;
            }
        }
        return false;
    }

    public boolean eliminar(int id) {
        for (int i = 0; i < listaLibros.size(); i++) {
            if (listaLibros.get(i).getIdLibro() == id) {
                listaLibros.remove(i);
                return true;
            }
        }
        return false;
    }

    public int retornarTotal() {
        return listaLibros.size();
    }

    public Collection<Libro> buscarPorTitulo(String titulo) {
        Collection<Libro> resultados = new ArrayList<>();

        if (titulo == null) {
            return resultados;
        }

        for (Libro libro : listaLibros) {
            if (libro.getTitulo() != null
                    && libro.getTitulo().equalsIgnoreCase(titulo)) {
                resultados.add(libro);
            }
        }
        return resultados;
    }

    public Collection<Libro> buscarPorAutor(String autor) {
        Collection<Libro> resultados = new ArrayList<>();

        if (autor == null) {
            return resultados;
        }

        for (Libro libro : listaLibros) {
            if (libro.getAutor() != null
                    && libro.getAutor().equalsIgnoreCase(autor)) {
                resultados.add(libro);
            }
        }
        return resultados;
    }

    public boolean consultarDisponibilidad(int id) {
        Libro libro = consultar(id);
        return libro != null && libro.consultarDisponibilidad();
    }

    @Override
    public String toString() {
        return "AdminBiblioteca{lista=" + listaLibros + '}';
    }
}
