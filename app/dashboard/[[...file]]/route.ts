import fs from "fs/promises";
import path from "path";
import { NextResponse } from "next/server";
import { basePath } from "@/lib/base-path";

const ROOT = path.resolve(process.cwd(), "investigacion-de-mercado", "dashboard-encuesta");

const MIME: Record<string, string> = {
  ".html": "text/html; charset=utf-8",
  ".js": "text/javascript; charset=utf-8",
  ".csv": "text/csv; charset=utf-8",
  ".json": "application/json; charset=utf-8",
  ".css": "text/css; charset=utf-8",
  ".svg": "image/svg+xml",
  ".png": "image/png",
  ".ico": "image/x-icon",
};

async function resolveFile(relativePath: string): Promise<string | null> {
  const target = path.resolve(ROOT, relativePath);
  if (target !== ROOT && !target.startsWith(ROOT + path.sep)) return null;

  try {
    const stat = await fs.stat(target);
    if (stat.isFile()) return target;
  } catch {
    const directory = path.dirname(target);
    const wanted = path.basename(target).toLowerCase();
    try {
      const entries = await fs.readdir(directory);
      const match = entries.find((entry) => entry.toLowerCase() === wanted);
      if (!match) return null;
      const resolved = path.resolve(directory, match);
      if (!resolved.startsWith(ROOT + path.sep)) return null;
      const stat = await fs.stat(resolved);
      return stat.isFile() ? resolved : null;
    } catch {
      return null;
    }
  }

  return null;
}

export async function GET(request: Request, context: { params: Promise<{ file?: string[] }> }) {
  const { file } = await context.params;

  if (!file || file.length === 0) {
    const destination = new URL(`${basePath}/dashboard/dashboard-encuesta.html`, request.url);
    return NextResponse.redirect(destination);
  }

  const relativePath = file.map((segment) => {
    try {
      return decodeURIComponent(segment);
    } catch {
      return segment;
    }
  }).join("/");

  if (relativePath.includes("\0")) {
    return new NextResponse("Forbidden", { status: 403 });
  }

  const filePath = await resolveFile(relativePath);
  if (!filePath) {
    return new NextResponse("Not found", { status: 404 });
  }

  const body = await fs.readFile(filePath);
  const ext = path.extname(filePath).toLowerCase();

  return new NextResponse(body, {
    headers: {
      "Content-Type": MIME[ext] ?? "application/octet-stream",
      "Cache-Control": "public, max-age=3600",
      "X-Content-Type-Options": "nosniff",
    },
  });
}
