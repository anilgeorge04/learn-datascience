# Try Catch
def echo(word, echo=1):
    try:
        echo_word = word * echo
        return echo_word
    except:
        print("word must be a string and echo must be an int")

# Raise error
def echo2(word, echo=1):
    if echo < 0:
        raise ValueError("echo value must be greater than 0")
    echo_word = word * echo
    return echo_word

echo("hey", "looo") # second argument causes except to be trigerred
echo2("hey", -2) # second argument causes raise error to be trigerred
