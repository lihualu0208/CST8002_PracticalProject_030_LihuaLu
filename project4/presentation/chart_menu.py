# presentation/chart_menu.py
"""
CST8002 - Practical Project Part 04
Professor: Stanley Pieda
Due Date: 2025-11-21
Author: Lihua Lu

This module handles the chart visualization menu and user interaction.
"""

import matplotlib.pyplot as plt
import pandas as pd
from business.chart_service import ChartService

class ChartMenu:
    """
    Handles the presentation layer for chart visualization features.
    """
    
    def __init__(self, seabird_service):
        """
        Initializes the chart menu with services.
        
        Parameters:
            seabird_service: The seabird service for data access
        """
        self.seabird_service = seabird_service
        self.chart_service = ChartService()
    
    def display_chart_menu(self):
        """Displays the chart visualization menu options."""
        print("\n=== CHART VISUALIZATION MENU ===")
        print("1. Species Count Bar Chart")
        print("2. Yearly Trends Bar Chart")
        print("3. Transect Comparison Chart")
        print("4. Custom Bar Chart")
        print("0. Back to Main Menu")
        print("-" * 40)
    
    def get_chart_dataframe(self):
        """
        Converts seabird records to pandas DataFrame for charting.
        
        Returns:
            pandas.DataFrame: DataFrame containing seabird data
        """
        records = self.seabird_service.get_all_records()
        if not records:
            print("No records available for charting.")
            return None
        
        # Convert records to dictionary format
        data = {
            'transect_number': [],
            'transect_name': [],
            'year': [],
            'species_code': [],
            'total_bird_count': [],
            'total_transect_distance': []
        }
        
        for record in records:
            data['transect_number'].append(record.transect_number)
            data['transect_name'].append(record.transect_name)
            data['year'].append(record.year)
            data['species_code'].append(record.species_code)
            data['total_bird_count'].append(record.total_bird_count)
            data['total_transect_distance'].append(record.total_transect_distance)
        
        return pd.DataFrame(data)
    
    def show_species_count_chart(self):
        """Displays bar chart of bird counts by species."""
        df = self.get_chart_dataframe()
        if df is None:
            return
        
        print("\nGenerating Species Count Bar Chart...")
        self.chart_service.create_species_count_chart(df)
        print("Chart displayed in separate window.")
    
    def show_yearly_trends_chart(self):
        """Displays bar chart of bird counts by year."""
        df = self.get_chart_dataframe()
        if df is None:
            return
        
        print("\nGenerating Yearly Trends Bar Chart...")
        self.chart_service.create_yearly_trends_chart(df)
        print("Chart displayed in separate window.")
    
    def show_transect_comparison_chart(self):
        """Displays bar chart comparing transects."""
        df = self.get_chart_dataframe()
        if df is None:
            return
        
        print("\nGenerating Transect Comparison Chart...")
        self.chart_service.create_transect_comparison_chart(df)
        print("Chart displayed in separate window.")
    
    def show_custom_chart(self):
        """Allows user to create custom bar chart with selected parameters."""
        df = self.get_chart_dataframe()
        if df is None:
            return
        
        print("\n=== CUSTOM BAR CHART ===")
        print("Available columns for grouping:")
        print("1. Species Code")
        print("2. Year")
        print("3. Transect Name")
        print("4. Transect Number")
        
        try:
            group_choice = input("Select grouping option (1-4): ").strip()
            
            if group_choice == "1":
                group_by = "species_code"
                title_suffix = "by Species"
            elif group_choice == "2":
                group_by = "year"
                title_suffix = "by Year"
            elif group_choice == "3":
                group_by = "transect_name"
                title_suffix = "by Transect Name"
            elif group_choice == "4":
                group_by = "transect_number"
                title_suffix = "by Transect Number"
            else:
                print("Invalid choice. Using default (Species).")
                group_by = "species_code"
                title_suffix = "by Species"
            
            print("\nAvailable aggregation methods:")
            print("1. Sum of bird counts")
            print("2. Average bird count")
            print("3. Maximum bird count")
            print("4. Count of records")
            
            agg_choice = input("Select aggregation method (1-4): ").strip()
            
            if agg_choice == "1":
                agg_method = "sum"
                y_label = "Total Bird Count"
            elif agg_choice == "2":
                agg_method = "mean"
                y_label = "Average Bird Count"
            elif agg_choice == "3":
                agg_method = "max"
                y_label = "Maximum Bird Count"
            elif agg_choice == "4":
                agg_method = "count"
                y_label = "Number of Records"
            else:
                print("Invalid choice. Using default (Sum).")
                agg_method = "sum"
                y_label = "Total Bird Count"
            
            chart_title = f"Seabird Data {title_suffix}"
            
            print(f"\nGenerating custom chart: {chart_title}")
            self.chart_service.create_custom_bar_chart(df, group_by, agg_method, chart_title, y_label)
            print("Custom chart displayed in separate window.")
            
        except Exception as e:
            print(f"Error creating custom chart: {e}")
    
    def run_chart_menu(self):
        """Runs the chart visualization menu system."""
        while True:
            self.display_chart_menu()
            choice = input("Enter your choice (0-4): ").strip()
            
            if choice == "0":
                break
            elif choice == "1":
                self.show_species_count_chart()
            elif choice == "2":
                self.show_yearly_trends_chart()
            elif choice == "3":
                self.show_transect_comparison_chart()
            elif choice == "4":
                self.show_custom_chart()
            else:
                print("Invalid choice. Please try again.")
            
            if choice != "0":
                input("\nPress Enter to continue...")