class Big
{
    private String companyOfGlass;
 
    void setGlasscompany(String companyOfGlass)
    {
        this.companyOfGlass=companyOfGlass;
    }
    void getGlassCompany()
    {
        System.out.println("Nikhil has "+ companyOfGlass +" Glasses");
    }
    public static void main(String[]args)
    {
        Big n=new Big();
        n.setGlasscompany("Lenskart");
        n.getGlassCompany();
    }
}