import streamlit as st
from bot import get_bot_response
from pathlib import Path
import json
import uuid
from datetime import datetime, timezone
from typing import Dict, List


st.set_page_config(page_title="React Solving", page_icon="🤖", layout="wide")

LOGS_DIR = Path(__file__).parent / "logs"
LOGS_DIR.mkdir(parents=True, exist_ok=True)


def _utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def _ensure_session():
    if "session_id" not in st.session_state:
        st.session_state.session_id = uuid.uuid4().hex
    if "session_started_at" not in st.session_state:
        st.session_state.session_started_at = _utc_now_iso()


def _session_log_path(session_id: str) -> Path:
    return LOGS_DIR / f"{session_id}.jsonl"


def _append_log_event(session_id: str, event: dict) -> None:
    path = _session_log_path(session_id)
    event = dict(event)
    event.setdefault("ts", _utc_now_iso())
    event.setdefault("session_id", session_id)
    with path.open("a", encoding="utf-8") as f:
        f.write(json.dumps(event, ensure_ascii=False) + "\n")


def _load_session_messages(session_id: str) -> List[Dict[str, str]]:
    path = _session_log_path(session_id)
    if not path.exists():
        return []
    messages: List[Dict[str, str]] = []
    with path.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                ev = json.loads(line)
            except json.JSONDecodeError:
                continue
            if ev.get("type") == "message" and ev.get("role") in ("user", "assistant"):
                messages.append({"role": ev["role"], "content": ev.get("content", "")})
    return messages


def _list_sessions() -> List[str]:
    # newest first
    paths = sorted(LOGS_DIR.glob("*.jsonl"), key=lambda p: p.stat().st_mtime, reverse=True)
    return [p.stem for p in paths]


_ensure_session()

if "messages" not in st.session_state:
    st.session_state.messages = []


st.title("🤖 React Solving")

st.sidebar.markdown("### Сессии")
sessions = _list_sessions()

col_a, col_b = st.sidebar.columns(2)
with col_a:
    if st.sidebar.button("🆕 Новая"):
        st.session_state.session_id = uuid.uuid4().hex
        st.session_state.session_started_at = _utc_now_iso()
        st.session_state.messages = []
        _append_log_event(st.session_state.session_id, {"type": "session_start"})
        st.rerun()

st.sidebar.caption(f"Текущая сессия: `{st.session_state.session_id}`")
current_log_path = _session_log_path(st.session_state.session_id)
if current_log_path.exists():
    st.sidebar.download_button(
        "⬇️ Скачать лог (jsonl)",
        data=current_log_path.read_bytes(),
        file_name=current_log_path.name,
        mime="application/jsonl",
    )

with st.sidebar.expander(f"Список сессий ({len(sessions)})", expanded=True):
    if not sessions:
        st.caption("Пока нет сохранённых сессий.")
    else:
        for sid in sessions:
            is_current = sid == st.session_state.session_id
            label = f"▶ {sid}" if is_current else sid
            if st.button(label, key=f"load_session_{sid}"):
                st.session_state.session_id = sid
                st.session_state.session_started_at = _utc_now_iso()
                st.session_state.messages = _load_session_messages(sid)
                st.rerun()

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

prompt = st.chat_input("Введите ваше сообщение…")
if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    _append_log_event(st.session_state.session_id, {"type": "message", "role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    response = get_bot_response(prompt)
    st.session_state.messages.append({"role": "assistant", "content": response})
    _append_log_event(st.session_state.session_id, {"type": "message", "role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.markdown(response)
