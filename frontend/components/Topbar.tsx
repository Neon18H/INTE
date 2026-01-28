import { Search, Moon } from "lucide-react";

export default function Topbar() {
  return (
    <header className="flex items-center justify-between bg-card border-b border-slate-800 px-6 py-4">
      <div>
        <p className="text-sm text-slate-400">CTI / Dashboard</p>
        <h1 className="text-xl font-semibold">Ciberinteligencia</h1>
      </div>
      <div className="flex items-center gap-3">
        <div className="flex items-center gap-2 bg-slate-900 border border-slate-700 rounded-md px-3 py-2">
          <Search size={16} className="text-slate-400" />
          <input
            aria-label="Buscar"
            placeholder="Buscar IOC, CVE, actor"
            className="bg-transparent text-sm outline-none text-slate-200"
          />
        </div>
        <button className="rounded-md border border-slate-700 p-2" aria-label="Modo oscuro">
          <Moon size={16} />
        </button>
      </div>
    </header>
  );
}
