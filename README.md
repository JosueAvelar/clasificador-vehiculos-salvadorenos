# Clasificador de Vehículos Urbanos Salvadoreños 🚦

## Descripción
Clasificador de imágenes que identifica 4 tipos de vehículos urbanos comunes 
en El Salvador: carros, motos, buses y microbuses salvadoreños. 
Construido con Transfer Learning usando ResNet50 pre-entrenada en ImageNet.

## Demo
🚧 Deploy en proceso.

## ¿Por qué este tema?
El transporte urbano en El Salvador es muy variado y visualmente interesante.
Los buses salvadoreños en particular son únicos por sus colores y diseños.
Este clasificador podría tener aplicaciones reales en sistemas de monitoreo 
de tráfico o análisis de transporte urbano.

## Dataset
- **Total de imágenes originales**: 160 (40 por clase)
- **Total con augmentation**: ~530 imágenes
- **Clases**:
  - 🚗 Carro (sedán y pickup)
  - 🏍️ Moto
  - 🚌 Bus Salvadoreño
  - 🚐 Microbús Salvadoreño
- **Fuentes**: Google Images (recolección manual)
- **Tamaño**: 160×160 píxeles, formato JPG

## Resultados
**Mejor accuracy en validación: 91%**

| Clase | Precision | Recall | F1 |
|-------|-----------|--------|----|
| Carro | 1.00 | 0.75 | 0.86 |
| Moto | 0.75 | 1.00 | 0.86 |
| Microbus Salvadoreno | 1.00 | 1.00 | 1.00 |

## Reflexión: Errores del Modelo

**¿Hay un patrón en los errores?**
Sí, los errores ocurren principalmente en imágenes tomadas de frente o en 
ángulos poco comunes, donde las características distintivas del vehículo 
(como el tamaño o la forma lateral) no son tan evidentes.

**¿Qué clase confunde más el modelo?**
El modelo confunde principalmente Carro y Moto entre sí. El recall de 0.75 
en Carro indica que algunos carros los clasifica como otra categoría, y la 
precision de 0.75 en Moto indica que a veces confunde otros vehículos 
con motos.

**¿Por qué crees que pasa?**
Hay varias razones posibles:
- Las fotos de carros y motos vienen en muchos ángulos y colores distintos, 
  lo que hace más difícil generalizar.
- Algunas fotos de pickups tomadas de cierto ángulo pueden parecerse 
  visualmente a un microbús o bus pequeño.
- Con solo 40 imágenes originales por clase, la diversidad visual 
  es limitada y el modelo puede no haber visto suficientes variaciones.

## Análisis de Errores
El modelo confunde con mayor frecuencia los Buses Salvadoreños con los 
Microbuses Salvadoreños, lo cual es esperado dado que ambos son vehículos 
grandes con características visuales similares como forma rectangular, 
ventanas amplias y colores llamativos. Los errores ocurren principalmente 
en fotos tomadas de frente donde la diferencia de tamaño entre ambos 
vehículos no es tan evidente.

## Aprendizajes
- El Transfer Learning con ResNet50 es sorprendentemente efectivo incluso 
  con pocos datos (~40 imágenes por clase).
- La calidad de las imágenes importa más que la cantidad.
- El parámetro `training=False` en la base model es crítico para evitar 
  el bug de BatchNormalization.
- Clases visualmente similares (bus vs microbús) son un desafío real 
  incluso para modelos con buen accuracy global.

## Tecnologías Usadas
- Python, TensorFlow/Keras
- Transfer Learning con ResNet50 (ImageNet)
- Data Augmentation con ImageDataGenerator
- Streamlit para interfaz web
- Google Colab para entrenamiento
- GitHub para control de versiones

## Autor
Josué Avelar  
Diplomado Python Avanzado — Universidad Don Bosco  
Módulo 4 — Sesión 4