# 🐍 Python Text Analyzer  
**Projekt 1 – Engeto Online Python Akademie**

**Autor:** Barbora Rašticová  
**Email:** rasticova.barbora@seznam.cz  
**Soubor:** `text_analyzer.py`  

---

## 🧠 Cíl projektu
Cílem projektu je vytvořit jednoduchý **textový analyzátor**, který se dokáže „prokousat“ libovolně dlouhým textem a zjistit o něm různé informace – například počet slov, typy slov nebo součet čísel.

Program umožňuje přihlášení uživatele, výběr textu a následnou analýzu vybraného textu.  
Je navržen tak, aby fungoval s libovolným počtem textů.

---

## ⚙️ Funkcionalita programu

### 1️⃣ Přihlášení uživatele
- Program si vyžádá **uživatelské jméno a heslo**.  
- Ověří správnost dvojice `jméno – heslo`.  
- Pokud uživatel není registrován, program se ukončí.

**Registrovaní uživatelé:**
| user | password     |
|------|---------------|
| bob  | 123           |
| ann  | pass123       |
| mike | password123   |
| liz  | pass123       |

---

### 2️⃣ Výběr textu
- Po úspěšném přihlášení se uživateli zobrazí počet dostupných textů.  
- Uživatel zadá číslo textu, který chce analyzovat.  

---

### 3️⃣ Textová analýza
Program analyzuje vybraný text a zjistí následující informace:

- Počet všech slov  
- Počet slov začínajících velkým písmenem  
- Počet slov psaných VELKÝMI písmeny  
- Počet slov psaných malými písmeny  
- Počet číselných řetězců  
- Součet všech čísel v textu  

---

### 4️⃣ Zobrazení výsledků
Program zobrazí přehled všech získaných informací a jednoduchý **sloupcový graf** s četností délky slov.

## 🖥️ Ukázka výstupu
Níže je ukázka výstupu v terminálu po přihlášení uživatele `bob` a analýze textu č. 1:

> 💡 *Poznámka:* Po zadání čísla textu (1–3) se v programu zobrazí samotný obsah vybraného textu.  
> V této ukázce je text vynechán kvůli přehlednosti výstupu.

```bash
username: bob
password: 123
----------------------------------------
Welcome to the app, bob
We have 3 texts to be analysed:
----------------------------------------
Enter a number btw 1 and 3 to select: 1
----------------------------------------
There are 54 words in the selected text.
There are 12 titlecase words.
There is 1 uppercase word.
There are 38 lowercase words.
There are 3 numeric strings.
The sum of all the numbers is 8510.
----------------------------------------
LEN|    OCCURENCES    |NR.
----------------------------------------
  1|*                 |1
  2|*********         |9
  3|******            |6
  4|***********       |11
  5|************      |12
  6|***               |3
  7|****              |4
  8|*****             |5
  9|*                 |1
 10|*                 |1
 11|*                 |1
```
## 🧩 Použité principy a metody
- podmínky (`if`, `elif`, `else`)  
- cykly `for`  
- práce se seznamy a slovníky  
- metody pro práci s textem:  
  `split()`, `strip()`, `istitle()`, `isupper()`, `islower()`, `isdigit()`  
- výpočet četností a formátovaný výstup (`rjust`)  

---

## ▶️ Jak program spustit

1. Stáhni soubor `text_analyzer.py`  
2. Spusť program v terminálu nebo v IDE (např. VS Code):  
   ```bash
   python text_analyzer.py