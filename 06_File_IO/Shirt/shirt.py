import sys
from pathlib import Path
from PIL import Image, ImageOps


def main():
    # Validate command-line arguments count.
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    input_path, output_path = Path(sys.argv[1]), Path(sys.argv[2])

    # Validate extensions
    valid_extensions = {".jpg", ".jpeg", ".png"}
    for f in [input_path, output_path]:
        if f.suffix.lower() not in valid_extensions:
            sys.exit("Not a .jpg, .jpeg, .png file")

    # Validate equal extensions.
    if input_path.suffix.lower() != output_path.suffix.lower():
        sys.exit("Error: Input and output  have different extensions")

    # Execution with error treatment
    try:
        overlay(input_path, output_path)
    except FileNotFoundError:
        sys.exit(f"Could not find {input_path}")


def overlay(input_p, output_p):
    """
    Processes the input image by resizing and cropping it
    to match the shirt's dimensions, then overlays
    'shirt.png' and saves the result
    """
    with Image.open(input_p) as input_img:
        with Image.open("shirt.png") as shirt_img:
            fit_crop = ImageOps.fit(
                input_img,
                shirt_img.size,
                method=Image.Resampling.BICUBIC,
                bleed=0.0,
                centering=(0.5, 0.5),
            )
            fit_crop.paste(shirt_img, shirt_img)
            fit_crop.save(output_p)


if __name__ == "__main__":
    main()
