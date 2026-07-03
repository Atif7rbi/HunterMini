# HunterMini

HunterMini is a validation sandbox derived from HunterBot. Its purpose is to test focused changes safely while HunterBot production continues running unchanged.

## Role

- **HunterBot**: production system. Do not modify for experiments.
- **HunterMini**: validation sandbox. Test one controlled experiment at a time.

## Defaults

| Item | Value |
|---|---|
| App name | HunterMini |
| Role | Validation Sandbox |
| Port | 8083 |
| Database | `data/Hunter_mini.db` |
| Logs | `logs/hunter_mini.log` |
| Active experiment | `experiments/active.yaml` |

## Golden Rule

No change is promoted to HunterBot until HunterMini produces a clear validation report.
