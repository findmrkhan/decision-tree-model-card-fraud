# Visualisation of elaborative decision trees with dtreeviz python library as compared to SKLearn tree for credit card fraud detection dataset

A picture is worth more than thousand words! Hence we need better visualisations. One of the python libraries named dtreeviz is aimed at enhancing the decision trees that are produced by SKLearn library. 
Below is the difference in images of SKLearn vs dtreeviz libraries.


#### SKLearn
![](img/skl42_3.png) 

#### dtreeviz
![](img/dtv42_3.png)

## Difference in node representation
The data shown in the **SKLearn** tree nodes is in text format which needs to be read and carefully understood to make sense of why the split of the tree was made at that value. In contrast the **dtreeviz** tree nodes are shown as graph which makes it very intuitive to understand why the split was made at that value. 

## Difference in color choice
The color selection of **SKLearn** for coloring the nodes is not very obvious for the observer as it lacks the legend. However the **dtreeviz** has a color legend as part of its node which eliminates the guess that observers have to do.
More such details are available on this [blog](https://explained.ai/decision-tree-viz/). 

## The data
The dataset used for the demo is the credit card fraud detection data set. It is a very well known dataset available on this [link](https://www.kaggle.com/mlg-ulb/creditcardfraud/download)

## The code
Lets understand the code which can generate the dtreeviz graph and some caveats needed to wrap it up into a REST API.
The function `getDtreeVizImg()` in `dtreevizgraph.py` generates the **dtreeviz graph**. The function can be customised to generate the different depth trees by adjusting the input parameters. First the code splits the data into training and test sets and uses **SKLearn's** `DecisionTreeClassifier()` for generating the decision tree model. Next the training of model is done using the `fit()` method. The method `dtreeviz()` isused to generate the tree and it is saved in `SVG` format using the save method. Another library **CairoSVG** is used to convert `SVG` to `PNG` format that is saved on disk using the `Image.save()` **Pillow** library.
In order to expose this function into a web API to send the image, the image data needs to be serialised into one of the well known format. **Base 64** format is one such well known format for doing this. This is done using the `base64.b64encode()` method.

