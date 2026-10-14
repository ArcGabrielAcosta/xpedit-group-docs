/**
 * Lee el CSV de la encuesta y vuelca KPIs + gráficos en el HTML.
 * Fuente: Encuesta de validación.csv (misma carpeta).
 *
 * Abrí con un servidor local (file:// bloquea fetch):
 *   cd investigacion-de-mercado/dashboard-encuesta
 *   node server.js
 * Luego: http://localhost:8080/dashboard-encuesta.html
 */

const CSV_FILE = "Encuesta de validación.csv";

const COLS = [
  "ts",
  "cobertura",
  "zona",
  "edad",
  "smartphone",
  "urgencia_24m",
  "primer_paso",
  "usuario_app",
  "claridad",
  "dolor",
  "friccion_107",
  "valora",
  "utilidad_idea",
  "comodidad_datos",
  "freno",
  "respaldo",
  "intencion",
  "frase",
];

const COLORS = [
  "#00B4D8",
  "#0A193F",
  "#FF4D6D",
  "#38BDF8",
  "#94A3B8",
  "#0EA5E9",
  "#1E3A5F",
  "#67E8F9",
];

const chartInstances = [];

/* ---------- CSV ---------- */

function parseCsv(text) {
  const rows = [];
  let row = [];
  let cell = "";
  let inQuotes = false;

  for (let i = 0; i < text.length; i++) {
    const ch = text[i];
    const next = text[i + 1];

    if (inQuotes) {
      if (ch === '"' && next === '"') {
        cell += '"';
        i++;
      } else if (ch === '"') {
        inQuotes = false;
      } else {
        cell += ch;
      }
      continue;
    }

    if (ch === '"') {
      inQuotes = true;
    } else if (ch === ",") {
      row.push(cell);
      cell = "";
    } else if (ch === "\r") {
      // skip
    } else if (ch === "\n") {
      row.push(cell);
      rows.push(row);
      row = [];
      cell = "";
    } else {
      cell += ch;
    }
  }

  if (cell.length || row.length) {
    row.push(cell);
    rows.push(row);
  }

  return rows.filter((r) => r.some((c) => String(c).trim() !== ""));
}

function rowsToRecords(rows) {
  if (rows.length < 2) return [];
  return rows.slice(1).map((cells) => {
    const rec = {};
    COLS.forEach((key, i) => {
      rec[key] = (cells[i] ?? "").trim();
    });
    for (const key of ["claridad", "utilidad_idea", "comodidad_datos", "intencion"]) {
      const n = Number(rec[key]);
      rec[key] = Number.isFinite(n) ? n : null;
    }
    return rec;
  });
}

/* ---------- Aggregations ---------- */

function shorten(s, n = 48) {
  const t = String(s);
  return t.length <= n ? t : t.slice(0, n - 1) + "…";
}

function valueCounts(values, limit = 8) {
  const map = new Map();
  for (const raw of values) {
    const key = String(raw ?? "").trim() || "(vacío)";
    map.set(key, (map.get(key) || 0) + 1);
  }
  const sorted = [...map.entries()].sort((a, b) => b[1] - a[1]).slice(0, limit);
  return {
    labels: sorted.map(([k]) => shorten(k)),
    values: sorted.map(([, v]) => v),
  };
}

function explodeMulti(values) {
  const out = [];
  for (const raw of values) {
    for (const piece of String(raw ?? "")
      .replace(/\|/g, ";")
      .split(";")) {
      const p = piece.trim();
      if (p) out.push(p);
    }
  }
  return out;
}

function scaleDist(values) {
  const counts = [0, 0, 0, 0, 0];
  let sum = 0;
  let n = 0;
  for (const v of values) {
    if (v == null || !Number.isFinite(v)) continue;
    const i = Math.round(v);
    if (i >= 1 && i <= 5) {
      counts[i - 1]++;
      sum += v;
      n++;
    }
  }
  return { counts, mean: n ? Math.round((sum / n) * 100) / 100 : 0 };
}

function includesAny(text, patterns) {
  const t = String(text ?? "").toLowerCase();
  return patterns.some((p) => t.includes(p));
}

function buildPayload(records) {
  const n = records.length;
  if (!n) {
    return {
      n: 0,
      kpis: { Respuestas: "0" },
      charts: {},
    };
  }

  const util = records.map((r) => r.utilidad_idea);
  const intent = records.map((r) => r.intencion);

  let high = 0;
  let utilGe4 = 0;
  let utilSum = 0;
  let utilN = 0;
  let intentSum = 0;
  let intentN = 0;

  for (let i = 0; i < n; i++) {
    const u = util[i];
    const it = intent[i];
    if (u != null) {
      utilSum += u;
      utilN++;
      if (u >= 4) utilGe4++;
    }
    if (it != null) {
      intentSum += it;
      intentN++;
    }
    if (u != null && it != null && u >= 4 && it >= 4) high++;
  }

  const covOs = records.filter((r) => includesAny(r.cobertura, ["obra social"])).length;
  const covPre = records.filter((r) => includesAny(r.cobertura, ["prepaga"])).length;
  const respaldoOs = records.filter((r) =>
    includesAny(r.respaldo, ["prepaga", "obra social"])
  ).length;
  const demora = records.filter((r) => includesAny(r.dolor, ["tarde"])).length;

  const pct = (x) => `${Math.round((100 * x) / n)}%`;
  const mean = (sum, count) => (count ? (sum / count).toFixed(2) : "—");

  const claridad = scaleDist(records.map((r) => r.claridad));
  const utilidad = scaleDist(util);
  const comodidad = scaleDist(records.map((r) => r.comodidad_datos));
  const intencion = scaleDist(intent);

  return {
    n,
    kpis: {
      Respuestas: String(n),
      "Alta intención": pct(high),
      "Respaldo OS/prepaga": pct(respaldoOs),
      "Dolor = demora": pct(demora),
      "Media utilidad": mean(utilSum, utilN),
      "Media intención": mean(intentSum, intentN),
      "Cobertura OS+prepaga": pct(covOs + covPre),
      "Utilidad ≥ 4": pct(utilGe4),
    },
    charts: {
      cobertura: valueCounts(records.map((r) => r.cobertura)),
      zona: valueCounts(records.map((r) => r.zona)),
      edad: valueCounts(records.map((r) => r.edad)),
      primer_paso: valueCounts(records.map((r) => r.primer_paso)),
      dolor: valueCounts(records.map((r) => r.dolor)),
      respaldo: valueCounts(records.map((r) => r.respaldo)),
      friccion_107: valueCounts(records.map((r) => r.friccion_107)),
      valora: valueCounts(records.map((r) => r.valora)),
      freno: valueCounts(explodeMulti(records.map((r) => r.freno)), 7),
      escalas: {
        claridad: claridad.counts,
        utilidad_idea: utilidad.counts,
        comodidad_datos: comodidad.counts,
        intencion: intencion.counts,
        means: {
          claridad: claridad.mean,
          utilidad_idea: utilidad.mean,
          comodidad_datos: comodidad.mean,
          intencion: intencion.mean,
        },
      },
    },
  };
}

/* ---------- Render ---------- */

function destroyCharts() {
  while (chartInstances.length) {
    const c = chartInstances.pop();
    try {
      c.destroy();
    } catch (_) {
      /* ignore */
    }
  }
}

function doughnut(id, pack) {
  const chart = new Chart(document.getElementById(id), {
    type: "doughnut",
    data: {
      labels: pack.labels,
      datasets: [{ data: pack.values, backgroundColor: COLORS }],
    },
    options: {
      plugins: { legend: { position: "bottom", labels: { boxWidth: 12 } } },
      cutout: "55%",
    },
  });
  chartInstances.push(chart);
}

function bar(id, pack, horizontal = false) {
  const chart = new Chart(document.getElementById(id), {
    type: "bar",
    data: {
      labels: pack.labels,
      datasets: [
        {
          data: pack.values,
          backgroundColor: COLORS[0],
          borderRadius: 6,
        },
      ],
    },
    options: {
      indexAxis: horizontal ? "y" : "x",
      plugins: { legend: { display: false } },
      scales: { x: { beginAtZero: true }, y: { beginAtZero: true } },
    },
  });
  chartInstances.push(chart);
}

function renderDashboard(data) {
  destroyCharts();

  document.getElementById("n").textContent = data.n;

  const kpisEl = document.getElementById("kpis");
  kpisEl.innerHTML = "";
  Object.entries(data.kpis).forEach(([label, value]) => {
    const d = document.createElement("div");
    d.className = "kpi";
    d.innerHTML = `<div class="v">${value}</div><div class="l">${label}</div>`;
    kpisEl.appendChild(d);
  });

  if (!data.charts || !data.charts.cobertura) return;

  Chart.defaults.color = "#94A3B8";
  Chart.defaults.borderColor = "#1E3A5F";

  doughnut("c_cobertura", data.charts.cobertura);
  doughnut("c_zona", data.charts.zona);
  bar("c_edad", data.charts.edad);
  bar("c_primer_paso", data.charts.primer_paso, true);
  bar("c_dolor", data.charts.dolor, true);
  doughnut("c_respaldo", data.charts.respaldo);
  bar("c_friccion_107", data.charts.friccion_107, true);
  bar("c_valora", data.charts.valora, true);
  bar("c_freno", data.charts.freno, true);

  const e = data.charts.escalas;
  const escalas = new Chart(document.getElementById("c_escalas"), {
    type: "bar",
    data: {
      labels: ["1", "2", "3", "4", "5"],
      datasets: [
        {
          label: `Claridad (μ=${e.means.claridad})`,
          data: e.claridad,
          backgroundColor: "#0A193F",
        },
        {
          label: `Utilidad (μ=${e.means.utilidad_idea})`,
          data: e.utilidad_idea,
          backgroundColor: "#00B4D8",
        },
        {
          label: `Ficha (μ=${e.means.comodidad_datos})`,
          data: e.comodidad_datos,
          backgroundColor: "#38BDF8",
        },
        {
          label: `Intención (μ=${e.means.intencion})`,
          data: e.intencion,
          backgroundColor: "#FF4D6D",
        },
      ],
    },
    options: {
      plugins: { legend: { position: "bottom" } },
      scales: { y: { beginAtZero: true } },
    },
  });
  chartInstances.push(escalas);
}

function setStatus(msg, isError = false) {
  const el = document.getElementById("status");
  if (!el) return;
  el.textContent = msg;
  el.className = isError ? "status error" : "status";
}

function showFileFallback(show) {
  const box = document.getElementById("file-fallback");
  if (box) box.hidden = !show;
}

async function loadFromText(csvText, sourceLabel) {
  const records = rowsToRecords(parseCsv(csvText));
  const data = buildPayload(records);
  renderDashboard(data);
  setStatus(`Cargado desde ${sourceLabel} · ${data.n} respuestas`);
  showFileFallback(false);
  return data;
}

async function loadCsvFromFetch() {
  const res = await fetch(encodeURI(CSV_FILE));
  if (!res.ok) throw new Error(`HTTP ${res.status}`);
  const text = await res.text();
  return loadFromText(text, CSV_FILE);
}

function wireFileInput() {
  const input = document.getElementById("csv-file");
  if (!input) return;
  input.addEventListener("change", async () => {
    const file = input.files && input.files[0];
    if (!file) return;
    try {
      const text = await file.text();
      await loadFromText(text, file.name);
    } catch (err) {
      setStatus(`No se pudo leer el archivo: ${err.message}`, true);
    }
  });
}

async function init() {
  wireFileInput();
  setStatus("Cargando CSV…");
  try {
    await loadCsvFromFetch();
  } catch (err) {
    setStatus(
      "No se pudo leer el CSV automáticamente (abrí con un servidor local, o elegí el archivo abajo).",
      true
    );
    showFileFallback(true);
    console.warn("Fetch CSV falló:", err);
  }
}

document.addEventListener("DOMContentLoaded", init);
