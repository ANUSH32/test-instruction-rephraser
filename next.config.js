/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  async rewrites() {
    return [
      {
        source: '/api/rephrase',
        destination: 'http://localhost:5000/api/rephrase',
      },
    ];
  },
};

module.exports = nextConfig;
