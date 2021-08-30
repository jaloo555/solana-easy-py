# Solana Epoch Counter

> @slurpcap

TLDR: 
```bash 
curl https://api.mainnet-beta.solana.com -X POST -H "Content-Type: application/json" -d '
  {"jsonrpc":"2.0","id":1, "method":"getEpochInfo"}
'
```

## Mainnet Beta
### Endpoints
- https://api.mainnet-beta.solana.com - Solana-hosted api node cluster, backed by a load balancer; rate-limited
- https://solana-api.projectserum.com - Project Serum-hosted api node
### Rate Limits
- Maximum number of requests per 10 seconds per IP: 100
- Maximum number of requests per 10 seconds per IP for a   single RPC: 40
- Maximum concurrent connections per IP: 40
- Maximum connection rate per 10 seconds per IP: 40
- Maximum amount of data per 30 second: 100 MB