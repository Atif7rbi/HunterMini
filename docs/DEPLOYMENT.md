# Deployment

## PM2

```bash
cd ~/Sniper/HunterMini
pm2 start ecosystem.config.js
pm2 save
```

## Manual

```bash
cd ~/Sniper/HunterMini
./run.sh
```

The dashboard binds to port `8083` by default.
