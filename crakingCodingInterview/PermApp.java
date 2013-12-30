class PermApp {
    public static void main(String[] args) {
        Parm pm = new Perm();
        ArrayList inputlists = new ArrayList(); 
        String alist [] = ['a1','a2','a3'];
        String blist [] = ['b1','b2','b3'];
        String clist = ['c1','c2','c3'];
        inputlists.add(alist);
   		inputlists.add(blist);
   		inputlists.add(clist);
        pm.getPermutation(inputlists);
        pm.print(); 
    }
}