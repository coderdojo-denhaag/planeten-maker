# Planetenmaker

Een Python-hulpmodule die met OpenRouter een verhaal en afbeelding van een zelfbedachte planeet maakt.

## Benodigdheden

- Python 3.10 of nieuwer
- Een OpenRouter API-sleutel

## Installeren

Maak een virtuele omgeving en installeer de afhankelijkheden:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Maak vervolgens een `.env`-bestand in de projectmap:

```dotenv
OPENROUTER_API_KEY=plaats_hier_je_api_sleutel
# Optioneel: overschrijf de standaardmodellen
OPENROUTER_MODEL_TEKST=google/gemini-3.1-flash-lite
OPENROUTER_MODEL_AFBEELDING=bytedance-seed/seedream-4.5
```

Bewaar je echte API-sleutel alleen in `.env`. Dit bestand wordt door Git genegeerd en hoort niet in GitHub.

## Gebruik

Importeer `maak_tekst` en `maak_afbeelding` vanuit `ai_hulp.py` in je eigen Python-programma. `maak_tekst(beschrijving)` geeft een verhaal terug. `maak_afbeelding(opdracht)` slaat de gegenereerde afbeelding op als `mijn_planeet.png` en geeft de bestandsnaam terug.
