# Multimodal-RBC-Segmentation
Stepwise image resolution reduction and evaluation of multimodal red blood cell segmentation to enhance DL-based malaria diagnostic solutions

# Introduction
Accurate segmentation of red blood cells (RBCs) is a key aspect of Deep Learning-based malaria diagnostics, enabling precise parasite classification and effective spectral analysis. This project explores the impact of image resolution and imaging modalities on segmentation accuracy, aiming to identify a resolution threshold that balances computational efficiency with diagnostic performance.

Using a subset of the Toy2 dataset (\cite{Merdasa2013}, captured using a multispectral multimodal microscope \cite{Brydegaard2011}), this study systematically reduces image resolutions from *1200x1600* to *60x80* pixels and evaluates the segmentation accuracy of two Cellpose 2.0 \cite{p} models. The models are trained on manually annotated ground truth cell masks and assessed using pixel-wise and cell-wise metrics, including Dice Score, Panoptic Quality Score, and F1 Score.

# Result Segmentation on Test Samples

<p align="center">
  <img src="images/test_result_0_9.png" alt="T07_Sample1_R - Factor 0.7" width="30%" />
  <img src="images/test_result_0_2.png" alt="T07_Sample1_R - Factor 0.2" width="30%" />
</p>

<p align="center">
  <strong>Image Resolution 1080x1440, Avg. Diameter Cell: 40.5 Pixel</strong> &nbsp; &nbsp;
  <strong>Image Resolution 240x320, Avg. Diameter Cell: 9 Pixel</strong>
</p>
Base image credits: A. Merdasa, M. Brydegaard, S. Svanberg, and J. T. Zoueu, “Staining-free malaria diagnostics by multispectral and multimodality light-emitting-diode microscopy,” J Biomed Opt, vol. 18, no. 3, p. 036002, Mar. 2013, doi: 10.1117/1.JBO.18.3.036002.

# Implementation
## Image & Mask Rescaling *resize_tif_png.py*
This Python script is designed to resize TIFF images (supporting 32-bit, 3-channel images) and their corresponding PNG masks to different resolutions, while preserving label integrity (Nearest neighbor interpolation).
- Input
  - Original TIFF image and an optional PNG mask (both with the same image resolution)
  - Scaling factors as a comma-separated list (e.g., 0.9,0.8,0.7)
- Output:
  - Rescaled TIFF images (e.g., original_name_resX_Y.tiff)
  - Rescaled PNG masks (e.g., original_name_resX_Y_masks.png)

Exaple Usage:
Before running the script, install the required dependencies by running:

```bash 
pip install -r requirements.txt
```
Then, execute the script by running the following command:

```bash
python resize_tif_png.py "0.9,0.8,0.7,0.6,0.5,0.4,0.3,0.2,0.1" /path/to/original_image.tiff /path/to/original_mask.png
```

