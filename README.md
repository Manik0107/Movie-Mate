# Movie-Mate

Movie‑Mate is a lightweight movie recommendation web app built with Streamlit. It uses a precomputed similarity matrix and a movie dataset to recommend titles similar to a selected movie and fetches additional details (poster, plot, genre, year) from the OMDb API.

## Key features

- Select a movie from a searchable dropdown list.
- Get the top 5 recommended movies based on a similarity matrix.
- Fetch poster, plot, year and genre information from the OMDb API for each recommendation.

## Repository structure

- `app.py` — Streamlit application entrypoint.
- `movie_list.pkl` — Pickled pandas DataFrame containing movie metadata (used by `app.py`).
- `similarity.pkl` — Pickled similarity matrix used to compute recommendations.
- `top10K-TMDB-movies.csv` — Original CSV dataset (reference / source).

> Note: The pickled files (`movie_list.pkl` and `similarity.pkl`) must be present in the project root for the app to work.

## Prerequisites

- Python 3.8 or newer
- A working internet connection to query the OMDb API

Recommended Python packages (minimum):

- streamlit
- pandas
- requests

You can install the essentials with pip. It's recommended to use a virtual environment.

```bash
# macOS / zsh example
python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install streamlit pandas requests
```

If you prefer, create a `requirements.txt` with the above packages and run:

```bash
pip install -r requirements.txt
```

## Configuration

The app queries the OMDb API to fetch movie posters and details. The current `app.py` contains a hard-coded API key placeholder. For production or personal use, replace the placeholder key with your own OMDb API key.

Two options to configure the key safely:

1. Edit `app.py` to set `api_key` to your key (quick but less secure).
2. Preferably, update `app.py` to read an environment variable (e.g., `OMDB_API_KEY`) and export it before running:

```bash
export OMDB_API_KEY="your_api_key_here"
```

If you choose option 2, update the `fetch_movie_details` function in `app.py` to read the key from `os.environ.get('OMDB_API_KEY')`.

## Running the app

From the project root, with your virtual environment activated and dependencies installed, run:

```bash
streamlit run app.py
```

Open the displayed local URL in your browser (Streamlit will show it in the terminal). Click the dropdown to choose a movie and press the "Recommend" button to see results.

## Troubleshooting

- If you see `FileNotFoundError` for `movie_list.pkl` or `similarity.pkl`, ensure they exist in the project root and are readable.
- If movie posters or details are missing, check your OMDb API key and the API usage limits.
- If the app fails to start with an ImportError, confirm required packages are installed in the active environment.

## Data and credits

The included CSV (`top10K-TMDB-movies.csv`) is a reference dataset. The app uses a precomputed similarity matrix and a pickled DataFrame; if you want to re-generate these artifacts you will need to preprocess the CSV (feature extraction, vectorization, similarity calculation) — this repository does not currently include that pipeline.

## Contributing

Contributions are welcome. If you plan to add features, please:

1. Open an issue describing the proposed change.
2. Create a feature branch and submit a pull request with tests or usage notes.

Suggested follow-ups:

- Add a `requirements.txt` and a small setup script to build the pickles from the CSV.
- Make the OMDb API key configurable via environment variables and document it.

## License

This project is provided under the MIT License. See `LICENSE` for details (add a LICENSE file if you want to publish the project).

---

If you'd like, I can also:

- create a `requirements.txt` for you based on the app imports,
- add a small script to validate that `movie_list.pkl` and `similarity.pkl` exist and report helpful errors,
- or modify `app.py` to read the OMDb key from an environment variable and update the README accordingly.
