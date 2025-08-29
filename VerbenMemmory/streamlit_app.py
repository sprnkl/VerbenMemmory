# streamlit_app.py
# Unregelmäßige Verben – Zuordnen (tap-to-match; iOS-freundlich)
import random
import time
from datetime import datetime, timezone
import streamlit as st

st.set_page_config(page_title="Unregelmäßige Verben – Zuordnen", page_icon="📚", layout="centered")

# --------------------
# Daten (vollständig)
# --------------------
VERBS = [
    {"infinitive": "be", "pastSimple": "was/were", "pastParticiple": "been", "meaning": "sein"},
    {"infinitive": "begin", "pastSimple": "began", "pastParticiple": "begun", "meaning": "beginnen, anfangen"},
    {"infinitive": "break", "pastSimple": "broke", "pastParticiple": "broken", "meaning": "brechen, zerbrechen"},
    {"infinitive": "bring", "pastSimple": "brought", "pastParticiple": "brought", "meaning": "bringen, mitbringen"},
    {"infinitive": "buy", "pastSimple": "bought", "pastParticiple": "bought", "meaning": "kaufen"},
    {"infinitive": "catch", "pastSimple": "caught", "pastParticiple": "caught", "meaning": "fangen, erwischen"},
    {"infinitive": "come", "pastSimple": "came", "pastParticiple": "come", "meaning": "kommen"},
    {"infinitive": "cost", "pastSimple": "cost", "pastParticiple": "cost", "meaning": "kosten"},
    {"infinitive": "cut", "pastSimple": "cut", "pastParticiple": "cut", "meaning": "schneiden, mähen"},
    {"infinitive": "do", "pastSimple": "did", "pastParticiple": "done", "meaning": "tun, machen"},
    {"infinitive": "drink", "pastSimple": "drank", "pastParticiple": "drunk", "meaning": "trinken"},
    {"infinitive": "drive", "pastSimple": "drove", "pastParticiple": "driven", "meaning": "(Auto) fahren, antreiben"},
    {"infinitive": "eat", "pastSimple": "ate", "pastParticiple": "eaten", "meaning": "essen"},
    {"infinitive": "fall", "pastSimple": "fell", "pastParticiple": "fallen", "meaning": "fallen, hinfallen"},
    {"infinitive": "feel", "pastSimple": "felt", "pastParticiple": "felt", "meaning": "fühlen"},
    {"infinitive": "find", "pastSimple": "found", "pastParticiple": "found", "meaning": "finden"},
    {"infinitive": "fly", "pastSimple": "flew", "pastParticiple": "flown", "meaning": "fliegen"},
    {"infinitive": "forget", "pastSimple": "forgot", "pastParticiple": "forgotten", "meaning": "vergessen"},
    {"infinitive": "get", "pastSimple": "got", "pastParticiple": "got/gotten", "meaning": "bekommen, holen"},
    {"infinitive": "give", "pastSimple": "gave", "pastParticiple": "given", "meaning": "geben"},
    {"infinitive": "go", "pastSimple": "went", "pastParticiple": "gone", "meaning": "gehen"},
    {"infinitive": "have", "pastSimple": "had", "pastParticiple": "had", "meaning": "haben"},
    {"infinitive": "hear", "pastSimple": "heard", "pastParticiple": "heard", "meaning": "hören"},
    {"infinitive": "hurt", "pastSimple": "hurt", "pastParticiple": "hurt", "meaning": "verletzen, wehtun"},
    {"infinitive": "keep", "pastSimple": "kept", "pastParticiple": "kept", "meaning": "behalten"},
    {"infinitive": "know", "pastSimple": "knew", "pastParticiple": "known", "meaning": "wissen, kennen"},
    {"infinitive": "leave", "pastSimple": "left", "pastParticiple": "left", "meaning": "abfahren, weggehen"},
    {"infinitive": "lose", "pastSimple": "lost", "pastParticiple": "lost", "meaning": "verlieren"},
    {"infinitive": "make", "pastSimple": "made", "pastParticiple": "made", "meaning": "machen"},
    {"infinitive": "mean", "pastSimple": "meant", "pastParticiple": "meant", "meaning": "bedeuten, meinen"},
    {"infinitive": "meet", "pastSimple": "met", "pastParticiple": "met", "meaning": "treffen, kennenlernen"},
    {"infinitive": "pay", "pastSimple": "paid", "pastParticiple": "paid", "meaning": "bezahlen"},
    {"infinitive": "put", "pastSimple": "put", "pastParticiple": "put", "meaning": "setzen, legen"},
    {"infinitive": "read", "pastSimple": "read", "pastParticiple": "read", "meaning": "lesen"},
    {"infinitive": "ride", "pastSimple": "rode", "pastParticiple": "ridden", "meaning": "reiten, fahren"},
    {"infinitive": "ring", "pastSimple": "rang", "pastParticiple": "rung", "meaning": "läuten, anrufen"},
    {"infinitive": "run", "pastSimple": "ran", "pastParticiple": "run", "meaning": "rennen, laufen"},
    {"infinitive": "say", "pastSimple": "said", "pastParticiple": "said", "meaning": "sagen"},
    {"infinitive": "see", "pastSimple": "saw", "pastParticiple": "seen", "meaning": "sehen"},
    {"infinitive": "sell", "pastSimple": "sold", "pastParticiple": "sold", "meaning": "verkaufen"},
    {"infinitive": "send", "pastSimple": "sent", "pastParticiple": "sent", "meaning": "schicken"},
    {"infinitive": "sing", "pastSimple": "sang", "pastParticiple": "sung", "meaning": "singen"},
    {"infinitive": "sit", "pastSimple": "sat", "pastParticiple": "sat", "meaning": "sitzen"},
    {"infinitive": "sleep", "pastSimple": "slept", "pastParticiple": "slept", "meaning": "schlafen"},
    {"infinitive": "speak", "pastSimple": "spoke", "pastParticiple": "spoken", "meaning": "sprechen"},
    {"infinitive": "spend", "pastSimple": "spent", "pastParticiple": "spent", "meaning": "ausgeben, verbringen"},
    {"infinitive": "stand", "pastSimple": "stood", "pastParticiple": "stood", "meaning": "stehen"},
    {"infinitive": "take", "pastSimple": "took", "pastParticiple": "taken", "meaning": "nehmen"},
    {"infinitive": "teach", "pastSimple": "taught", "pastParticiple": "taught", "meaning": "unterrichten"},
    {"infinitive": "tell", "pastSimple": "told", "pastParticiple": "told", "meaning": "erzählen"},
    {"infinitive": "think", "pastSimple": "thought", "pastParticiple": "thought", "meaning": "denken"},
    {"infinitive": "throw", "pastSimple": "threw", "pastParticiple": "thrown", "meaning": "werfen"},
    {"infinitive": "understand", "pastSimple": "understood", "pastParticiple": "understood", "meaning": "verstehen"},
    {"infinitive": "wear", "pastSimple": "wore", "pastParticiple": "worn", "meaning": "tragen, anhaben"},
    {"infinitive": "win", "pastSimple": "won", "pastParticiple": "won", "meaning": "gewinnen"},
    {"infinitive": "write", "pastSimple": "wrote", "pastParticiple": "written", "meaning": "schreiben"},
]

TARGETS = [
    ("Infinitive", "infinitive"),
    ("Past Simple", "pastSimple"),
    ("Past Participle", "pastParticiple"),
    ("Meaning (Deutsch)", "meaning"),
]

PLACEHOLDER = "— bitte wählen —"

# --------------------
# State / Rundenlogik
# --------------------
def new_round():
    verb = random.choice(VERBS)
    items = [
        {"text": verb["infinitive"], "match": "infinitive", "hidden": False},
        {"text": verb["pastSimple"], "match": "pastSimple", "hidden": False},
        {"text": verb["pastParticiple"], "match": "pastParticiple", "hidden": False},
        {"text": verb["meaning"], "match": "meaning", "hidden": False},
    ]
    random.shuffle(items)
    st.session_state.round = {
        "verb": verb,
        "items": items,
        "matches": {t[1]: None for t in TARGETS},
        "start": datetime.now(timezone.utc).timestamp(),
        "completed": False,
    }
    st.session_state.selected_idx = None
    st.session_state.word_radio = PLACEHOLDER  # Radio auf Platzhalter setzen

# Init
if "points_total" not in st.session_state:
    st.session_state.points_total = 0
if "round" not in st.session_state:
    new_round()
if "selected_idx" not in st.session_state:
    st.session_state.selected_idx = None
if "word_radio" not in st.session_state:
    st.session_state.word_radio = PLACEHOLDER

# --------------------
# UI
# --------------------
st.title("Unregelmäßige Verben – Zuordnen (Tippen statt Ziehen)")
st.caption("Links ein **Wort** wählen, rechts das **Ziel** tippen. Nach einem Treffer springt die Auswahl automatisch zurück.")

c1, c2, c3 = st.columns(3)
with c1:
    if st.button("🔁 Runde neu starten"):
        new_round()
with c2:
    if st.button("🧹 Punkte zurücksetzen"):
        st.session_state.points_total = 0
        new_round()
with c3:
    if st.button("❌ Auswahl aufheben"):
        st.session_state.selected_idx = None
        st.session_state.word_radio = PLACEHOLDER

elapsed = int(time.time() - st.session_state.round["start"])
st.markdown(f"**Zeit:** {elapsed} Sek.  **Punkte gesamt:** {st.session_state.points_total}")

left, right = st.columns(2, gap="large")

# --------- Wörter (stabile Auswahl via Radio) ----------
with left:
    st.subheader("Wörter")
    options = [(idx, it["text"]) for idx, it in enumerate(st.session_state.round["items"]) if not it["hidden"]]
    if options:
        labels = [PLACEHOLDER] + [txt for _, txt in options]
        indices = [None] + [idx for idx, _ in options]

        # Falls aktuell gewähltes Wort inzwischen versteckt wurde → zurücksetzen
        if st.session_state.selected_idx is not None:
            if st.session_state.round["items"][st.session_state.selected_idx]["hidden"]:
                st.session_state.selected_idx = None
                st.session_state.word_radio = PLACEHOLDER

        # Radio gezielt auf den in Session stehenden Wert setzen
        if st.session_state.word_radio not in labels:
            st.session_state.word_radio = PLACEHOLDER

        # Index für das Radio bestimmen
        idx_default = labels.index(st.session_state.word_radio)
        chosen_label = st.radio("Wähle ein Wort", labels, index=idx_default, key="word_radio")

        # Auswahl in Index zurückübersetzen
        st.session_state.selected_idx = indices[labels.index(chosen_label)]
        if st.session_state.selected_idx is not None:
            st.info(f"Ausgewählt: **{chosen_label}**")
    else:
        st.write("Alle Wörter sind zugeordnet ✅")

# --------- Ziele (Buttons) ----------
with right:
    st.subheader("Ziele")
    for label, target_key in TARGETS:
        current_match = st.session_state.round["matches"][target_key]
        if current_match is None:
            clicked = st.button(label, key=f"target_{target_key}")
        else:
            matched_text = st.session_state.round["items"][current_match]["text"]
            clicked = st.button(f"{label}: ✅ {matched_text}", key=f"target_{target_key}", disabled=True)

        if clicked:
            sel_idx = st.session_state.selected_idx
            if sel_idx is None:
                st.warning("Bitte erst links ein Wort auswählen.")
            else:
                item = st.session_state.round["items"][sel_idx]
                if item["match"] == target_key:
                    # korrekt → Wort verstecken, Ziel markieren
                    st.session_state.round["matches"][target_key] = sel_idx
                    st.session_state.round["items"][sel_idx]["hidden"] = True
                    st.session_state.points_total += 1
                    # WICHTIG: Auswahl automatisch auf Platzhalter zurücksetzen
                    st.session_state.selected_idx = None
                    st.session_state.word_radio = PLACEHOLDER
                    st.success("Richtig! ✅")
                else:
                    st.error("Falsch – wähle ein anderes Ziel (Auswahl bleibt).")

# --------- Rundenabschluss ----------
all_done = all(v is not None for v in st.session_state.round["matches"].values())
if all_done and not st.session_state.round["completed"]:
    st.session_state.round["completed"] = True
    total_time = int(time.time() - st.session_state.round["start"])
    st.success(f"Geschafft! Zeit: {total_time} Sek.")
    st.button("Nächste Runde starten", on_click=new_round)
