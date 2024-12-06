########1########
•  Workspace Setup
Connect Data: Open Tableau → Connect → Text File → Select vgsales.csv.
Data Preview: Check data, rename columns if needed → Click Sheet 1.
•  Key Terminologies
Dimensions: Qualitative fields (e.g., Platform, Genre).
Measures: Quantitative fields (e.g., Global_Sales).
Rows/Columns Shelf: Structure visualization by dragging fields.
Marks: Style data (e.g., bar, color, size).
Filters: Limit displayed data.
Pages Shelf: Create animations or segmented views.
•  Basic Functions
Bar Chart:
Drag Genre to Columns; Global_Sales to Rows.
Right-click Global_Sales → Measure → Sum.
Sort axis descending.
Filtering: Drag Year to Filters; choose range (e.g., 2000–2016).
Animation: Add Year to Pages for time-based views.
•  Advanced
Line Chart: Drag Year to Columns, Global_Sales to Rows → Add Genre (color).
Dashboard:
Open Dashboard tab → Add Bar & Line Chart.
Set Size → Automatic → Arrange charts
.
########2##########

Tableau Quick Steps
Setup
Connect: Open Tableau → Connect → Text File → vgsales.csv.
Preview: Rename columns if needed → Click Sheet 1.
Terms
Dimensions: Qualitative (e.g., Genre, Platform).
Measures: Quantitative (e.g., Global_Sales).
Rows/Columns: Drag fields to structure visuals.
Marks: Adjust style (e.g., bar, color).
Filters: Limit displayed data.
Pages: For animations or categories.
Basic Visuals
Bar Chart:
Drag Genre to Columns; Global_Sales to Rows.
Aggregate: Right-click Global_Sales → Measure → Sum.
Sort: Descend Global_Sales axis.
Filters: Drag Year to Filters; set range (e.g., 2000–2016).
Animation: Add Year to Pages.
Advanced
Line Chart: Drag Year to Columns, Global_Sales to Rows → Add Genre (color).
Dashboard: Add Bar & Line Charts → Set size → Arrange.



########3##########

Tableau Cheat Sheet
Setup
Open Tableau → Connect → Text File → vgsales.csv.
Preview & rename columns → Click Sheet 1.
Key Terms
Dimensions: Qualitative (e.g., Genre, Platform).
Measures: Quantitative (e.g., Global_Sales).
Rows/Columns: Organize visuals.
Marks: Style (e.g., bar, color).
Filters: Limit data.
Pages: For animations.
Basic Visuals
Bar Chart: Drag Genre (Columns), Global_Sales (Rows) → Sum → Sort descending.
Filters: Drag Year → Set range (2000–2016).
Animation: Add Year to Pages.
Advanced
Line Chart: Drag Year (Columns), Global_Sales (Rows) → Add Genre (color).
Dashboard: Add Bar & Line Charts → Auto-size → Arrange.

########4#########
Tableau Story & Dashboard Guide
Step 1: Create a Story
New Story: Click New Story at the bottom right.
Add Sheets: Drag Sheet 1 & Sheet 2 to the "Drag a sheet here" section.
Rename Sheet 1: "Provincial Health Expenditure in 2016."
Rename Sheet 2: "Provincial Health Expenditure from 1975-2018."
Highlight Ontario:
Drag another copy of Sheet 1 → Rename it "Ontario."
Click Ontario on the map → Select Update.
Navigate & Update:
Click right arrow → Hover Ontario line in Sheet 2 → Highlight 2016 data → Click Update.
Add Textbox: Drag "Drag to add text" to the graph → Add:
"Ontario had the highest health expenditure in Canada in 2016, spending $87,195.70M."
Step 2: Publish & Save
Save to Tableau Public: File → Save to Tableau Public As...
Step 3: Create a Dashboard
New Dashboard: Click the Dashboard tab.
Add Sheets: Drag Sheet 1 (map) & Sheet 2 (line graph) to the center.
Edit Titles: Double-click titles → Rename them:
Example: "Canada Health Expenditure" (map) and "Provincial Health Expenditure by Year" (line graph).
Add Elements: Drag Text or Image from Objects panel → Add captions/titles.
Interactive Filters: Click line graph → Enable filter icon → Clicking a line updates the map.
Step 4: Finalize Dashboard
Adjust Layout: Align sheets; ensure space for titles and features.
Test Filters: Ensure interactivity works.
Save/Publish: Save or publish your interactive dashboard to Tableau Public.


########6##########
Power BI: Querying and Transforming Data
Step 1: Open Power BI Desktop
Launch Power BI → Open a blank report.
Step 2: Connect to Data Source
Go to Home → Get Data → Excel Workbook.
Select your Excel/CSV file in the Navigator.
Load: Import data directly.
Transform Data: Open Power Query Editor to clean/modify data.
Step 3: Transform Data in Power Query Editor
Rename Columns: Right-click column header → Rename.
Change Data Types: Highlight column → Home tab → Data Type → Select type.
Remove Rows: Home → Reduce Rows → Remove Rows → Specify rows.
Remove Columns: Select columns → Right-click → Remove Columns.
Applied Steps Panel: View, reorder, rename, or delete transformations.
Step 4: Apply Changes
Click Close & Apply to load transformed data into Power BI Desktop.
Step 5: Create Reports
Use Report View:
Drag fields onto Canvas.
Select chart types from Visualizations pane.
Customize visuals using Format pane.
Filters: Refine displayed data.
Step 6: Save Work
Save as .pbix for future use




def forward_chaining(rules,facts,goal):
    inferred_facts=set(facts)
    new_facts=True
    while new_facts:
        new_facts=False
        for condition,result in rules:
            if all(cond in inferred_facts for cond in condition) and result not in inferred_facts:
                inferred_facts.add(result)
                new_facts=True
            if result==goal:
                return True
    return False
def backward_chaining(rules,facts,goal):
    def ask(query):
        if query in facts:
            return True
        for condition,result in rules:
            if result==query and all(ask(cond) for cond in condition):
                return True
        return False
    return ask(goal)
rules=[(['hair','live young'],'mammal'),(['feathers','fly'],'bird')]
facts=['hair','live young']
goal='mammal'
is_mammal=forward_chaining(rules,facts,goal)
if is_mammal:
    print("The cat is classified as a mammal.")
else:
    print("The cat is not classified as a mammal.")
facts=['feathers','fly']
goal='bird'
is_bird=backward_chaining(rules,facts,goal)
if is_bird:
    print("The pigeon is classified as a bird.")
else:
    print("The pigeon is not classified as a bird.")