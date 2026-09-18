import subprocess


def capture_screen():
    subprocess.run(
        [
            "python.exe",
            "-c",
            (
                "from PIL import ImageGrab; "
                "ImageGrab.grab().save('screen.png')"
            ),
            ],
        check=True,
    )


if __name__ == "__main__":
    capture_screen()
    print("Screenshot saved as screen.png")