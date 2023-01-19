import java.util.*;
import java.io.*;

class Pair{
	public int x;
	public int y;
	
	public Pair(int x, int y) {
		this.x = x;
		this.y = y;
	}
}

public class Main {
	public static void main(String[] args) {
		
		// N, L, R 입력 받음
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int L = sc.nextInt();
		int R = sc.nextInt();
		
		// 나라 배열 A 선언
		int[][] A = new int[N][N];
		
		// A 값 할당: i=행, j=열
		for(int i=0; i<N; i++)
			for(int j=0; j<N; j++)
				A[i][j] = sc.nextInt();
		
		int result = 0;
		end : while(true) {
			int flag = 0;
			int[][][] nat = border(A, L, R);
			fo: for(int i =0; i<N; i++) {
				for(int j=0; j<N; j++) {
					if (nat[i][j][0] == 1) {flag = 1; break fo;}
					if (nat[i][j][1] == 1) {flag = 1; break fo;}
				}
			}
			if (flag == 0) break end;
			A = migration(A, nat);
//			for(int[] a: A) System.out.println(Arrays.toString(a));
			result ++;
		}
		System.out.println(result);
	}
	static int[][][] border(int[][] A, int L, int R) {
		//국경선을 표시하는 변수
		//nat[0][0][0]은 A[0][0]와 A[0][1]의 국경선이 1(열림), 0(딛힘)을 표시
		//nat[0][0][1]은 A[0][0]와 A[1][0]의 국경선이 1(열림), 0(닫힘)을 표시
		int[][][] nat = new int[A.length][A.length][2];
		
		for(int i=0; i<A.length; i++) {
			for(int j=0; j<A.length; j++) {
				if (j<A.length-1) {
				if(Math.abs(A[i][j] - A[i][j+1]) >=L && Math.abs(A[i][j] - A[i][j+1]) <= R)
					nat[i][j][0] = 1;
				else nat[i][j][0] = 0;
				}
				if(i<A.length-1) {
				if(Math.abs(A[i+1][j] - A[i][j]) >=L && Math.abs(A[i+1][j] - A[i][j]) <= R)
					nat[i][j][1] = 1;
				else nat[i][j][1] = 0;
				}
			}
		}
		return nat;
	}
	//national end
	
	static int[][] migration(int[][] A, int[][][] nat) {
		
		int[][] visited = new int[A.length][A.length];
		//Pair[] p = new Pair[A.length*A.length];
		
		for(int i=0; i<A.length; i++) {
			label : for(int j=0; j<A.length; j++) {
				int count = A[i][j];
				int cnt = 1;
				Queue<Pair> q = new LinkedList<>();
				Queue<Pair> move = new LinkedList<>();
				
				if (visited[i][j] == 1) continue label;
				q.add(new Pair(i, j));
				move.add(new Pair(i,j));
				visited[i][j] = 1;
				while(!q.isEmpty()) {
					Pair p = q.poll();
					if(p.y < A.length-1) {
						if(nat[p.x][p.y][0] == 1) { 
							if (visited[p.x][p.y+1] != 1) {
								visited[p.x][p.y+1] = 1;
								count += A[p.x][p.y+1]; cnt++;
								if ((p.x < A.length-1) || (p.y < A.length-1))
									q.add(new Pair(p.x, p.y+1));
								move.add(new Pair(p.x, p.y+1));
							}
						}
					}
					if(p.x < A.length -1) {
						if(nat[p.x][p.y][1] == 1) { 
							if (visited[p.x+1][p.y] != 1) {
								visited[p.x+1][p.y] = 1;
								count += A[p.x+1][p.y]; cnt++;
								if ((p.x < A.length-1) || (p.y < A.length-1))
									q.add(new Pair(p.x+1, p.y));
								move.add(new Pair(p.x+1, p.y));
							}
						}
					}
					
					
					if(p.y > 0) {
						if(nat[p.x][p.y-1][0] == 1) { 
							if (visited[p.x][p.y-1] != 1) {
								visited[p.x][p.y-1] = 1;
								count += A[p.x][p.y-1]; cnt++;
								if ((p.x < A.length-1) || (p.y < A.length-1))
									q.add(new Pair(p.x, p.y-1));
								move.add(new Pair(p.x, p.y-1));
							}
						}
					}
					if(p.x > 0) {
						if(nat[p.x-1][p.y][1] == 1) { 
							if (visited[p.x-1][p.y] != 1) {
								visited[p.x-1][p.y] = 1;
								count += A[p.x-1][p.y]; cnt++;
								if ((p.x < A.length-1) || (p.y < A.length-1))
									q.add(new Pair(p.x-1, p.y));
								move.add(new Pair(p.x-1, p.y));
							}
						}
					}
				}
				int m = count / cnt;
				while(!move.isEmpty()) {
					Pair p = move.poll();
					A[p.x][p.y] = m;
					
				}
			}
		}
		
		return A;
	}
	// migration end
}
