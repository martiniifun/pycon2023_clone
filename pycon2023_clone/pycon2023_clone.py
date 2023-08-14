import reflex as rx

from pycon2023_clone.sponsor import sponsor


class State(rx.State):
    pass


def index() -> rx.Component:
    return rx.box(
        rx.heading("다시, 우리, 파이썬", size="4xl"),
        rx.heading("2023.08.11 - 13", size="4xl"),
        rx.heading("COEX 그랜드볼룸 & 아셈볼룸", size="4xl"),
        rx.link(rx.button("라이트닝 토크 신청"),
                href="https://docs.google.com/forms/d/e/1FAIpQLScBhqfcisbb5m7fT7IOQDvwd4he1xRvpaJo9gU8teGa_ganFg/closedform"),
        sponsor(),
    )


# Add state and page to the app.
app = rx.App()
app.add_page(index)
app.compile()
