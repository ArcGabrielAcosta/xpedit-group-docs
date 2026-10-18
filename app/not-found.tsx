import Link from "next/link";

export default function NotFound() {
  return (
    <div className="not-found">
      <p className="eyebrow">404</p>
      <h1>Ese documento no está</h1>
      <p>El enlace no coincide con ningún archivo de la investigación.</p>
      <Link href="/" className="button">
        Volver al índice
      </Link>
    </div>
  );
}
