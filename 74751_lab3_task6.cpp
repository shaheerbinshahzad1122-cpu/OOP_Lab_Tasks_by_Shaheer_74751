// Lab Task 6: MRI Scan intensity grid
#include <iostream>
#include <vector>
#include <string>
#include <iomanip>
#include <cmath>

using namespace std;

class MRIGrid {
private:
    int bme_rows;
    int bme_cols;
    vector<vector<int>> bme_grid;
    
    // Helper method to classify tissue type
    string classifyTissue(int bme_intensity) {
        if (bme_intensity <= 85) {
            return "Dark Tissue (Air/Fluid)";
        } else if (bme_intensity <= 170) {
            return "Grey Tissue (Soft Tissue)";
        } else {
            return "Bright Tissue (Bone/Fat)";
        }
    }
    
    // Helper method to display grid
    void displayGrid() {
        cout << "\n📋 CURRENT MRI GRID:" << endl;
        cout << "------------------------------------------------------------" << endl;
        cout << "     ";
        for (int bme_c = 0; bme_c < bme_cols; bme_c++) {
            cout << "C" << (bme_c + 1) << "    ";
        }
        cout << endl;
        cout << "     ";
        for (int bme_c = 0; bme_c < bme_cols; bme_c++) {
            cout << "-----";
        }
        cout << endl;
        
        for (int bme_row = 0; bme_row < bme_rows; bme_row++) {
            cout << "R" << (bme_row + 1) << "  |";
            for (int bme_col = 0; bme_col < bme_cols; bme_col++) {
                int bme_val = bme_grid[bme_row][bme_col];
                cout << setw(4) << bme_val << " ";
            }
            cout << "|" << endl;
        }
        cout << "------------------------------------------------------------" << endl;
    }
    
public:
    // Constructor
    MRIGrid(int rows, int cols) {
        bme_rows = rows;
        bme_cols = cols;
        bme_grid.assign(bme_rows, vector<int>(bme_cols, 0));
    }
    
    // Method to fill grid with user input
    void fillGrid() {
        cout << "\n============================================================" << endl;
        cout << "🖼️  MRI SCAN INTENSITY GRID INPUT" << endl;
        cout << "============================================================" << endl;
        cout << "Intensity range: 0 (dark/air/fluid) to 255 (bright/bone/fat)" << endl;
        cout << "------------------------------------------------------------" << endl;
        
        for (int bme_row = 0; bme_row < bme_rows; bme_row++) {
            cout << "\n📊 Row " << (bme_row + 1) << " of " << bme_rows << ":" << endl;
            for (int bme_col = 0; bme_col < bme_cols; bme_col++) {
                int bme_value;
                bool bme_valid = false;
                
                while (!bme_valid) {
                    cout << "  Column " << (bme_col + 1) << ": ";
                    cin >> bme_value;
                    
                    if (bme_value < 0 || bme_value > 255) {
                        cout << "    ⚠️  Invalid! Value must be between 0-255. Re-enter:" << endl;
                    } else {
                        bme_valid = true;
                        bme_grid[bme_row][bme_col] = bme_value;
                    }
                }
            }
        }
        
        cout << "\n✅ Grid filled successfully!" << endl;
        displayGrid();
    }
    
    // Method to set grid from existing data (for testing)
    void setGridFromData(vector<vector<int>> bme_data) {
        if (bme_data.size() == bme_rows && bme_data[0].size() == bme_cols) {
            bme_grid = bme_data;
            cout << "\n📊 Test data loaded into grid" << endl;
            displayGrid();
        } else {
            cout << "\n⚠️ Data dimensions don't match grid size!" << endl;
        }
    }
    
    // Method to classify pixels and detect edges
    void classifyPixels() {
        if (bme_grid.empty()) {
            cout << "\n⚠️ No grid data found. Please fill the grid first." << endl;
            return;
        }
        
        cout << "\n============================================================" << endl;
        cout << "🔬 MRI SCAN ANALYSIS - Pixel Classification" << endl;
        cout << "============================================================" << endl;
        
        // Initialize counters
        int bme_dark_count = 0;
        int bme_grey_count = 0;
        int bme_bright_count = 0;
        
        // Store edge points
        struct EdgePoint {
            int row;
            int col;
            int value;
            int left_value;
            int difference;
        };
        vector<EdgePoint> bme_edge_points;
        
        // Nested loops to process each cell
        for (int bme_row = 0; bme_row < bme_rows; bme_row++) {
            for (int bme_col = 0; bme_col < bme_cols; bme_col++) {
                int bme_intensity = bme_grid[bme_row][bme_col];
                
                // Classify and count tissue types
                if (bme_intensity <= 85) {
                    bme_dark_count++;
                } else if (bme_intensity <= 170) {
                    bme_grey_count++;
                } else {
                    bme_bright_count++;
                }
                
                // Check for edge point (skip first column)
                if (bme_col > 0) {
                    int bme_left_neighbour = bme_grid[bme_row][bme_col - 1];
                    int bme_difference = abs(bme_intensity - bme_left_neighbour);
                    
                    if (bme_difference > 80) {
                        EdgePoint bme_point;
                        bme_point.row = bme_row + 1;
                        bme_point.col = bme_col + 1;
                        bme_point.value = bme_intensity;
                        bme_point.left_value = bme_left_neighbour;
                        bme_point.difference = bme_difference;
                        bme_edge_points.push_back(bme_point);
                    }
                }
            }
        }
        
        // Display tissue type counts
        int bme_total = bme_rows * bme_cols;
        cout << "\n📊 TISSUE TYPE DISTRIBUTION:" << endl;
        cout << "--------------------------------------------------" << endl;
        cout << "  🟤 Dark Tissue (0-85):     " << bme_dark_count 
             << " pixels (" << (bme_dark_count * 100 / bme_total) << "%)" << endl;
        cout << "  ⚪ Grey Tissue (86-170):   " << bme_grey_count 
             << " pixels (" << (bme_grey_count * 100 / bme_total) << "%)" << endl;
        cout << "  ⬤ Bright Tissue (171-255): " << bme_bright_count 
             << " pixels (" << (bme_bright_count * 100 / bme_total) << "%)" << endl;
        
        // Display legend
        cout << "\n📖 Tissue Type Legend:" << endl;
        cout << "  🔘 Dark Tissue (0-85)   → Air, Fluid, CSF" << endl;
        cout << "  ◉  Grey Tissue (86-170) → Muscle, Organs, Brain matter" << endl;
        cout << "  ⬤ Bright Tissue (171-255) → Bone, Fat, Contrast agent" << endl;
        
        // Display edge points
        cout << "\n============================================================" << endl;
        cout << "📍 EDGE DETECTION RESULTS" << endl;
        cout << "============================================================" << endl;
        cout << "Edge points detected where intensity differs from left neighbour by >80 units" << endl;
        cout << "--------------------------------------------------" << endl;
        
        if (!bme_edge_points.empty()) {
            cout << "\nFound " << bme_edge_points.size() << " edge point(s):" << endl;
            cout << left << setw(6) << "Row" << setw(6) << "Col" 
                 << setw(12) << "Intensity" << setw(12) << "Left Value" 
                 << setw(12) << "Difference" << endl;
            cout << "--------------------------------------------------" << endl;
            
            for (const auto& bme_point : bme_edge_points) {
                cout << left << setw(6) << bme_point.row 
                     << setw(6) << bme_point.col
                     << setw(12) << bme_point.value
                     << setw(12) << bme_point.left_value
                     << setw(12) << bme_point.difference << endl;
                
                if (bme_point.value > bme_point.left_value) {
                    cout << "      ↗️  Sharp increase (dark to bright transition)" << endl;
                } else {
                    cout << "      ↘️  Sharp decrease (bright to dark transition)" << endl;
                }
            }
        } else {
            cout << "\n  ✅ No edge points detected. Tissue boundaries are smooth." << endl;
        }
        
        // Additional clinical observations
        findRegionsOfInterest(bme_dark_count, bme_grey_count, bme_bright_count);
        
        cout << "\n============================================================" << endl;
        cout << "Analysis complete" << endl;
        cout << "============================================================" << endl;
    }
    
    // Helper method for clinical observations
    void findRegionsOfInterest(int bme_dark, int bme_grey, int bme_bright) {
        int bme_total = bme_rows * bme_cols;
        
        cout << "\n🎯 CLINICAL OBSERVATIONS:" << endl;
        cout << "--------------------------------------------------" << endl;
        
        if (bme_bright > bme_total * 0.5) {
            cout << "  ⚠️  >50% Bright Tissue detected: Possible dense bone structure or calcification" << endl;
        } else if (bme_dark > bme_total * 0.4) {
            cout << "  📍 >40% Dark Tissue detected: Large fluid/air-filled regions present" << endl;
        }
        
        if (bme_grey > bme_total * 0.6) {
            cout << "  ℹ️  Predominantly soft tissue - Typical for organ imaging" << endl;
        }
        
        if (bme_dark > 0 && bme_bright > 0 && bme_grey > 0) {
            cout << "  🔬 All three tissue types present - Heterogeneous tissue composition" << endl;
        }
        
        // Count very low and very high values
        int bme_very_low = 0;
        int bme_very_high = 0;
        for (int bme_row = 0; bme_row < bme_rows; bme_row++) {
            for (int bme_col = 0; bme_col < bme_cols; bme_col++) {
                int bme_val = bme_grid[bme_row][bme_col];
                if (bme_val < 20) bme_very_low++;
                if (bme_val > 240) bme_very_high++;
            }
        }
        
        if (bme_very_low > bme_total * 0.3) {
            cout << "  ⚠️  Large very dark regions (<20) - Check for imaging artifact or air pockets" << endl;
        }
        if (bme_very_high > bme_total * 0.3) {
            cout << "  ⚠️  Large very bright regions (>240) - Possible saturation or metal artifact" << endl;
        }
    }
};

int main() {
    cout << "🏥 MRI SCAN INTENSITY GRID ANALYSER" << endl;
    cout << "Radiology Department - Tissue Classification System" << endl;
    cout << "============================================================" << endl;
    
    cout << "\nChoose input method:" << endl;
    cout << "1. Enter intensity values manually" << endl;
    cout << "2. Use demo data" << endl;
    cout << "Enter choice (1 or 2): ";
    
    int bme_choice;
    cin >> bme_choice;
    
    if (bme_choice == 1) {
        int bme_rows, bme_cols;
        cout << "\nEnter number of rows: ";
        cin >> bme_rows;
        cout << "Enter number of columns: ";
        cin >> bme_cols;
        
        MRIGrid bme_mri(bme_rows, bme_cols);
        bme_mri.fillGrid();
        bme_mri.classifyPixels();
    } else {
        // Demo data covering all scenarios
        cout << "\n📊 Loading demo MRI scan data..." << endl;
        
        // Test Case 1: Smooth transition (no edges)
        cout << "\n🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯" << endl;
        cout << "TEST CASE 1: Smooth Tissue Transition" << endl;
        cout << "🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯" << endl;
        MRIGrid bme_mri1(3, 4);
        bme_mri1.setGridFromData({
            {50, 55, 60, 65},
            {100, 105, 110, 115},
            {200, 205, 210, 215}
        });
        bme_mri1.classifyPixels();
        
        // Test Case 2: Multiple edges (sharp boundaries)
        cout << "\n🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯" << endl;
        cout << "TEST CASE 2: Sharp Tissue Boundaries (Multiple Edges)" << endl;
        cout << "🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯" << endl;
        MRIGrid bme_mri2(4, 5);
        bme_mri2.setGridFromData({
            {30, 150, 30, 150, 30},
            {200, 50, 200, 50, 200},
            {80, 180, 80, 180, 80},
            {240, 40, 240, 40, 240}
        });
        bme_mri2.classifyPixels();
        
        // Test Case 3: Predominantly one tissue type
        cout << "\n🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯" << endl;
        cout << "TEST CASE 3: Homogeneous Tissue (Bone Scan)" << endl;
        cout << "🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯" << endl;
        MRIGrid bme_mri3(4, 4);
        bme_mri3.setGridFromData({
            {210, 215, 220, 218},
            {212, 220, 225, 222},
            {208, 218, 230, 225},
            {215, 220, 222, 228}
        });
        bme_mri3.classifyPixels();
        
        // Test Case 4: Clinical MRI simulation
        cout << "\n🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯" << endl;
        cout << "TEST CASE 4: Clinical MRI - Brain Scan Simulation" << endl;
        cout << "🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯" << endl;
        MRIGrid bme_mri4(5, 5);
        bme_mri4.setGridFromData({
            {20, 25, 30, 25, 20},
            {25, 150, 155, 150, 25},
            {30, 155, 200, 155, 30},
            {25, 150, 155, 150, 25},
            {20, 25, 30, 25, 20}
        });
        bme_mri4.classifyPixels();
    }
    
    cout << "\n============================================================" << endl;
    cout << "MRI Analysis Complete" << endl;
    cout << "============================================================" << endl;
    
    return 0;
}