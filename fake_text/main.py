import random

LATIN_WORDS = (
    "molestiae assumendalabore molestias fugit culpa error quo aspernatur nesciunt pariatur"
    "laboriosam suscipitfugiat voluptatesHarum corrupti dolorum unde quaerat natus nobis placeat"
    "animi praesentium veritatis officiis maxime delectus at id non asperiores sit illo ducimus quis"
    "eaque ratione repellat in dolor modi deleniti cumque exercitationem veniam facere cum voluptatem"
    "iste necessitatibus aliquid sequi expedita nam soluta reiciendis maiores eum aliquam atque officia"
    "consectetur adipisci numquam distinctio saepe accusamus vero omnisfacere vero ipsa amet doloresdeserunt"
    "voluptatibus optio dolorequibusdam nam alias voluptate nostrum").split()

ENGLISH_WORDS = ("").split()



class TextGenerator:
    """Generate random text that looks like Latin/English (like the given language).
    """
    
    def __init__(self, lang=None, words=None, wsep=" ", ssep=" ", psep="\n\n", srange=(4, 8), prange=(5, 10), trange=(3, 6)):
        """Initialize the Random Text Generator

        Args:
            lang (str | None): Language code to use [lat, en] or None. Defaults to "lat" (Latin)
            words (Any, optional): Words to be used to generate texts. Defaults to None.
            wsep (str, optional): Words seprator. Defaults to space.
            ssep (str, optional): Sentence seprator. Defaults to space.
            psep (str, optional): Paragraph seprator. Defaults to double new line.
            
            srange (tuple, optional): Range of sentence's length. Defaults to (4, 8).
            prange (tuple, optional): Range of paragraph's length. Defaults to (5, 10).
            trange (tuple, optional): Range of text's length. Defaults to (3, 6).
        """
        self._lang = lang
        self._wsep = wsep
        self._ssep = ssep
        self._psep = psep
        self._srange = srange
        self._prange = prange
        self._trange = trange
        
        if words:
            self._words = str(words).split() # Convert given words to a list of strings
        else:
            self._words = self.get_words()
        
        # if lang:
        #     self._lang = str(lang)
        # else:
        #     self._lang = "lat" # by default
        
    

    def get_words(self) -> list:
        if self._lang and self._lang is not None:
            if self._lang == "en":
                self._words = ENGLISH_WORDS
            else:
                self._words = LATIN_WORDS
        else:
            self._words = LATIN_WORDS
        return self._words
    
    def _word(self):
        return random.choice(self._words)

    def sentence(self, *args, **kwargs):
        n = random.randint(*self._srange)
        s = self._wsep.join(self._word() for i in range(n))
        return s[0].upper() + s[1:] + "."
    
    def paragraph(self, *args, **kwargs):
        n = random.randint(*self._prange)
        p = self._ssep.join(self.sentence() for _ in range(n))
        return p
    
    def text(self, *args, **kwargs):
        n = random.randint(*self._trange)
        t = self._psep.join(self.paragraph() for _ in range(n))
        return t
