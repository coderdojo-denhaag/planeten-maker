
import os
import base64
import requests
from dotenv import load_dotenv

load_dotenv()

API_SLEUTEL = os.getenv("OPENROUTER_API_KEY")

MODEL_TEKST = os.getenv(
    "OPENROUTER_MODEL_TEKST",
    "google/gemini-3.1-flash-lite"
)

MODEL_AFBEELDING = os.getenv(
    "OPENROUTER_MODEL_AFBEELDING",
    "bytedance-seed/seedream-4.5"
)

BASIS_URL = "https://openrouter.ai/api/v1"


def maak_tekst(beschrijving):
    """Maak met AI een verhaal over de planeet."""

    if not API_SLEUTEL:
        raise RuntimeError(
            "De OpenRouter API-sleutel ontbreekt in het .env-bestand."
        )

    opdracht = (
        "Je bent een creatieve schrijver voor kinderen van 10 tot 13 jaar. "
        "Schrijf een spannend verhaal van ongeveer 150 woorden over deze "
        "planeet. Houd rekening met de zwaartekracht, de bewoners, het "
        "water, de planten en het aantal manen. Verander deze kenmerken "
        "niet. Gebruik begrijpelijk Nederlands.\n\n"
        "Beschrijving van de planeet:\n"
        + beschrijving
    )

    antwoord = requests.post(
        f"{BASIS_URL}/chat/completions",
        headers={
            "Authorization": f"Bearer {API_SLEUTEL}",
            "Content-Type": "application/json"
        },
        json={
            "model": MODEL_TEKST,
            "messages": [
                {
                    "role": "user",
                    "content": opdracht
                }
            ],
            "temperature": 0.8,
            "max_tokens": 500
        },
        timeout=120
    )

    antwoord.raise_for_status()
    gegevens = antwoord.json()

    return gegevens["choices"][0]["message"]["content"]


def maak_afbeelding(opdracht):
    """Maak een afbeelding van de planeet en sla deze lokaal op."""

    if not API_SLEUTEL:
        raise RuntimeError(
            "De OpenRouter API-sleutel ontbreekt in het .env-bestand."
        )

    antwoord = requests.post(
        f"{BASIS_URL}/images",
        headers={
            "Authorization": f"Bearer {API_SLEUTEL}",
            "Content-Type": "application/json"
        },
        json={
            "model": MODEL_AFBEELDING,
            "prompt": opdracht,
            "aspect_ratio": "16:9",
            "resolution": "1K"
        },
        timeout=180
    )

    antwoord.raise_for_status()
    gegevens = antwoord.json()

    afbeelding_data = gegevens["data"][0]["b64_json"]
    afbeeldings_bytes = base64.b64decode(afbeelding_data)

    bestandsnaam = "mijn_planeet.png"

    with open(bestandsnaam, "wb") as bestand:
        bestand.write(afbeeldings_bytes)

    return bestandsnaam
