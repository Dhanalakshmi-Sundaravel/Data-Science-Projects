import java.math.BigInteger;
import java.nio.charset.StandardCharsets;

//$Id$

public class UnScramblePassword {
	public static void main(String[] args) {
	    char[] password = "banana5662525628".toCharArray();
	    char[] email    = "sumidhanalakshmi2013@gmail.com".substring(0, 16).toCharArray();
	    int[] output = new int[16];
	    System.out.println("password.length: "+password.length);
	    System.out.println("email.length: "+email.length);
	    for(int i = 0; i< 16; i++) {
	    	output[i] = password[i] ^ email[i];
	    }
	    for(int i = 0; i< 16; i++) {
	    	System.out.print(email[i]);
	    }
	    System.out.println();
	    String emailHex = "73756d696468616e616c616b73686d69";
	    Integer timeStamp = 1553021518;
	    System.out.println(Integer.toHexString(timeStamp));
	    Integer timeStamp1 = 1553021519;
	    System.out.println(Integer.toHexString(timeStamp1));
	    Integer timeStamp2 = 1553021520;
	    System.out.println(Integer.toHexString(timeStamp2));
	    Integer timeStamp3 = 1553021521;
	    System.out.println(Integer.toHexString(timeStamp3));
	    Integer timeStamp4 = 1553021522;
	    System.out.println(Integer.toHexString(timeStamp4));
	    Integer timeStamp5 = 1553021523;
	    System.out.println(Integer.toHexString(timeStamp5));
	    Integer timeStamp6 = 1553021524;
	    System.out.println(Integer.toHexString(timeStamp6));
	    Integer timeStamp7 = 1553021525;
	    System.out.println(Integer.toHexString(timeStamp7));
	    Integer timeStamp8 = 1553021526;
	    System.out.println(Integer.toHexString(timeStamp8));
	    Integer timeStamp9 = 1553021527;
	    System.out.println(Integer.toHexString(timeStamp9));
	    Integer timeStamp10 = 1553021528;
	    System.out.println(Integer.toHexString(timeStamp10));
	    Integer timeStamp11 = 1553021529;
	    System.out.println(Integer.toHexString(timeStamp11));
	}
}
