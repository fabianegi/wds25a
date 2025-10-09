<!-- Banner -->
<p align="center">
  <img src="https://raw.githubusercontent.com/edent/SuperTinyIcons/master/images/svg/python.svg" alt="Python Logo" width="120"/>
</p>

<h1 align="center">🐍 Python Kurs – Hochschule Projekt</h1>

<p align="center">
  <b>Ein kreatives, praxisnahes Python-Projekt im Rahmen meines Hochschulkurses</b><br/>
  <sub>Von ersten Grundlagen bis hin zu komplexeren Anwendungen</sub>
</p>

---

<!-- Badges -->
<p align="center">
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3.11%2B-blue.svg?logo=python" alt="Python Version"></a>
  <a href="https://github.com/dein-benutzername/dein-repo/stargazers"><img src="https://img.shields.io/github/stars/dein-benutzername/dein-repo?color=yellow&logo=github" alt="Stars"></a>
  <a href="https://github.com/dein-benutzername/dein-repo/issues"><img src="https://img.shields.io/github/issues/dein-benutzername/dein-repo.svg" alt="Issues"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License"></a>
</p>

---

## 📚 Inhaltsverzeichnis

- [Über das Projekt](#-über-das-projekt)
- [Features](#-features)
- [Technologien](#-technologien)
- [Installation](#-installation)
- [Verwendung](#-verwendung)
- [Projektstruktur](#-projektstruktur)
- [Beispielcode](#-beispielcode)
- [Screenshots](#-screenshots)
- [Roadmap](#-roadmap)
- [Mitwirken](#-mitwirken)
- [Lizenz](#-lizenz)
- [Kontakt](#-kontakt)

---

## 🧠 Über das Projekt

Dieses Projekt ist im Rahmen meines Python-Kurses an der **[Name der Hochschule](https://www.example.com)** entstanden.  
Ziel ist es, praxisnah Programmierkonzepte zu erlernen, eigene Lösungen zu entwickeln und die erarbeiteten Programme strukturiert in einem öffentlichen Repository zu präsentieren.

> ✨ *Von den ersten "Hello World"-Programmen bis zu datengetriebenen Mini-Anwendungen – dieses Repo begleitet den gesamten Lernweg.*

---

## ✨ Features

- 📝 Sauber strukturierter Python-Code  
- 📦 Modulares Projekt-Setup mit Packages & Modulen  
- ⚡ Interaktive Konsolenanwendungen  
- 📊 Datenauswertung mit Pandas & Matplotlib (späterer Teil)  
- 🧪 Unit-Tests für mehr Code-Qualität  
- 🌐 Optional: kleine Web-Komponenten mit Flask (für Fortgeschrittene)

---

## 🧰 Technologien

| Technologie       | Version  | Verwendung                           |
|-------------------|----------|---------------------------------------|
| Python            | 3.11+    | Hauptprogrammiersprache              |
| pip / venv        | –        | Paketverwaltung & virtuelle Umgebung |
| Git & GitHub      | –        | Versionskontrolle & Hosting          |
| (optional) Flask  | 2.x      | Webserver für Projekte               |
| (optional) Pandas | 2.x      | Datenanalyse                         |

---

## 🛠 Installation

```bash
# Repository klonen
git clone https://github.com/dein-benutzername/dein-repo.git
cd dein-repo

# Virtuelle Umgebung erstellen
python -m venv venv

# Aktivieren (Windows)
venv\Scripts\activate

# Aktivieren (macOS / Linux)
source venv/bin/activate

# Abhängigkeiten installieren
pip install -r requirements.txt
```

---

## 🚀 Verwendung

Nach der Installation kannst du das Hauptprogramm starten:

```bash
python main.py
```

Je nach Übungsabschnitt findest du verschiedene Teilprogramme im `src/` Verzeichnis.  
Jede Übung ist nummeriert und dokumentiert, z.B.:

```bash
python src/uebung_03_rekursion.py
```

---

## 🧭 Projektstruktur

```plaintext
📦 python-kurs
├─ 📁 src
│  ├─ uebung_01_grundlagen.py
│  ├─ uebung_02_schleifen.py
│  ├─ uebung_03_rekursion.py
│  └─ ...
├─ 📁 tests
│  ├─ test_uebung_01.py
│  └─ ...
├─ requirements.txt
├─ main.py
├─ README.md
└─ LICENSE
```

---

## 💡 Beispielcode

```python
def factorial(n: int) -> int:
    """
    Berechnet die Fakultät einer Zahl rekursiv.
    Beispiel: 5! = 5 × 4 × 3 × 2 × 1
    """
    if n <= 1:
        return 1
    return n * factorial(n - 1)


if __name__ == "__main__":
    zahl = int(input("Gib eine Zahl ein: "))
    print(f"Die Fakultät von {zahl} ist {factorial(zahl)}")
```

---

## 🖼 Screenshots

<p align="center">
  <img src="https://via.placeholder.com/800x400.png?text=Beispiel+Screenshot" alt="Screenshot" width="80%"/>
</p>

---

## 🗓 Roadmap

* [x] Grundlagen Python
* [x] Kontrollstrukturen & Funktionen
* [x] Datenstrukturen & Fehlerbehandlung
* [ ] Objektorientierung
* [ ] Datenanalyse mit Pandas
* [ ] Mini-Projekt: Anwendung entwickeln
* [ ] Web-Interface mit Flask (Bonus)

---

## 🤝 Mitwirken

Pull Requests sind willkommen!  
Für größere Änderungen eröffne bitte zuerst ein Issue, um die geplante Änderung zu besprechen.

1. Forke das Projekt  
2. Erstelle einen neuen Branch (`git checkout -b feature/neues-feature`)  
3. Committe deine Änderungen (`git commit -m 'Add neues Feature'`)  
4. Push auf den Branch (`git push origin feature/neues-feature`)  
5. Öffne einen Pull Request

---

## 📄 Lizenz

Dieses Projekt steht unter der **MIT-Lizenz** – siehe [LICENSE](LICENSE) Datei für Details.

---

## 📬 Kontakt

📧 **Dein Name** – [deine.email@hochschule.de](mailto:deine.email@hochschule.de)  
🌐 GitHub: [@dein-benutzername](https://github.com/dein-benutzername)

<p align="center">
  <sub>© 2025 – Hochschule & Dein Name. Alle Rechte vorbehalten.</sub>
</p>
