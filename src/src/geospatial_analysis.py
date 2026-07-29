"""
===============================================================
Geospatial Analysis
===============================================================

Methods Section 2.15

Purpose

Visualize regional reporting patterns
of fluoroquinolone-associated
cardiovascular adverse drug reactions
within the UAE.

Note

Spatial analyses describe reporting
patterns only and should not be
interpreted as causal disease risk.
"""

import geopandas as gpd


class GeospatialAnalysis:

    def load_regions(self, file):

        return gpd.read_file(file)

    def merge_data(self,
                   map_df,
                   report_df):

        """
        Merge reporting data
        with geographic regions.
        """
        pass

    def generate_map(self):

        """
        Generate choropleth map.
        """
        pass


if __name__ == "__main__":
    print("Geospatial module ready.")
