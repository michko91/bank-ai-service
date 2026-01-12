def berechne_kredit_limit(gehalt: float, faktor: int = 3) -> float:
    """Berechnet das Limit basierend auf dem Gehalt (Java-Stil Typisierung)"""
    return gehalt * faktor

mein_limit = berechne_kredit_limit(5000.0)
print(f"Dein Kreditlimit ist: {mein_limit}€")