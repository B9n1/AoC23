### part 1
class Round:
    def __init__(self, green: int = 0, red: int = 0, blue: int = 0):
        self.green: int = green
        self.red: int = red
        self.blue: int = blue
class Game:
    def __init__(self, id: int, rounds: list[Round]):
        self.id: int = id
        self.rounds: list[Round] = rounds
        
def readDocument(input_document):
    inputArray = []
    with open(input_document, 'r') as file:
        for line in file:
            line = line.strip('\n')
            inputArray.append(line)
    return inputArray

def gameStrToGameobj(roundStr: str) -> Game:
    splitStr = roundStr.split(":")
    gameId = splitStr[0].split(" ")[1]
    roundsStr = splitStr[1].split(";")
    rounds: list[Round]= []
    for roundStr in roundsStr:
        roundStr = roundStr[1:]
        splitedColors = roundStr.split(",")
        green:int = 0
        red:int = 0
        blue:int = 0
        for color in splitedColors:
            splitedColor = color.split(" ")
            splitedColor = list(filter(None, splitedColor))
            number: int = int(splitedColor[0])
            match splitedColor[1]:
                case 'blue':
                    blue = number
                case 'red':
                    red = number
                case 'green':
                    green = number
        rounds.append(Round(green, red, blue))
    return Game(gameId, rounds)

def gameStringsToGames(gameStrings: list[str])-> list[Game]:
    games: list[Game] = []
    for gameString in gameStrings:
        games.append(gameStrToGameobj(gameString))
    return games

def returnIdIfGameIsPossible(game: Game) -> int:
    rValue: int = 0
    isGamePossible: bool = True
    for round in game.rounds:
        if int(round.green) > 13 or int(round.blue) > 14 or int(round.red) > 12:
            isGamePossible = False
    if isGamePossible:
        rValue = game.id
    return int(rValue)

gamesStrings = readDocument('02_input.txt')
games = gameStringsToGames(gamesStrings)
sum = 0
for game in games:
    sum += returnIdIfGameIsPossible(game)
print("Part 1: " + str(sum))

### part 2
def GetMinCubesReturnPower(game: Game) ->int:
    red:int = 1
    green:int = 1
    blue:int = 1
    for round in game.rounds:
        if round.green > green:
            green = round.green
        if round.red > red:
            red = round.red
        if round.blue > blue:
            blue = round.blue
    return red * green * blue
sum2:int = 0
for game in games:
    sum2+= GetMinCubesReturnPower(game)
print("Part 2: " + str(sum2))