"""
Fichier python pour tester Streamlit sur les sorties de MAELIA
"""

import altair as alt
import pandas as pd
import streamlit as st
import os


if __name__ == "__main__":
    # log_MAELIA_01 = "/Users/g.taburet/Gama_Workspace/MAELIA_1.4.27_GAMA_2025-06/models/main/log/terrainTest_mais_tousSols_irr_organique_ApresAjoutIrrigationITK/"
    # log_MAELIA_02 = "/Users/g.taburet/Gama_Workspace/MAELIA_1.4.27_GAMA_2025-06/models/main/log/terrainTest_mais_tousSols_irr_organique_AvantAjoutIrrigationITK/"
    # title_plot_01 = "avec_irrigation"
    # title_plot_02 = "sans_irrigation"
    # log_MAELIA_01 = "/Users/g.taburet/Gama_Workspace/MAELIA_1.4.27_GAMA_2025-06/models/main/log/terrainTest_biodiversite_sudouest_prairie_35_1/"
    # log_MAELIA_02 = "/Users/g.taburet/Gama_Workspace/MAELIA_1.4.27_GAMA_2025-06/models/main/log/terrainTest_biodiversite_sudouest_prairie_42_1/"
    # title_plot_01 = "sudouest_prairie_35_1"
    # title_plot_02 = "sudouest_prairie_42_1"
    # log_MAELIA_01 = "/Users/g.taburet/Gama_Workspace/MAELIA_1.4.27_GAMA_2025-06/models/main/log/terrainTest_2026-01-29_testMaisDP/"
    log_MAELIA_01 = "data/terrainTest_2026-01-29_testMaisDP_AvecIrri_Rendemdent14_v2/"
    log_MAELIA_02 = (
        "data/terrainTest_2026-01-29_testMaisDP_alfalfa_AvecIrri_Rendemdent14/"
    )
    title_plot_01 = "maisDP"
    title_plot_02 = "alfalfa_maisDP"

    # Fichiers de sorties MAELIA
    # Rendements
    filename = "suiviOTParParcelle.csv"
    # Lixiviation
    filename_CN = "sorties_CN.csv"
    # Emission GES
    filename_GES = "sorties_GES.csv"
    # Irrigation
    filename_EAU = "sorties_eau.csv"
    # Biodiversité
    filename_bio = "resultats_iBIO.csv"

    # Streamlit App
    st.title("Dashboard – MAELIA")
    # Créer les onglets pour chaque plot
    tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8 = st.tabs(
        [
            "Rendement",
            "Lixiviation",
            "Azote mineralise",
            "GES",
            "Irrigation",
            "Biodiversité",
            "Satisfaction Culture",
            "Variation stock Carbone",
        ]
    )

    # -------------------
    # Onglet 1 : Rendement
    with tab1:
        df_01 = pd.read_csv(log_MAELIA_01 + filename, sep=";")
        df_02 = pd.read_csv(log_MAELIA_02 + filename, sep=";")

        rendement_01 = (
            df_01[["RECOLTE_rendement[t/ha]", "annee"]]
            .dropna()
            .groupby("annee")["RECOLTE_rendement[t/ha]"]
            .sum()
        )
        rendement_02 = (
            df_02[["RECOLTE_rendement[t/ha]", "annee"]]
            .dropna()
            .groupby("annee")["RECOLTE_rendement[t/ha]"]
            .sum()
        )
        annees = list(range(2020, 2031))

        df_plot = pd.DataFrame(
            {
                title_plot_01: rendement_01,
                title_plot_02: rendement_02,
            },
            index=annees,
        )
        df_plot.index.name = "Année"
        st.line_chart(df_plot, x_label="Année", y_label="[t/ha]")

    # -------------------
    # Onglet 2 : Lixiviation
    with tab2:
        df_01 = pd.read_csv(log_MAELIA_01 + filename_CN, sep=";")
        df_02 = pd.read_csv(log_MAELIA_02 + filename_CN, sep=";")

        lixiviation_01 = (
            df_01[["N_lixivie[kgN/ha]", "annee"]]
            .dropna()
            .groupby("annee")["N_lixivie[kgN/ha]"]
            .sum()
        )
        lixiviation_02 = (
            df_02[["N_lixivie[kgN/ha]", "annee"]]
            .dropna()
            .groupby("annee")["N_lixivie[kgN/ha]"]
            .sum()
        )
        annees = range(2020, 2031)

        df_plot = pd.DataFrame(
            {
                title_plot_01: lixiviation_01,
                title_plot_02: lixiviation_02,
            },
            index=annees,
        )
        df_plot.index.name = "Année"
        st.line_chart(df_plot, x_label="Année", y_label="[kgN/ha]")

    # -------------------
    # Onglet 3 : Azote minéralisé
    with tab3:
        df_01 = pd.read_csv(log_MAELIA_01 + filename_CN, sep=";")
        df_02 = pd.read_csv(log_MAELIA_02 + filename_CN, sep=";")

        azote_mineralise_01 = (
            df_01[["N_mineralise_net_SOM[kgN/ha]", "annee"]]
            .dropna()
            .groupby("annee")["N_mineralise_net_SOM[kgN/ha]"]
            .sum()
        )
        azote_mineralise_02 = (
            df_02[["N_mineralise_net_SOM[kgN/ha]", "annee"]]
            .dropna()
            .groupby("annee")["N_mineralise_net_SOM[kgN/ha]"]
            .sum()
        )
        annees = range(2020, 2031)

        df_plot = pd.DataFrame(
            {
                title_plot_01: azote_mineralise_01,
                title_plot_02: azote_mineralise_02,
            },
            index=annees,
        )
        df_plot.index.name = "Année"
        st.line_chart(df_plot, x_label="Année", y_label="N_mineralise_net_SOM [kgN/ha]")

    # -------------------
    # Onglet 4 : GES
    with tab4:
        df_01 = pd.read_csv(log_MAELIA_01 + filename_GES, sep=";")
        df_02 = pd.read_csv(log_MAELIA_02 + filename_GES, sep=";")

        ges_01 = (
            df_01[["bilan_net_GES[kg_eqCO2/ha]", "annee"]]
            .dropna()
            .groupby("annee")["bilan_net_GES[kg_eqCO2/ha]"]
            .sum()
        )
        ges_02 = (
            df_02[["bilan_net_GES[kg_eqCO2/ha]", "annee"]]
            .dropna()
            .groupby("annee")["bilan_net_GES[kg_eqCO2/ha]"]
            .sum()
        )
        annees = range(2020, 2031)

        df_plot = pd.DataFrame(
            {
                title_plot_01: ges_01,
                title_plot_02: ges_02,
            },
            index=annees,
        )
        df_plot.index.name = "Année"
        st.line_chart(df_plot, x_label="Année", y_label="bilan_net_GES [kg_eqCO2/ha]")

    # -------------------
    # Onglet 5 : Irrigation
    with tab5:
        df_01 = pd.read_csv(log_MAELIA_01 + filename_EAU, sep=";")
        df_02 = pd.read_csv(log_MAELIA_02 + filename_EAU, sep=";")

        eau_01 = (
            df_01[["irrigation[mm]", "annee"]]
            .dropna()
            .groupby("annee")["irrigation[mm]"]
            .sum()
        )
        eau_02 = (
            df_02[["irrigation[mm]", "annee"]]
            .dropna()
            .groupby("annee")["irrigation[mm]"]
            .sum()
        )
        annees = range(2020, 2031)

        df_plot = pd.DataFrame(
            {
                title_plot_01: eau_01,
                title_plot_02: eau_02,
            },
            index=annees,
        )
        df_plot.index.name = "Année"
        st.line_chart(df_plot, x_label="Année", y_label="[mm]")

    with tab6:
        if os.path.exists(log_MAELIA_01 + filename_bio):
            df_01 = pd.read_csv(
                log_MAELIA_01 + filename_bio,
                sep=";",
                skiprows=11,
                header=None,
                names=["annee", "indicateur_bio"],
            )
            df_02 = pd.read_csv(
                log_MAELIA_02 + filename_bio,
                sep=";",
                skiprows=11,
                header=None,
                names=["annee", "indicateur_bio"],
            )

            chart_01 = (
                alt.Chart(df_01)
                .mark_point(filled=True, size=200)
                .encode(
                    x=alt.X("annee:O", title="Année"),
                    y=alt.Y(
                        "indicateur_bio:O",
                        sort=["Very low", "Low", "Medium", "High"],
                    ),
                    color=alt.Color(
                        "indicateur_bio:O",
                        scale=alt.Scale(
                            domain=["Very low", "Low", "Medium", "High"],
                            range=["red", "orange", "green", "lightgreen"],
                        ),
                    ),
                )
            )
            chart_02 = (
                alt.Chart(df_02)
                .mark_point(filled=True, size=200)
                .encode(
                    x=alt.X("annee:O", title="Année"),
                    y=alt.Y(
                        "indicateur_bio:O",
                        sort=["Very low", "Low", "Medium", "High"],
                    ),
                    color=alt.Color(
                        "indicateur_bio:O",
                        scale=alt.Scale(
                            domain=["Very low", "Low", "Medium", "High"],
                            range=["red", "orange", "green", "lightgreen"],
                        ),
                    ),
                )
            )
            st.text(title_plot_01)
            st.altair_chart(chart_01, use_container_width=True)
            st.text(title_plot_02)
            st.altair_chart(chart_02, use_container_width=True)

    # -------------------
    # Onglet 7 : Satisfaction Azote
    with tab7:
        df_01 = pd.read_csv(log_MAELIA_01 + filename_CN, sep=";")
        df_02 = pd.read_csv(log_MAELIA_02 + filename_CN, sep=";")

        satisfaction_azote_01 = (
            df_01[["satisfactionAzote_culture[%]", "annee"]]
            .dropna()
            .groupby("annee")["satisfactionAzote_culture[%]"]
            .sum()
        )
        satisfaction_azote_02 = (
            df_02[["satisfactionAzote_culture[%]", "annee"]]
            .dropna()
            .groupby("annee")["satisfactionAzote_culture[%]"]
            .sum()
        )
        annees = range(2020, 2031)

        df_plot = pd.DataFrame(
            {
                title_plot_01: satisfaction_azote_01,
                title_plot_02: satisfaction_azote_02,
            },
            index=annees,
        )
        df_plot.index.name = "Année"
        st.line_chart(df_plot, x_label="Année", y_label="satisfactionAzote_culture [%]")

        df_01 = pd.read_csv(log_MAELIA_01 + filename_EAU, sep=";")
        df_02 = pd.read_csv(log_MAELIA_02 + filename_EAU, sep=";")

        satisfaction_eau_01 = (
            df_01[["satisfactionHydrique[%]", "annee"]]
            .dropna()
            .groupby("annee")["satisfactionHydrique[%]"]
            .sum()
        )
        satisfaction_eau_02 = (
            df_02[["satisfactionHydrique[%]", "annee"]]
            .dropna()
            .groupby("annee")["satisfactionHydrique[%]"]
            .sum()
        )
        annees = range(2020, 2031)

        df_plot = pd.DataFrame(
            {
                title_plot_01: satisfaction_eau_01,
                title_plot_02: satisfaction_eau_02,
            },
            index=annees,
        )
        df_plot.index.name = "Année"
        st.line_chart(df_plot, x_label="Année", y_label="satisfactionHydrique [%]")

    # -------------------
    # Onglet 8 : Variation stock Carbone
    with tab8:
        df_01 = pd.read_csv(log_MAELIA_01 + filename_GES, sep=";")
        df_02 = pd.read_csv(log_MAELIA_02 + filename_GES, sep=";")

        corg_01 = (
            df_01[["delta_Corg[kg_eqCO2/ha]", "annee"]]
            .dropna()
            .groupby("annee")["delta_Corg[kg_eqCO2/ha]"]
            .sum()
        )
        corg_02 = (
            df_02[["delta_Corg[kg_eqCO2/ha]", "annee"]]
            .dropna()
            .groupby("annee")["delta_Corg[kg_eqCO2/ha]"]
            .sum()
        )
        annees = list(range(2020, 2031))

        df_plot = pd.DataFrame(
            {
                title_plot_01: corg_01,
                title_plot_02: corg_02,
            },
            index=annees,
        )
        df_plot.index.name = "Année"
        st.line_chart(df_plot, x_label="Année", y_label="delta_Corg[kg_eqCO2/ha]")
