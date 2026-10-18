import Link from "next/link";
import { sections } from "@/lib/catalog";

export default function HomePage() {
  return (
    <div className="home">
      <header className="hero">
        <p className="eyebrow">Investigación de mercado</p>
        <h1>Xpedit Group</h1>
        <p className="claim">Donde corresponde, cuando importa.</p>
        <p className="lead">
          SaaS de bandera blanca para obras sociales y prepagas: un módulo embebible en sus apps, no una
          aplicación propia de cara al afiliado. Esta documentación reúne la presentación del proyecto, la
          encuesta de validación, los estudios y el mapa de competencia.
        </p>
        <div className="hero-actions">
          <Link href="/01-documento-proyecto" className="button">
            Leer la presentación
          </Link>
          <Link href="/dashboard/dashboard-encuesta.html" className="button button-ghost">
            Abrir el dashboard
          </Link>
        </div>
      </header>

      <ul className="stats">
        <li>
          <strong>18</strong>
          <span>documentos</span>
        </li>
        <li>
          <strong>384</strong>
          <span>respuestas de la encuesta</span>
        </li>
        <li>
          <strong>7</strong>
          <span>análisis de competencia</span>
        </li>
      </ul>

      {sections.map((section) => (
        <section key={section.id} className="doc-group" aria-labelledby={section.id}>
          <h2 id={section.id}>{section.title}</h2>
          <ul>
            {section.docs.map((doc) => (
              <li key={doc.slug}>
                <Link href={`/${doc.slug}`}>
                  <span>{doc.slug.slice(0, 2)}</span>
                  <strong>{doc.title}</strong>
                  <small>{doc.description}</small>
                </Link>
              </li>
            ))}
          </ul>
        </section>
      ))}
    </div>
  );
}
