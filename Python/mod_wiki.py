import wikipedia

wikipedia.set_lang('de')
ws = str(wikipedia.search("Indien", results=1))
print(ws)

x = wikipedia.summary(ws, sentences=2)
print(x)
