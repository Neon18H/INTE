import { ReactNode } from "react";

interface CardProps {
  title: string;
  value?: string;
  children?: ReactNode;
}

export default function Card({ title, value, children }: CardProps) {
  return (
    <div className="bg-card border border-slate-800 rounded-xl p-5">
      <div className="text-sm text-slate-400">{title}</div>
      {value && <div className="text-2xl font-semibold mt-2">{value}</div>}
      {children && <div className="mt-4">{children}</div>}
    </div>
  );
}
