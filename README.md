# Mars Project
A computer vision project to extract features from a single dense image of Mars from the Mars Reconnaissance Orbiter.

![Thumbnail Image](https://github.com/davidmvermillion/VisualExplorations/blob/main/Mars/ESP_072719_1970_RED.browse.jpg)

# Project Plan

1. Examine image for extractable features \
	a. Crater count [start here] \
		i. SkImage [example](https://scikit-image.org/docs/stable/auto_examples/features_detection/plot_holes_and_peaks.html#sphx-glr-auto-examples-features-detection-plot-holes-and-peaks-py) \
	b. Crater diameters (requires extra data) \
	c. Ejecta diameters \
	d. Ridge counts \
	e. Compare smooth to cratered surface statistics \
	f. Boulder counts
2. Determine package and pre-trained model to use
	a. Python \
		i. OpenCV \
		ii. Scikit-Image \
			a. https://scikit-image.org/docs/stable/user_guide/ \
		iii. PIL (Python Imaging Library) \
		iv. Tensorflow \
		v. Keras \
	b. R \
		i. Rvision
		
3. Determine computer vision model to use \
	a. [Gabor filter banks for texture classification](https://scikit-image.org/docs/stable/auto_examples/features_detection/plot_gabor.html#sphx-glr-auto-examples-features-detection-plot-gabor-py) \
	b. [Local Binary Pattern for texture classification](https://scikit-image.org/docs/stable/auto_examples/features_detection/plot_local_binary_pattern.html#sphx-glr-auto-examples-features-detection-plot-local-binary-pattern-py) \
	c. [Multi-Block Local Binary Pattern for texture classification](https://scikit-image.org/docs/stable/auto_examples/features_detection/plot_multiblock_local_binary_pattern.html#sphx-glr-auto-examples-features-detection-plot-multiblock-local-binary-pattern-py) \
	d. [Morphological Filtering](https://scikit-image.org/docs/stable/auto_examples/applications/plot_morphology.html#sphx-glr-auto-examples-applications-plot-morphology-py) \
	e. [Colocalization metrics](https://scikit-image.org/docs/stable/auto_examples/applications/plot_colocalization_metrics.html#sphx-glr-auto-examples-applications-plot-colocalization-metrics-py) \
	f. [Registration using optical flow](https://scikit-image.org/docs/stable/auto_examples/registration/plot_opticalflow.html#sphx-glr-auto-examples-registration-plot-opticalflow-py) \
	g. [Removing small objects in grayscale images with a top hat filter](https://scikit-image.org/docs/stable/auto_examples/filters/plot_tophat.html#sphx-glr-auto-examples-filters-plot-tophat-py) \
	h. [Using window functions with images](https://scikit-image.org/docs/stable/auto_examples/filters/plot_window.html#sphx-glr-auto-examples-filters-plot-window-py)

## Files
1. [ESP_072719_1970_RED.browse.jpg](https://github.com/davidmvermillion/VisualExplorations/blob/main/Mars/ESP_072719_1970_RED.browse.jpg) is the low-resolution dataset preview image.
2. [ESP_072719_1970_RED.LBL](https://github.com/davidmvermillion/VisualExplorations/blob/main/Mars/ESP_072719_1970_RED.LBL) has the detailed information about the image in the LBL format.
3. [ESP_072719_1970_RED.XML](https://github.com/davidmvermillion/VisualExplorations/blob/main/Mars/ESP_072719_1970_RED.XML) has the detailed information about the image in the XML format.

## Data Source
1. [Mars Reconnaissance Orbiter ESP_072719_1970_RED.JP2](https://pds-imaging.jpl.nasa.gov/beta/record?uri=atlas:pds3:mro:mars_reconnaissance_orbiter:/MROHR_0001/data/RDR/ESP/ORB_072700_072799/ESP_072719_1970/ESP_072719_1970_RED.JP2)

## Other Notes
Consider combining algorithms. E.g. hole detection with blob detection