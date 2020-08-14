import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class DbHelper {
    private String userName="root";
    private   String passwoord="12345";
    private String dbUrl="jdbc:mysql://localhost:3306/students?useUnicode=true&useJDBCCompliantTimezoneShift=true&useLegacyDatetimeCode=false&serverTimezone=UTC";
    public Connection getConnection() throws SQLException {
        return DriverManager.getConnection(dbUrl,userName,passwoord);
    }
    public void showErrorMassage(SQLException e){
        System.out.println("Error:"+e.getMessage());
        System.out.println("Error code:"+e.getErrorCode());
    }
}
