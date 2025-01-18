from __future__ import annotations
from datetime import date


class Tweet:
    """
    A tweet, like in Twitter.

    === Attributes ===
    userid: the id of the user who wrote the tweet.
    created_at: the date the tweet was written.
    content: the contents of the tweet.
    likes: the number of likes this tweet has received.

    """
    userid: str
    created_at: date
    content: str
    likes: int

    def __init__(self, who: str, when: date, what: str) -> None:
        """Initialize a new Tweet.
        """
        self.userid = who
        self.created_at = when
        self.content = what
        self.likes = 0

    def like(self, tweet: Tweet, n: int):
        """Record the fact that <tweet> received <n> likes.

        Precondition: n >= 0

        >>> t = Tweet('Rukhsana', date(2022, 1, 16), 'Hey!')
        >>> like(t, 3)
        >>> t.likes
        3
        """
        tweet.likes += n






