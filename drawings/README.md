# Editable CAD drawings

Store reviewed, editable DXF master files here.

The first planned drawing is phase1_site_base.dxf, generated from site/phase1_traverse_coordinates.csv by scripts/generate_site_base.py.

The first DXF has now been generated and passed automated structural and geometry checks in GitHub Actions. It is available in the `plate2-phase1-cad-6` workflow artifact, but is not yet committed as a repository file. Download it from the [successful workflow run](https://github.com/justryan-n2d/plate_2_bsd/actions/runs/38008699847). Manual inspection in a compatible CAD application is still pending. Model-space units must be metres. The actual parcel outline must use courses 1-2 through 4-5 plus the adjusted P5-1 closing course. The original P5-1 and diagnostic gap are reference data, not extra boundary segments.
