import Link from "next/link";
import type { Metadata } from "next";
import { notFound } from "next/navigation";
import { MarkdownView } from "@/components/MarkdownView";
import { TableOfContents } from "@/components/TableOfContents";
import { docsInOrder, findDoc, findSection, neighbors } from "@/lib/catalog";
import { getDoc } from "@/lib/docs";

type Params = { slug: string };

export function generateStaticParams(): Params[] {
  return docsInOrder.map((doc) => ({ slug: doc.slug }));
}

export const dynamicParams = false;

export async function generateMetadata({ params }: { params: Promise<Params> }): Promise<Metadata> {
  const { slug } = await params;
  const entry = findDoc(slug);
  const doc = getDoc(slug);
  if (!entry || !doc) return { title: "No encontrado" };
  return {
    title: entry.title,
    description: entry.description,
  };
}

export default async function DocPage({ params }: { params: Promise<Params> }) {
  const { slug } = await params;
  const doc = getDoc(slug);
  const entry = findDoc(slug);
  if (!doc || !entry) notFound();

  const section = findSection(slug);
  const { prev, next } = neighbors(slug);

  return (
    <div className="doc-layout">
      <article className="doc">
        <p className="eyebrow">
          {section?.title} · {slug.slice(0, 2)}
        </p>
        <MarkdownView content={doc.content} />
        <nav className="pager" aria-label="Documentos anteriores y siguientes">
          {prev ? (
            <Link href={`/${prev.slug}`} className="pager-link">
              <small>Anterior</small>
              <strong>
                {prev.slug.slice(0, 2)} {prev.title}
              </strong>
            </Link>
          ) : (
            <span />
          )}
          {next ? (
            <Link href={`/${next.slug}`} className="pager-link next">
              <small>Siguiente</small>
              <strong>
                {next.slug.slice(0, 2)} {next.title}
              </strong>
            </Link>
          ) : (
            <span />
          )}
        </nav>
      </article>
      <TableOfContents items={doc.toc} />
    </div>
  );
}
