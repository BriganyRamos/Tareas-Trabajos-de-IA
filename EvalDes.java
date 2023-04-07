import net.sourceforge.jFuzzyLogic.FIS;
/**Escalante Penuelas
 * y
 * Ramos Moreno
 * */
public class EvalDes {
    public static void main(String[] args) {
        // Cargar archivo de configuración del sistema experto
        String fileName = "C:\\Users\\windows 10\\eclipse-workspace\\EvaDes\\src\\evaluacion_desempeno.fcl";
        FIS fis = FIS.load(fileName, true);
        // Verificar si se cargó el archivo correctamente
        if (fis == null) {
            System.err.println("Error al cargar el archivo de configuración del sistema experto.");
            return;
        }
        // Establecer los valores de las entradas del sistema experto
        fis.setVariable("habilidad_tecnica", 6.8);
        fis.setVariable("actitud_trabajo", 7);
        // Evaluar el sistema experto
        fis.evaluate();
        // Obtener el valor de la salida del sistema experto
        double evaluacion = fis.getVariable("evaluacion_desempeno").getValue();
        // Imprimir el resultado
        System.out.println("Escalante Penuelas y Ramos Moreno");
        System.out.println("La evaluación de desempeño del empleado es: " + evaluacion);
    }
}
