class ChatTree:
    """A data type that represents a whole chatbot chat."""
    def __init__(self, level=0):
        # The user's chat response that prompted this tree
        self.prompt_response = None
        self.data = None  # What data this tree node contains
        # A chat response will typically have at least 2 responses
        self.branch1 = ChatTree(level=level+1)
        self.branch2 = ChatTree(level=level+1)
        # Some questions will have 3 responses
        self.branch3 = None


class CardResponses:
    def __init__(self):
        self.cards = []  # A list of Card objects


class Card:
    def __init__(self):
        self.responses = []  # A list of CardResponse objects


class CardResponse:
    def __init__(self):
        self.data = None
