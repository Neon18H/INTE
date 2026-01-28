import Badge from "../../components/Badge";
import Card from "../../components/Card";
import Table from "../../components/Table";

export default function ActorsPage() {
  return (
    <div className="space-y-6">
      <Card title="Threat Actors">
        <Table
          headers={["Actor", "Region", "Campaigns"]}
          rows={[
            ["Shadow Lynx", "LATAM", "Operation Dusk"],
            ["Silver Fox", "EU", "Night Pulse"],
          ]}
        />
      </Card>

      <Card title="Detalle Actor">
        <div className="grid gap-4 md:grid-cols-2">
          <div>
            <p className="text-sm text-slate-400">Actor</p>
            <p className="text-lg">Shadow Lynx</p>
            <p className="text-sm text-slate-300 mt-2">Regional APT focused on phishing.</p>
          </div>
          <div>
            <p className="text-sm text-slate-400">Related</p>
            <div className="mt-2 flex flex-wrap gap-2">
              <Badge>Operation Dusk</Badge>
              <Badge>BlackFang</Badge>
              <Badge>IOC: malicious.example</Badge>
            </div>
          </div>
        </div>
      </Card>
    </div>
  );
}
