# Lab Task 6: MRI Scan Intensity Grid with SQLite Database
import sqlite3
from datetime import datetime

class MRIGrid:
    def __init__(self, bme_rows, bme_cols, bme_scan_name="MRI_Scan"):
        """
        CONSTRUCTOR: Creates MRI grid with database
        """
        self.bme_rows = bme_rows
        self.bme_cols = bme_cols
        self.bme_scan_name = bme_scan_name
        self.bme_grid = [[0 for _ in range(bme_cols)] for _ in range(bme_rows)]
        
        # ========== DATABASE SETUP ==========
        self.bme_db_connection = sqlite3.connect('mri_database.db')
        self.bme_cursor = self.bme_db_connection.cursor()
        
        # Create MRI scans table
        self.bme_cursor.execute('''
            CREATE TABLE IF NOT EXISTS mri_scans (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                scan_name TEXT,
                rows INTEGER,
                cols INTEGER,
                created_at TIMESTAMP
            )
        ''')
        
        # Create pixel data table
        self.bme_cursor.execute('''
            CREATE TABLE IF NOT EXISTS mri_pixels (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                scan_id INTEGER,
                row_num INTEGER,
                col_num INTEGER,
                intensity INTEGER,
                tissue_type TEXT,
                FOREIGN KEY (scan_id) REFERENCES mri_scans (id)
            )
        ''')
        
        # Create analysis results table
        self.bme_cursor.execute('''
            CREATE TABLE IF NOT EXISTS mri_analysis (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                scan_id INTEGER,
                dark_count INTEGER,
                grey_count INTEGER,
                bright_count INTEGER,
                edge_count INTEGER,
                analysis_date TIMESTAMP,
                FOREIGN KEY (scan_id) REFERENCES mri_scans (id)
            )
        ''')
        
        # Register this scan
        self.bme_cursor.execute('''
            INSERT INTO mri_scans (scan_name, rows, cols, created_at)
            VALUES (?, ?, ?, ?)
        ''', (bme_scan_name, bme_rows, bme_cols, datetime.now()))
        
        self.bme_db_connection.commit()
        self.bme_scan_id = self.bme_cursor.lastrowid
        print(f"✅ MRI Database initialized - Scan ID: {self.bme_scan_id}")
    
    def fillGrid(self):
        """Populates grid and saves to database"""
        print("\n" + "=" * 60)
        print("🖼️  MRI SCAN INTENSITY GRID INPUT")
        print("=" * 60)
        print("Intensity range: 0 to 255")
        print("-" * 60)
        
        for bme_row in range(self.bme_rows):
            print(f"\n📊 Row {bme_row + 1}:")
            for bme_col in range(self.bme_cols):
                while True:
                    try:
                        bme_value = int(input(f"  Column {bme_col + 1}: "))
                        if bme_value < 0 or bme_value > 255:
                            print("    ⚠️  Value must be between 0-255.")
                            continue
                        self.bme_grid[bme_row][bme_col] = bme_value
                        
                        # Save pixel to database
                        tissue = self._classifyTissue(bme_value)
                        self.bme_cursor.execute('''
                            INSERT INTO mri_pixels (scan_id, row_num, col_num, intensity, tissue_type)
                            VALUES (?, ?, ?, ?, ?)
                        ''', (self.bme_scan_id, bme_row + 1, bme_col + 1, bme_value, tissue))
                        self.bme_db_connection.commit()
                        
                        break
                    except ValueError:
                        print("    ⚠️  Invalid input!")
        
        print("\n✅ Grid saved to database!")
        self._displayGrid()
    
    def _displayGrid(self):
        """Displays the grid"""
        print("\n📋 CURRENT MRI GRID:")
        print("-" * 60)
        print("     ", end="")
        for bme_c in range(self.bme_cols):
            print(f"C{bme_c+1:^6}", end="")
        print("\n" + " " * 5 + "-" * (6 * self.bme_cols))
        
        for bme_row in range(self.bme_rows):
            print(f"R{bme_row+1:<3} |", end="")
            for bme_col in range(self.bme_cols):
                bme_val = self.bme_grid[bme_row][bme_col]
                if bme_val <= 85:
                    print(f" {bme_val:3d}🔘", end="")
                elif bme_val <= 170:
                    print(f" {bme_val:3d}◉ ", end="")
                else:
                    print(f" {bme_val:3d}⬤ ", end="")
            print(" |")
        print("-" * 60)
    
    def _classifyTissue(self, bme_intensity):
        if bme_intensity <= 85:
            return "Dark Tissue"
        elif bme_intensity <= 170:
            return "Grey Tissue"
        else:
            return "Bright Tissue"
    
    def classifyPixels(self):
        """Classifies pixels and saves analysis to database"""
        if not self.bme_grid:
            print("\n⚠️ No grid data found.")
            return
        
        print("\n" + "=" * 60)
        print("🔬 MRI SCAN ANALYSIS")
        print("=" * 60)
        
        bme_dark_count = 0
        bme_grey_count = 0
        bme_bright_count = 0
        bme_edge_points = []
        
        for bme_row in range(self.bme_rows):
            for bme_col in range(self.bme_cols):
                bme_intensity = self.bme_grid[bme_row][bme_col]
                
                if bme_intensity <= 85:
                    bme_dark_count += 1
                elif bme_intensity <= 170:
                    bme_grey_count += 1
                else:
                    bme_bright_count += 1
                
                if bme_col > 0:
                    bme_left = self.bme_grid[bme_row][bme_col - 1]
                    if abs(bme_intensity - bme_left) > 80:
                        bme_edge_points.append({
                            'row': bme_row + 1, 'col': bme_col + 1,
                            'value': bme_intensity, 'left_value': bme_left
                        })
        
        print("\n📊 TISSUE TYPE DISTRIBUTION:")
        print("-" * 50)
        total = self.bme_rows * self.bme_cols
        print(f"  Dark Tissue:   {bme_dark_count:3d} pixels ({bme_dark_count*100//total}%)")
        print(f"  Grey Tissue:   {bme_grey_count:3d} pixels ({bme_grey_count*100//total}%)")
        print(f"  Bright Tissue: {bme_bright_count:3d} pixels ({bme_bright_count*100//total}%)")
        
        print("\n📍 EDGE DETECTION:")
        print("-" * 50)
        if bme_edge_points:
            print(f"Found {len(bme_edge_points)} edge point(s)")
            for ep in bme_edge_points[:5]:
                print(f"  Row {ep['row']}, Col {ep['col']}: {ep['left_value']} → {ep['value']}")
        else:
            print("  No edge points detected")
        
        # Save analysis to database
        self.bme_cursor.execute('''
            INSERT INTO mri_analysis (scan_id, dark_count, grey_count, bright_count, edge_count, analysis_date)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (self.bme_scan_id, bme_dark_count, bme_grey_count, bme_bright_count, 
              len(bme_edge_points), datetime.now()))
        self.bme_db_connection.commit()
        
        print("\n💾 Analysis saved to database!")
        print("=" * 60)
    
    def setGridFromData(self, bme_data):
        """Sets grid from data and saves to database"""
        self.bme_grid = bme_data
        print("\n📊 Test data loaded")
        
        # Save to database
        for row in range(self.bme_rows):
            for col in range(self.bme_cols):
                tissue = self._classifyTissue(self.bme_grid[row][col])
                self.bme_cursor.execute('''
                    INSERT INTO mri_pixels (scan_id, row_num, col_num, intensity, tissue_type)
                    VALUES (?, ?, ?, ?, ?)
                ''', (self.bme_scan_id, row + 1, col + 1, self.bme_grid[row][col], tissue))
        self.bme_db_connection.commit()
        
        self._displayGrid()
    
    def __del__(self):
        """DESTRUCTOR: Closes database connection"""
        if hasattr(self, 'bme_db_connection'):
            print(f"\n🗑️ Closing MRI database for {self.bme_scan_name}")
            self.bme_db_connection.close()
            print(f"   ✅ Database closed")


# Main program
print("🏥 MRI SCAN INTENSITY GRID ANALYSER WITH DATABASE")
print("=" * 60)

print("\n📊 Loading demo MRI scan data...")

# Test Case 1
print("\n" + "🎯" * 20)
print("TEST CASE 1: Smooth Tissue Transition")
print("🎯" * 20)
mri1 = MRIGrid(3, 4, "Smooth_Transition")
mri1.setGridFromData([
    [50, 55, 60, 65],
    [100, 105, 110, 115],
    [200, 205, 210, 215]
])
mri1.classifyPixels()

# Test Case 2
print("\n" + "🎯" * 20)
print("TEST CASE 2: Sharp Boundaries")
print("🎯" * 20)
mri2 = MRIGrid(4, 5, "Sharp_Boundaries")
mri2.setGridFromData([
    [30, 150, 30, 150, 30],
    [200, 50, 200, 50, 200],
    [80, 180, 80, 180, 80],
    [240, 40, 240, 40, 240]
])
mri2.classifyPixels()

print("\n✅ All MRI data saved to mri_database.db")
