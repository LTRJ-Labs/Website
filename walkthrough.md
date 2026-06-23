# Walkthrough — Latest Changes

## 1. Project Cost Estimator Removal

- **[MODIFY] [contact/index.html](file:///c:/Users/ryan2/Documents/GitHub/Website/contact/index.html)**: Removed all estimator HTML, JS logic, and meta tag references.
- **[MODIFY] [agency.css](file:///c:/Users/ryan2/Documents/GitHub/Website/css/agency.css)**: Removed ~150 lines of `.estimator-*` CSS rules.
- **Commit**: `4762c3d`

## 2. Water Tank Page Navbar Fix

- **[MODIFY] [portfolio/watertank/index.html](file:///c:/Users/ryan2/Documents/GitHub/Website/portfolio/watertank/index.html)**: Changed navbar `container-fluid` to `container` to match site-wide layout.
- **Commit**: `4762c3d` (same commit as above)

---

## 3. Interactive 3D PCB Assembly Viewer & Rendering Pipeline Optimizations

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
| **Single-Pass Position Update** | Replaced the laggy loop of 99 individual `useFrame` callbacks with a single `useEffect` hook that updates the Y-offset positions of all meshes in a single batch whenever the slider changes. |
| **Theme Synchronization** | Integrated a theme switcher button that syncs with `localStorage.getItem('theme')` (used by `js/theme.js`). Toggling theme dynamically switches the canvas background, lights, glass panels, slider, and buttons between light and dark modes. |
| **Exploded View Slider** | Custom-styled range slider that separates layers vertically along the local Y-axis of the model. |
| **Component Classification** | 108 GLTF nodes classified into 5 logical groups: Enclosure, Connectors, ICs & Modules, Passives, PCB Board |
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
| **PCB Board** | `0` (anchor) | `RemoteTankMonitoring_PCB`, `MainBoard`, `SOLID*` |

### Integration

- **[MODIFY] [portfolio/watertank/index.html](file:///c:/Users/ryan2/Documents/GitHub/Website/portfolio/watertank/index.html)**: Added an "Interactive 3D Assembly" section with a styled "Launch 3D Viewer" button that opens `viewer.html`.
- **Commits**: `fde2138`, `990f439`, `ca25bb8`, `12d279b`

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
