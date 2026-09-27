"""
Deterministic Devanagari (Hindi) to Latin transliterator for ENTIVYRE.
Provides phonetic and dictionary transliteration for Indian business names.
Air-gapped: zero external web calls or models.
"""
from __future__ import annotations

import re
from typing import Dict, Tuple

# Common Hindi business term transliterations
HINDI_BUSINESS_TERMS: Dict[str, str] = {
    "एंटरप्राइजेज": "enterprises",
    "इन्टरप्राइजेज": "enterprises",
    "इंटरप्राइजेज": "enterprises",
    "इंटरप्राइज": "enterprise",
    "उद्योग": "udyog",
    "उद्योगों": "udyog",
    "प्राइवेट": "private",
    "प्रा": "pvt",
    "लिमिटेड": "limited",
    "लि": "ltd",
    "कंपनी": "company",
    "ट्रेडर्स": "traders",
    "ट्रेडिंग": "trading",
    "स्टोर्स": "stores",
    "स्टोर": "store",
    "दुकान": "store",
    "सर्विसेज": "services",
    "सर्विस": "service",
    "संस": "sons",
    "ब्रदर्स": "brothers",
    "एसोसिएट्स": "associates",
    "एंड": "and",
    "श्री": "shri",
    "महालक्ष्मी": "mahalaxmi",
    "लक्ष्मी": "laxmi",
    "गणेश": "ganesh",
    "बालाजी": "balaji",
    "कृष्णा": "krishna",
    "शिव": "shiva",
    "होटल": "hotel",
    "रेस्टोरेंट": "restaurant",
    "भंडार": "bhandar",
    "मेडिकल": "medical",
    "फार्मा": "pharma",
    "टेक्सटाइल्स": "textiles",
    "ज्वेलर्स": "jewellers",
    "ऑटो": "auto",
    "मोटर्स": "motors",
    "इंटरनेशनल": "international",
    "इन्टरनेशनल": "international",
    "लॉजिस्टिक्स": "logistics",
    "लॉजिस्टिक": "logistics",
    "टेक्नोलॉजी": "technology",
    "टेक्नोलॉजीज": "technologies",
    "इंजीनियरिंग": "engineering",
    "कंस्ट्रक्शन": "construction",
    "इंफ्रास्ट्रक्चर": "infrastructure",
    "इंफ्रा": "infra",
    "ग्लोबल": "global",
    "सिक्योरिटी": "security",
    "फाइनेंस": "finance",
    "फाइनेंशियल": "financial",
    "इंडिया": "india",
    "इंडियन": "indian",
    "डेवलपर्स": "developers",
    "प्रॉपर्टीज": "properties",
    "केमिकल्स": "chemicals",
    "इलेक्ट्रिकल्स": "electricals",
    "इलेक्ट्रॉनिक्स": "electronics",
    "मैनेजमेंट": "management",
    "कंसल्टेंसी": "consultancy",
    "कंसल्टेंट्स": "consultants",
    "एग्रो": "agro",
    "फूड्स": "foods",
    "पैकर्स": "packers",
    "मूवर्स": "movers",
    "हाईटेक": "hitech",
    "हाइटेक": "hitech",
    "एस्टेट": "estate",
    "इस्टेट": "estate",
}

def map_indic_to_devanagari(text: str) -> str:
    """
    Maps all major Brahmi-derived Indic scripts (Bengali, Gurmukhi, Gujarati, Oriya,
    Tamil, Telugu, Kannada, Malayalam) to Devanagari using the exact 0x80 Unicode block alignment.
    """
    res = []
    has_indic = False
    for c in text:
        code = ord(c)
        if 0x0980 <= code <= 0x0D7F:
            res.append(chr(0x0900 + (code % 0x80)))
            has_indic = True
        else:
            res.append(c)
    return "".join(res) if has_indic else text

# Devanagari Unicode character mapping (consonants, vowels, matras)
DEVANAGARI_MAP: Dict[str, str] = {
    # Vowels
    "अ": "a", "आ": "aa", "इ": "i", "ई": "ee", "उ": "u", "ऊ": "oo",
    "ऋ": "ri", "ए": "e", "ऐ": "ai", "ओ": "o", "औ": "au",
    # Consonants
    "क": "k", "ख": "kh", "ग": "g", "घ": "gh", "ङ": "ng",
    "च": "ch", "छ": "chh", "ज": "j", "झ": "jh", "ञ": "ny",
    "ट": "t", "ठ": "th", "ड": "d", "ढ": "dh", "ण": "n",
    "त": "t", "थ": "th", "द": "d", "ध": "dh", "न": "n",
    "प": "p", "फ": "ph", "ब": "b", "भ": "bh", "म": "m",
    "य": "y", "र": "r", "ल": "l", "व": "v", "श": "sh",
    "ष": "sh", "स": "s", "ह": "h",
    # Additional
    "क्ष": "ksh", "त्र": "tr", "ज्ञ": "gy",
    # Matras (vowel signs)
    "ा": "a", "ि": "i", "ी": "ee", "ु": "u", "ू": "oo",
    "ृ": "ri", "े": "e", "ै": "ai", "ो": "o", "ौ": "au",
    "ं": "n", "ँ": "n", "ः": "h", "्": "",
    # Numerals
    "०": "0", "१": "1", "२": "2", "३": "3", "४": "4",
    "५": "5", "६": "6", "७": "7", "८": "8", "९": "9",
}

DEVANAGARI_REGEX = re.compile(r"[\u0900-\u097F]+")


def transliterate_devanagari(text: str) -> Tuple[str, bool]:
    """
    Transliterates Devanagari and Brahmi-derived Indic words to Latin script.
    First maps any Indic scripts to Devanagari, then matches full business terms;
    then falls back to character mapping. Returns (transliterated_text, was_modified).
    """
    text = map_indic_to_devanagari(text)
    if not DEVANAGARI_REGEX.search(text):
        return text, False

    words = text.split()
    out_words = []

    for word in words:
        # Check dictionary match
        cleaned_word = re.sub(r"[^\u0900-\u097F]", "", word)
        if cleaned_word in HINDI_BUSINESS_TERMS:
            out_words.append(HINDI_BUSINESS_TERMS[cleaned_word])
            continue

        # Character-by-character transliteration
        trans_chars = []
        for ch in word:
            if ch in DEVANAGARI_MAP:
                trans_chars.append(DEVANAGARI_MAP[ch])
            else:
                trans_chars.append(ch)
        out_words.append("".join(trans_chars))

    return " ".join(out_words), True
