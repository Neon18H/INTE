import Badge from "../../components/Badge";
import Card from "../../components/Card";
import Table from "../../components/Table";

export default function IocPage() {
  return (
    <div className="space-y-6">
      <Card title="Busqueda global de IOC">
        <div className="flex flex-col md:flex-row gap-3">
          <input
            aria-label="Buscar IOC"
            className="flex-1 rounded-md bg-slate-900 border border-slate-700 px-3 py-2"
            placeholder="ip, dominio, hash"
          />
          <button className="rounded-md bg-accent text-slate-900 font-semibold px-4 py-2">
            Buscar
          </button>
        </div>
      </Card>

      <Card title="Resultados recientes">
        <Table
          headers={["IOC", "Tipo", "Confianza", "Tags"]}
          rows={[
            ["malicious.example", "Domain", "80%", <Badge key="phish">phishing</Badge>],
            ["8.8.8.8", "IP", "40%", <Badge key="infra">infra</Badge>],
          ]}
        />
      </Card>

      <Card title="Detalle IOC">
        <div className="grid gap-4 md:grid-cols-2">
          <div>
            <p className="text-sm text-slate-400">Valor</p>
            <p className="text-lg">malicious.example</p>
            <div className="mt-3 flex gap-2">
              <Badge>phishing</Badge>
              <Badge>mock</Badge>
            </div>
          </div>
          <div>
            <p className="text-sm text-slate-400">Timeline</p>
            <ul className="mt-2 text-sm text-slate-200 space-y-1">
              <li>First seen: 2024-06-01</li>
              <li>Last seen: 2024-06-18</li>
              <li>Severity: 4</li>
            </ul>
          </div>
        </div>
      </Card>
    </div>
  );
}
