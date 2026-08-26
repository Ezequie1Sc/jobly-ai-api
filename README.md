# Jobly AI API 

<p align="center">
  <strong>Backend REST para análisis de CV, extracción de habilidades y recomendación de vacantes de job.</strong>
</p>

<p align="center">
  <a href="https://github.com/Ezequie1Sc/jobly-ai-api">
    <img src="https://img.shields.io/badge/GitHub-Repository-181717?style=for-the-badge&logo=github" alt="GitHub Repository">
  </a>
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/FastAPI-REST%20API-009688?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI">
  <img src="https://img.shields.io/badge/PDF-pypdf-B02E0C?style=for-the-badge" alt="PDF">
</p>

## 📌 Descripción

**Jobly AI API** es el backend de la plataforma **Jobly**, diseñado para procesar información profesional de candidatos y ayudar a relacionarla con oportunidades laborales.

Actualmente proporciona tres capacidades principales:

- 📄 **Análisis de CV en PDF**
- 🎯 **Cálculo de compatibilidad entre habilidades y vacantes**
- 💬 **Asistente de chat contextual para CV y vacantes**

La API está construida con **FastAPI** y utiliza `pypdf` para extraer texto de archivos PDF. La detección de habilidades y el matching actual se realizan mediante reglas determinísticas, por lo que el proyecto puede evolucionar posteriormente hacia modelos de IA/LLM sin cambiar la interfaz principal de la API.

## ✨ Características

| Funcionalidad | Descripción |
|---|---|
| 📄 CV Analyzer | Recibe un PDF y extrae su contenido |
| 🧠 Skill Extraction | Detecta habilidades técnicas conocidas dentro del CV |
| 🎯 Job Matching | Calcula un porcentaje de compatibilidad con cada vacante |
| 💬 Chat | Responde preguntas sobre habilidades, CV y vacantes |
| 📚 OpenAPI | Documentación interactiva generada automáticamente por FastAPI |
| 🔒 Validación | Valida formato, tamaño y contenido del CV |

## 🏗️ Arquitectura

```text
jobly-ai-api/
│
├── app/
│   ├── main.py
│   │
│   ├── routers/
│   │   ├── cv.py
│   │   ├── recommendations.py
│   │   └── chat.py
│   │
│   └── services/
│       ├── pdf_service.py
│       ├── matching_service.py
│       └── chat_service.py
│
├── requirements.txt
├── .gitignore
└── README.md
