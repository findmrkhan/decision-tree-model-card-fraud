# Visualization of elaborative decision trees with dtreeviz python library as compared to SKLearn tree for credit card fraud detection dataset

A picture is worth more than thousand words! Hence we need better visualisations. One of the python libraries named **dtreeviz** is aimed at enhancing the decision trees that are produced by SKLearn library. In this post I will explain the usage of this library in python code which can generate the **dtreeviz** graph and some caveats needed to expose it through a **REST API**.


## The data
The dataset used for the demo is the credit card fraud detection data set. It is a very well known dataset available on this [link](https://www.kaggle.com/mlg-ulb/creditcardfraud/download).
The `creditcard.csv` file uploaded here has few sample rows for viewing & understanding the data and not the complete data due to github's file size restrictions.

### SKLearn vs dtreeviz
Below is the difference in images of **SKLearn vs dtreeviz** libraries.


#### SKLearn
![](img/skl42_3.png) 

#### dtreeviz
![](img/dtv42_3.png)

## Difference in node representation
Both the trees are 3 level deep.
The data shown in the **SKLearn** tree nodes is in text format which needs to be read and carefully understood to make sense of why the split of the tree was made at that value. In contrast the **dtreeviz** tree nodes are shown as graph which makes it very intuitive to understand why the split was made at that value. No further drilling down is needed into the data. This save a lot of time and energy. 

## Difference in color choice
The color selection of **SKLearn** for coloring the nodes is not very obvious for the observer as it lacks the legend. However the **dtreeviz** has a color legend as part of its node which eliminates the guess that observers have to do.
More such details are available on this [blog](https://explained.ai/decision-tree-viz/). 


## The code

The function `getDtreeVizImg()` in `dtreevizgraph.py` generates the **dtreeviz graph**. The function can be customised to generate the different depth trees by adjusting the input parameters. First the code splits the data into training and test sets and uses **SKLearn's** `DecisionTreeClassifier()` for generating the decision tree model. Next the training of model is done using the `fit()` method. The method `dtreeviz()` isused to generate the tree and it is saved in `SVG` format using the save method. Another library **CairoSVG** is used to convert `SVG` to `PNG` format that is saved on disk using the `Image.save()` **Pillow** library.
In order to expose this function into a web API to send the image, the image data needs to be serialised into one of the well known format. **Base 64** format is one such well known format for doing this. This is done using the `base64.b64encode()` method.

The file `sklearngraph.py` generates the SKLearn style graph.

The `main.py` is the entry point of the program. The line `app = Flask(__name__)` initialises a **Flask** Web app and `app.run(host='0.0.0.0', port=5005)` makes it listening on port `5005`.
Next, the line `@app.route('/getCardFraudDtree', methods=['POST'])` exposes the `POST` endpoint `/getCardFraudDtree`. It accepts the style chosen by end users in `JSON` format. A sample data packet is `{ "style" : "dtreeviz" }`. The style `sklearn` shows the **sklearn** graph and `dtreeviz` shows **dtreeviz** graph. 

## Running the application
For running the application you need to have **Python 3** and **PIP** installed on your system. Download this code on your local system. Further you need to run the below command to install all the dependencies from `requirements.txt` file

`pip install -r requirements.txt`

Then run the below command and Voila! your REST API is ready to be consumed.

`python main.py`


![](img/running-app.png)


## The client program to test the exposed API
The file `post2url-client.py` has the code to consume the REST API by sending the JSON data.
Open another terminal and run the below command

`python post2url-client.py`

The generated graph will be displayed on the screen.

## The conclusion
The graphical representation of **dtreeviz** nodes and the color choices makes it a clear winner for visualizing decision trees.

If there are any questions, suggestions or comments, please let me know @ findmrkhan@gmail.com
