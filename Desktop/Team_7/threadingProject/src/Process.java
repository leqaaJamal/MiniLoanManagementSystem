//import java.util.concurrent.Semaphore;

public class Process extends Thread implements Runnable {

	public int processID;
	ProcessState status = ProcessState.New;

	public Process(int m) {
		processID = m;
	}

	@Override
	public void run() {

		switch (processID) {
		case 1:
			try {
				process1();
			} catch (InterruptedException e1) {
				// TODO Auto-generated catch block
				e1.printStackTrace();
			}
			break;
		case 2:
			try {
				process2();
			} catch (InterruptedException e1) {
				// TODO Auto-generated catch block
				e1.printStackTrace();
			}
			break;
		case 3:
			try {
				process3();
			} catch (InterruptedException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
			break;
		case 4:
			try {
				process4();
			} catch (InterruptedException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
			break;
		case 5:
			try {
				process5();
			} catch (InterruptedException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
			break;
		}

	}

	private void process1() throws InterruptedException {
		
		// ....leqaa
		setProcessState(this, ProcessState.Running);
		// ....leqaa
		
		
		OperatingSystem.semPrintWait();
		System.out.println("P1 TOOK PRINT SEMAPHORE");
		OperatingSystem.printText("Enter File Name for p1 : ");
		OperatingSystem.semInputWait();
		System.out.println("P1 TOOK INPUT SEMAPHORE");
		String filename=OperatingSystem.TakeInput();
		OperatingSystem.semInputPost();
		System.out.println("P1 RELEASED INPUT SEMAPHORE");
		OperatingSystem.semReadWait();
		System.out.println("P1 TOOK READ SEMAPHORE");
		String readfile=OperatingSystem.readFile(filename);
		OperatingSystem.semReadPost();
		System.out.println("P1 RELEASED READ SEMAPHORE");
		OperatingSystem.printText(readfile);
		OperatingSystem.semPrintPost();
		System.out.println("P1 RELEASED PRINT SEMAPHORE");
		setProcessState(this, ProcessState.Terminated);

		
		

	}

	private void process2() throws InterruptedException {
	
		// ....leqaa
		setProcessState(this, ProcessState.Running);
		// ....leqaa
		
		OperatingSystem.semPrintWait();
		System.out.println("P2 TOOK PRINT SEMAPHORE");
		OperatingSystem.printText("Enter File Name: ");
		OperatingSystem.semInputWait();
		System.out.println("P2 TOOK INPUT SEMAPHORE");
		String filename = OperatingSystem.TakeInput();
		OperatingSystem.printText("Enter Data: ");
	//	OperatingSystem.semPrintPost();//heyya mafrood kedda 5alaset el print bas msh 3arfa convenient n7otaha henna walla eh 
		String data = OperatingSystem.TakeInput();
		OperatingSystem.semInputPost();
		System.out.println("P2 RELEASED INPUT SEMAPHORE");
		OperatingSystem.semPrintPost();//ana shayfa henna a7san 3ashan matde3sh fe el nos
		System.out.println("P2 RELEASED PRINT SEMAPHORE");
		OperatingSystem.semWriteWait();
		System.out.println("P2 TOOK WRITE SEMAPHORE");
		OperatingSystem.writefile(filename, data);
		OperatingSystem.semWritePost();
		System.out.println("P2 RELEASED WRITE SEMAPHORE");
		setProcessState(this, ProcessState.Terminated);

	
		
	}

	private void process3() throws InterruptedException {
		
		// ....leqaa
		setProcessState(this, ProcessState.Running);
		// ....leqaa
		OperatingSystem.semPrintWait();
		System.out.println("P3 TOOK PRINT SEMAPHORE");


		int x = 0;
		while (x < 301) {
			OperatingSystem.printText(x + "\n");
			x++;
		}
		setProcessState(this, ProcessState.Terminated);
		OperatingSystem.semPrintPost();
		System.out.println("P3 RELEASED PRINT SEMAPHORE");
		
	}

	private void process4() throws InterruptedException {
		
		// ....leqaa
		setProcessState(this, ProcessState.Running);
		// ....leqaa
		
		OperatingSystem.semPrintWait();
		System.out.println("P4 TOOK PRINT SEMAPHORE");
		int x = 500;
		while (x < 1001) {
			OperatingSystem.printText(x + "\n");
			x++;
		}
		setProcessState(this, ProcessState.Terminated);
		OperatingSystem.semPrintPost();
		System.out.println("P4 RELEASED PRINT SEMAPHORE");
		
	}

	private void process5() throws InterruptedException {
		
		// ....leqaa
		setProcessState(this, ProcessState.Running);
		// ....leqaa

	
		OperatingSystem.semPrintWait();
		System.out.println("P5 TOOK PRINT SEMAPHORE");
		OperatingSystem.printText("Enter LowerBound: ");
		OperatingSystem.semInputWait();
		System.out.println("P5 TOOK INPUT SEMAPHORE");
		String lower = OperatingSystem.TakeInput();
		OperatingSystem.printText("Enter UpperBound: ");
		String upper = OperatingSystem.TakeInput();
		OperatingSystem.semInputPost();
		System.out.println("P5 RELEASED INPUT SEMAPHORE");
		OperatingSystem.semPrintPost();//nafs el kalam
		System.out.println("P5 RELEASED PRINT SEMAPHORE");
//Thread.sleep(100);
		int lowernbr = Integer.parseInt(lower);
		int uppernbr = Integer.parseInt(upper);
		String data = "";

		while (lowernbr <= uppernbr) {
			data += lowernbr++ + "\n";
		}

		OperatingSystem.semWriteWait();
		System.out.println("P5 TOOK WRITE SEMAPHORE");
		OperatingSystem.writefile("P5.txt", data);
		OperatingSystem.semWritePost();
		System.out.println("P5 RELEASED WRITE SEMAPHORE");

		setProcessState(this, ProcessState.Terminated);

	
	
	}

	public static void setProcessState(Process p, ProcessState s) {
		p.status = s;
		if (s == ProcessState.Terminated) {
			System.out.println(s);
			OperatingSystem.ProcessTable.remove(OperatingSystem.ProcessTable.indexOf(p));
			// ....leqaa
			// OperatingSystem.readyqueue.removeFirst();
			OperatingSystem.flagready = false;
			// ....leqaa
		}
		// ....leqaa
		if (s == ProcessState.Ready) {
			OperatingSystem.readyqueue.addLast(p);
		}
		// ....leqaa
	}

	public static ProcessState getProcessState(Process p) {
		return p.status;
	}
}