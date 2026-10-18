import Link from "next/link";
import type { Components } from "react-markdown";
import ReactMarkdown from "react-markdown";
import rehypeSlug from "rehype-slug";
import remarkGfm from "remark-gfm";
import { rewriteHref } from "@/lib/docs";

const components: Components = {
  a({ href, children }) {
    const target = rewriteHref(href);
    if (target.external) {
      return (
        <a href={target.href} target="_blank" rel="noreferrer">
          {children}
        </a>
      );
    }
    if (target.href.startsWith("#")) {
      return <a href={target.href}>{children}</a>;
    }
    return <Link href={target.href}>{children}</Link>;
  },
  table({ children }) {
    return (
      <div className="table-wrap">
        <table>{children}</table>
      </div>
    );
  },
};

export function MarkdownView({ content }: { content: string }) {
  return (
    <div className="prose">
      <ReactMarkdown remarkPlugins={[remarkGfm]} rehypePlugins={[rehypeSlug]} components={components}>
        {content}
      </ReactMarkdown>
    </div>
  );
}
