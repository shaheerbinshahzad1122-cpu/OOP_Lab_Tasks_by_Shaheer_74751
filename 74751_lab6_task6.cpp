// Lab Task 6: MRI Scan Intensity Grid with Destructors
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
    string bme_scan_name;
    vector<vector<int>> bme_grid;
    int bme_scan_id;
    static int bme_next_id;
    
    string classifyTissue(int intensity) {
        if (intensity <= 85) return "Dark Tissue (Air/Fluid)";
        else if (intensity <= 170) return "Grey Tissue (Soft Tissue)";
        else return "Bright Tissue (Bone/Fat)";
    }
    
    void displayGrid() {
        cout << "\nCURRENT MRI GRID:" << endl;
        cout << "------------------------------------------------------------" << endl;
        cout << "     ";
        for (int c = 0; c < bme_cols; c++) {
            cout << "C" << (c+1) << "    ";
        }
        cout << endl;
        cout << "     ";
        for (int c = 0; c < bme_cols; c++) {
            cout << "-----";
        }
        cout << endl;
        
        for (int r = 0; r < bme_rows; r++) {
            cout << "R" << (r+1) << "  |";
            for (int c = 0; c < bme_cols; c++) {
                int val = bme_grid[r][c];
                if (val <= 85) {
                    cout << " " << setw(3) << val << "x";
                } else if (val <= 170) {
                    cout << " " << setw(3) << val << "x";
                } else {
                    cout << " " << setw(3) << val << "x";
                }
            }
            cout << " |" << endl;
        }
        cout << "------------------------------------------------------------" << endl;
    }
    
public:
    // Constructor
    MRIGrid(int rows, int cols, string scan_name = "MRI_Scan") {
        bme_rows = rows;
        bme_cols = cols;
        bme_scan_name = scan_name;
        bme_grid.assign(bme_rows, vector<int>(bme_cols, 0));
        bme_scan_id = bme_next_id++;
        
        cout << "MRI Scan '" << bme_scan_name << "' created (ID: " << bme_scan_id << ")" << endl;
    }
    
    // Method to set grid from data
    void setGridFromData(vector<vector<int>> data) {
        bme_grid = data;
        displayGrid();
        cout << "Grid data loaded" << endl;
    }
    
    // Method to classify pixels and detect edges
    void classifyPixels() {
        if (bme_grid.empty()) {
            cout << "\nNo grid data found." << endl;
            return;
        }
        
        cout << "\n============================================================" << endl;
        cout << "MRI SCAN ANALYSIS - Pixel Classification" << endl;
        cout << "============================================================" << endl;
        
        int dark = 0, grey = 0, bright = 0;
        vector<tuple<int, int, int, int>> edges;
        
        for (int r = 0; r < bme_rows; r++) {
            for (int c = 0; c < bme_cols; c++) {
                int val = bme_grid[r][c];
                if (val <= 85) dark++;
                else if (val <= 170) grey++;
                else bright++;
                
                // Check for edge point (skip first column)
                if (c > 0) {
                    int left = bme_grid[r][c-1];
                    int diff = abs(val - left);
                    if (diff > 80) {
                        edges.push_back({r+1, c+1, val, left});
                    }
                }
            }
        }
        
        int total = bme_rows * bme_cols;
        cout << "\nTISSUE TYPE DISTRIBUTION:" << endl;
        cout << "--------------------------------------------------" << endl;
        cout << "Dark Tissue (0-85):     " << dark << " pixels (" << (dark * 100 / total) << "%)" << endl;
        cout << "Grey Tissue (86-170):   " << grey << " pixels (" << (grey * 100 / total) << "%)" << endl;
        cout << "Bright Tissue (171-255): " << bright << " pixels (" << (bright * 100 / total) << "%)" << endl;
        
        cout << "\nTissue Type Legend:" << endl;
        cout << "Dark Tissue (0-85)   → Air, Fluid, CSF" << endl;
        cout << "Grey Tissue (86-170) → Muscle, Organs, Brain matter" << endl;
        cout << "Bright Tissue (171-255) → Bone, Fat, Contrast agent" << endl;
        
        cout << "\n============================================================" << endl;
        cout << "EDGE DETECTION RESULTS" << endl;
        cout << "============================================================" << endl;
        cout << "Edge points detected where intensity differs from left neighbour by >80 units" << endl;
        cout << "--------------------------------------------------" << endl;
        
        if (!edges.empty()) {
            cout << "\nFound " << edges.size() << " edge point(s):" << endl;
            cout << left << setw(6) << "Row" << setw(6) << "Col" 
                 << setw(12) << "Intensity" << setw(12) << "Left Value" 
                 << setw(12) << "Difference" << endl;
            cout << "--------------------------------------------------" << endl;
            
            for (size_t i = 0; i < min(edges.size(), size_t(10)); i++) {
                auto [row, col, val, left] = edges[i];
                cout << left << setw(6) << row << setw(6) << col
                     << setw(12) << val << setw(12) << left
                     << setw(12) << abs(val - left) << endl;
                
                if (val > left) {
                    cout << " Sharp increase (dark to bright transition)" << endl;
                } else {
                    cout << " Sharp decrease (bright to dark transition)" << endl;
                }
            }
        } else {
            cout << "\n No edge points detected. Tissue boundaries are smooth." << endl;
        }
        
        // Clinical observations
        cout << "\nCLINICAL OBSERVATIONS:" << endl;
        cout << "--------------------------------------------------" << endl;
        
        if (bright > total * 0.5) {
            cout << " >50% Bright Tissue detected: Possible dense bone structure" << endl;
        } else if (dark > total * 0.4) {
            cout << ">40% Dark Tissue detected: Large fluid/air-filled regions present" << endl;
        }
        
        if (grey > total * 0.6) {
            cout << "Predominantly soft tissue - Typical for organ imaging" << endl;
        }
        
        if (dark > 0 && bright > 0 && grey > 0) {
            cout << "All three tissue types present - Heterogeneous tissue composition" << endl;
        }
        
        cout << "\nAnalysis complete" << endl;
        cout << "============================================================" << endl;
    }
    
    // DESTRUCTOR
    ~MRIGrid() {
        cout << "\nDESTRUCTOR: MRI Scan " << bme_scan_id << " ('" << bme_scan_name << "') is being destroyed" << endl;
    }
};

int MRIGrid::bme_next_id = 1;

int main() {
    cout << "MRI SCAN INTENSITY GRID ANALYSER" << endl;
    cout << "Radiology Department - Tissue Classification System" << endl;
    cout << "============================================================" << endl;
    
    // Test Case 1: Smooth transition
    cout << "\n============================================================" << endl;
    cout << "TEST CASE 1: Smooth Tissue Transition" << endl;
    cout << "============================================================" << endl;
    MRIGrid mri1(3, 4, "Smooth_Transition");
    mri1.setGridFromData({
        {50, 55, 60, 65},
        {100, 105, 110, 115},
        {200, 205, 210, 215}
    });
    mri1.classifyPixels();
    
    // Test Case 2: Sharp boundaries
    cout << "\n============================================================" << endl;
    cout << "TEST CASE 2: Sharp Tissue Boundaries (Multiple Edges)" << endl;
    cout << "============================================================" << endl;
    MRIGrid mri2(4, 5, "Sharp_Boundaries");
    mri2.setGridFromData({
        {30, 150, 30, 150, 30},
        {200, 50, 200, 50, 200},
        {80, 180, 80, 180, 80},
        {240, 40, 240, 40, 240}
    });
    mri2.classifyPixels();
    
    // Test Case 3: Homogeneous bone scan
    cout << "\n============================================================" << endl;
    cout << "TEST CASE 3: Homogeneous Tissue (Bone Scan)" << endl;
    cout << "============================================================" << endl;
    MRIGrid mri3(4, 4, "Bone_Scan");
    mri3.setGridFromData({
        {210, 215, 220, 218},
        {212, 220, 225, 222},
        {208, 218, 230, 225},
        {215, 220, 222, 228}
    });
    mri3.classifyPixels();
    
    // Test Case 4: Brain scan simulation
    cout << "\n============================================================" << endl;
    cout << "TEST CASE 4: Clinical MRI - Brain Scan Simulation" << endl;
    cout << "============================================================" << endl;
    MRIGrid mri4(5, 5, "Brain_Scan");
    mri4.setGridFromData({
        {20, 25, 30, 25, 20},
        {25, 150, 155, 150, 25},
        {30, 155, 200, 155, 30},
        {25, 150, 155, 150, 25},
        {20, 25, 30, 25, 20}
    });
    mri4.classifyPixels();
    
    cout << "\nProgram ending - Destructors will be called automatically!" << endl;
    
    return 0;
}
