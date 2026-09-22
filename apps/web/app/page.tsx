import Link from 'next/link';
import Image from 'next/image';

const steps = [
  ['01', 'Quick Input', 'Add your website, product and market goal.'],
  ['02', 'AI Snapshot', 'Reveal local opportunities and audience signals.'],
  ['03', 'AI Consultant', 'Answer only the follow-up questions that matter.'],
  ['04', 'Final Report', 'Receive a structured plan your team can execute.'],
];

const marqueeItems = [
  'Australian customer signals',
  'Local positioning',
  'Channel priorities',
  'Launch budget',
  'Creator strategy',
  'Campaign planning',
];

export default function Home() {
  return (
    <main className="arc-page">
      <nav className="arc-nav" aria-label="Primary navigation">
        <Link className="arc-brand" href="/" aria-label="Common Ground Creative home">
          <Image src="/brand/common-ground-creative-logo-orange.png" alt="Common Ground Creative" width={1774} height={887} priority />
        </Link>
        <div className="arc-nav-links">
          <a href="#how-it-works">How it works</a>
          <a href="#solutions">Solutions</a>
          <a href="#reports">Reports</a>
          <a href="#about">About</a>
        </div>
        <Link className="arc-nav-cta" href="/agent">Start analysis</Link>
      </nav>

      <section className="arc-hero" id="about">
        <div className="arc-hero-copy">
          <p className="arc-kicker">AI MARKET ENTRY PLATFORM / AUSTRALIA</p>
          <h1>Enter Australia.<br />Execute with<br />confidence.</h1>
          <p className="arc-intro">Turn market insight into an executable Australian growth plan — powered by AI and reviewed by marketing specialists.</p>
          <Link className="arc-primary-button" href="/agent">Build my plan <span>→</span></Link>
        </div>

        <aside className="snapshot-card" aria-label="Example market snapshot">
          <p className="arc-kicker">LIVE DEMO PREVIEW</p>
          <h2>Intelligent<br />Market Snapshot</h2>
          <p className="snapshot-context">Brand: Xiaomi <i>/</i> Product: YU7 GT</p>
          <div className="snapshot-grid">
            <div><span>Opportunity</span><strong>82 / 100</strong></div>
            <div><span>Priority</span><strong>HIGH</strong></div>
            <div><span>Customer segments</span><strong>03</strong></div>
            <div><span>Channels</span><strong>05</strong></div>
          </div>
        </aside>
      </section>

      <section className="arc-process" id="how-it-works">
        <header>
          <p className="arc-kicker">HOW IT WORKS</p>
          <h2>A direct path from input to<br />action.</h2>
        </header>
        <div className="arc-step-grid">
          {steps.map(([number, title, description]) => (
            <article key={number}>
              <span>{number}</span>
              <h3>{title}</h3>
              <p>{description}</p>
            </article>
          ))}
        </div>
      </section>

      <section className="arc-marquee" id="solutions" aria-label="What your market brief covers">
        <p className="arc-kicker">WHAT YOUR PLAN COVERS</p>
        <div className="scroller" data-animated="true" data-speed="slow">
          <ul className="tag-list scroller__inner">
            {marqueeItems.map((item) => <li key={item}>{item}</li>)}
            {marqueeItems.map((item) => <li key={`${item}-duplicate`} aria-hidden="true">{item}</li>)}
          </ul>
        </div>
      </section>

      <section className="arc-report" id="reports">
        <p className="arc-kicker">A PLAN BUILT TO MOVE</p>
        <h2>From local context<br />to clear next moves.</h2>
        <p>Use an AI-led working session to turn your business context into a focused Australian opportunity, then move forward with a practical plan and specialist support.</p>
        <Link className="arc-primary-button" href="/agent">Start analysis <span>→</span></Link>
      </section>

      <footer className="arc-footer">
        <Image src="/brand/common-ground-creative-logo-orange.png" alt="Common Ground Creative" width={1774} height={887} />
        <span>Built for brands entering Australia.</span>
        <span>© 2026</span>
      </footer>
    </main>
  );
}
