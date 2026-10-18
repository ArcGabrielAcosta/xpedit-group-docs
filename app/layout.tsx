import type { Metadata } from "next";
import { Geist, Outfit } from "next/font/google";
import { DocsShell } from "@/components/DocsShell";
import { sections } from "@/lib/catalog";
import "./globals.css";

const sans = Outfit({
  subsets: ["latin"],
  variable: "--font-sans",
});

const body = Geist({
  subsets: ["latin"],
  variable: "--font-body",
});

export const metadata: Metadata = {
  title: {
    default: "Documentación · Xpedit Group",
    template: "%s · Xpedit Docs",
  },
  description:
    "Investigación de mercado de Xpedit Group: proyecto, encuesta, personas, estudios y competencia.",
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="es" className={`${sans.variable} ${body.variable}`}>
      <body>
        <DocsShell sections={sections}>{children}</DocsShell>
      </body>
    </html>
  );
}
