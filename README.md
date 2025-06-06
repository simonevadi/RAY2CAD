# RAY2CAD

**RAY2CAD** is a minimal pipeline to convert beamline geometry from a RAY tracing `.rml` file into a 3D visualization in FreeCAD.

## Prerequisites

- Python with [`raypyng`](https://raypyng.readthedocs.io/en/latest/) installed  
- FreeCAD

## Usage

### Step 1: Extract beamline positions

Run the following from the root of the project to convert the `.rml` file to JSON:

```bash
python extract_beamline.py
```

This will read `sotexs/sotexs.rml` and create `sotexs/sotexs.json` with the absolute positions of each beamline element.

### Step 2: Visualize in FreeCAD

Open FreeCAD, go to `Macro` → `Macros…`, and run `draw_cad.FCMacro`.

This will:
- Create a 3D model of the beamline
- Place red spheres at each beamline element
- Draw a polyline showing the beam path
- Save the `.FCStd` file under `sotexs/sotexs.FCStd`

## Notes

- All dimensions are assumed to be in millimeters.
- The beamline elements are visualized as cubes or spheres for simplicity.
- The script assumes the first element is the source and centers it visually.

## License

This project is provided under the terms of the MIT License.
