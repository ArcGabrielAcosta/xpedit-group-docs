# Xpedit Group Docs

Sitio Next.js de la documentación de Xpedit. Los markdown de `investigacion-de-mercado/` siguen siendo la fuente: el sitio los lee y los publica bajo `/docs`.

## Desarrollo

```bash
npm install
npm run dev
```

Índice: [http://localhost:3000/docs](http://localhost:3000/docs)

## Despliegue en `tudominio.com/docs`

El `basePath` por defecto es `/docs`, así que enlaces y assets ya salen con ese prefijo. El servidor tiene que recibir la ruta completa, incluido `/docs`.

```nginx
location /docs/ {
  proxy_pass http://127.0.0.1:3000/docs/;
}
```

```bash
npm run build
npm start
```

Para servir el sitio en la raíz en lugar de `/docs`, construí con `NEXT_PUBLIC_BASE_PATH=` vacío. El mismo valor tiene que existir al hacer `next build` y al ejecutar `next start`.

## Contenido

- `investigacion-de-mercado/*.md` — documentos
- `investigacion-de-mercado/dashboard-encuesta/` — dashboard de la encuesta, publicado en `/docs/dashboard/dashboard-encuesta.html`

Un cambio en un markdown entra en el sitio con el próximo build.
