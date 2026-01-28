"use client";

import Card from "../components/Card";
import Table from "../components/Table";
import { LineChart, Line, XAxis, YAxis, Tooltip, ResponsiveContainer } from "recharts";

const trendData = [
  { date: "Mon", value: 12 },
  { date: "Tue", value: 18 },
  { date: "Wed", value: 8 },
  { date: "Thu", value: 22 },
  { date: "Fri", value: 16 },
];

export default function DashboardPage() {
  return (
    <div className="space-y-6">
      <div className="grid gap-4 md:grid-cols-2 lg:grid-cols-4">
        <Card title="IOCs hoy" value="24" />
        <Card title="CVEs KEV" value="12" />
        <Card title="Alertas abiertas" value="6" />
        <Card title="Severidad top" value="High" />
      </div>

      <div className="grid gap-6 lg:grid-cols-3">
        <Card title="Tendencia de actividad">
          <div className="h-48">
            <ResponsiveContainer width="100%" height="100%">
              <LineChart data={trendData}>
                <XAxis dataKey="date" stroke="#94a3b8" />
                <YAxis stroke="#94a3b8" />
                <Tooltip />
                <Line type="monotone" dataKey="value" stroke="#22d3ee" strokeWidth={2} />
              </LineChart>
            </ResponsiveContainer>
          </div>
        </Card>
        <Card title="Top IOC Types">
          <ul className="space-y-2 text-sm">
            <li className="flex justify-between"><span>Domains</span><span>40%</span></li>
            <li className="flex justify-between"><span>IPs</span><span>25%</span></li>
            <li className="flex justify-between"><span>Hashes</span><span>20%</span></li>
            <li className="flex justify-between"><span>URLs</span><span>15%</span></li>
          </ul>
        </Card>
        <Card title="Alertas recientes">
          <Table
            headers={["Rule", "Severity", "Status"]}
            rows={[
              ["High Severity", "High", "Open"],
              ["IOC Keyword", "Medium", "Investigating"],
            ]}
          />
        </Card>
      </div>
    </div>
  );
}
