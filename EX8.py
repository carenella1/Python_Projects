# Declaring the formatter variable to setup up printing of whichever parameter we assign
formatter = "%s %s %s %s"

# Replaces %r with the ints
print formatter % (1, 2, 3, 4)
# Replaces %r with 4 strings
print formatter % ("one", "two", "three", "four")
# Replaces %r with 4 boolean values
print formatter % (True, False, False, True)
# Incepta-Formatter (4 formatters within the formatter)
print formatter % (formatter, formatter, formatter, formatter)
# Replaces %r with 4 strings
print formatter %(
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing." ,
    "So I said goodnight."
)
