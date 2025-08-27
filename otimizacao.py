import re
import unicodedata

def preprocess(text):
    # remove tags HTML
    text = re.sub(r'<[^>]+>', '', text)

    # remove URLs
    text = re.sub(r'http\S+|www\.\S+', '', text)

    # removi emojis e caracteres especiais
    text = ''.join(c for c in text if unicodedata.category(c)[0] != 'So')

    # reduz repetição de letras (3 ou mais)
    text = re.sub(r'(.)\1{2,}', r'\1', text)

    # reduz repetições de pontuação
    text = re.sub(r'([!?.,])\1+', r'\1', text)

    # remove rizadas e interjeições comuns 
    text = re.sub(r'\b(rs|haha|hihihi|kkk)+\b', '', text, flags=re.IGNORECASE)

    # remove tokens não alfabéticos com muitos caracteres
    text = re.sub(r'\b[^ ]*[^a-zA-Z0-9\s][^ ]*\b', '', text)

    # remove espaços extras
    text = re.sub(r'\s+', ' ', text).strip()

    return text

exemplo = """
<div>COMPRE AGORA!!! www.site-fake.com</div>
Éééééé tipo assimmmm, sabe???? rsrs
x9fj9348sdkfj934...
"""

print(preprocess(exemplo))