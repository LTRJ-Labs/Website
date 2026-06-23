# Walkthrough — Latest Changes

## 1. Project Cost Estimator Removal

- **[MODIFY] [contact/index.html](file:///c:/Users/ryan2/Documents/GitHub/Website/contact/index.html)**: Removed all estimator HTML, JS logic, and meta tag references.
- **[MODIFY] [agency.css](file:///c:/Users/ryan2/Documents/GitHub/Website/css/agency.css)**: Removed ~150 lines of `.estimator-*` CSS rules.
- **Commit**: `4762c3d`

## 2. Water Tank Page Navbar Fix

- **[MODIFY] [portfolio/watertank/index.html](file:///c:/Users/ryan2/Documents/GitHub/Website/portfolio/watertank/index.html)**: Changed navbar `container-fluid` to `container` to match site-wide layout.
- **Commit**: `4762c3d` (same commit as above)

---

## 3. Interactive 3D PCB Assembly Viewer & CAD Orientation Tools

### What Was Built & Optimized

- **[NEW] [viewer.html](file:///c:/Users/ryan2/Documents/GitHub/Website/portfolio/watertank/viewer.html)**: A self-contained React Three Fiber 3D viewer page.
- **[NEW] [RemoteTankMonitoring-Enclosure+TankMountMainBoard.gltf](file:///c:/Users/ryan2/Documents/GitHub/Website/img/RemoteTankMonitoring-Enclosure+TankMountMainBoard.gltf)**: 3D model geometry.
- **[NEW] [RemoteTankMonitoring-Enclosure+TankMountMainBoard.bin](file:///c:/Users/ryan2/Documents/GitHub/Website/img/RemoteTankMonitoring-Enclosure+TankMountMainBoard.bin)**: 3D model binary data.

### Technical Approach

Since Node.js is not installed on this machine, the viewer uses **ESM import maps** to load React, React Three Fiber, @react-three/drei, lucide-react, and Three.js directly from `esm.sh` CDN. Tailwind CSS is loaded from the CDN as well. This makes the page fully self-contained — no build step needed.

### Features & Performance Optimizations

| Feature / Optimization | Description |
|---|---|
| **On-Demand Rendering** | Configured the Canvas with `frameloop="demand"`. Renders are now only scheduled when the camera changes (OrbitControls fires `change`), when the slider is modified, or when auto-rotate is active, dropping GPU usage to 0% when idle. |
| **Cap Device Pixel Ratio** | Capped DPR at 2 (`renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2))`) in the canvas context to prevent performance bottlenecks on 4K/high-density screens. |
| **Draco Decoder Path** | Set globally using `useGLTF.setDecoderPath(...)`. This downloads the Google Draco decoder scripts *only on-demand* (if the GLTF model contains compressed geometry), optimizing load time. |
| **Strictly Vertical Explode** | Fixed the coordinate rotation issue where components drifted sideways when exploded. By transforming the parent-space vertical Y-axis `(0, 1, 0)` into each child's local coordinate system (using inverted child quaternions), all meshes now separate **strictly straight up**. |
| **Trace Floating Layer** | Separated the copper traces and solder pads (`SOLID` meshes with 1,937 primitives) into their own floating layer that separates at `offsetMag: 0.001` (between the PCB substrate at 0 and the passives at 0.002). |
| **Translucent Substrate** | PCB substrate meshes (`RemoteTankMonitoring_PCB` and `body_4`) dynamically transition to `opacity: 0.45` and `transparent: true` when `explodeFactor > 0`. This reveals the internal planes and traces as they separate, returning to opaque when closed. |
| **Default Top-Down View** | Initial camera position starts straight down from the top `(0.01, 1.5, 0.01)` to look directly at the board layout on page load. |
| **Interactive CAD View Cube** | Integrated Drei's `<GizmoViewcube>` in the bottom-right corner. It is synchronized with the camera and allows clicking faces, edges, or corners to smoothly align the perspective. |
| **90° Rotation D-pad** | Overlaid a glassmorphic D-pad controller (Up, Down, Left, Right, Home) above the View Cube to rotate the camera exactly 90 degrees (around world Y for horizontal, or camera local X for vertical) using a smooth custom 250ms ease-InOutQuad animation. |
| **Exploded View Slider** | Custom-styled range slider that separates layers vertically along the local Y-axis of the model. |
| **Component Classification** | 108 GLTF nodes classified into 6 logical groups: Enclosure, Connectors, ICs & Modules, Passives, Traces & Solder, PCB Board |
| **Layer Legend** | Color-coded legend panel showing which group is which |
| **Auto-Rotate Toggle** | Button to enable/disable slow automatic model rotation |
| **Reset Button** | Returns the slider to 0% and collapses the exploded view |
| **Glassmorphism UI** | Frosted glass panels with `backdrop-filter: blur(16px)` for a premium look |

### Component Group Classification

The 108 GLTF nodes are classified by name prefix into:

| Group | Offset Magnitude | Example Nodes |
|---|---|---|
| **Enclosure** | `0.006` | `FRAME`, `.step 1.47.1` |
| **Connectors** | `0.004` | `DB301V`, `SIM8051`, `TYPE-C`, `JST_PH2.0`, `DSJ0014A` |
| **ICs & Modules** | `0.003` | `ESP32-C3-WROOM`, `INA219`, `lr62xe`, `SOT23-*` |
| **Passives** | `0.002` | `res_*`, `ceramic_cap_*`, `DO-214*`, `led_*`, `25ZLH*` |
| **Traces & Solder** | `0.001` | `SOLID` (1,937 primitives), `SOLID001` to `SOLID015` |
| **PCB Board** | `0` (anchor) | `RemoteTankMonitoring_PCB`, `body_4` |

### Integration

- **[MODIFY] [portfolio/watertank/index.html](file:///c:/Users/ryan2/Documents/GitHub/Website/portfolio/watertank/index.html)**: Placed the small styled "3D View" button inline with the "Project Overview" heading on the right.
- **Commits**: `fde2138`, `990f439`, `ca25bb8`, `12d279b`, `0fc77c2`, `5b4f8ac`, `5815c04`

### Verification

> [!IMPORTANT]
> The viewer requires an HTTP server to function (CORS restrictions prevent GLTF loading from `file://`). It will work on the live site at `www.ltrjlabs.com` after pushing to GitHub Pages, or from any local HTTP server.

### How to Test Locally

If you install Node.js or Python, you can test locally:
```bash
# Python
python -m http.server 8000

# Node.js  
npx serve .
```
Then open `http://localhost:8000/portfolio/watertank/viewer.html`.
