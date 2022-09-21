
import java.io.*;
import org.json.simple.*;
import org.json.simple.parser.JSONParser;
import org.json.simple.parser.ParseException;

/**
 *
 * @author ivan_
 */

public class Json_FileHandle {
    
    Estudiante es;
    
    public void write_JSON(Estudiante e){
        JSONObject estudiante = new JSONObject();
        estudiante.put("Código", e.getCod());
        estudiante.put("Nombre", e.getNom());
        estudiante.put("Apellido", e.getApe());
        estudiante.put("CentroU", e.getCen());
        estudiante.put("Télefono", e.getNum());
        
        try(FileWriter file = new FileWriter("estudiantes.json")){
            file.write(estudiante.toJSONString());
            file.flush();
        } catch (IOException ex) {
            ex.printStackTrace();
        }
    }
    
    public Estudiante read_JSON(){
        JSONParser jR = new JSONParser();
        es = new Estudiante();
        try{
            Object ob = new JSONParser().parse(new FileReader("estudiantes.json"));
            JSONObject est = (JSONObject) ob; 
            es.setCod(String.valueOf(est.get("Código")));
            es.setNom(String.valueOf(est.get("Nombre")));
            es.setApe(String.valueOf(est.get("Apellido")));
            es.setCen(String.valueOf(est.get("CentroU")));
            es.setNum(String.valueOf(est.get("Télefono")));
        } catch (IOException ex) {
            ex.printStackTrace();
        } catch (ParseException ex) {
            ex.printStackTrace();
        }
        return es;
    }
}
