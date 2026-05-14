# SnapClass – AI Attendance

Streamlit app that takes classroom attendance from photos (face recognition with dlib) or audio
(speaker verification with Resemblyzer). Backed by Supabase.

## Local development

```bash
python3.13 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

Create `.streamlit/secrets.toml` (already gitignored):

```toml
SUPABASE_URL = "https://<your-project>.supabase.co"
SUPABASE_KEY = "<your-anon-key>"
# Optional: only needed if you want share QR codes to use a fixed public URL
# APP_URL = "https://your-app.streamlit.app"
```

Run:

```bash
streamlit run app.py
```

## System packages (`packages.txt`)

`librosa` needs `libsndfile1` at the OS level – that's what `packages.txt` provides.
Streamlit Cloud installs everything in `packages.txt` via `apt-get` automatically.

## Deploying to Streamlit Cloud

1. Push this repository to GitHub.
2. On [share.streamlit.io](https://share.streamlit.io), create a new app pointing at `app.py`.
3. In **Advanced settings** make sure Python version is **3.13** (also pinned by `.python-version`).
4. Open **Settings → Secrets** for the app and paste the same TOML you use locally:

   ```toml
   SUPABASE_URL = "..."
   SUPABASE_KEY = "..."
   APP_URL = "https://<your-app>.streamlit.app"
   ```

   `APP_URL` is optional – without it, the share-QR dialog auto-detects the current
   browser origin and falls back to `localhost:8501` only when neither is available.
5. Click **Deploy**. The first build compiles nothing (everything ships as wheels):
   `dlib-bin` provides `dlib` as a pre-built wheel for Python 3.13, and
   `face_recognition_models` is pulled from GitHub with `setuptools<70` to keep its
   legacy `setup.py` happy.

## Project layout

```
app.py                       # Entry point – routes to student / teacher / home
src/
  screens/                   # Top-level pages
  components/                # Reusable widgets and @st.dialog modals
  pipelines/face_pipeline.py # dlib face detection + SVM classifier
  pipelines/voice_pipeline.py# Resemblyzer voice embeddings
  database/                  # Supabase client + queries
  ui/base_layout.py          # Shared CSS / theme
```

## Supabase schema

The code expects these tables/columns to exist:

- `teachers`: `teacher_id`, `username`, `password`, `name`
- `students`: `student_id`, `name`, `face_embedding` (float8[]), `voice_embedding` (float8[])
- `subjects`: `subject_id`, `subject_code`, `name`, `section`, `teacher_id`
- `subject_students`: `student_id`, `subject_id`
- `attendance_logs`: `student_id`, `subject_id`, `timestamp`, `is_present`
