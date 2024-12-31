import os
import numpy as np
from skimage.transform import resize
from skimage.io import imread, imsave
import argparse
import warnings

def resize_image(input_image, scale_factor):
    """
    Resizes a 3-channel, 32-bit image while preserving precision.

    Parameters:
    - input_image: np.ndarray, Input image with shape (H, W, C) and dtype=np.float32
    - scale_factor: float, Scale factor for resizing

    Returns:
    - resized_image: np.ndarray, Resized image with preserved precision
    """
    if input_image.ndim != 3 or input_image.shape[-1] != 3:
        raise ValueError("Input image must have 3 channels (H, W, 3).")
    if input_image.dtype != np.float32:
        raise ValueError("Input image must be of dtype np.float32.")

    # Calculate the target dimensions
    target_shape = (
        int(input_image.shape[0] * scale_factor),  # New height
        int(input_image.shape[1] * scale_factor),  # New width
        input_image.shape[2]  # Channels remain the same
    )

    # Resize each channel independently to preserve precision
    resized_channels = [
        resize(
            input_image[..., c],
            (target_shape[0], target_shape[1]),
            preserve_range=True,
            anti_aliasing=True
        ) for c in range(3)
    ]

    # Stack resized channels back into a 3-channel image
    resized_image = np.stack(resized_channels, axis=-1).astype(np.float32)

    return resized_image

def main():
    parser = argparse.ArgumentParser(description="Resize a TIFF image and optionally a PNG mask.")
    parser.add_argument("scale_factors", type=str, help="Comma-separated list of scale factors (e.g., '0.9,0.8,0.7').")
    parser.add_argument("tif_file", type=str, help="Path to the input TIFF image.")
    parser.add_argument("png_file", type=str, nargs="?", default=None, help="Path to the input PNG mask (optional).")
    args = parser.parse_args()

    scale_factors = [float(factor) for factor in args.scale_factors.split(",")]
    tif_file = args.tif_file
    png_file = args.png_file

    for scale_factor in scale_factors:
        # Load the TIFF image
        tif_image = imread(tif_file).astype(np.float32)

        # Resize the TIFF image
        tif_image_resized = resize_image(tif_image, scale_factor)

        # Extract the base filename without directory and extension
        basename = os.path.splitext(os.path.basename(tif_file))[0]
        res_factor_name = f"res{scale_factor:.2f}".replace('.', '_')

        # Generate output path for the resized TIFF image
        tif_output_file = f"{os.path.dirname(tif_file)}/{basename}_{res_factor_name}.tiff"

        # Save the resized TIFF image
        imsave(tif_output_file, tif_image_resized)
        print(f"Downsampled TIFF saved to: {tif_output_file}")

        if png_file:
            # Load the PNG mask
            png_mask = imread(png_file)

            # Convert RGB mask to single-channel if necessary
            if png_mask.ndim == 3:
                png_mask = png_mask[..., 0]

            # Calculate new dimensions for the mask
            new_shape_mask = tuple([int(dim * scale_factor) for dim in png_mask.shape[:2]])

            # Resize the mask using nearest neighbor interpolation
            mask_resized = resize(
                png_mask,
                new_shape_mask,
                order=0,  # Nearest Neighbor for discrete labels
                preserve_range=True,
                anti_aliasing=False
            ).astype(np.uint16)

            original_labels = np.unique(png_mask)
            resized_labels = np.unique(mask_resized)
            # Ensure no labels are lost during resizing
            try:
                # Ensure no labels are lost during resizing
                assert set(original_labels).issubset(set(resized_labels)), "Some labels are missing after resizing!"
            except AssertionError as e:
                print(f"Warning: {str(e)}")
                print(f"Original labels: {len(original_labels)}")
                print(f"Resized labels: {len(resized_labels)}")

            # Generate output path for the resized mask
            mask_output_file = f"{os.path.dirname(png_file)}/{basename}_{res_factor_name}_masks.png"
            # Suppress specific warnings
            warnings.filterwarnings("ignore", message=".*is a low contrast image.*")
            # Save the resized mask
            imsave(mask_output_file, mask_resized)
            print(f"Rescaled mask saved to: {mask_output_file}")

if __name__ == "__main__":
    main()
