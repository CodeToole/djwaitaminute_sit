import sys
import os
import reflex as rx

# Fix for IDE/Linter: Add project root to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from rxconfig import config


class State(rx.State):
    """The app state."""
    pass


def nav_link(text: str, url: str) -> rx.Component:
    return rx.link(
        text,
        href=url,
        color="#94A3B8",  # slate-400
        font_family="Orbitron",
        font_size="0.875rem",
        font_weight="500",
        text_transform="uppercase",
        letter_spacing="0.1em",
        _hover={"color": "#00F0FF", "text_shadow": "0 0 10px #00F0FF"},
        transition="all 0.3s",
    )

def navbar() -> rx.Component:
    return rx.box(
        rx.flex(
            # Logo Section
            rx.hstack(
                rx.box(
                    rx.image(
                        src="/mascot.png",
                        width="2.5rem",
                        height="2.5rem",
                        transition="all 0.3s",
                    ),
                    position="relative",
                    _hover={"filter": "drop-shadow(0 0 10px #00F0FF)"},
                ),
                rx.text(
                    "DJ",
                    rx.text.span("WAITAMINUTE", color="#00F0FF"),
                    font_family="Orbitron",
                    font_weight="700",
                    font_size="1.25rem",
                    letter_spacing="0.1em",
                    color="white",
                    _hover={"text_shadow": "0 0 10px #00F0FF"},
                    transition="all 0.3s",
                ),
                spacing="3",
                align="center",
                cursor="pointer",
                on_click=rx.redirect("/"),
            ),
            
            # Navigation Links & Subscribe Button
            rx.flex(
                nav_link("Music", "/music"),
                nav_link("Tour", "/tour"),
                nav_link("Merch", "/"),
                nav_link("About", "/#about"),
                rx.link(
                    rx.button(
                        "Subscribe",
                        variant="outline",
                        font_family="Orbitron",
                        font_size=["0.75rem", "0.875rem"],
                        font_weight="700",
                        text_transform="uppercase",
                        letter_spacing="0.1em",
                        color="white",
                        border_color="white",
                        _hover={
                            "bg": "#00F0FF",
                            "color": "black",
                            "border_color": "#00F0FF",
                            "box_shadow": "0 0 15px rgba(0, 240, 255, 0.5)",
                        },
                        transition="all 0.3s",
                        padding_x=["4", "6"],
                        border_radius="0",
                    ),
                    href="https://www.youtube.com/@djwaitaminute84",
                    is_external=True,
                ),
                gap=["3", "4", "8"],
                align="center",
                justify="center",
                flex_wrap="wrap",
                margin_top=["4", "4", "0"],
            ),
            
            justify="between",
            align="center",
            flex_direction=["column", "column", "row"],
            max_width="80rem",
            margin_x="auto",
            padding_x="4",
            padding_y="4",
            min_height="5rem",
            width="100%",
        ),
        
        width="100%",
        position="fixed",
        top="0",
        z_index="50",
        backdrop_filter="blur(12px)",
        bg="rgba(5, 5, 8, 0.8)",
        border_bottom="1px solid rgba(255, 255, 255, 0.1)",
    )

def social_icon(label: str, url: str) -> rx.Component:
    return rx.link(
        rx.text(
            label,
            color="#00F0FF",
            font_family="Orbitron",
            font_size="1.25rem",
            font_weight="700",
            _hover={"filter": "drop-shadow(0 0 8px #00F0FF)", "color": "white"},
            transition="all 0.3s",
        ),
        href=url,
        is_external=True,
    )

def footer() -> rx.Component:
    return rx.box(
        rx.box(
            width="100%",
            height="1px",
            bg="linear-gradient(to right, transparent, #334155, transparent)",
            margin_y="8",
        ),
        rx.vstack(
            rx.hstack(
                social_icon("IG", "https://instagram.com/djwaitaminute"),
                social_icon("YT", "https://www.youtube.com/@djwaitaminute84"),
                social_icon("MC", "https://mixcloud.com/djwaitaminute"),
                social_icon("SC", "https://soundcloud.com/djwaitaminute"),
                social_icon("FB", "https://facebook.com/djwaitaminute"),
                social_icon("X", "https://x.com/djwaitaminute"),
                spacing="6",
                justify="center",
                flex_wrap="wrap",
            ),
            rx.text(
                "© 2026 DJWAITAMINUTE | MOBILE, AL",
                font_family="Orbitron",
                color="#94A3B8",
                font_size="0.875rem",
                margin_top="4",
                letter_spacing="0.1em",
            ),
            align="center",
            width="100%",
            padding_bottom="8",
        ),
        width="100%",
    )


def about_section() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.heading(
                "THE OPERATOR",
                font_family="Orbitron",
                font_size=["2rem", "2.5rem"],
                font_weight="900",
                text_transform="uppercase",
                letter_spacing="0.1em",
                color="white",
                margin_bottom="6",
                border_left="4px solid #00F0FF",
                padding_left="4",
            ),
            rx.text(
                "Cornelius (DJWaitaminute)",
                font_size="1.25rem",
                font_weight="700",
                color="#00F0FF",
                margin_bottom="2",
            ),
            rx.text(
                "Drum and Bass producer and DJ based in Mobile, AL.",
                color="#94A3B8",
                margin_bottom="4",
            ),
            rx.text(
                "Host of the 'Terminal Code' show on in2GrooveRadio (Tuesdays 5-7 PM / Wednesdays 6-8 PM CST).",
                color="#94A3B8",
                margin_bottom="4",
            ),
            rx.box(
                rx.text("credentials //", font_family="monospace", color="#00F0FF", font_size="0.875rem", margin_bottom="2"),
                rx.text(
                    "Certified in Google Digital Marketing & E-commerce",
                    color="white", font_size="0.875rem"
                ),
                rx.text(
                    "Certified in Google Prompting Essentials",
                    color="white", font_size="0.875rem"
                ),
                bg="#050508",
                padding="4",
                border_radius="sm",
                border="1px solid #1E293B",
                width="100%",
                margin_top="4",
            ),
            align="start",
            width="100%",
            max_width="48rem",
            bg="#121212",
            padding="8",
            border_radius="sm",
            border="1px solid #1E293B",
            box_shadow="0 0 20px rgba(0, 240, 255, 0.15)",
        ),
        id="about",
        width="100%",
        display="flex",
        justify_content="center",
        padding_y="8rem",
        padding_x="4",
        bg="#050508",
    )


def tag(text: str) -> rx.Component:
    return rx.text(
        text,
        font_weight="700",
        letter_spacing="0.1em",
        text_transform="uppercase",
        color="#94A3B8",  # slate-400
        font_size=["0.75rem", "1.125rem"],
    )


def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.box(
        # Navigation
        navbar(),
        # Hero Section
        rx.box(
            # Background Layers
            rx.box(
                rx.image(
                    src="https://lh3.googleusercontent.com/aida-public/AB6AXuCubVLKzS4hOD-NLSHtjSZYT7lwx3CuES_--OA7XLE5mCuzV3nnlZlGr-IEJVV0SpEtpg_zZvjFU8yIS9zIdeot_3X9t6gMMZzqdLjHIIbPzV-c2B-AGIQ5HC5zJQWD1W977enchukcm6zoIphgU-9Hc_I6iRSoNiNHDIc0cGRCeobC-b76_dfON--4SbVrs-7yWnqX9oJrdZh2ENfV5B3ZCfhigJQe3wQVKuJBS8yo7z4igs9LjDpG6Q41I1eV8THMmJjFCPYBtw",
                    width="100%",
                    height="100%",
                    object_fit="cover",
                    opacity="0.4",
                    filter="grayscale(100%) contrast(125%) brightness(50%)",
                ),
                rx.box(
                    width="100%",
                    height="100%",
                    position="absolute",
                    top="0",
                    class_name="bg-noise",
                    opacity="0.3",
                    mix_blend_mode="overlay",
                ),
                rx.box(
                    width="100%",
                    height="100%",
                    position="absolute",
                    top="0",
                    class_name="bg-gradient-overlay",
                ),
                # Scanlines
                rx.box(
                    width="100%",
                    height="1px",
                    bg="linear-gradient(to right, transparent, rgba(0, 240, 255, 0.3), transparent)",
                    position="absolute",
                    top="25%",
                ),
                rx.box(
                    width="100%",
                    height="1px",
                    bg="linear-gradient(to right, transparent, rgba(0, 240, 255, 0.3), transparent)",
                    position="absolute",
                    bottom="25%",
                ),
                width="100%",
                height="100%",
                position="absolute",
                top="0",
                z_index="0",
            ),
            # Decorative Animated Shapes
            rx.box(
                rx.box(
                    width="16rem",
                    height="16rem",
                    border="1px solid rgba(255, 255, 255, 0.05)",
                    border_radius="full",
                    position="absolute",
                    top="20%",
                    right="10%",
                    class_name="animate-pulse-slow",
                ),
                rx.box(
                    width="24rem",
                    height="24rem",
                    border="1px solid rgba(0, 240, 255, 0.1)",
                    border_radius="full",
                    position="absolute",
                    bottom="10%",
                    left="5%",
                    class_name="animate-pulse-slow",
                ),
                width="100%",
                height="100%",
                position="absolute",
                top="0",
                z_index="0",
                overflow="hidden",
                pointer_events="none",
            ),
            # Main Content
            rx.vstack(
                # Signal Indicator
                rx.hstack(
                    rx.box(
                        rx.box(
                            width="100%",
                            height="100%",
                            bg="#00F0FF",
                            border_radius="full",
                            opacity="0.75",
                            animation="ping 1s cubic-bezier(0, 0, 0.2, 1) infinite",
                            position="absolute",
                        ),
                        rx.box(
                            width="0.75rem",
                            height="0.75rem",
                            bg="#00F0FF",
                            border_radius="full",
                            position="relative",
                        ),
                        width="0.75rem",
                        height="0.75rem",
                        position="relative",
                        display="flex",
                        align_items="center",
                        justify_content="center",
                    ),
                    rx.text(
                        "Signal Locked: Transmission Live",
                        font_family="Orbitron",
                        font_size=["0.75rem", "0.875rem"],
                        letter_spacing="0.3em",
                        text_transform="uppercase",
                        color="#00F0FF",
                        font_weight="700",
                    ),
                    spacing="2",
                    align="center",
                    margin_bottom="6",
                ),
                # Central Mascot (Visual Anchor)
                rx.center(
                    rx.box(
                        rx.image(
                            src="/mascot.png",
                            width=["12rem", "16rem", "20rem"],
                            height="auto",
                            transition="all 0.5s",
                            filter="drop-shadow(0 0 20px rgba(0, 240, 255, 0.3))",
                        ),
                        _hover={"transform": "scale(1.05)", "filter": "drop-shadow(0 0 30px rgba(0, 240, 255, 0.5))"},
                        transition="all 0.5s",
                        class_name="animate-glitch",
                    ),
                    width="100%",
                    margin_bottom="4",
                ),
                # Heading
                rx.heading(
                    "TRANSMISSION",
                    font_family="Orbitron",
                    font_weight="900",
                    font_size=["3rem", "4.5rem", "6rem", "8rem"],
                    letter_spacing="-0.05em",
                    line_height="1",
                    color="white",
                    background_image="linear-gradient(to bottom, white, #64748B)",
                    background_clip="text",
                    text_fill_color="transparent",
                    margin_bottom="2",
                ),
                # Tags
                rx.hstack(
                    tag("Drum & Bass"),
                    rx.box(width="0.25rem", height="0.25rem", bg="#00F0FF", border_radius="full", display=["none", "block"]),
                    tag("Jungle"),
                    rx.box(width="0.25rem", height="0.25rem", bg="#00F0FF", border_radius="full", display=["none", "block"]),
                    tag("Liquid"),
                    rx.box(width="0.25rem", height="0.25rem", bg="#00F0FF", border_radius="full", display=["none", "block"]),
                    tag("Neurofunk"),
                    spacing="6",
                    align="center",
                    margin_bottom="12",
                    flex_wrap="wrap",
                    justify="center",
                ),
                # Action Buttons
                rx.hstack(
                    rx.link(
                        rx.button(
                            rx.hstack(
                                rx.text("Book DJWaitaminute"),
                                rx.text("arrow_forward", class_name="material-symbols-outlined", font_size="1.25rem"),
                                spacing="2",
                                align="center",
                            ),
                            bg="#00F0FF",
                            color="black",
                            font_family="Orbitron",
                            font_weight="700",
                            font_size="1.125rem",
                            text_transform="uppercase",
                            letter_spacing="0.1em",
                            padding_x="8",
                            padding_y="7",
                            border_radius="0",
                            _hover={
                                "bg": "white",
                                "box_shadow": "0 0 30px rgba(255, 255, 255, 0.6)",
                            },
                            transition="all 0.3s",
                            box_shadow="0 0 20px rgba(0, 240, 255, 0.4)",
                        ),
                        href="mailto:cornelius@djwaitaminute.com",
                        is_external=True,
                    ),
                    rx.link(
                        rx.hstack(
                            rx.text("play_circle", class_name="material-symbols-outlined", font_size="1.5rem"),
                            rx.text("Latest Mix"),
                            spacing="3",
                            align="center",
                        ),
                        href="#latest-mix",
                        padding_x="8",
                        padding_y="4",
                        border="1px solid rgba(255, 255, 255, 0.2)",
                        color="white",
                        font_family="Orbitron",
                        font_weight="700",
                        font_size="1.125rem",
                        text_transform="uppercase",
                        letter_spacing="0.1em",
                        backdrop_filter="blur(4px)",
                        bg="rgba(255, 255, 255, 0.05)",
                        _hover={"border_color": "#00F0FF", "color": "#00F0FF"},
                        transition="all 0.3s",
                    ),
                    spacing="6",
                    flex_direction=["column", "row"],
                ),
                width="100%",
                padding_x="4",
                text_align="center",
                margin_top="16",
                position="relative",
                z_index="10",
            ),
            # Vertical Sidebars
            rx.box(
                rx.box(
                    width="1px",
                    height="16rem",
                    bg="linear-gradient(to bottom, transparent, rgba(255, 255, 255, 0.2), transparent)",
                ),
                rx.text(
                    "SYS.402 // FREQUENCY.MOD",
                    font_family="monospace",
                    font_size="10px",
                    color="rgba(255, 255, 255, 0.3)",
                    class_name="vertical-text-rl",
                    transform="translateX(-1rem) rotate(180deg)",
                ),
                position="absolute",
                left="2rem",
                top="50%",
                transform="translateY(-50%)",
                display=["none", "none", "none", "flex"],
                align_items="center",
                justify_content="center",
                z_index="20",
            ),
            rx.box(
                rx.box(
                    width="1px",
                    height="16rem",
                    bg="linear-gradient(to bottom, transparent, rgba(255, 255, 255, 0.2), transparent)",
                ),
                rx.text(
                    "BPM: 174 // STATUS: ACTIVE",
                    font_family="monospace",
                    font_size="10px",
                    color="rgba(255, 255, 255, 0.3)",
                    class_name="vertical-text-rl",
                    transform="translateX(1rem)",
                ),
                position="absolute",
                right="2rem",
                top="50%",
                transform="translateY(-50%)",
                display=["none", "none", "none", "flex"],
                align_items="center",
                justify_content="center",
                z_index="20",
            ),
            # Scroll indicator
            rx.vstack(
                rx.text("Scroll to Initiate", font_size="10px", text_transform="uppercase", letter_spacing="0.2em", color="#64748B"),
                rx.text("keyboard_double_arrow_down", class_name="material-symbols-outlined animate-bounce", color="#00F0FF"),
                position="absolute",
                bottom="2.5rem",
                width="100%",
                align="center",
                opacity="0.7",
                display=["none", "flex"],
            ),
            width="100%",
            min_height="100vh",
            position="relative",
            display="flex",
            align_items="center",
            justify_content="center",
            overflow="hidden",
            background="#050508",
        ),
        # About Section
        about_section(),
        # Footer
        footer(),
        width="100%",
        min_height="100vh",
        background="#050508",
        color="white",
        font_family="Montserrat",
        display="flex",
        flex_direction="column",
    )


def tour() -> rx.Component:
    # Tour & Bookings Page
    return rx.box(
        # Navigation
        navbar(),

        # Header / Hero Section
        rx.box(
            rx.box(
                rx.image(
                    src="https://lh3.googleusercontent.com/aida-public/AB6AXuCkZNZ0dvbLt33p97nFPEatNsm2RJUPVj1FpU03V-WgquJOvZmQpqxFqDUzJyGWb18eFiC-ceZHXaGseSqaiFUAua_yCEq5rcHpklxKEBeE77ic7M7WOsjsBlO8mDWSqMSHqWxS53GPSukfMlXiwdKi8um81Jn2jaN3yOu1V2EQUq3uINNst9tM2ceb-vfU9GxD3_lyByDIV_piGB8tqwTyCHHQKlSzgXbVY9cWE80jq28MZ9UpyU-ACXIjtIKwG7DcTxwExbnRjQ",
                    width="100%",
                    height="100%",
                    object_fit="cover",
                    opacity="0.3",
                    mix_blend_mode="overlay",
                ),
                rx.box(
                    width="100%",
                    height="100%",
                    position="absolute",
                    top="0",
                    bg="linear-gradient(to bottom, rgba(5,5,8,0.5), #050508, #050508)",
                ),
                width="100%",
                height="100%",
                position="absolute",
                top="0",
                z_index="0",
            ),
            rx.vstack(
                rx.heading(
                    "LIVE AVAILABILITY",
                    font_family="Orbitron",
                    font_size=["3rem", "4.5rem", "5rem"],
                    font_weight="900",
                    letter_spacing="-0.05em",
                    text_transform="uppercase",
                    bg_clip="text",
                    color="transparent",
                    background_image="linear-gradient(to right, #94A3B8, #E2E8F0, #94A3B8)",
                    class_name="glitch-effect",
                    margin_bottom="4",
                ),
                rx.text(
                    "2024 / 2025 Global Tour & Residency Schedule",
                    font_size="1.25rem",
                    color="#94A3B8",
                    font_weight="300",
                    letter_spacing="0.1em",
                    text_transform="uppercase",
                ),
                rx.box(
                    height="0.25rem",
                    width="6rem",
                    bg="#00F0FF",
                    border_radius="full",
                    box_shadow="0 0 10px rgba(0,240,255,0.7)",
                    margin_top="8",
                ),
                position="relative",
                z_index="10",
                max_width="80rem",
                margin_x="auto",
                padding_x="4",
                align="center",
                text_align="center",
            ),
            position="relative",
            padding_top=["8rem", "12rem"],
            padding_bottom=["4rem", "6rem"],
            overflow="hidden",
        ),

        # Main Content Grid
        rx.box(
            rx.grid(
                # Column 1: Upcoming Shows
                rx.box(
                    rx.heading(
                        "Upcoming Shows",
                        font_family="Orbitron",
                        font_size="1.5rem",
                        font_weight="700",
                        color="white",
                        text_transform="uppercase",
                        letter_spacing="0.05em",
                        border_left="4px solid #00F0FF",
                        padding_left="4",
                        margin_bottom="8",
                    ),
                    rx.vstack(
                        # Show 1
                        rx.box(
                            rx.flex(
                                rx.box(
                                    rx.text("Oct 14, 2024", font_size="0.875rem", font_weight="700", color="#00F0FF", letter_spacing="0.1em", text_transform="uppercase", margin_bottom="1"),
                                    rx.heading("Fabric London", font_family="Orbitron", font_size="1.25rem", font_weight="700", color="white", text_transform="uppercase", _hover={"color": "#00F0FF"}, transition="colors 0.3s"),
                                    rx.text("London, United Kingdom", color="#94A3B8", font_weight="300"),
                                    flex="1",
                                ),
                                rx.button(
                                    "Tickets",
                                    variant="outline",
                                    border_color="white",
                                    color="white",
                                    font_family="Orbitron",
                                    font_weight="700",
                                    font_size="0.875rem",
                                    text_transform="uppercase",
                                    letter_spacing="0.1em",
                                    _hover={"bg": "#00F0FF", "border_color": "#00F0FF", "color": "black", "box_shadow": "0 0 15px rgba(0,240,255,0.5)"},
                                    transition="all 0.3s",
                                    padding_x="8",
                                    padding_y="6",
                                    width=["100%", "auto"],
                                ),
                                flex_direction=["column", "row"],
                                align_items=["flex-start", "center"],
                                justify_content="space-between",
                                gap="4",
                            ),
                            border_bottom="1px solid #1E293B",
                            padding_y="6",
                            padding_x="4",
                            margin_x="-4",
                            border_radius="lg",
                            _hover={"bg": "#0F172A"},
                            transition="colors 0.3s",
                            width="100%",
                        ),
                        # Show 2
                        rx.box(
                            rx.flex(
                                rx.box(
                                    rx.text("Oct 21, 2024", font_size="0.875rem", font_weight="700", color="#00F0FF", letter_spacing="0.1em", text_transform="uppercase", margin_bottom="1"),
                                    rx.heading("Rampage Open Air", font_family="Orbitron", font_size="1.25rem", font_weight="700", color="white", text_transform="uppercase", _hover={"color": "#00F0FF"}, transition="colors 0.3s"),
                                    rx.text("Lommel, Belgium", color="#94A3B8", font_weight="300"),
                                    flex="1",
                                ),
                                rx.button(
                                    "Tickets",
                                    variant="outline",
                                    border_color="white",
                                    color="white",
                                    font_family="Orbitron",
                                    font_weight="700",
                                    font_size="0.875rem",
                                    text_transform="uppercase",
                                    letter_spacing="0.1em",
                                    _hover={"bg": "#00F0FF", "border_color": "#00F0FF", "color": "black", "box_shadow": "0 0 15px rgba(0,240,255,0.5)"},
                                    transition="all 0.3s",
                                    padding_x="8",
                                    padding_y="6",
                                    width=["100%", "auto"],
                                ),
                                flex_direction=["column", "row"],
                                align_items=["flex-start", "center"],
                                justify_content="space-between",
                                gap="4",
                            ),
                            border_bottom="1px solid #1E293B",
                            padding_y="6",
                            padding_x="4",
                            margin_x="-4",
                            border_radius="lg",
                            _hover={"bg": "#0F172A"},
                            transition="colors 0.3s",
                            width="100%",
                        ),
                        # Show 3 (Sold Out)
                        rx.box(
                            rx.flex(
                                rx.box(
                                    rx.text("Nov 04, 2024", font_size="0.875rem", font_weight="700", color="#00F0FF", letter_spacing="0.1em", text_transform="uppercase", margin_bottom="1"),
                                    rx.heading("Warehouse Project", font_family="Orbitron", font_size="1.25rem", font_weight="700", color="white", text_transform="uppercase", _hover={"color": "#00F0FF"}, transition="colors 0.3s"),
                                    rx.text("Manchester, UK", color="#94A3B8", font_weight="300"),
                                    flex="1",
                                ),
                                rx.button(
                                    "Sold Out",
                                    bg="#1E293B",
                                    color="#64748B",
                                    font_family="Orbitron",
                                    font_weight="700",
                                    font_size="0.875rem",
                                    text_transform="uppercase",
                                    letter_spacing="0.1em",
                                    cursor="not-allowed",
                                    padding_x="8",
                                    padding_y="6",
                                    width=["100%", "auto"],
                                    _hover={"bg": "#1E293B"},
                                ),
                                flex_direction=["column", "row"],
                                align_items=["flex-start", "center"],
                                justify_content="space-between",
                                gap="4",
                            ),
                            border_bottom="1px solid #1E293B",
                            padding_y="6",
                            padding_x="4",
                            margin_x="-4",
                            border_radius="lg",
                            _hover={"bg": "#0F172A"},
                            transition="colors 0.3s",
                            width="100%",
                        ),
                        # Show 4
                        rx.box(
                            rx.flex(
                                rx.box(
                                    rx.text("Nov 18, 2024", font_size="0.875rem", font_weight="700", color="#00F0FF", letter_spacing="0.1em", text_transform="uppercase", margin_bottom="1"),
                                    rx.heading("Printworks", font_family="Orbitron", font_size="1.25rem", font_weight="700", color="white", text_transform="uppercase", _hover={"color": "#00F0FF"}, transition="colors 0.3s"),
                                    rx.text("London, United Kingdom", color="#94A3B8", font_weight="300"),
                                    flex="1",
                                ),
                                rx.button(
                                    "Tickets",
                                    variant="outline",
                                    border_color="white",
                                    color="white",
                                    font_family="Orbitron",
                                    font_weight="700",
                                    font_size="0.875rem",
                                    text_transform="uppercase",
                                    letter_spacing="0.1em",
                                    _hover={"bg": "#00F0FF", "border_color": "#00F0FF", "color": "black", "box_shadow": "0 0 15px rgba(0,240,255,0.5)"},
                                    transition="all 0.3s",
                                    padding_x="8",
                                    padding_y="6",
                                    width=["100%", "auto"],
                                ),
                                flex_direction=["column", "row"],
                                align_items=["flex-start", "center"],
                                justify_content="space-between",
                                gap="4",
                            ),
                            border_bottom="1px solid #1E293B",
                            padding_y="6",
                            padding_x="4",
                            margin_x="-4",
                            border_radius="lg",
                            _hover={"bg": "#0F172A"},
                            transition="colors 0.3s",
                            width="100%",
                        ),
                        # Show 5 (Low Tickets)
                        rx.box(
                            rx.flex(
                                rx.box(
                                    rx.text("Dec 31, 2024", font_size="0.875rem", font_weight="700", color="#00F0FF", letter_spacing="0.1em", text_transform="uppercase", margin_bottom="1"),
                                    rx.heading("Origin NYE", font_family="Orbitron", font_size="1.25rem", font_weight="700", color="white", text_transform="uppercase", _hover={"color": "#00F0FF"}, transition="colors 0.3s"),
                                    rx.text("Perth, Australia", color="#94A3B8", font_weight="300"),
                                    flex="1",
                                ),
                                rx.button(
                                    "Low Tickets",
                                    variant="outline",
                                    border_color="#00F0FF",
                                    color="#00F0FF",
                                    font_family="Orbitron",
                                    font_weight="700",
                                    font_size="0.875rem",
                                    text_transform="uppercase",
                                    letter_spacing="0.1em",
                                    _hover={"bg": "#00F0FF", "color": "black", "box_shadow": "0 0 15px rgba(0,240,255,0.5)"},
                                    transition="all 0.3s",
                                    padding_x="8",
                                    padding_y="6",
                                    width=["100%", "auto"],
                                    class_name="animate-pulse",
                                ),
                                flex_direction=["column", "row"],
                                align_items=["flex-start", "center"],
                                justify_content="space-between",
                                gap="4",
                            ),
                            border_bottom="1px solid #1E293B",
                            padding_y="6",
                            padding_x="4",
                            margin_x="-4",
                            border_radius="lg",
                            _hover={"bg": "#0F172A"},
                            transition="colors 0.3s",
                            width="100%",
                        ),
                        width="100%",
                        align_items="stretch",
                        spacing="0",
                    ),
                    rx.box(
                        rx.button(
                            rx.hstack(
                                rx.text("expand_more", class_name="material-symbols-outlined", font_size="1rem"),
                                rx.text("Load More Dates"),
                                spacing="2",
                            ),
                            variant="ghost",
                            color="#94A3B8",
                            font_family="Orbitron",
                            text_transform="uppercase",
                            letter_spacing="0.1em",
                            font_size="0.875rem",
                            _hover={"color": "#00F0FF", "bg": "transparent"},
                            margin_top="8",
                            width="100%",
                        ),
                        text_align="center",
                    ),
                    col_span=[1, 1, 2],
                ),

                # Column 2: Booking Form Sidebar
                rx.box(
                    rx.box(
                        rx.box(
                            width="100%",
                            height="0.25rem",
                            bg="linear-gradient(to right, transparent, #00F0FF, transparent)",
                            opacity="0.7",
                            position="absolute",
                            top="0",
                            left="0",
                        ),
                        rx.heading(
                            rx.text.span("Request "),
                            rx.text.span("Booking", color="#00F0FF"),
                            font_family="Orbitron",
                            font_size="1.5rem",
                            font_weight="700",
                            color="white",
                            text_transform="uppercase",
                            letter_spacing="0.05em",
                            margin_bottom="6",
                        ),
                        rx.form(
                            rx.vstack(
                                rx.box(
                                    rx.text("Promoter / Organization", font_size="0.75rem", font_weight="700", color="#94A3B8", text_transform="uppercase", letter_spacing="0.1em", margin_bottom="2"),
                                    rx.input(placeholder="e.g. Bass Events", bg="black", border_color="#334155", color="white", padding="3", _focus={"border_color": "#00F0FF", "box_shadow": "0 0 0 1px #00F0FF"}, border_radius="sm"),
                                    width="100%",
                                ),
                                rx.grid(
                                    rx.box(
                                        rx.text("Date", font_size="0.75rem", font_weight="700", color="#94A3B8", text_transform="uppercase", letter_spacing="0.1em", margin_bottom="2"),
                                        rx.input(type="date", bg="black", border_color="#334155", color="white", padding="3", _focus={"border_color": "#00F0FF", "box_shadow": "0 0 0 1px #00F0FF"}, border_radius="sm"),
                                        width="100%",
                                    ),
                                    rx.box(
                                        rx.text("Offer Range", font_size="0.75rem", font_weight="700", color="#94A3B8", text_transform="uppercase", letter_spacing="0.1em", margin_bottom="2"),
                                        rx.select(
                                            ["Select...", "$5k - $10k", "$10k - $20k", "$20k+"],
                                            bg="black", border_color="#334155", color="white", padding="3", _focus={"border_color": "#00F0FF", "box_shadow": "0 0 0 1px #00F0FF"}, border_radius="sm"
                                        ),
                                        width="100%",
                                    ),
                                    columns="2",
                                    spacing="4",
                                    width="100%",
                                ),
                                rx.box(
                                    rx.text("Contact Email", font_size="0.75rem", font_weight="700", color="#94A3B8", text_transform="uppercase", letter_spacing="0.1em", margin_bottom="2"),
                                    rx.input(type="email", placeholder="agent@example.com", bg="black", border_color="#334155", color="white", padding="3", _focus={"border_color": "#00F0FF", "box_shadow": "0 0 0 1px #00F0FF"}, border_radius="sm"),
                                    width="100%",
                                ),
                                rx.box(
                                    rx.text("Event Details", font_size="0.75rem", font_weight="700", color="#94A3B8", text_transform="uppercase", letter_spacing="0.1em", margin_bottom="2"),
                                    rx.text_area(placeholder="Venue, capacity, other lineup...", bg="black", border_color="#334155", color="white", padding="3", _focus={"border_color": "#00F0FF", "box_shadow": "0 0 0 1px #00F0FF"}, border_radius="sm", rows="3"),
                                    width="100%",
                                ),
                                rx.button(
                                    "Submit Inquiry",
                                    type="submit",
                                    width="100%",
                                    bg="#00F0FF",
                                    color="black",
                                    font_family="Orbitron",
                                    font_weight="900",
                                    font_size="1.125rem",
                                    text_transform="uppercase",
                                    letter_spacing="0.1em",
                                    padding_y="6",
                                    _hover={"bg": "#00C2CC", "transform": "translateY(-4px)", "box_shadow": "0 0 20px rgba(0,240,255,0.4)"},
                                    transition="all 0.3s",
                                ),
                                spacing="5",
                                width="100%",
                            ),
                        ),
                        rx.box(
                            rx.heading("Representation", font_family="Orbitron", font_size="0.875rem", font_weight="700", color="#94A3B8", text_transform="uppercase", letter_spacing="0.1em", margin_bottom="4"),
                            rx.hstack(
                                rx.box(
                                    rx.text("public", class_name="material-symbols-outlined", color="#00F0FF"),
                                    bg="#0F172A",
                                    padding="2",
                                    border_radius="sm",
                                ),
                                rx.box(
                                    rx.text("World (Ex-NA)", font_weight="700", color="white", text_transform="uppercase", letter_spacing="0.05em"),
                                    rx.text("Primary Talent International", font_size="0.875rem", color="#94A3B8", margin_top="1"),
                                    rx.link("bookings@primary.com", href="mailto:bookings@primary.com", font_size="0.875rem", color="#00F0FF", font_family="monospace", _hover={"color": "white"}, transition="colors", margin_top="1", display="block"),
                                ),
                                align_items="flex-start",
                                gap="4",
                                margin_bottom="6",
                            ),
                            rx.hstack(
                                rx.box(
                                    rx.text("flag", class_name="material-symbols-outlined", color="#00F0FF"),
                                    bg="#0F172A",
                                    padding="2",
                                    border_radius="sm",
                                ),
                                rx.box(
                                    rx.text("North America", font_weight="700", color="white", text_transform="uppercase", letter_spacing="0.05em"),
                                    rx.text("United Talent Agency", font_size="0.875rem", color="#94A3B8", margin_top="1"),
                                    rx.link("bookings@uta.com", href="mailto:bookings@uta.com", font_size="0.875rem", color="#00F0FF", font_family="monospace", _hover={"color": "white"}, transition="colors", margin_top="1", display="block"),
                                ),
                                align_items="flex-start",
                                gap="4",
                            ),
                            border_top="1px solid #1E293B",
                            margin_top="8",
                            padding_top="8",
                        ),
                        bg="#121212",
                        border="1px solid #1E293B",
                        padding="8",
                        border_radius="sm",
                        box_shadow="xl",
                        position="relative",
                        overflow="hidden",
                    ),
                    position="sticky",
                    top="6rem",
                    col_span=1,
                ),
                columns={"initial": "1", "sm": "1", "lg": "3"},
                gap="12",
                max_width="80rem",
                margin_x="auto",
                padding_x="4",
                padding_bottom="6rem",
                width="100%",
                align_items="start",
            ),
            flex_grow="1",
            width="100%",
            z_index="10",
        ),
        
        # Footer
        footer(),

        width="100%",
        min_height="100vh",
        background="#050508",
        color="white",
        font_family="Montserrat",
        display="flex",
        flex_direction="column",
    )

def music() -> rx.Component:
    # Music & Streams Page
    return rx.box(
        # Navigation
        navbar(),

        # Header / Hero Section
        rx.box(
            rx.box(
                rx.image(
                    src="https://lh3.googleusercontent.com/aida-public/AB6AXuCkZNZ0dvbLt33p97nFPEatNsm2RJUPVj1FpU03V-WgquJOvZmQpqxFqDUzJyGWb18eFiC-ceZHXaGseSqaiFUAua_yCEq5rcHpklxKEBeE77ic7M7WOsjsBlO8mDWSqMSHqWxS53GPSukfMlXiwdKi8um81Jn2jaN3yOu1V2EQUq3uINNst9tM2ceb-vfU9GxD3_lyByDIV_piGB8tqwTyCHHQKlSzgXbVY9cWE80jq28MZ9UpyU-ACXIjtIKwG7DcTxwExbnRjQ",
                    width="100%",
                    height="100%",
                    object_fit="cover",
                    opacity="0.3",
                    mix_blend_mode="overlay",
                ),
                rx.box(
                    width="100%",
                    height="100%",
                    position="absolute",
                    top="0",
                    bg="linear-gradient(to bottom, rgba(5,5,8,0.5), #050508, #050508)",
                ),
                width="100%",
                height="100%",
                position="absolute",
                top="0",
                z_index="0",
            ),
            rx.vstack(
                rx.heading(
                    "AUDIO & TRANSMISSION",
                    font_family="Orbitron",
                    font_size=["2.5rem", "4rem", "5rem"],
                    font_weight="900",
                    letter_spacing="-0.05em",
                    text_transform="uppercase",
                    bg_clip="text",
                    color="transparent",
                    background_image="linear-gradient(to right, #94A3B8, #E2E8F0, #94A3B8)",
                    class_name="glitch-effect",
                    margin_bottom="4",
                ),
                rx.box(
                    height="0.25rem",
                    width="6rem",
                    bg="#00F0FF",
                    border_radius="full",
                    box_shadow="0 0 10px rgba(0,240,255,0.7)",
                    margin_top="8",
                ),
                position="relative",
                z_index="10",
                max_width="80rem",
                margin_x="auto",
                padding_x="4",
                align="center",
                text_align="center",
            ),
            position="relative",
            padding_top=["8rem", "12rem"],
            padding_bottom=["4rem", "4rem"],
            overflow="hidden",
        ),

        # Main Content Grid
        rx.box(
            rx.grid(
                # Column 1: Outbound to Kick
                rx.box(
                    rx.heading(
                        "Live Transmission",
                        font_family="Orbitron",
                        font_size="1.5rem",
                        font_weight="700",
                        color="white",
                        text_transform="uppercase",
                        letter_spacing="0.05em",
                        border_left="4px solid #00F0FF",
                        padding_left="4",
                        margin_bottom="6",
                    ),
                    rx.text(
                        "Catch my live Drum & Bass residency on Kick. Don't miss the next transmission.",
                        color="#94A3B8",
                        margin_bottom="6",
                    ),
                    rx.link(
                        rx.button(
                            "Join Live Transmission on Kick",
                            bg="#00F0FF",
                            color="black",
                            font_family="Orbitron",
                            font_weight="900",
                            font_size="1.125rem",
                            text_transform="uppercase",
                            letter_spacing="0.1em",
                            padding_y="6",
                            padding_x="8",
                            _hover={"bg": "#00C2CC", "transform": "translateY(-4px)", "box_shadow": "0 0 20px rgba(0,240,255,0.4)"},
                            transition="all 0.3s",
                            width="100%",
                            class_name="animate-pulse",
                        ),
                        href="https://kick.com/In2GrooveRadio",
                        is_external=True,
                    ),
                    bg="#121212",
                    border="1px solid #1E293B",
                    padding="8",
                    border_radius="sm",
                    box_shadow="xl",
                    margin_bottom="8",
                ),
                # Column 2: Video Embed and Youtube Link
                rx.box(
                    rx.heading(
                        "Latest Set",
                        font_family="Orbitron",
                        font_size="1.5rem",
                        font_weight="700",
                        color="white",
                        text_transform="uppercase",
                        letter_spacing="0.05em",
                        border_left="4px solid #00F0FF",
                        padding_left="4",
                        margin_bottom="6",
                    ),
                    rx.video(
                        url="https://youtu.be/02uIb61pcQc",
                        width="100%",
                        height="300px",
                        border_radius="sm",
                        box_shadow="0 0 20px rgba(0,240,255,0.2)",
                        margin_bottom="6",
                    ),
                    rx.link(
                        rx.button(
                            rx.hstack(
                                rx.text("play_circle", class_name="material-symbols-outlined"),
                                rx.text("Full YouTube Archive"),
                                spacing="2",
                            ),
                            variant="outline",
                            border_color="#00F0FF",
                            color="#00F0FF",
                            font_family="Orbitron",
                            font_weight="700",
                            font_size="0.875rem",
                            text_transform="uppercase",
                            letter_spacing="0.1em",
                            _hover={"bg": "#00F0FF", "color": "black", "box_shadow": "0 0 15px rgba(0,240,255,0.5)"},
                            transition="all 0.3s",
                            width="100%",
                            padding_y="6",
                        ),
                        href="https://www.youtube.com/@DJWaitaminute84",
                        is_external=True,
                    ),
                    bg="#121212",
                    border="1px solid #1E293B",
                    padding="8",
                    border_radius="sm",
                    box_shadow="xl",
                ),
                columns={"initial": "1", "md": "2"},
                gap="12",
                max_width="80rem",
                margin_x="auto",
                padding_x="4",
                padding_bottom="6rem",
                width="100%",
                align_items="start",
            ),
            flex_grow="1",
            width="100%",
            z_index="10",
        ),
        
        # Footer
        footer(),

        width="100%",
        min_height="100vh",
        background="#050508",
        color="white",
        font_family="Montserrat",
        display="flex",
        flex_direction="column",
    )


app = rx.App(
    stylesheets=[
        "https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;700;900&family=Orbitron:wght@400;700&display=swap",
        "https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@24,400,0,0",
        "/style.css",
    ],
    overlay_component=rx.fragment(),
)
app.add_page(index)
app.add_page(tour, route="/tour")
app.add_page(music, route="/music")
