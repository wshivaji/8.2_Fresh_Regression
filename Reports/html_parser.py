from pathlib import Path

from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
# import pandas as pd
import os


def generate_summary_statistics(html_file_path):
    if not os.path.exists(html_file_path):
        print("Error: File not found.")
        return

    # Load HTML file
    with open(html_file_path, 'r') as file:
        html_content = file.read()

    soup = BeautifulSoup(html_content, 'html.parser')

    # Find the div with class="filter"
    filter_div = soup.find('div', class_='filters')
    color = ["#ff595e", "#ff924c", "#ffca3a", "#c5ca30", "#8ac926", "#52a675", "#1982c4", "#4267ac", "#6a4c93", "#b5a6c9"]
    # Extract the values from the div
    filter_values = {}
    for input_tag in filter_div.find_all('input', class_='filter'):
        value = input_tag.get('data-test-result')
        count_span = input_tag.find_next_sibling('span')
        count = int(count_span.text.split()[0])  # Extract the count value
        filter_values[value] = count

    # Calculate total count
    total_count = sum(filter_values.values())

    # Create a bar plot
    plt.figure(figsize=(8, 6))
    bars = plt.bar(filter_values.keys(), filter_values.values(), color=color)

    # Add percentages on top of each bar
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, height + 0.5, f'{height / total_count:.0%}', ha='center', fontsize=12)

    # Add labels and title
    plt.xlabel('Test Result', fontsize=14)
    plt.ylabel('Count', fontsize=14)
    plt.title('Summary Statistics', fontsize=16)

    # Customize ticks and grid
    plt.xticks(rotation=45, ha='right', fontsize=12)
    plt.yticks(fontsize=12)
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    # Save plot with the same name as the HTML file
    output_file_path = html_file_path.replace('.html', '_stats.png')
    plt.savefig(output_file_path)

    # Close plot
    plt.close()


file_path = f"{Path(__file__).parent}\\HTML_Reports\\p1_re-test_report_21_03_2024_08_07_41.html"
print(f"html file path: {file_path}")
generate_summary_statistics(file_path)
