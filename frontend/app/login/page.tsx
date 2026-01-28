export default function LoginPage() {
  return (
    <div className="max-w-md mx-auto bg-card border border-slate-800 rounded-xl p-6">
      <h2 className="text-xl font-semibold mb-4">Iniciar sesión</h2>
      <form className="space-y-4">
        <div>
          <label className="text-sm text-slate-300" htmlFor="email">Usuario</label>
          <input
            id="email"
            type="text"
            className="mt-2 w-full rounded-md bg-slate-900 border border-slate-700 px-3 py-2"
            placeholder="analyst"
          />
        </div>
        <div>
          <label className="text-sm text-slate-300" htmlFor="password">Contraseña</label>
          <input
            id="password"
            type="password"
            className="mt-2 w-full rounded-md bg-slate-900 border border-slate-700 px-3 py-2"
            placeholder="••••••••"
          />
        </div>
        <button className="w-full rounded-md bg-accent text-slate-900 font-semibold py-2">
          Entrar
        </button>
      </form>
    </div>
  );
}
