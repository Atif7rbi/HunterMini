module.exports = {
  apps: [
    {
      name: "HunterMini",
      script: ".venv/bin/python",
      args: "-m ui.app",
      cwd: __dirname,
      interpreter: "none",
      autorestart: true,
      watch: false,
      max_memory_restart: "500M",
      env: {
        PYTHONUNBUFFERED: "1",
        LH_UI_PORT: "8083",
        LH_UI_HOST: "0.0.0.0"
      }
    }
  ]
};
