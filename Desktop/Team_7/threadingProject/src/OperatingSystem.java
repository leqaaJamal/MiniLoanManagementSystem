import java.io.BufferedWriter;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Scanner;
import java.util.concurrent.Semaphore;

import sun.awt.image.ImageWatched.Link;
import sun.misc.Queue;

public class OperatingSystem {

	static int semR = 1;
	static int R = 1;
	static LinkedList<Integer> qR = new LinkedList<Integer>();
//...menna
	static int semW = 1;
	static int W = 1;
	static int semI = 1;
	static int I = 1;
	static LinkedList<Integer> qW = new LinkedList<Integer>();
	static LinkedList<Integer> qI = new LinkedList<Integer>();
	// ..menna
	static int semP = 1;
	static int P = 1;
	static LinkedList<Integer> qP = new LinkedList<Integer>();

	// .....leqaaa
	static LinkedList<Process> readyqueue = new LinkedList();
	static boolean flagready = false;
	// .....leqaaa

	public static ArrayList<Thread> ProcessTable;

	// public static int activeProcess= 0;
	// system calls:
	// 1- Read from File

	// ....Menna
	public static void semWriteWait() throws InterruptedException {
		int id = W++;
		if (semW == 1) {
			semW = 0;
		} else {
			qW.add(id);
			while (qW.contains(id)) {
				Thread.sleep(1);
			}
		}
	}

	public static void semWritePost() {
		if (qW.isEmpty()) {
			semW = 1;
		} else {
			qW.remove();

		}
	}

	// ..Menna
	public static void semInputWait() throws InterruptedException {
		int id = I++;
		if (semI == 1) {
			semI = 0;
		} else {
			qI.add(id);
			while (qI.contains(id)) {
				Thread.sleep(1);
			}
		}
	}

	public static void semInputPost() {
		if (qI.isEmpty()) {
			semI = 1;
		} else {
			qI.remove();

		}
	}
	// Menna

	public static void semReadWait() throws InterruptedException {
		int id = R++;
		if (semR == 1) {
			semR = 0;
		} else {
			qR.add(id);
			while (qR.contains(id)) {
				Thread.sleep(1);
			}
		}
	}

	public static void semReadPost() {
		if (qR.isEmpty()) {
			semR = 1;
		} else
			qR.remove();
	}

	public static void semPrintWait() throws InterruptedException {
		int id = P++;
		if (semP == 1) {
			semP = 0;
		} else {
			qP.add(id);
			while (qP.contains(id)) {
				Thread.sleep(1);
			}
		}
	}

	public static void semPrintPost() {

		if (qP.isEmpty()) {
			semP = 1;
		} else
			System.out.println(qP.remove());
	}

	@SuppressWarnings("unused")
	public static String readFile(String name) {
		String Data = "";
		File file = new File(name);
		try {
			Scanner scan = new Scanner(file);
			while (scan.hasNextLine()) {
				Data += scan.nextLine() + "\n";
			}
			scan.close();
		} catch (FileNotFoundException e) {
			System.out.println(e.getMessage());
		}
		return Data;
	}

	// 2- Write into file
	@SuppressWarnings("unused")
	public static void writefile(String name, String data) {
		try {
			BufferedWriter BW = new BufferedWriter(new FileWriter(name));
			BW.write(data);
			BW.close();
		} catch (IOException e) {
			System.out.println(e.getMessage());
		}

	}

	// 3- print to console
	@SuppressWarnings("unused")
	public static void printText(String text) {

		System.out.println(text);

	}

	// 4- take input

	@SuppressWarnings("unused")
	public static String TakeInput() {
		Scanner in = new Scanner(System.in);
		String data = in.nextLine();
		return data;

	}

	private static void createProcess(int processID) {
		Process p = new Process(processID);
		ProcessTable.add(p);
		Process.setProcessState(p, ProcessState.Ready);
		// ....leqaa
//		p.start(); // hna
		// ....leqaa

	}

	// ....leqaa
	private static void FCFS() {
		int i = 0;
		while (!readyqueue.isEmpty()) {
			Process p = readyqueue.getFirst();
			if (p.status == ProcessState.Ready && !flagready) {
				System.out.println(i++);
				p.start();
				flagready = true;
			}
			readyqueue.removeFirst();
			while (p.isAlive()) {

			}
			// System.out.println(p.status);
		}
	}
	// ....leqaa

	public static void main(String[] args) throws InterruptedException {
		ProcessTable = new ArrayList<Thread>();
		createProcess(3);
		createProcess(1);
		createProcess(4);
		createProcess(2);
		createProcess(5);
		
		// Thread.sleep(1);

		// ...leqaa
		 FCFS(); //hna
		// ...leqaa

	}
}