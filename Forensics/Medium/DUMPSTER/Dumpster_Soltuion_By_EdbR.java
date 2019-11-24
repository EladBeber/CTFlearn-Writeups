import javax.crypto.Cipher;
import javax.crypto.spec.SecretKeySpec;
import java.util.Base64;

public class Dumpster_Solution {

    public static final String FLAG = "S+kUZtaHEYpFpv2ixuTnqBdORNzsdVJrAxWznyOljEo=";

    public static byte [] decrypt(byte[] msg,byte [] passHash) throws Exception
    {
        SecretKeySpec spec = new SecretKeySpec(passHash, "AES");
        Cipher cipher = Cipher.getInstance("AES/ECB/PKCS5Padding");
        cipher.init(Cipher.DECRYPT_MODE, spec);
        return cipher.doFinal(msg);
    }

    public static void main(String[] args) throws Exception
    {
        byte [] passHash = {7, 95, -34, 16, -89, -86, 73, 108, -128, 71, 43, 41, 100, 40, 53, -24};
        System.out.println(new String(decrypt(Base64.getDecoder().decode(FLAG.getBytes()),passHash)));
        Thread.sleep(5000); //We did a heap dump right here.
    }
}
