import seaborn as sns
import pandas as pd

# Import data from shared.py
from shared import df

from shinyswatch import theme
from shiny.express import input, render, ui
from shiny import reactive

ui.page_opts(title="팔머펭귄 데이터 대시보드")

var_choice={"bill_length_mm": "부리길이(mm)",
            "bill_depth_mm": "부리깊이(mm)",
            "flipper_length_mm": "날개길이(mm)",
            "body_mass_g": "체중(g)"}

species_choice = pd.Series({
    "Adelie": "아델리(Adelie)",
    "Gentoo": "겐투(Gentoo)",
    "Chinstrap": "친스트랩(Chinstrap)",
})

with ui.sidebar(open="desktop"):
    "산점도 변수 2개 선택:"
    ui.input_select(
        "var1",
        "변수 1", 
        choices=var_choice,
        selected="bill_length_mm"
    )
    ui.input_select(
        "var2",
        "변수 2",
        choices=var_choice,
        selected="bill_depth_mm"
    )
    ui.input_checkbox_group(
        "var3",
        "종(species) 선택",
        choices=species_choice,  # 선택지
        selected=["Adelie", "Gentoo", "Chinstrap"]
    )
    with ui.layout_columns():
        ui.input_action_button("apply", "적용")
        ui.input_action_button("reset", "리셋")

# 사용자가 Apply를 눌렀을 때만 반영
filtered_df = reactive.Value(df)
input_1 = reactive.Value("bill_length_mm")
input_2 = reactive.Value("bill_depth_mm")
@reactive.effect
@reactive.event(input.apply)
def _():
    filtered_df.set(df[df["species"].isin(input.var3())])
    input_1.set(input.var1())
    input_2.set(input.var2())

# 리셋버튼 - ui 값 조정
@reactive.effect
@reactive.event(input.reset)
def _():
    ui.update_select("var1", selected="bill_length_mm")
    ui.update_select("var2", selected="bill_depth_mm")
    ui.update_checkbox_group("var3", selected=["Adelie", "Gentoo", "Chinstrap"])

color_match={
    "Adelie": "red",
    "Gentoo": "green",
    "Chinstrap": "blue"
}

with ui.nav_panel("Page 1"):
    with ui.layout_columns():
        with ui.card():
            @render.plot
            def scatter():
                p = sns.scatterplot(
                        data=filtered_df(), 
                        x=input_1(),
                        y=input_2(),
                        hue="species",
                        palette=color_match)
                p.set_xlabel(var_choice[input_1()])
                p.set_ylabel(var_choice[input_2()])
                handles, _ = p.get_legend_handles_labels()
                p.legend(handles=handles,
                         labels=species_choice.reindex(input.var3()).tolist(),
                         title = "종 정보")
                return p
        with ui.card():
            @render.data_frame
            def data():
                return filtered_df()   


with ui.nav_panel("Page 2"):
    "This is the second 'page'."


