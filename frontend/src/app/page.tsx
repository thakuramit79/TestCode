const stats = [
  { label: 'Avg queue time', value: '11 min', color: 'bg-emerald-50 text-emerald-700' },
  { label: 'SLA compliance', value: '96.4%', color: 'bg-blue-50 text-blue-700' },
  { label: 'Appointments booked', value: '24.8K', color: 'bg-violet-50 text-violet-700' },
  { label: 'Customer rating', value: '4.8/5', color: 'bg-amber-50 text-amber-700' },
];

const modules = [
  'Multi-tenant onboarding',
  'Live queue management',
  'Smart appointment scheduling',
  'AI queue optimization',
  'Digital check-in and reminders',
  'Analytics and CRM integration',
];

export default function HomePage() {
  return (
    <main className="min-h-screen px-6 py-10 text-slate-900">
      <div className="mx-auto max-w-7xl">
        <header className="mb-10 flex items-center justify-between rounded-2xl border border-slate-200 bg-white/80 p-5 shadow-soft backdrop-blur">
          <div>
            <p className="text-xs font-semibold uppercase tracking-[0.2em] text-blue-600">Smart Queue Management</p>
            <h1 className="mt-2 text-3xl font-black">BookMyQ</h1>
          </div>
          <button className="rounded-xl bg-slate-900 px-5 py-3 text-sm font-semibold text-white shadow-lg shadow-slate-900/10 transition hover:bg-slate-700">
            Book demo
          </button>
        </header>

        <section className="grid gap-6 lg:grid-cols-[1.3fr_0.7fr]">
          <div className="rounded-3xl bg-slate-900 p-8 text-white shadow-soft">
            <p className="mb-3 text-sm uppercase tracking-[0.2em] text-cyan-300">Enterprise SaaS platform</p>
            <h2 className="max-w-xl text-4xl font-black leading-tight">
              Reduce wait time. Improve service quality. Delight every customer.
            </h2>
            <p className="mt-5 max-w-xl text-base text-slate-300">
              BookMyQ powers multi-location queue orchestration for hospitals, banks, clinics, government offices, and service centers through AI-assisted scheduling, live dashboards, and customer-centric self-service.
            </p>
            <div className="mt-8 flex gap-3">
              <button className="rounded-xl bg-cyan-400 px-5 py-3 font-semibold text-slate-900">Get started</button>
              <button className="rounded-xl border border-slate-700 px-5 py-3 font-semibold text-white">View product</button>
            </div>
          </div>

          <div className="rounded-3xl border border-slate-200 bg-white p-6 shadow-soft">
            <p className="text-sm font-semibold uppercase tracking-[0.2em] text-slate-500">Live operations</p>
            <div className="mt-6 space-y-4">
              {[
                ['Queue load', '72%'],
                ['VIP priority', '08'],
                ['Waiting room', '24'],
                ['No-show risk', 'Low'],
              ].map(([label, value]) => (
                <div key={label} className="flex items-center justify-between rounded-2xl bg-slate-50 p-3">
                  <span className="text-sm text-slate-500">{label}</span>
                  <span className="text-lg font-bold">{value}</span>
                </div>
              ))}
            </div>
          </div>
        </section>

        <section className="mt-10 grid gap-4 md:grid-cols-2 xl:grid-cols-4">
          {stats.map((stat) => (
            <div key={stat.label} className={`${stat.color} rounded-2xl p-4 shadow-soft`}>
              <div className="text-2xl font-black">{stat.value}</div>
              <div className="mt-2 text-sm font-medium">{stat.label}</div>
            </div>
          ))}
        </section>

        <section className="mt-12 grid gap-6 lg:grid-cols-[0.9fr_1.1fr]">
          <div className="rounded-3xl border border-slate-200 bg-white p-6 shadow-soft">
            <p className="text-sm font-semibold uppercase tracking-[0.2em] text-slate-500">Core modules</p>
            <ul className="mt-6 space-y-3">
              {modules.map((module) => (
                <li key={module} className="flex items-center gap-3 rounded-2xl bg-slate-50 p-3">
                  <span className="inline-flex h-6 w-6 items-center justify-center rounded-full bg-emerald-500 text-xs font-black text-white">✓</span>
                  <span>{module}</span>
                </li>
              ))}
            </ul>
          </div>

          <div className="rounded-3xl border border-slate-200 bg-white p-6 shadow-soft">
            <p className="text-sm font-semibold uppercase tracking-[0.2em] text-slate-500">Why BookMyQ</p>
            <div className="mt-6 grid gap-4 md:grid-cols-2">
              {[
                ['Tenant isolation', 'Secure data separation for each business, branch, and user workspace.'],
                ['AI-powered triage', 'Predictive wait times and service routing for reduced queue friction.'],
                ['Appointment intelligence', 'Smart capacity planning and scheduling across service teams.'],
                ['Omnichannel engagement', 'SMS, email, WhatsApp, and push notifications at every queue stage.'],
              ].map(([title, description]) => (
                <div key={title} className="rounded-2xl border border-slate-200 bg-slate-50 p-4">
                  <h3 className="font-bold">{title}</h3>
                  <p className="mt-2 text-sm text-slate-600">{description}</p>
                </div>
              ))}
            </div>
          </div>
        </section>
      </div>
    </main>
  );
}
