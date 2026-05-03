import json
import os
import sys
from pathlib import Path

import webview

APP_NAME = "AlgoDesk"
STATE_FILE_NAME = "state.json"


def resource_path(filename):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, filename)
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), filename)


def state_file_path():
    appdata = os.getenv("APPDATA")
    if appdata:
        base_dir = Path(appdata)
    else:
        base_dir = Path.home() / "AppData" / "Roaming"
    app_dir = base_dir / APP_NAME
    app_dir.mkdir(parents=True, exist_ok=True)
    return app_dir / STATE_FILE_NAME


class AppBridge:
    def __init__(self):
        self.path = state_file_path()

    def _default_state(self):
        return {"progress": {}}

    def _normalize_progress(self, progress):
        if not isinstance(progress, dict):
            return {}
        return {str(key): bool(value) for key, value in progress.items()}

    def _read_state(self):
        if not self.path.exists():
            return self._default_state()
        try:
            data = json.loads(self.path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            return self._default_state()
        if not isinstance(data, dict):
            return self._default_state()
        return {"progress": self._normalize_progress(data.get("progress", {}))}

    def _write_state(self, state):
        payload = {"progress": self._normalize_progress(state.get("progress", {}))}
        self.path.write_text(json.dumps(payload, indent=2), encoding="utf-8")

    def load_progress(self):
        return self._read_state().get("progress", {})

    def save_progress(self, progress):
        state = self._read_state()
        state["progress"] = self._normalize_progress(progress)
        self._write_state(state)
        return {"ok": True, "count": len(state["progress"]), "path": str(self.path)}


html_path = resource_path("dsa_notes_interview_cp.html")
bridge = AppBridge()

webview.create_window(
    APP_NAME,
    html_path,
    js_api=bridge,
    maximized=True,
    resizable=True,
    confirm_close=True,
)

webview.start()
