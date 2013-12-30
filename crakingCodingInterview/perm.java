public class perm (){

	//Solutions. Both Take advantage of the constrain. Choose only one from the list. Assume no dubplicate on the list

	//This solution takes advantage of the fact the patterns of the permutation. Assume given list [a1,a2,a3][b1,b2,b3]
	//and [c1, c2, c3]. The answer will look like [a1,b1,c1],[a1,b1,c2],[a1,b1,c3].. So a1 contitues to the total length
	//of the anser in this case, 27, divided by length of the list. in this case,3. 

	public ArrayList getPermutation(ArrayList n){

		ArrayList<List> result = new ArrayList<List>();
		int numarray = n.length();
		String sublist [] = new String [numarray];
		int total=1;
		int len,a,j=0,i=0,multiple=1, position=0

		for (i=0;i<n;i++){
			total=total*n[i].length() // total length of the set 
		}

		for (i=0;i<total;i++){
			result.add(sublist);  // Add each sublist (permutation) to the result set 
 		}

		
		for (int k=0;k<n;k++) { 
			len=n[k].length()
			a=total/(len*multiple);
			multiple*=numarray; 

			i=0;
			while(i<total){
				int j=0;
				while(j<a){
					result[i][k]=position; // result[i].sublist[k] 
					i++;
					j++;
				}
				position++; 
			}
		}
		return results; 
		
	}

	//This solution acts like a counter. its increment index one by one. 
	

	public ArrayList getPermutation2(ArrayList n) {

		boolean done=false;
		int len=n.length();
		int index [] = new int [len];
		String node [] = new String [len];
		ArrayList result = new ArrayList<List>(); 
		int i;

		for(i=0;i<len;i++)
			index[i]=0;

		while(!done){
			for (i=0;i<len;i++)
				node[i]=n[i].[index[i]];
			result.add(node);

			for (i=0;i<len;i++){
				index[i]++;
				if(index[i]==n[i].length())
					if(i==index.length-1)
						done=true
					else
						index[i]=0
				else
					break;

			}
	
		}
		return result; 

	}
	
}