# ManimAnims: A Collection of Manim Animations

Manim is an animation engine for explanatory math videos. It's used to create precise animations programmatically, and in this repository, we've curated some of the most fascinating animations using Manim.

## 🌌 Gallery

- 🔘 Sets In Math
  - ![Sets In Math Animation](SetsInMath/sets_in_math.mp4)

## 🚀 Getting Started

### Prerequisites

To use the animations in this repository, you need:
- [Python 3.11](https://www.python.org/downloads/)
- [Manim 0.17.3](https://docs.manim.community/en/stable/installation.html)
- [FFMPEG](https://ffmpeg.org/download.html)

### Installation Steps

**Clone the Repository**:
```bash
git clone https://github.com/Inc44/ManimAnims.git
```

## 🛠️ Usage

Navigate to the desired animation script and run it using Manim's CLI. For instance, to render an animation from `sets_in_math.py`:

```bash
manim sets_in_math.py
```

## Small Recommendation to Save Some Space

If you want to compress your lossless videos and save space, consider converting them to the AV1 format using FFMPEG:

```bash
ffmpeg -i input.mov -c:v libsvtav1 -preset 6 -pix_fmt yuv420p10le output.mp4
```

## 🎨 Customization

Feel free to tweak the animations to suit your needs. Modify parameters, colors, and equations within the scripts to customize the visuals.

## 🤝 Contribution

We highly encourage contributions! Whether you want to add a new animation or improve an existing one, all changes are welcome. Please initiate an issue for discussions before submitting a pull request.

## 📜 License

This collection is licensed under the Creative Commons Attribution-NonCommercial 4.0 International (CC-BY-NC-4.0) License. For comprehensive details, refer to [LICENSE.md](LICENSE.md).