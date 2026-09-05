import "./globals.css";

export const metadata = {
  title: "Hallo Welt",
  description: "Eine kleine Begrüßung an die Welt.",
};

export default function RootLayout({ children }) {
  return (
    <html lang="de">
      <body>{children}</body>
    </html>
  );
}
