# ⚾ LVBP Analytics: Temporada 2025-2026

Este proyecto es una aplicación web interactiva diseñada para el análisis de estadísticas de la **Liga Venezolana de Béisbol Profesional (LVBP)**. La app permite visualizar el rendimiento de los jugadores mediante métricas en tiempo real y gráficos dinámicos.

---

## 🚀 Características Principales

* **Procesamiento de Datos:** Limpieza y transformación de datasets utilizando **Pandas**.
* **Visualización Avanzada:** Gráficos de barras horizontales interactivos con **Plotly Express**.
* **Filtros Dinámicos:** Segmentación de datos por equipo para un análisis detallado.

## 📊 Lógica de Negocio y Fórmulas
Para garantizar la precisión estadística, la aplicación realiza cálculos automáticos sobre el dataset cargado. La métrica principal es el promedio de bateo, calculado mediante la fórmula:

$$AVG = \frac{H}{VB}$$

Donde:
* **H:** Hits.
* **VB:** Veces al Bate.

---

## 🛠️ Tecnologías Utilizadas

| Herramienta | Uso |
| :--- | :--- |
| **Python 3.14** | Lenguaje base del proyecto. |
| **Streamlit** | Framework para la creación de la interfaz web. |
| **Pandas** | Manipulación y análisis de estructuras de datos. |
| **Plotly** | Generación de gráficos interactivos. |