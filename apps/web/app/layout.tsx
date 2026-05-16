import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "TechCase",
  description: "기업 기술 블로그 기반 기술 사례 검색 서비스",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="ko">
      <body>{children}</body>
    </html>
  );
}

