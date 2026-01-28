import type { ReactNode } from "react";
import "../styles/globals.css";
import Sidebar from "../components/Sidebar";
import Topbar from "../components/Topbar";

export const metadata = {
  title: "CTI Sentinel",
  description: "CTI & Malware Tracking Dashboard",
};

export default function RootLayout({ children }: { children: ReactNode }) {
  return (
    <html lang="es" className="dark">
      <body className="min-h-screen bg-background">
        <div className="flex">
          <Sidebar />
          <div className="flex-1 flex flex-col">
            <Topbar />
            <main className="p-6 space-y-6">{children}</main>
          </div>
        </div>
      </body>
    </html>
  );
}
