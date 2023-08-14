import reflex as rx


def sponsor():
    return rx.fragment(
        rx.heading("후원사 목록"),
        rx.heading("사파이어"),
        rx.responsive_grid(
            rx.link(rx.image(
                src="https://pyconkr-api-v2-static.s3.amazonaws.com/sponsor/logo/None/lockup_GoogleCloud_FullColor_rgb_2900x512px.png",
                width="500px", margin="auto"), href="https://2023.pycon.kr/sponsor/list/39"),
            rx.link(rx.image(
                src="https://pyconkr-api-v2-static.s3.amazonaws.com/sponsor/logo/59/PSF-Logo-Shapes.jpg",
                width="500px", margin="auto"), href="https://2023.pycon.kr/sponsor/list/59"),
            columns=[1, 2, 3], spacing="4"),

        rx.heading("플래티넘"),
        rx.responsive_grid(
            rx.image(
                src="https://pyconkr-api-v2-static.s3.amazonaws.com/sponsor/logo/None/payhere_logo_basic_1.jpg",
                width="500px", margin="auto"),
            rx.image(
                src="https://pyconkr-api-v2-static.s3.amazonaws.com/sponsor/logo/None/HYU_Logo_Horizontal_Blue_RGB.png",
                width="500px", margin="auto"),
            columns=[1, 2, 3], spacing="4"),
        rx.heading("루비"),
        rx.responsive_grid(
            rx.image(
                src="https://pyconkr-api-v2-static.s3.amazonaws.com/sponsor/logo/None/Lablup_Logo_with_text_vertical_text_with_color_L.png",
                width="500px", margin="auto"),
            rx.image(src="https://pyconkr-api-v2-static.s3.amazonaws.com/sponsor/logo/None/color.png",
                     width="500px",
                     margin="auto"),
            rx.image(
                src="https://pyconkr-api-v2-static.s3.amazonaws.com/sponsor/logo/None/%ED%81%AC%EB%A6%BC_%EB%A1%9C%EA%B3%A0.PNG",
                width="500px", margin="auto"),
            rx.image(
                src="https://pyconkr-api-v2-static.s3.amazonaws.com/sponsor/logo/56/combi-logo_H_bg_W.png",
                width="500px", margin="auto"),
            rx.image(
                src="https://pyconkr-api-v2-static.s3.amazonaws.com/sponsor/logo/None/Taipy-logo-square.png",
                width="500px", margin="auto"),
            rx.image(
                src="https://pyconkr-api-v2-static.s3.amazonaws.com/sponsor/logo/None/MEGAZONECLOUD_NEW_CI_B.png",
                width="500px", margin="auto"),
            columns=[1, 2, 3, 4, 5, 6], spacing="4"),
        rx.heading("골드"),
        rx.heading("실버"),
        rx.heading("출판사"),
        rx.heading("기술 후원"),
        rx.heading("장소 후원"), )
