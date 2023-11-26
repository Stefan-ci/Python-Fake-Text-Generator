# Python Fake Text Generator Package

## Summary
Random text generator that looks like Latin/English (given the language).

## Installation

### With pip

```bash
pip install fake_text
```

### Manualy

```bash
python setup.py install
```

## Usage

### Basic

```python
import fake_text

sent = fake_text.sentence() # Alias unde quo asperiores quiseaque.
par = fake_text.paragraph() # Delectus sit aliquam quaerat delectus …
tex = fake_text.text() # Distinctio delectus sit quiseaque vero dolorum nobis fugit …
```


### Advanced

```python
from fake_text import TextGenerator

generator = TextGenerator(
    lang="lat", # Latin or "en" for English
    words="Distinctio delectus sit quiseaque vero dolorum nobis fugit", # Words or a given sentence
    wsep=" ", # Space (for words separator)
    ssep=".", # Sentences separator
    psep="\n", # Paragraphs separator
    ...
)

sentence = generator.sentence()
paragraph = generator.paragraph()
text = generator.text()
```
