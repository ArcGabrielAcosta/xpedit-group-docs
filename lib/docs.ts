import fs from "fs";
import path from "path";
import GithubSlugger from "github-slugger";

const DOCS_DIR = path.join(process.cwd(), "investigacion-de-mercado");

export type TocItem = {
  depth: 2 | 3;
  text: string;
  id: string;
};

export type DocPage = {
  slug: string;
  title: string;
  content: string;
  toc: TocItem[];
};

function plainHeading(text: string): string {
  return text
    .replace(/\[([^\]]+)\]\([^)]+\)/g, "$1")
    .replace(/[*_`]/g, "")
    .replace(/\s+#+\s*$/, "")
    .trim();
}

export function extractToc(markdown: string): TocItem[] {
  const slugger = new GithubSlugger();
  const items: TocItem[] = [];

  for (const line of markdown.split("\n")) {
    const match = /^(#{1,3})\s+(.+)$/.exec(line);
    if (!match) continue;
    const depth = match[1].length;
    const text = plainHeading(match[2]);
    const id = slugger.slug(text);
    if (depth === 2 || depth === 3) {
      items.push({ depth: depth as 2 | 3, text, id });
    }
  }

  return items;
}

export function getDoc(slug: string): DocPage | null {
  if (!/^[a-z0-9-]+$/.test(slug)) return null;

  const filePath = path.join(DOCS_DIR, `${slug}.md`);
  if (!fs.existsSync(filePath)) return null;

  const content = fs
    .readFileSync(filePath, "utf8")
    .replace(/^\uFEFF/, "")
    .replace(/\r\n/g, "\n")
    .replace(/\r/g, "\n");
  const title = content.match(/^#\s+(.+)$/m)?.[1]?.trim() ?? slug;

  return {
    slug,
    title: plainHeading(title),
    content,
    toc: extractToc(content),
  };
}

export function rewriteHref(href: string | undefined): { href: string; external: boolean } {
  if (!href) return { href: "#", external: false };
  if (href.startsWith("#") || href.startsWith("mailto:")) {
    return { href, external: false };
  }
  if (/^https?:\/\//i.test(href)) {
    return { href, external: true };
  }

  const hashIndex = href.indexOf("#");
  const pathPart = hashIndex === -1 ? href : href.slice(0, hashIndex);
  const hash = hashIndex === -1 ? "" : href.slice(hashIndex);

  let decoded = pathPart;
  try {
    decoded = decodeURIComponent(pathPart);
  } catch {
    decoded = pathPart;
  }

  const clean = decoded.replace(/^\.\//, "");

  if (clean.endsWith(".md")) {
    const slug = clean.replace(/\.md$/, "").split("/").pop() ?? "";
    return { href: `/${slug}${hash}`, external: false };
  }

  if (clean === "dashboard-encuesta" || clean.startsWith("dashboard-encuesta/")) {
    const rest = clean.replace(/^dashboard-encuesta\/?/, "");
    const target = rest ? `/dashboard/${rest.split("/").map(encodeURIComponent).join("/")}` : "/dashboard/dashboard-encuesta.html";
    return { href: `${target}${hash}`, external: false };
  }

  return { href, external: false };
}
