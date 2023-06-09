# SWFWaterHack: Predicting Crops from Rasterized Satellite Evapotranspiration Data with Random Forest, and Visualization using ArcGIS

By Carolyn Cui, Luis Fujarte, Yulin Lin, Ryan Milstrey, Joshua Tapia

---

Our project predicts crops based on evapotransporation data and multiple additional environmental parameters. Trained on data from 100,000 fields in California's Central Valley, we can determine what type of crop is planted in a field, from nine different categories and with just over 50% accuracy.

## Problem Statement

Water management is a persistent issue in California, and one that continues to grow with climate change, as we adapt to dealing with more unpredictable weather patterns and prolonged periods of drought. The problem becomes more pertinent in the Central Valley and during periods of heavy rain. The Central Valley's water demand is high due to farming, while heavy rain sometimes brings too much water, too soon.

Determining what crops are planted in a field through remote methods could be an effective way to understand where resources can be diverted for better farming practices. Thus, we aimed to identify a potential solution that combines these datasets with modern tools.

## Our Approach

We were provided with mostly preprocessed data extracted from raster satellite images.

Evapotranspiration is one such variable and, in short, is the combination of evaporation from ground soil and the transpiration from plants.

We aimed to develop an understanding of how evapotranspiration correlates to crops and then apply that to crop identification.

We had three main steps in our approach: data analysis and processing, model development/training, and presentation.
Starting with data analysis, we would run 2018 and 2019 mean ET data extracted through rasters in a machine learning model, then have it predict 2020 crops in farming fields given incomplete data. Then, we could integrate those predictions into an interactive map exported to ArcGIS Online or Leaflet.

The map would display 3 years of data: 2018, 2019, and 2020. 2018 and 2019 would display the given data, while 2020 would draw data from our predictions. Anyone browsing the map would be able to browse across multiple years, and in each year, select a field and see information about the field. This information would include the crop planted in the field, the size of the field, and basic evapotranspiration data.

We determined a random forest model to be most fitting for our scenario, as it could help not only with classification, but with determining the most important factors in categorizing the crops.

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

* <a href="https://www.arcgis.com/apps/mapviewer/index.html?webmap=7a0a5b5d089b4fde8eae106f495906c6" target="_blank">ArcGIS Online Interactive Map</a>
* [Slideshow](https://docs.google.com/presentation/d/1qvFzjBrlVxAdcrutZ4Sz9cOp1wOMiHDqi7clqqaK5u8/edit?usp=sharing)
