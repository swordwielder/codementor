public class customer {

    private String name;
    private int contact;

    public customer(String name, int contact) {
        this.name = name;
        this.contact = contact;
    }

    public String getName() {
        return this.name;
    }

    public int getContact() {
        return this.contact;
    }

    public void setName(String contact) {
        this.contact = contact;
    }
}