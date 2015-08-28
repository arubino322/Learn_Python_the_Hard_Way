formatter = "%r %r %r %r"

print formatter % (1,2,3,4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (
	"I had this thing.",
	"That you could type up right.",
	"But it didn't sing.",
	"So I said goodnight."
)

#remember: %r will give you the raw programmer's version
#of variable, also know as the representation
#otherwise, fi you aren't debugging, stick with %s, %d, etc