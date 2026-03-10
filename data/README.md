# Airfoil CFD Datasets
This directory contains the raw and processed datasets generated from automated ANSYS Fluent batch runs, used to train surrogate machine learning models.

## 1. Raw Data (`raw/`)
Contains the direct outputs from the Fluent solver sweeps.
* **Airfoil_sweep:** Contains subfolders for each Angle of Attack (AoA) run. Each folder includes:
  * `history_*.out`: Force convergence history (contains final Cl and Cd).
  * `cp_upper_*.csv` & `cp_lower_*.csv`: Unstructured, space-delimited surface pressure coefficient data.
* **Nozzle_sweep:** Contains subfolders for Nozzle Pressure Ratio (NPR) runs, including thrust histories and wall pressure distributions.

## 2. Processed Datasets (`datasets/`)
Contains the cleaned, normalized, and interpolated matrices ready to train surrogate machine learning models.
* **`airfoil_dataset.npz`:**
  * `X`: Input feature matrix `[AoA, Reynolds Number]`.
  * `y_cp`: Target matrix containing 200 concatenated points (100 upper surface, 100 lower surface) interpolated onto a uniform x/c grid.
  * `y_cl`, `y_cd`: Target arrays for scalar lift and drag coefficients.
  * `x_grid`: The normalized 1D chordwise spatial array used for interpolation.