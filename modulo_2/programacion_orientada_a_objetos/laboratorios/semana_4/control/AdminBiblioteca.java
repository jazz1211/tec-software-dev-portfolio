package control;

import java.util.ArrayList;
import java.util.Collection;
import java.util.Iterator;

public class AdminBiblioteca {

    private Collection<Libro> listaLibros;

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

        Iterator<Libro> iterator = listaLibros.iterator();
        while (iterator.hasNext()) {
            if (iterator.next().getIdLibro() == libro.getIdLibro()) {
                iterator.remove();
                listaLibros.add(libro);
                return true;
            }
        }
        return false;
    }

    public boolean eliminar(int id) {
        Iterator<Libro> iterator = listaLibros.iterator();
        while (iterator.hasNext()) {
            if (iterator.next().getIdLibro() == id) {
                iterator.remove();
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
