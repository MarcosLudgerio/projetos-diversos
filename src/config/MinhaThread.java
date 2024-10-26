package config;

import java.sql.SQLOutput;

public class MinhaThread extends Thread {

    public void run(){
        System.out.println("A thread começou: " + this.getName());
    }
}
