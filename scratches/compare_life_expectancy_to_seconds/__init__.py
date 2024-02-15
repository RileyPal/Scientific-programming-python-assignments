
life_span: float = 76.4
Samplelife_span = (10**9)/(60*60*24*365)
result=life_span/Samplelife_span
print("Can a newborn baby in the United States expect to live for one billion (10**9) seconds?")
if result<=1:print("yes")
else:print("no")