# CTI Sentinel (Dev-Only)

Plataforma de Ciberinteligencia (CTI) y rastreo de malware/vulnerabilidades en modo **solo desarrollo/pruebas**. Incluye backend Django 5 + DRF + JWT y frontend Next.js 14 con Tailwind.

## Estructura del repo

```
/backend
  /core
  /cti
  /data
/frontend
  /app
  /components
  /services
```

## Backend (Django)

### Setup

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
```

### Datos demo

```bash
python manage.py load_vulns --path backend/data/demo_vulns.json
python manage.py seed_demo
```

### Ejecutar

```bash
python manage.py runserver 0.0.0.0:8000
```

### Endpoints principales

- Auth JWT: `POST /api/v1/auth/token/`
- IOC Hub: `/api/v1/indicators/`
- Vulnerabilities: `/api/v1/vulnerabilities/`
- Threat Actors: `/api/v1/threat-actors/`
- Alerts: `/api/v1/alert-events/`
- Dashboard: `/api/v1/dashboard/`

### Ejecutar reglas de alertas

```bash
python manage.py run_alert_rules
```

## Frontend (Next.js 14)

### Setup

```bash
cd frontend
npm install
```

### Ejecutar

```bash
npm run dev
```

La UI estará disponible en `http://localhost:3000`.

## Variables de entorno

Frontend:

```
NEXT_PUBLIC_API_BASE=http://localhost:8000/api/v1
```

## Notas

- CORS restringido a `http://localhost:3000`.
- Enrichments son mock providers sin llaves reales.
- El entorno está diseñado para uso local únicamente.
