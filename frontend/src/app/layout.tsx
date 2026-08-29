import './globals.css';
import type { Metadata } from 'next';

export const metadata: Metadata = {
  title: 'BookMyQ',
  description: 'Smart Queue Management & Appointment Booking Platform',
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
