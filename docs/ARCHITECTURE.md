# HunterMini Architecture

HunterMini keeps the HunterBot trading logic intact at baseline, but separates runtime identity and storage.

```text
HunterBot Production   -> unchanged, official results
HunterMini Validation  -> isolated test candidate
```

## Isolation Boundaries

- Separate database: `data/Hunter_mini.db`
- Separate PM2 process name: `HunterMini`
- Separate UI port: `8083`
- Separate logs: `logs/hunter_mini.log`
- Separate experiment metadata: `experiments/active.yaml`

## Promotion Path

```text
Idea -> HunterMini experiment -> Mini report -> Decision -> optional HunterBot promotion
```
