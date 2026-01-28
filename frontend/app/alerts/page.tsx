import Badge from "../../components/Badge";
import Card from "../../components/Card";
import Table from "../../components/Table";

export default function AlertsPage() {
  return (
    <div className="space-y-6">
      <Card title="Bandeja de alertas">
        <Table
          headers={["Rule", "Severity", "Status", "Date"]}
          rows={[
            ["High Severity", <Badge key="high">High</Badge>, "Open", "2024-06-18"],
            ["IOC Keyword", <Badge key="med">Medium</Badge>, "Investigating", "2024-06-17"],
          ]}
        />
      </Card>

      <Card title="Detalle de alerta">
        <div className="grid gap-4 md:grid-cols-2">
          <div>
            <p className="text-sm text-slate-400">Regla</p>
            <p className="text-lg">High Severity</p>
            <p className="text-sm text-slate-300 mt-2">Match: severity >= 4</p>
          </div>
          <div>
            <p className="text-sm text-slate-400">Estado</p>
            <div className="mt-2 flex gap-2">
              <Badge>Open</Badge>
              <Badge>Priority: P1</Badge>
            </div>
          </div>
        </div>
      </Card>
    </div>
  );
}
