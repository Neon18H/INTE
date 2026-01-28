import type { Config } from "tailwindcss";

const config: Config = {
  content: ["./app/**/*.{ts,tsx}", "./components/**/*.{ts,tsx}"],
  darkMode: "class",
  theme: {
    extend: {
      colors: {
        background: "#0b1120",
        card: "#111827",
        accent: "#22d3ee",
      },
    },
  },
  plugins: [],
};

export default config;
