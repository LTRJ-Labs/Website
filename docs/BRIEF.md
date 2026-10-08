# TASK: Build the Single-Page LTRJ Labs Website (ltrjlabs.com)

You are tasked with redesigning and building a clean, modern, single-page website for **LTRJ Labs Ltd.** (an independent hard-tech startup based in Victoria, BC).

The goal of this site is not to sell client services (LTRJ Labs does not take consulting work). Instead, it serves as the company's "R&D Lab / Skunkworks Forge": projecting the company's vision, core values, technical pedigree, and hardware history, while serving as a high-priority springboard/funnel to its flagship product, **MothNode**.

---

## 1. Aesthetic Direction: "Ethereal Hard-Tech"
Merge deep industrial engineering with an ethereal, luminous aesthetic:
* **Background Canvas:** Deep, atmospheric obsidian / near-black (`#08080a`, `#0d0d11`).
* **Brand Colors & Ethereal Glows:** 
  * Primary Accent: LTRJ Labs Safety Orange (`#FF6600` / `#FF7A1A`).
  * Atmospheric Lighting: Soft, diffused radial ambient glows (`rgba(255, 102, 0, 0.08)` to `0.15`), giving the impression of glowing vacuum tubes, distant telemetry beacons, or amber photons behind frosted glass.
* **Surfaces & Cards:** Dark translucent glassmorphic containers (`bg-zinc-900/40`, `backdrop-blur-md`) with ultra-fine, hairline borders (`border border-white/5` or `border-orange-500/20` on hover).
* **Typography:**
  * Headers & Body: Clean, modern sans-serif (`Inter`, `Geist`, or `Montserrat`).
  * Technical Specs, Timestamps & Labels: Crisp monospace (`JetBrains Mono`, `SF Mono`, or `Space Mono`) for a lab instrument / field-notebook feel.
* **Tone:** Grounded, authentic, self-assured. Avoid generic SaaS cartoon illustrations or corporate clichés. Show real hardware, schematics, and raw bench progress.

---

## 2. Core Copy & Messaging (Must Use Exact Text)

### Hero Manifesto:
* **Tagline / Headline:** 
  > A hard-tech startup building IoT products.
* **Body / Vision Statement:**
  > We envision IoT infrastructure that feels completely custom, yet deploys at scale across industries. A system that advances operations, builds community, and is always online. Regardless of the project, we design with a focus on this vision.
* **Primary Funnel Action (Hero Button):**
  > `[ Explore Flagship System: MothNode ↗ ]` (High-contrast, luminous orange CTA linking to the product site).

---

## 3. Page Structure & Section Flow (Single-Page Layout)

Keep the page sleek, uncluttered, and punchy. The user should be able to scroll through the entire story in 60 seconds:

### A. Navigation Bar (Floating & Frosted)
* Left: LTRJ Labs SVG logo (`img/SVGLogos/Full_Logo.svg`).
* Center/Right: Jump links (`Flagship`, `Principles`, `Timeline`, `Events`, `Contact`).
* Right Accent: A glowing status pill: `● MOTHNODE R3 IN TESTING` or a direct link: `Visit MothNode →`.

### B. Hero Section (The Manifesto & Immediate Product Exit)
* Ambient ethereal orange light gradient behind the headline.
* Display the Tagline and Vision statement with refined typography.
* Prominent CTA button directing accidental product visitors straight to MothNode.

### C. Flagship Showcase: MothNode
* High-visibility card highlighting MothNode as LTRJ Labs' first deployed system.
* **Visual:** High-resolution hardware photography (e.g. `img/MothNodePhoto1.jpg` or PCBA bench photos).
* **Story & Architecture Summary:** 
  * "Born out of volunteer firefighting at Willis Point, BC to solve critical off-grid water supply monitoring."
  * "Zero-maintenance, solar-powered, multi-network telemetry (Cellular, LoRa, Bluetooth). Runs year-round in extreme Canadian weather."
* **Direct Link Button:** `Launch MothNode Platform →`.

### D. Core Principles ("How We Build")
A 3-column or 4-column minimal grid highlighting why LTRJ Labs is different:
1. **High-Velocity Iteration:** Fast-moving execution from breadboard rev 1 to custom fab and compliance testing in months, not years.
2. **Bespoke Feel, Global Scale:** Hardware designed with deep domain empathy that feels purpose-built for the operator, built on a robust architecture that deploys everywhere.
3. **Resilient & Local-First:** Solar-harvesting, fault-tolerant systems designed to run 24/7—even when the cloud goes dark.
4. **Proprietary Focus:** No agency work, no billable consulting hours. 100% of our cycles go into building systems we own and believe should exist.

### E. The Lab Notebook (Milestone Timeline)
A technical changelog showing relentless execution:
* **May 2026:** Problem identified at Willis Point Fire Dept; Rev 1 breadboard bench tests.
* **July 2026:** Rev 2 deployed in the field on active rural water cisterns.
* **Sept 2026:** Rev 3 custom PCBA (ESP32-S3, BG95 cellular, LoRa), custom polycarbonate IP66 tooling.
* **Fall 2026:** Pre-compliance and regulatory testing (ISED / FCC) at Camosun College.
* **Winter 2026:** Commercial release & volume manufacturing.

### F. Field Appearances & Events
A clean, monospaced schedule table showing where the team is in the real world:
* `Dec 18, 2026` — **Camosun Capstone Symposium** — Victoria, BC — *Final R3 Demo & Presentation*
* Subtext: *"Heads down on bench testing in Victoria, BC. Ping us to connect or talk hardware."*

### G. Direct Signal / Footer
* No bloated marketing forms.
* Clean contact lines:
  * **General / Coffee:** `hello@ltrjlabs.com`
  * **Investors & Hardware Inquiries:** Direct contact line.
  * Location: Victoria, British Columbia.
  * Copyright & link back to `mothnode.com`.

---

## 4. Technical Requirements & Existing Assets
* **Stack:** Clean HTML5, modern CSS / Tailwind CSS, and vanilla JS for smooth interactions.
* **Assets Available in Workspace:**
  * Logo: `img/SVGLogos/Full_Logo.svg`, `img/SVGLogos/Small_Logo.svg`
  * Photos: `img/MothNodePhoto1.jpg`, `img/MothNodeCover.jpg`, `img/AboutPagePhoto2.jpg`
  * CNAME: `www.ltrjlabs.com`
* **Performance:** Lightweight, zero heavy framework overhead, instant page load, fully responsive on mobile.

---

> Note (2026-10-07): asset paths above refer to the old repo layout. They now live at `img/logo/Full_Logo.svg`, `img/logo/Small_Logo.svg`, and `img/photo/*.jpg`.
