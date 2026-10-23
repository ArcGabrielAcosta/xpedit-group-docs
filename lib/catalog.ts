export type DocEntry = {
  slug: string;
  title: string;
  description: string;
};

export type DocSection = {
  id: string;
  title: string;
  docs: DocEntry[];
};

export const sections: DocSection[] = [
  {
    id: "proyecto",
    title: "Proyecto",
    docs: [
      {
        slug: "01-documento-proyecto",
        title: "Documento de proyecto",
        description: "Presentación inicial del proyecto",
      },
      {
        slug: "18-documento-de-alcance",
        title: "Documento de alcance",
        description: "Propuesta de proyecto y alcance de esta etapa",
      },
    ],
  },
  {
    id: "personas",
    title: "Personas",
    docs: [
      {
        slug: "02-buyer-persona-provisional-v1",
        title: "Buyer persona provisional",
        description: "Persona afiliado provisional, previa a la encuesta",
      },
      {
        slug: "07-buyer-persona-b2b-white-label",
        title: "Buyer persona B2B",
        description: "Cliente que compra: obra social o prepaga",
      },
      {
        slug: "08-usuario-final-actualizado",
        title: "Usuario final",
        description: "Afiliado actualizado después de la encuesta",
      },
    ],
  },
  {
    id: "encuesta",
    title: "Encuesta",
    docs: [
      {
        slug: "03-diseno-encuesta-validacion",
        title: "Diseño de la encuesta",
        description: "Filtros y preguntas de validación",
      },
      {
        slug: "06-analisis-encuesta-validacion",
        title: "Análisis de la encuesta",
        description: "Resultados (N=384) y KPIs",
      },
    ],
  },
  {
    id: "estudios",
    title: "Estudios",
    docs: [
      {
        slug: "04-estudio-poblacion-urgencias-v1",
        title: "Población y urgencias",
        description: "Mortalidad, efecto espectador y encaje",
      },
      {
        slug: "05-estudio-llamados-emergencias-v2",
        title: "Llamados de emergencia",
        description: "Llamados, código rojo y efecto pirámide",
      },
    ],
  },
  {
    id: "estrategia",
    title: "Estrategia",
    docs: [
      {
        slug: "09-scamper",
        title: "SCAMPER",
        description: "SCAMPER sobre la oferta actual",
      },
      {
        slug: "10-benchmark",
        title: "Benchmark",
        description: "Matriz de características frente a la competencia",
      },
    ],
  },
  {
    id: "competencia",
    title: "Competencia",
    docs: [
      {
        slug: "11-analisis-competencia-shaman-sge",
        title: "Shaman SGE",
        description: "Shaman SGE / Shaman AID",
      },
      {
        slug: "12-analisis-competencia-opsi-sipeme",
        title: "Opsi (Sipeme)",
        description: "Competencia: Opsi (Sipeme)",
      },
      {
        slug: "13-analisis-competencia-inthegra",
        title: "Inthegra",
        description: "Competidor principal local",
      },
      {
        slug: "14-analisis-competencia-aura",
        title: "Aura",
        description: "Competencia: Aura (Kenia)",
      },
      {
        slug: "15-analisis-competencia-rescue-co",
        title: "Rescue.co",
        description: "Competencia: Rescue.co (Kenia)",
      },
      {
        slug: "16-analisis-competencia-red-health",
        title: "RED Health",
        description: "Competencia: RED Health (India)",
      },
      {
        slug: "17-analisis-competencia-rapidsos",
        title: "RapidSOS",
        description: "Límite del mapa: RapidSOS Health (EE. UU.)",
      },
    ],
  },
  {
    id: "modelado",
    title: "Modelado",
    docs: [
      {
        slug: "19-diagrama-casos-de-uso",
        title: "Casos de uso",
        description: "Versión inicial del diagrama de casos de uso del piloto",
      },
    ],
  },
];

export const docs = sections.flatMap((section) => section.docs);

export const docsInOrder = [...docs].sort((a, b) => a.slug.localeCompare(b.slug));

export function findDoc(slug: string): DocEntry | undefined {
  return docs.find((doc) => doc.slug === slug);
}

export function findSection(slug: string): DocSection | undefined {
  return sections.find((section) => section.docs.some((doc) => doc.slug === slug));
}

export function neighbors(slug: string): { prev?: DocEntry; next?: DocEntry } {
  const index = docsInOrder.findIndex((doc) => doc.slug === slug);
  if (index === -1) return {};
  return {
    prev: docsInOrder[index - 1],
    next: docsInOrder[index + 1],
  };
}
