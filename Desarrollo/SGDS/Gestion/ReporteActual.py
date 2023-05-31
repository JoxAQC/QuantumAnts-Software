
import datetime

def generar_reporte():
    # Título y propósito del informe
    informe = "Reporte de Estado Actual del Software: Sistema de Donación de Sangre\n\nPropósito:\nEl propósito de este proyecto es desarrollar un Sistema de Donación de Sangre en línea que permita a los donantes de sangre encontrar hospitales cercanos y programar sus citas de donación de sangre de manera eficiente. El sistema también permitirá a los donantes registrar sus datos personales y la cantidad de sangre donada, así como a los hospitales validar y recompensar la donación con un beneficio, como una consulta gratis. Con este sistema, se espera fomentar la donación de sangre y mejorar el acceso a los servicios de donación de sangre para la población.\n\n"
    
    # Índice
    informe += "Índice:\n"
    informe += "1. Propósito\n"
    informe += "2. Objetivos\n"
    informe += "3. Hito 1\n"
    informe += "4. Hito 2\n"
    informe += "5. Estado Actual del Software\n"
    informe += "6. Planes Futuros\n"
    informe += "7. Conclusiones\n\n"

    # Objetivos
    informe += "Objetivos:\n"
    objetivos = [
        "Promover y fomentar la realización de campañas de donación de sangre, a través de la implementación de una solución tecnológica integral y eficiente.",
        "Establecer una base de datos centralizada y segura que almacene la información de los donantes de sangre y los hospitales asociados; permitiendo una gestión más efectiva de la información, reducción de errores y duplicaciones de datos.",
        "Mejorar la eficiencia y la transparencia del proceso de donación de sangre al eliminar la necesidad de llenar formularios en papel y permitir el seguimiento de la cantidad de sangre donada y los beneficios otorgados a los donantes.",
        "Mejorar la accesibilidad de la sangre donada, consiguiendo que esta esté disponible para los pacientes que la necesitan, mediante procesos de distribución eficientes y bien coordinados, así como de la implementación de un sistema de seguimiento para el uso de la sangre donada."
    ]
    for objetivo in objetivos:
        informe += "- " + objetivo + "\n"
        informe += "\n"

    # Hito 1
    informe += "Hito 1:\n"
    hito1_actividades = [
        "Reunión con el Stakeholder",
        "Idear Proyecto innovador",
        "Desarrollar el Plan de Proyecto",
        "Elaborar el Cronograma del Proyecto",
        "Crear el repositorio del proyecto",
        "Especificar Requisitos del Software 1: Registro de hospitales",
        "Especificar Requisitos del Software 2: Registro de donantes",
        "Especificar Requisitos del Software 3: Programación de citas",
        "Especificar Requisitos del Software 4: Validación de beneficios",
        "Especificar Requisitos del Software 5: Entrega de beneficios",
        "Especificar Requisitos del Software 6: Seguridad de la información",
        "Especificar Requisitos del Software 7: Reporte y Estadísticas",
        "Especificar Requisitos del Software 8: Accesibilidad",
        "Especificar Requisitos del Software 9: Integración con sistemas existentes",
        "Especificar la Arquitectura y Diseño del Software",
        "Especificar el diseño de la Base de Datos",
        "Proponer el diseño inicial de la Interfaz Web (UI)",
        "Establecer estilos para la web"
    ]
    for actividad in hito1_actividades:
        informe += "- " + actividad + "\n"
        informe += "\n"

        # Hito 2
    informe += "Hito 2:\n"
    hito2_actividades = [
        "Implementación y Verificación del Requisito 01: Registro de hospitales",
        "Implementación y Verificación del Requisito 02: Registro de donantes",
        "Implementación y Verificación del Requisito 03: Programación de citas",
        "Implementación y Verificación de la Base de datos",
        "Implementación y Verificación de 1/3 de la Interfaz de la Web",
        "Verificar y Actualizar documento de Especificación de UI",
        "Reportar estado actual del software"
        ]
    for actividad in hito2_actividades:
        informe += "- " + actividad + "\n"
        informe += "\n"

# Estado Actual del Software
    informe += "Estado Actual del Software:\n"
    informe += "Actualmente, el desarrollo del Sistema de Donación de Sangre se encuentra en el Hito 2, donde se ha completado exitosamente la implementación y verificación de los requisitos relacionados con el registro de hospitales, registro de donantes y programación de citas. Además, se ha realizado la implementación y verificación de una parte de la interfaz de la web.\n"
    informe += "El equipo de desarrollo ha seguido una metodología ágil, lo que ha permitido una entrega continua de funcionalidades y una colaboración estrecha con los stakeholders. Se han realizado pruebas exhaustivas para garantizar la calidad del software, incluyendo pruebas unitarias, pruebas de integración y pruebas de aceptación.\n"
    informe += "En cuanto al Hito 1, se completó al 100%, abarcando actividades como reuniones con los stakeholders, la ideación del proyecto, el desarrollo del plan de proyecto, la especificación de requisitos del software, el diseño de la arquitectura y la base de datos, así como la propuesta del diseño inicial de la interfaz web.\n\n"

# Planes Futuros
    informe += "Planes Futuros:\n"
    informe += "Para los próximos pasos del proyecto, se espera finalizar el Hito 2 completando la implementación y verificación de los requisitos restantes de la interfaz de la web. Además, se llevará a cabo la verificación y actualización del documento de especificación de la interfaz de usuario.\n"
    informe += "Se continuará trabajando en la implementación de los requisitos pendientes, como la validación de beneficios, entrega de beneficios, seguridad de la información, reporte y estadísticas, accesibilidad e integración con sistemas existentes.\n"
    informe += "Asimismo, se realizará la planificación y ejecución del Sprint Retrospective para evaluar el progreso del proyecto hasta el momento y realizar mejoras continuas en el proceso de desarrollo.\n\n"

# Conclusiones
    informe += "Conclusiones:\n"
    informe += "El Sistema de Donación de Sangre ha logrado avances significativos en su desarrollo, cumpliendo con los objetivos establecidos de promover y fomentar la donación de sangre, establecer una base de base de datos centralizada y segura, mejorar la eficiencia y transparencia del proceso de donación, y mejorar la accesibilidad de la sangre donada.\n"
    informe += "El equipo de desarrollo ha trabajado de manera colaborativa y se ha asegurado la calidad del software a través de pruebas exhaustivas. El proyecto continúa su curso, avanzando hacia la implementación completa de los requisitos y la entrega de un sistema robusto y eficiente que cumpla con las necesidades de los donantes de sangre y los hospitales.\n"

# Generar el archivo de informe
    with open("informe.txt", "w") as archivo:
     archivo.write(informe)

print("¡El informe se ha generado exitosamente!")
generar_reporte()
