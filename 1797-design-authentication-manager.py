class AuthenticationManager:

    def __init__(self, timeToLive: int):
        # construct AuthenticationManager
        # sets the timeToLive
        self.tokens = {}
        self.ttl = timeToLive


    def generate(self, tokenId: str, currentTime: int) -> None:
        # generate new token with the given tokenId at currentTime
        self.tokens[tokenId] = currentTime + self.ttl

    def renew(self, tokenId: str, currentTime: int) -> None:
        # renews the unexpired token
        # if no unexpired tokens, ignore
        if tokenId in self.tokens and self.tokens[tokenId] > currentTime:
            self.tokens[tokenId] = currentTime + self.ttl

    def countUnexpiredTokens(self, currentTime: int) -> int:
        count = 0
        for dieTime in self.tokens.values():
            if dieTime > currentTime:
                count += 1
        return count

# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)