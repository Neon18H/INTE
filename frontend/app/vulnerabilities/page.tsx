"use client";

import Card from "../../components/Card";
import Table from "../../components/Table";
import { BarChart, Bar, XAxis, YAxis, Tooltip, ResponsiveContainer } from "recharts";

const data = [
  { date: "2023", total: 3 },
  { date: "2024", total: 5 },
];

export default function VulnerabilitiesPage() {
  return (
    <div className="space-y-6">
      <Card title="Filtros">
        <div className="grid gap-3 md:grid-cols-3">
          <input className="rounded-md bg-slate-900 border border-slate-700 px-3 py-2" placeholder="Buscar" />
          <input className="rounded-md bg-slate-900 border border-slate-700 px-3 py-2" placeholder="CVSS >=" />
          <select className="rounded-md bg-slate-900 border border-slate-700 px-3 py-2">
            <option>KEV Only</option>
            <option>All</option>
          </select>
        </div>
      </Card>

      <Card title="Lista CVEs">
        <Table
          headers={["CVE", "Title", "CVSS", "KEV"]}
          rows={[
            ["CVE-2024-1234", "Mock auth bypass", "8.7", "Yes"],
            ["CVE-2023-7788", "Sample overflow", "6.5", "No"],
          ]}
        />
      </Card>

      <Card title="Tendencia por fecha">
        <div className="h-52">
          <ResponsiveContainer width="100%" height="100%">
            <BarChart data={data}>
              <XAxis dataKey="date" stroke="#94a3b8" />
              <YAxis stroke="#94a3b8" />
              <Tooltip />
              <Bar dataKey="total" fill="#22d3ee" />
            </BarChart>
          </ResponsiveContainer>
        </div>
      </Card>
    </div>
  );
}
