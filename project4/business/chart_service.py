# business/chart_service.py
"""
CST8002 - Practical Project Part 04
Professor: Stanley Pieda
Due Date: 2025-11-21
Author: Lihua Lu

This module contains the business logic for generating seabird data visualizations
using Matplotlib for vertical bar charts.
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

class ChartService:
    """
    Service class that handles business logic for chart generation
    using Matplotlib library.
    """
    
    def __init__(self):
        """Initializes the chart service with matplotlib settings."""
        plt.style.use('ggplot')  # Use a professional style
        self.fig_size = (12, 8)  # Default figure size
    
    def create_species_count_chart(self, df):
        """
        Creates a vertical bar chart showing total bird counts by species.
        
        Parameters:
            df (pandas.DataFrame): Seabird data DataFrame
        """
        try:
            # Group by species and calculate total bird count
            species_data = df.groupby('species_code')['total_bird_count'].sum().sort_values(ascending=False)
            
            # Create the chart
            plt.figure(figsize=self.fig_size)
            bars = plt.bar(species_data.index, species_data.values, 
                          color=plt.cm.Set3(np.linspace(0, 1, len(species_data))))
            
            # Customize the chart
            plt.title('Total Bird Count by Species (1994-2017)', fontsize=16, fontweight='bold')
            plt.xlabel('Species Code', fontsize=12)
            plt.ylabel('Total Bird Count', fontsize=12)
            plt.xticks(rotation=45)
            plt.grid(axis='y', alpha=0.3)
            
            # Add value labels on bars
            for bar in bars:
                height = bar.get_height()
                plt.text(bar.get_x() + bar.get_width()/2., height,
                        f'{int(height):,}', ha='center', va='bottom', fontsize=9)
            
            plt.tight_layout()
            plt.show()
            
        except Exception as e:
            print(f"Error creating species count chart: {e}")
    
    def create_yearly_trends_chart(self, df):
        """
        Creates a vertical bar chart showing bird counts by year.
        
        Parameters:
            df (pandas.DataFrame): Seabird data DataFrame
        """
        try:
            # Group by year and calculate total bird count
            yearly_data = df.groupby('year')['total_bird_count'].sum()
            
            # Create the chart
            plt.figure(figsize=self.fig_size)
            bars = plt.bar(yearly_data.index, yearly_data.values, color='steelblue', alpha=0.7)
            
            # Customize the chart
            plt.title('Yearly Bird Count Trends (1994-2017)', fontsize=18, fontweight='bold')
            plt.xlabel('Year', fontsize=12)
            plt.ylabel('Total Bird Count', fontsize=12)
            plt.grid(axis='y', alpha=0.3)
            
            # Add value labels on bars
            for bar in bars:
                height = bar.get_height()
                plt.text(bar.get_x() + bar.get_width()/2., height,
                        f'{int(height):,}', ha='center', va='bottom', fontsize=9)
            
            plt.tight_layout()
            plt.show()
            
        except Exception as e:
            print(f"Error creating yearly trends chart: {e}")
    
    def create_transect_comparison_chart(self, df):
        """
        Creates a vertical bar chart comparing bird counts across transects.
        
        Parameters:
            df (pandas.DataFrame): Seabird data DataFrame
        """
        try:
            # Group by transect name and calculate total bird count
            transect_data = df.groupby('transect_name')['total_bird_count'].sum().sort_values(ascending=False)
            
            # Create the chart
            plt.figure(figsize=self.fig_size)
            bars = plt.bar(transect_data.index, transect_data.values, 
                          color=['#1f77b4', '#ff7f0e', '#2ca02c'])
            
            # Customize the chart
            plt.title('Bird Count Comparison by Transect', fontsize=16, fontweight='bold')
            plt.xlabel('Transect Name', fontsize=12)
            plt.ylabel('Total Bird Count', fontsize=12)
            plt.grid(axis='y', alpha=0.3)
            
            # Add value labels on bars
            for bar in bars:
                height = bar.get_height()
                plt.text(bar.get_x() + bar.get_width()/2., height,
                        f'{int(height):,}', ha='center', va='bottom', fontsize=11, fontweight='bold')
            
            plt.tight_layout()
            plt.show()
            
        except Exception as e:
            print(f"Error creating transect comparison chart: {e}")
    
    def create_custom_bar_chart(self, df, group_by, agg_method, title, y_label):
        """
        Creates a custom vertical bar chart based on user parameters.
        
        Parameters:
            df (pandas.DataFrame): Seabird data DataFrame
            group_by (str): Column to group by
            agg_method (str): Aggregation method ('sum', 'mean', 'max', 'count')
            title (str): Chart title
            y_label (str): Y-axis label
        """
        try:
            # Perform aggregation based on method
            if agg_method == 'sum':
                grouped_data = df.groupby(group_by)['total_bird_count'].sum()
            elif agg_method == 'mean':
                grouped_data = df.groupby(group_by)['total_bird_count'].mean()
            elif agg_method == 'max':
                grouped_data = df.groupby(group_by)['total_bird_count'].max()
            elif agg_method == 'count':
                grouped_data = df.groupby(group_by).size()
            else:
                grouped_data = df.groupby(group_by)['total_bird_count'].sum()
            
            # Sort by value for better visualization
            grouped_data = grouped_data.sort_values(ascending=False)
            
            # Create the chart
            plt.figure(figsize=self.fig_size)
            bars = plt.bar(grouped_data.index.astype(str), grouped_data.values, 
                          color=plt.cm.viridis(np.linspace(0, 1, len(grouped_data))))
            
            # Customize the chart
            plt.title(title, fontsize=16, fontweight='bold')
            plt.xlabel(group_by.replace('_', ' ').title(), fontsize=12)
            plt.ylabel(y_label, fontsize=12)
            plt.xticks(rotation=45)
            plt.grid(axis='y', alpha=0.3)
            
            # Add value labels on bars
            for bar in bars:
                height = bar.get_height()
                if agg_method == 'mean':
                    plt.text(bar.get_x() + bar.get_width()/2., height,
                            f'{height:.1f}', ha='center', va='bottom', fontsize=9)
                else:
                    plt.text(bar.get_x() + bar.get_width()/2., height,
                            f'{int(height):,}', ha='center', va='bottom', fontsize=9)
            
            plt.tight_layout()
            plt.show()
            
        except Exception as e:
            print(f"Error creating custom chart: {e}")