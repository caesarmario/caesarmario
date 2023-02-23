####
## author       : mario.caesar
## link         : linktr.ee/caesarmario_
## file.name    : 'secret sauce' config for mnist fashion
## created      : 2023-02-08
###

# --- Import 'Secret Sauce' Libraries ---
import os
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import warnings

# --- Applying 'Secret Sauce' Font ---
def apply_font():
    font_path = "/kaggle/input/caesarmario/font"
    for x in os.listdir(font_path):
        for y in os.listdir(f"{font_path}/{x}"):
            if (y.split(".")[-1] == "ttf") or (y.split(".")[-1] == "otf"):
                fm.fontManager.addfont(f"{font_path}/{x}/{y}")
                try:
                    fm.FontProperties(weight=y.split("-")[-1].split(".")[0].lower(), fname=y.split("-")[0])
                except Exception:
                    continue

# --- Libraries Settings ---
warnings.filterwarnings("ignore")
sns.set_style("whitegrid")
sns.set(rc={"axes.facecolor": "#FBFBFB", "figure.facecolor": "#FBFBFB"})
plt.rcParams["figure.dpi"] = 600
plt.rcParams["font.family"] = "Poppins"

class clr:
    bold = "\033[1m"
    color = "\033[91m"
    start = color + bold
    end = "\033[0m"

apply_font()