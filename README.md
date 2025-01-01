# Multimodal-RBC-Segmentation
Stepwise image resolution reduction and evaluation of multimodal red blood cell segmentation to enhance DL-based malaria diagnostic solutions

# Introduction
Accurate segmentation of red blood cells (RBCs) is a key aspect of Deep Learning-based malaria diagnostics, enabling precise parasite classification and effective spectral analysis. This project explores the impact of image resolution and imaging modalities on segmentation accuracy, aiming to identify a resolution threshold that balances computational efficiency with diagnostic performance.

Using a subset of the Toy2 dataset (\cite{Merdasa2013}, captured using a multispectral multimodal microscope \cite{Brydegaard2011}), this study systematically reduces image resolutions from *1200x1600* to *60x80* pixels and evaluates the segmentation accuracy of two Cellpose 2.0 models. The models are trained on manually annotated ground truth cell masks and assessed using pixel-wise and cell-wise metrics, including Dice Score, Panoptic Quality Score, and F1 Score.

# Segmentation on Unknown Test Samples
# Segmentation on Unknown Test Samples

<div style="display: flex; justify-content: space-between;">
  <img src="images/test_result_0_9.eps" alt="T07_Sample1_R - Factor 0.9" width="45%" />
  <img src="images/test_result_0_2.png" alt="T07_Sample1_R - Factor 0.2" width="45%" />
</div>

Base image credits: A. Merdasa, M. Brydegaard, S. Svanberg, and J. T. Zoueu, “Staining-free malaria diagnostics by multispectral and multimodality light-emitting-diode microscopy,” J Biomed Opt, vol. 18, no. 3, p. 036002, Mar. 2013, doi: 10.1117/1.JBO.18.3.036002.




# Methodology
## Segmentation model
- Cellpose 2.0 model 'cyto3' \cite{Pachitariu2022}
## Manual Preprocessing:
- Images inverted for Reflectance and Transmission modes to ensure bright objects on a dark background.
- Channels reduced from 13 to 3 using ImageJ tools
## Manual Ground Truth Generation
- Reflection mode images used to create ground truth masks for instance segmentation
- Manually corrected segmentation errors using Cellpose GUI

# Dynamic Diameter Adjustment
- Adjusted pixel diameter based on image resolution for consistent segmentation performance.
- Example: Diameter of 45 pixels for *1200x1600*, Diameter of 22.5 pixels for *120x160*

# Image & Mask Rescaling *resize_tif_png.py*
Generating scaled images and masks
- Input:
- Output:
  Run: 
# Credits
