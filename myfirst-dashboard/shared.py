from pathlib import Path
import sqlite3
import pandas as pd

import matplotlib as mpl
import matplotlib.font_manager as fm

app_dir = Path(__file__).parent
conn = sqlite3.connect(app_dir / "data/penguins.db")
df = pd.read_sql_query("SELECT * FROM penguins;", conn)

# 한글 폰트 설정: MaruBuri-Regular.ttf 직접 로드
font_path = app_dir / "MaruBuri-Regular.ttf"
font_prop = fm.FontProperties(fname=font_path)

fm.fontManager.addfont(str(font_path))          # ✅ 폰트 등록
font_prop = fm.FontProperties(fname=font_path)
mpl.rcParams["font.family"] = font_prop.get_name()  # ✅ 전역 기본 폰트 지정
mpl.rcParams["axes.unicode_minus"] = False