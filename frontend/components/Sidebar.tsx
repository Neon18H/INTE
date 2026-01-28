import Link from "next/link";
import { ShieldAlert, Radar, Bug, UserCircle2, Bell, LayoutDashboard } from "lucide-react";

const items = [
  { href: "/", label: "Dashboard", icon: LayoutDashboard },
  { href: "/ioc", label: "IOC Hub", icon: Radar },
  { href: "/vulnerabilities", label: "Vulnerabilities", icon: Bug },
  { href: "/actors", label: "Threat Actors", icon: UserCircle2 },
  { href: "/alerts", label: "Alerts", icon: Bell },
];

export default function Sidebar() {
  return (
    <aside className="hidden lg:flex lg:flex-col w-64 bg-card text-slate-100 border-r border-slate-800 min-h-screen p-6">
      <div className="flex items-center gap-2 text-xl font-semibold">
        <ShieldAlert className="text-accent" />
        CTI Sentinel
      </div>
      <nav className="mt-8 space-y-2">
        {items.map((item) => (
          <Link
            key={item.href}
            href={item.href}
            className="flex items-center gap-3 rounded-md px-3 py-2 text-sm hover:bg-slate-800 transition"
          >
            <item.icon size={18} />
            {item.label}
          </Link>
        ))}
      </nav>
      <div className="mt-auto text-xs text-slate-400">DEV / Demo only</div>
    </aside>
  );
}
