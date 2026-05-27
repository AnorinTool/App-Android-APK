import flet as ft
import uvicorn
import base64


def main(page: ft.Page):

    page.title = "An Orin Tool"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = "#0d0d0d"
    page.padding = 20
    page.scroll = ft.ScrollMode.AUTO

    # =========================
    # SNACKBAR (Cấu trúc chuẩn hóa Mobile)
    # =========================
    def show_snack(message: str, color: str = "#00e5ff"):
        # Khởi tạo đối tượng SnackBar sạch, không dùng thuộc tính .open = True trực tiếp
        snack = ft.SnackBar(
            content=ft.Text(
                message,
                color="#0d0d0d",
                weight=ft.FontWeight.W_600
            ),
            bgcolor=color,
            duration=2500,
            show_close_icon=True,
        )
        # Sử dụng phương thức mở an toàn của hệ thống để tránh xung đột luồng biên dịch
        page.open(snack)
        page.update()

    # =========================
    # ENCODE
    # =========================
    def do_encode(e):
        raw = input_field.value.strip()

        if not raw:
            show_snack("⚠ Input is empty", "#ff6b35")
            return

        try:
            encoded = base64.b64encode(
                raw.encode("utf-8")
            ).decode("utf-8")

            output_field.value = encoded
            page.update()
            show_snack("✓ Encoded to Base64")

        except Exception as exc:
            show_snack(f"Error: {exc}", "#ff3d71")

    # =========================
    # DECODE
    # =========================
    def do_decode(e):
        raw = input_field.value.strip()

        if not raw:
            show_snack("⚠ Input is empty", "#ff6b35")
            return

        try:
            decoded = base64.b64decode(
                raw
            ).decode("utf-8")

            output_field.value = decoded
            page.update()
            show_snack("✓ Decoded from Base64", "#a8ff78")

        except Exception:
            show_snack("✗ Invalid Base64 string", "#ff3d71")

    # =========================
    # CLEAR
    # =========================
    def do_clear(e):
        input_field.value = ""
        output_field.value = ""
        page.update()
        show_snack("✓ Cleared", "#b0bec5")

    # =========================
    # COPY
    # =========================
    def copy_output(e):
        if output_field.value:
            page.set_clipboard(output_field.value)
            show_snack("✓ Copied to clipboard", "#ce93d8")
        else:
            show_snack("⚠ Nothing to copy", "#ff6b35")

    # =========================
    # INPUT FIELD
    # =========================
    input_field = ft.TextField(
        label="Input",
        hint_text="Paste text or Base64 here...",
        multiline=True,
        min_lines=5,
        max_lines=10,
        bgcolor="#1a1a2e",
        border_color="#00e5ff",
        focused_border_color="#00bcd4",
        color="#e0e0e0",
        cursor_color="#00e5ff",
        expand=True,
    )

    # =========================
    # OUTPUT FIELD
    # =========================
    output_field = ft.TextField(
        label="Output",
        hint_text="Result appears here...",
        multiline=True,
        min_lines=5,
        max_lines=10,
        read_only=True,
        bgcolor="#0f1923",
        border_color="#546e7a",
        focused_border_color="#00bcd4",
        color="#a8d8ea",
        expand=True,
    )

    # =========================
    # BUTTONS
    # =========================
    btn_encode = ft.ElevatedButton(
        "Encode →",
        on_click=do_encode,
        bgcolor="#00bcd4",
        color="#0d0d0d",
        expand=True,
    )

    btn_decode = ft.ElevatedButton(
        "← Decode",
        on_click=do_decode,
        bgcolor="#1de9b6",
        color="#0d0d0d",
        expand=True,
    )

    btn_clear = ft.ElevatedButton(
        "Clear",
        on_click=do_clear,
        bgcolor="#37474f",
        color="#e0e0e0",
        expand=True,
    )

    btn_copy = ft.ElevatedButton(
        "Copy Output",
        on_click=copy_output,
        bgcolor="#6a1b9a",
        color="#e0e0e0",
        expand=True,
    )

    # =========================
    # HEADER
    # =========================
    header = ft.Container(
        content=ft.Column(
            [
                ft.Row(
                    [
                        ft.Icon(
                            ft.Icons.LOCK_OUTLINE,
                            color="#00e5ff",
                            size=28
                        ),
                        ft.Text(
                            "An Orin Tool",
                            size=26,
                            weight=ft.FontWeight.BOLD,
                            color="#00e5ff",
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                ft.Text(
                    "Base64 Encoder / Decoder",
                    size=13,
                    color="#546e7a",
                    text_align=ft.TextAlign.CENTER,
                ),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        padding=20,
    )

    # =========================
    # MAIN LAYOUT
    # =========================
    page.add(
        ft.Column(
            [
                header,
                input_field,
                ft.Container(height=10),
                ft.Row(
                    [btn_encode, btn_decode],
                    spacing=10
                ),
                ft.Container(height=10),
                output_field,
                ft.Container(height=10),
                ft.Row(
                    [btn_copy, btn_clear],
                    spacing=10
                ),
                ft.Divider(),
                ft.Text(
                    "v1.0 · com.anorin.tool",
                    size=11,
                    color="#455a64",
                    text_align=ft.TextAlign.CENTER,
                ),
            ],
            spacing=5,
            expand=True,
        )
    )


if __name__ == "__main__":
    ft.app(target=main)
