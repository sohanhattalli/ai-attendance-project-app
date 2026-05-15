# SnapClass Landing Page (Flask)

Marketing site for SnapClass. The live app runs on [Streamlit Cloud](https://snapclass-maino.streamlit.app/).

## Local development

```bash
cd frontend
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

Open http://localhost:5002

## Deploy on Vercel

1. Push this repo to GitHub.
2. [vercel.com](https://vercel.com) → **Add New Project** → import the repo.
3. Set **Root Directory** to `frontend`.
4. Framework: auto-detected from `vercel.json` (Python / Flask).
5. Deploy.

Or from this folder with the Vercel CLI:

```bash
npx vercel --prod
```
