from tkinter import *
import tkinter as tk
from tkinter import ttk,messagebox
class Rest:
    def __init__(self,root):
        self.root = root
        self.root.title("Restaraunt Management App")
        self.menu_items = {"Fries Meal":2,"Lunch Meal":2,"Burger Meal":3,"Pizza Meal":4,"Cheese Burger":2.5,"Drinks":1,}
        self.exchange_rate = 82 
        self.setup_background(root)
        f = ttk.Frame(root)
        f.place(relx=0.5,rely=0.5,anchor=tk.CENTER)
        ttk.Label(f,text="Restaurant Order",font=("Arial",20,"bold")).grid(row=0,columnspan=3,padx=10,pady=10)
        self.menu_labels = {}
        self.menu_quantities = ()
        for i,(item,price) in enumerate(self.menu_items.items(),start=1):
            label = ttk.Label(f,text=f"{item} (${price}):",font=("Arial",12))
            label.grid(row=i,column=0,padx=10,pady=5)
            self.menu_label[item]=label 
            quantity_entry = ttk.Entry(f,width=5)
            quantity_entry.grid(row=i,column=1,padx=10,pady=5)
            self.menu_quantities[item]=quantity_entry
            self.currency_var = tk.StringVar()
            ttk.Label(f,text="Currency:",font=("Arial",12)).grid(row=len(self.menu_items)+1,column=0,padx=10,pady=5)
            currency_dropdown = ttk.Combobox(f,textvariable=self.currency_var,state="readonly",width=18,values=("USD","INR"))
            currency_dropdown.grid(row=len(self.menu_items)+1,column=1,padx=10,pady=5)
            self.currency_var.trace("w",self.update_menu_prices)

        def setup_background(self, root):
            bg_width, bg_height = 800, 600
            canvas = tk.Canvas(root, width=bg_width, height=bg_height)
            canvas.pack()
            original_image = tk.PhotoImage(file="background.png")
            background_image = original_image.subsample(
            original_image.width() // bg_width, original_image.height() // bg_height
        )
            canvas.create_image(0, 0, anchor=tk.NW, image=background_image)
            canvas.image = background_image 
        def update_menu_prices(self, *args):
            currency = self.currency_var.get()
            symbol = "₹" if currency == "INR" else "$"
            rate = self.exchange_rate if currency == "INR" else 1
            for item, label in self.menu_labels.items():
                price = self.menu_items[item] * rate
                label.config(text=f"{item} ({symbol}{price}):")

    # Method to place an order
    def place_order(self):
        total_cost = 0
        order_summary = "Order Summary:\n"
        currency = self.currency_var.get()
        symbol = "₹" if currency == "INR" else "$"
        rate = self.exchange_rate if currency == "INR" else 1
        for item, entry in self.menu_quantities.items():
            quantity = entry.get()
            if quantity.isdigit():
                quantity = int(quantity)
                price = self.menu_items[item] * rate
                cost = quantity * price
                total_cost += cost
                if quantity > 0:
                    order_summary += (
                        f"{item}: {quantity} x {symbol}{price} = {symbol}{cost}\n"
                    )
        if total_cost > 0:
            order_summary += f"\nTotal Cost: {symbol}{total_cost}"
            messagebox.showinfo(
                "Order Placed", order_summary
            )  # Show order summary in a message box
        else:
            # Show error if no items are ordered
            messagebox.showerror("Error", "Please order at least one item.")


# Main block to run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = Rest(root)
    root.geometry("800x600")  # Set the size of the window
    root.mainloop()  # Start the GUI loop