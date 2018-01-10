print("Here are some examples of escape sequences as well as string formats")

backslashes = "\\\\\\\\"

print(f"Four backslashes {backslashes}")

print("Four backslashes using a different formatter: {}".format(backslashes))

line_returns = "This sentence\nis three\nlines long."

print(line_returns)

tabs = "{}\t{}\t{}"


print(tabs.format("Tabs will", "separate", "these words."))

carriage_return = "\r"
vertical_tab = "\v"
form_feed = "\f"
backspace = "\b"

print("""Here's a carriage return {}
    A vertical tab {}
    A form feed {}
    And a backspace {}
    """.format(carriage_return, vertical_tab, form_feed, backspace))
