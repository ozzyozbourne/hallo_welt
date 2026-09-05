export default function Home() {
  return (
    <main>
      <div className="halo" aria-hidden="true" />
      <section className="greeting" aria-labelledby="greeting-title">
        <p className="eyebrow">Eine Nachricht von Ozzy</p>
        <h1 id="greeting-title">
          Hallo<span>.</span>
          <br />
          Welt<span>!</span>
        </h1>
        <p className="signoff">Schön, dass du da bist.</p>
      </section>
      <p className="coordinate" aria-hidden="true">
        52° N · 2026
      </p>
    </main>
  );
}
