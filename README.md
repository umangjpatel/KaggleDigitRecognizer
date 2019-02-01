<h1>KaggleDigitRecognizer</h1>
<p>Kaggle competition repository for correctly identifying digits from MNIST dataset of tens of thousands of handwritten images, coded in Python.</p>

<h2>Competition Description</h2>
<p>MNIST ("Modified National Institute of Standards and Technology") is the de facto “hello world” dataset of computer vision. Since its release in 1999, this classic dataset of handwritten images has served as the basis for benchmarking classification algorithms. As new machine learning techniques emerge, MNIST remains a reliable resource for researchers and learners alike.</p>
<p>In this competition, our goal is to correctly identify digits from a dataset of tens of thousands of handwritten images.</p>

<h2>Data</h2>
<p>The data files train.csv and test.csv contain gray-scale images of hand-drawn digits, from zero through nine.</p>
<p>Each image is 28 pixels in height and 28 pixels in width, for a total of 784 pixels in total. Each pixel has a single pixel-value associated with it, indicating the lightness or darkness of that pixel, with higher numbers meaning darker. This pixel-value is an integer between 0 and 255, inclusive.</p>
<p>The training data set, (train.csv), has 785 columns. The first column, called "label", is the digit that was drawn by the user. The rest of the columns contain the pixel-values of the associated image.</p>
<p>Each pixel column in the training set has a name like pixelx, where x is an integer between 0 and 783, inclusive. To locate this pixel on the image, suppose that we have decomposed x as x = i * 28 + j, where i and j are integers between 0 and 27, inclusive. Then pixelx is located on row i and column j of a 28 x 28 matrix, (indexing by zero).</p>
<p>For example, pixel31 indicates the pixel that is in the fourth column from the left, and the second row from the top, as in the ascii-diagram below.</p>
<p>Visually, if we omit the "pixel" prefix, the pixels make up the image like this:</p>
<pre>000 001 002 003 ... 026 027
028 029 030 031 ... 054 055
056 057 058 059 ... 082 083
 |   |   |   |  ...  |   |
728 729 730 731 ... 754 755
756 757 758 759 ... 782 783</pre>
<p>The test data set, (test.csv), is the same as the training set, except that it does not contain the "label" column.</p>
<p>The submission file is in the following format: For each of the 28000 images in the test set, output a single line containing the ImageId and the digit you predict. For example, if you predict that the first image is of a 3, the second image is of a 7, and the third image is of a 8, then your submission file would look like:</p>
<pre>ImageId,Label
1,3
2,7
3,8 
(27997 more lines)</pre>

<h2>Code</h2>
<p>I have used the following packages :</p>
<ol>
<li><b>NumPy</b>, for vectorized calculations</li>
<li><b>Pandas</b>, for reading the dataset</li>
<li><b>Matplotlib</b>, for data visualization</li>
<li><b>Keras</b>, for building the Neural Network</li>
</ol>

<p>Using Keras, we have built a 4-layer neural network, consisting of :</p>
<ol>
<li><b>1 input layer</b> of <b>784</b> input units</li>
<li><b>2 hidden layers</b>, each of <b>16</b> hidden units</li>
<li><b>1 output layer</b> of <b>10</b> output units</li>
</ol>
<p>10 output units for classifying a digit as a "0", "1", ..., "9"</p>
