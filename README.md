# SWFWaterHack: Crop Mapping

A project that predicts crops based on evapotransporation parameters.

## Problem Statement

Water management continues to be an issue in California, especially in the Central Valley and during periods of heavy rain.

Determining what crops are planted in a field through remote methods could be an effective way to understand where resources can be diverted for better farming practices. Then, how can we combine modern tools with these datasets to assist in water management?

## Our Approach

A basic solution to determining crops in a field is simply asking the farmers, but considering the sheer amount of farmers in the Central Valley, this is impractical.

We can instead extract data from satellite images, which in turn provide us with valuable information on the variables that can help determine the crops in a field.

Evapotranspiration is one such variable and, in short, is the combination of evaporation from ground soil and the transpiration from plants.

We aimed to develop an understanding of how evapotranspiration correlates to crops and then apply that to crop identification.

Our plan was to run 2018 and 2019 mean ET data extracted through rasters in a machine learning model, then have it predict 2020 crops in farming fields given incomplete data. predictions, and create an interactive map through ArcGIS Pro exported to ArcGIS Online or Leaflet.

The map would display 3 years of data: 2018, 2019, and 2020. 2018 and 2019 would display the given data, while 2020 would draw data from our predictions. Anyone browsing the map would be able to browse across multiple years, and in each year, select a field and see information about the field. This information would include the crop planted in the field, the size of the field, and basic evapotranspiration data.

We decided to use a random forest model, which is good at classification.

## Running the Model

To run the model, run the following command in the terminal:

`python3 randomforest.py`

## Results

We achieved an accuracy of 50-54% on our model, with an average recall of 53%. We also discovered ET and Surface Downwelling Shortwave Flux in Air (srad) were the biggest factors in determining the crop contained in each field.

Sample results:

![sample results](https://media.discordapp.net/attachments/1099156880607170671/1099756060287443096/image.png?width=626&height=416)

Importance of each variable:

![Feature importances](https://media.discordapp.net/attachments/1099156880607170671/1099756060052553849/image.png?width=881&height=625)

Scatterplot:

![Scatterplot](https://media.discordapp.net/attachments/1099156880607170671/1099760399378817064/Figure_1.png?width=800&height=600)

Our model struggled significantly with determining where young perennials (YP) were planted; this category of plants tended to have the lowest accuracy. These results were outliers and tended to bring all the averages down.

## Future Improvements

Due to limited time, there are a lot of improvements that we can make to our model, our maps, and our website.

After we plotted the data, we discovered a few key issues, one of them being spread, which is not optimal for random forest models. Additionally, we may have failed to account for extra dimensions for extra variables, resulting in compression.

A complete solution would consist of a more comprehensive site that includes more detailed results along with an ArcGIS Online or Leaflet map embedded.

## Resources

* <a href="https://www.arcgis.com/home/item.html?id=7a0a5b5d089b4fde8eae106f495906c6" target="_blank">ArcGIS Online Interactive Map</a>
* [Slideshow](https://docs.google.com/presentation/d/1qvFzjBrlVxAdcrutZ4Sz9cOp1wOMiHDqi7clqqaK5u8/edit?usp=sharing)
