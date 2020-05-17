import wolframalpha
client = wolframalpha.Client("G4H2VA-496G3827Y9")
res = client.query('temperature in Washington, DC on October 3, 2012')

print(next(res.results).text)
