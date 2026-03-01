import type { Cancion } from "../interfaces/Cancion";

export async function obtenerCanciones(): Promise<Cancion[]> {
  const response = await fetch("http://localhost:8000/canciones");
  const data = await response.json();
  return data;
}
