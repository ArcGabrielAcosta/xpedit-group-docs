"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";
import { useEffect, useMemo, useState } from "react";
import type { DocSection } from "@/lib/catalog";

const DASHBOARD_HREF = "/dashboard/dashboard-encuesta.html";

export function DocsShell({
  sections,
  children,
}: {
  sections: DocSection[];
  children: React.ReactNode;
}) {
  const pathname = usePathname();
  const [open, setOpen] = useState(false);
  const [query, setQuery] = useState("");

  useEffect(() => {
    setOpen(false);
  }, [pathname]);

  const filtered = useMemo(() => {
    const needle = query.trim().toLocaleLowerCase("es");
    if (!needle) return sections;
    return sections
      .map((section) => ({
        ...section,
        docs: section.docs.filter((doc) =>
          `${doc.title} ${doc.description} ${doc.slug}`.toLocaleLowerCase("es").includes(needle),
        ),
      }))
      .filter((section) => section.docs.length > 0);
  }, [query, sections]);

  const dashboardActive = pathname.startsWith("/dashboard");

  return (
    <div className="app">
      <a className="skip" href="#contenido">
        Saltar al contenido
      </a>
      <header className="topbar">
        <button
          type="button"
          className="menu-button"
          aria-expanded={open}
          aria-controls="documentos"
          onClick={() => setOpen((value) => !value)}
        >
          Documentos
        </button>
        <Link href="/" className="topbar-mark">
          Xpedit
        </Link>
      </header>
      <aside id="documentos" className={open ? "nav open" : "nav"}>
        <Link href="/" className="brand">
          <span className="brand-mark" aria-hidden="true">
            X
          </span>
          <span>
            <strong>Xpedit Group</strong>
            <small>Documentación</small>
          </span>
        </Link>
        <label className="search">
          <span className="sr-only">Buscar documentos</span>
          <input
            type="search"
            value={query}
            placeholder="Buscar documentos"
            onChange={(event) => setQuery(event.target.value)}
          />
        </label>
        <nav aria-label="Documentos">
          <Link href="/" className={pathname === "/" ? "nav-link active" : "nav-link"} data-home="true">
            Inicio
          </Link>
          {filtered.map((section) => (
            <div key={section.id} className="nav-section">
              <p>{section.title}</p>
              <ul>
                {section.docs.map((doc) => {
                  const href = `/${doc.slug}`;
                  const active = pathname === href;
                  return (
                    <li key={doc.slug}>
                      <Link href={href} className={active ? "nav-link active" : "nav-link"} aria-current={active ? "page" : undefined}>
                        <span>{doc.slug.slice(0, 2)}</span>
                        {doc.title}
                      </Link>
                    </li>
                  );
                })}
              </ul>
            </div>
          ))}
          {filtered.length === 0 ? <p className="nav-empty">Sin resultados</p> : null}
        </nav>
        <Link href={DASHBOARD_HREF} className={dashboardActive ? "dashboard-link active" : "dashboard-link"}>
          Dashboard de la encuesta
        </Link>
      </aside>
      {open ? <button type="button" className="backdrop" aria-label="Cerrar menú" onClick={() => setOpen(false)} /> : null}
      <main id="contenido" className="main">
        {children}
      </main>
    </div>
  );
}
