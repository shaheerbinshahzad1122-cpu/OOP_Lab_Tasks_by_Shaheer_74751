# Lab Task 6: MRI Scan intensity grid
class MRIGrid:
    def __init__(self, bme_rows, bme_cols):
        """
        Constructor for MRI Grid
        Creates a 2D grid of size rows × cols initialized with zeros
        """
        self.bme_rows = bme_rows
        self.bme_cols = bme_cols
        # Initialize 2D grid with zeros
        self.bme_grid = [[0 for _ in range(bme_cols)] for _ in range(bme_rows)]
    
    def fillGrid(self):
        """
        Populates the grid with intensity values entered by user
        Uses nested loops: rows (outer) × columns (inner)
        """
        print("\n" + "=" * 60)
        print("🖼️  MRI SCAN INTENSITY GRID INPUT")
        print("=" * 60)
        print("Intensity range: 0 (dark/air/fluid) to 255 (bright/bone/fat)")
        print("-" * 60)
        
        for bme_row in range(self.bme_rows):
            print(f"\n📊 Row {bme_row + 1} of {self.bme_rows}:")
            for bme_col in range(self.bme_cols):
                while True:  # Input validation loop
                    try:
                        bme_value = int(input(f"  Column {bme_col + 1}: "))
                        if bme_value < 0 or bme_value > 255:
                            print(f"    ⚠️  Invalid! Value must be between 0-255. Re-enter:")
                            continue
                        self.bme_grid[bme_row][bme_col] = bme_value
                        break
                    except ValueError:
                        print("    ⚠️  Invalid input! Please enter an integer.")
        
        print("\n✅ Grid filled successfully!")
        self._displayGrid()
    
    def _displayGrid(self):
        """Helper method to display the grid in a formatted way"""
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
                # Color-code based on tissue type
                if bme_val <= 85:
                    print(f" {bme_val:3d}🔘", end="")
                elif bme_val <= 170:
                    print(f" {bme_val:3d}◉ ", end="")
                else:
                    print(f" {bme_val:3d}⬤ ", end="")
            print(" |")
        print("-" * 60)
    
    def _classifyTissue(self, bme_intensity):
        """
        Classifies a single intensity value into tissue type
        Returns: string tissue type
        """
        if bme_intensity <= 85:
            return "Dark Tissue (Air/Fluid)"
        elif bme_intensity <= 170:
            return "Grey Tissue (Soft Tissue)"
        else:  # 171-255
            return "Bright Tissue (Bone/Fat)"
    
    def classifyPixels(self):
        """
        Iterates through all cells and:
        1. Classifies each pixel into tissue type
        2. Counts total occurrences of each tissue type
        3. Detects edge points (difference > 80 from left neighbour)
        """
        if not self.bme_grid:
            print("\n⚠️ No grid data found. Please fill the grid first.")
            return
        
        print("\n" + "=" * 60)
        print("🔬 MRI SCAN ANALYSIS - Pixel Classification")
        print("=" * 60)
        
        # Initialize counters for tissue types
        bme_dark_count = 0
        bme_grey_count = 0
        bme_bright_count = 0
        
        # Store edge points for display
        bme_edge_points = []
        
        # Nested loops to process each cell
        for bme_row in range(self.bme_rows):
            for bme_col in range(self.bme_cols):
                bme_intensity = self.bme_grid[bme_row][bme_col]
                
                # Classify tissue type and update counter
                bme_tissue = self._classifyTissue(bme_intensity)
                if bme_intensity <= 85:
                    bme_dark_count += 1
                elif bme_intensity <= 170:
                    bme_grey_count += 1
                else:
                    bme_bright_count += 1
                
                # Check for edge point (difference from left neighbour > 80)
                # Skip first column (col = 0) as it has no left neighbour
                if bme_col > 0:
                    bme_left_neighbour = self.bme_grid[bme_row][bme_col - 1]
                    bme_difference = abs(bme_intensity - bme_left_neighbour)
                    
                    if bme_difference > 80:
                        bme_edge_points.append({
                            'row': bme_row + 1,  # Convert to 1-indexed for display
                            'col': bme_col + 1,
                            'value': bme_intensity,
                            'left_value': bme_left_neighbour,
                            'difference': bme_difference
                        })
        
        # Display tissue type counts
        print("\n📊 TISSUE TYPE DISTRIBUTION:")
        print("-" * 50)
        print(f"  🟤 Dark Tissue (0-85):     {bme_dark_count:3d} pixels ({bme_dark_count * 100 // (self.bme_rows * self.bme_cols)}%)")
        print(f"  ⚪ Grey Tissue (86-170):   {bme_grey_count:3d} pixels ({bme_grey_count * 100 // (self.bme_rows * self.bme_cols)}%)")
        print(f"  ⬤ Bright Tissue (171-255): {bme_bright_count:3d} pixels ({bme_bright_count * 100 // (self.bme_rows * self.bme_cols)}%)")
        
        # Display tissue type legend
        print("\n📖 Tissue Type Legend:")
        print("  🔘 Dark Tissue (0-85)   → Air, Fluid, CSF")
        print("  ◉  Grey Tissue (86-170) → Muscle, Organs, Brain matter")
        print("  ⬤ Bright Tissue (171-255) → Bone, Fat, Contrast agent")
        
        # Display edge points
        print("\n" + "=" * 60)
        print("📍 EDGE DETECTION RESULTS")
        print("=" * 60)
        print("Edge points detected where intensity differs from left neighbour by >80 units")
        print("-" * 60)
        
        if bme_edge_points:
            print(f"\nFound {len(bme_edge_points)} edge point(s):")
            print(f"{'Row':<6} {'Col':<6} {'Intensity':<12} {'Left Value':<12} {'Difference':<12}")
            print("-" * 60)
            for bme_point in bme_edge_points:
                print(f"{bme_point['row']:<6} {bme_point['col']:<6} {bme_point['value']:<12} "
                      f"{bme_point['left_value']:<12} {bme_point['difference']:<12}")
                
                # Add visual indicator
                if bme_point['value'] > bme_point['left_value']:
                    print(f"      ↗️  Sharp increase (dark to bright transition)")
                else:
                    print(f"      ↘️  Sharp decrease (bright to dark transition)")
        else:
            print("\n  ✅ No edge points detected. Tissue boundaries are smooth.")
        
        # Additional analysis: Find regions of interest
        self._findRegionsOfInterest(bme_dark_count, bme_grey_count, bme_bright_count)
        
        print("\n" + "=" * 60)
        print("Analysis complete")
        print("=" * 60)
    
    def _findRegionsOfInterest(self, bme_dark, bme_grey, bme_bright):
        """Helper method to identify clinical regions of interest"""
        bme_total = self.bme_rows * self.bme_cols
        
        print("\n🎯 CLINICAL OBSERVATIONS:")
        print("-" * 50)
        
        if bme_bright > bme_total * 0.5:
            print("  ⚠️  >50% Bright Tissue detected: Possible dense bone structure or calcification")
        elif bme_dark > bme_total * 0.4:
            print("  📍 >40% Dark Tissue detected: Large fluid/air-filled regions present")
        
        if bme_grey > bme_total * 0.6:
            print("  ℹ️  Predominantly soft tissue - Typical for organ imaging")
        
        # Check for tissue heterogeneity
        if bme_dark > 0 and bme_bright > 0 and bme_grey > 0:
            print("  🔬 All three tissue types present - Heterogeneous tissue composition")
        
        # Quality check
        bme_very_low = sum(1 for row in self.bme_grid for val in row if val < 20)
        bme_very_high = sum(1 for row in self.bme_grid for val in row if val > 240)
        
        if bme_very_low > bme_total * 0.3:
            print("  ⚠️  Large very dark regions (<20) - Check for imaging artifact or air pockets")
        if bme_very_high > bme_total * 0.3:
            print("  ⚠️  Large very bright regions (>240) - Possible saturation or metal artifact")
    
    def setGridFromData(self, bme_data):
        """Helper method to set grid directly from data (for testing)"""
        if len(bme_data) == self.bme_rows and len(bme_data[0]) == self.bme_cols:
            self.bme_grid = bme_data
            print("\n📊 Test data loaded into grid")
            self._displayGrid()
        else:
            print("\n⚠️ Data dimensions don't match grid size!")


# Main program - Test the MRI Grid
print("🏥 MRI SCAN INTENSITY GRID ANALYSER")
print("Radiology Department - Tissue Classification System")
print("=" * 60)

# Choose input method
print("\nChoose input method:")
print("1. Enter intensity values manually")
print("2. Use demo data")
bme_choice = input("Enter choice (1 or 2): ")

if bme_choice == "1":
    bme_rows = int(input("\nEnter number of rows: "))
    bme_cols = int(input("Enter number of columns: "))
    
    bme_mri = MRIGrid(bme_rows, bme_cols)
    bme_mri.fillGrid()
    bme_mri.classifyPixels()

else:
    # Demo data covering all scenarios
    print("\n📊 Loading demo MRI scan data...")
    
    # Test Case 1: Smooth transition (no edges)
    print("\n" + "🎯" * 20)
    print("TEST CASE 1: Smooth Tissue Transition")
    print("🎯" * 20)
    bme_mri1 = MRIGrid(3, 4)
    bme_mri1.setGridFromData([
        [50, 55, 60, 65],   # Dark tissue region
        [100, 105, 110, 115],  # Grey tissue region
        [200, 205, 210, 215]   # Bright tissue region
    ])
    bme_mri1.classifyPixels()
    
    # Test Case 2: Multiple edges (sharp boundaries)
    print("\n" + "🎯" * 20)
    print("TEST CASE 2: Sharp Tissue Boundaries (Multiple Edges)")
    print("🎯" * 20)
    bme_mri2 = MRIGrid(4, 5)
    bme_mri2.setGridFromData([
        [30, 150, 30, 150, 30],    # Alternating dark/grey
        [200, 50, 200, 50, 200],    # Alternating bright/dark
        [80, 180, 80, 180, 80],     # Alternating grey/bright
        [240, 40, 240, 40, 240]     # Alternating bright/dark
    ])
    bme_mri2.classifyPixels()
    
    # Test Case 3: Predominantly one tissue type
    print("\n" + "🎯" * 20)
    print("TEST CASE 3: Homogeneous Tissue (Bone Scan)")
    print("🎯" * 20)
    bme_mri3 = MRIGrid(4, 4)
    bme_mri3.setGridFromData([
        [210, 215, 220, 218],
        [212, 220, 225, 222],
        [208, 218, 230, 225],
        [215, 220, 222, 228]
    ])
    bme_mri3.classifyPixels()
    
    # Test Case 4: Mixed with edges at boundaries
    print("\n" + "🎯" * 20)
    print("TEST CASE 4: Clinical MRI - Brain Scan Simulation")
    print("🎯" * 20)
    bme_mri4 = MRIGrid(5, 5)
    bme_mri4.setGridFromData([
        [20, 25, 30, 25, 20],    # CSF/Dark at edges
        [25, 150, 155, 150, 25],  # Grey matter
        [30, 155, 200, 155, 30],  # White matter
        [25, 150, 155, 150, 25],  # Grey matter
        [20, 25, 30, 25, 20]      # CSF/Dark at edges
    ])
    bme_mri4.classifyPixels()

print("\n" + "=" * 60)
print("MRI Analysis Complete")
print("=" * 60)