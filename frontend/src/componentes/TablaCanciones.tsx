import { useEffect, useState } from "react";
import { obtenerCanciones } from "../servicios/canciones";
import type { Cancion } from "../interfaces/Cancion";

export default function TablaCanciones() {
  const [canciones, setCanciones] = useState<Cancion[]>([]);

  useEffect(() => {
    const fetchCanciones = async () => {
      const dataCanciones = await obtenerCanciones();
      setCanciones(dataCanciones);
    };
    fetchCanciones();
  }, []);
  return (
    <table>
      <thead>
        <tr>
          <th>Título</th>
          <th>Minutos</th>
          <th>Segundos</th>
          <th>Interprete</th>
        </tr>
      </thead>
      <tbody>
        {canciones.map((cancion) => (
          <tr key={cancion.id}>
            <td>{cancion.titulo}</td>
            <td>{cancion.minutos}</td>
            <td>{cancion.segundos}</td>
            <td>{cancion.interprete}</td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}
