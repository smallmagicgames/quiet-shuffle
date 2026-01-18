import asyncio
from quiet_shuffle.deck_data.deck import create_deck, draw_card, shuffle_deck


async def quiet_shuffle() -> None:
    deck = shuffle_deck(create_deck())
    card = draw_card(deck)
    print(str(card))


if __name__ == "__main__":
    asyncio.run(quiet_shuffle())