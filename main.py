import tkinter as tk
from tkinter import messagebox, simpledialog  # Asegúrate de importar simpledialog
from datetime import datetime
from gym_class import Gym
from commons import get_current_date, separator_string
from initial_data import michael_gym
from user_class_gym import Client

# Crear la ventana principal
root = tk.Tk()
root.title("Gym Management System")
root.geometry("800x600")  # Establecer tamaño de la ventana principal

# Funciones para las opciones del menú principal
def customer_management():
    customer_window = tk.Toplevel(root)
    customer_window.title("Customer Management")

    def add_customer():
        add_window = tk.Toplevel(customer_window)
        add_window.title("Add Customer")

        tk.Label(add_window, text="Client Document:").grid(row=0)
        tk.Label(add_window, text="Client Name:").grid(row=1)
        tk.Label(add_window, text="Client Last Name:").grid(row=2)
        tk.Label(add_window, text="Client Age:").grid(row=3)
        tk.Label(add_window, text="Client Phone:").grid(row=4)
        tk.Label(add_window, text="Membership Type:").grid(row=5)

        client_id = tk.Entry(add_window)
        client_name = tk.Entry(add_window)
        client_last_name = tk.Entry(add_window)
        client_age = tk.Entry(add_window)
        client_phone = tk.Entry(add_window)
        membership_type = tk.Entry(add_window)

        client_id.grid(row=0, column=1)
        client_name.grid(row=1, column=1)
        client_last_name.grid(row=2, column=1)
        client_age.grid(row=3, column=1)
        client_phone.grid(row=4, column=1)
        membership_type.grid(row=5, column=1)

        def submit():
            id = int(client_id.get())
            name = client_name.get()
            last_name = client_last_name.get()
            age = int(client_age.get())
            phone = client_phone.get()
            membership = membership_type.get()
            hoy = datetime.now()
            fecha_formateada = hoy.strftime("%Y-%m-%d")
            michael_gym.add_client(id, name, last_name, age, phone, True, membership, True, fecha_formateada, False)
            messagebox.showinfo("Success", f"Client {name} added successfully.")
            add_window.destroy()

        tk.Button(add_window, text="Submit", command=submit).grid(row=6, column=1)

    def verify_customer():
        verify_window = tk.Toplevel(customer_window)
        verify_window.title("Verify Customer")

        tk.Label(verify_window, text="Client Document:").grid(row=0)
        client_id = tk.Entry(verify_window)
        client_id.grid(row=0, column=1)

        def verify():
            id = int(client_id.get())
            client = michael_gym.get_client(id)
            messagebox.showinfo("Client Info", str(client))
            verify_window.destroy()

        tk.Button(verify_window, text="Verify", command=verify).grid(row=1, column=1)

    def disable_customer():
        disable_window = tk.Toplevel(customer_window)
        disable_window.title("Disable Customer")

        tk.Label(disable_window, text="Client Document:").grid(row=0)
        client_id = tk.Entry(disable_window)
        client_id.grid(row=0, column=1)

        def disable():
            id = int(client_id.get())
            michael_gym.delete_client_membership(id)
            client = michael_gym.get_client(id)
            client.set_membership_active = False
            client.set_is_active = False
            messagebox.showinfo("Success", f"Client {id} disabled successfully.")
            disable_window.destroy()

        tk.Button(disable_window, text="Disable", command=disable).grid(row=1, column=1)

    def update_customer():
        update_window = tk.Toplevel(customer_window)
        update_window.title("Update Customer Data")

        tk.Label(update_window, text="Client Document:").grid(row=0)
        client_id = tk.Entry(update_window)
        client_id.grid(row=0, column=1)

        def update():
            id = int(client_id.get())
            client = michael_gym.get_client(id)
            # Aquí puedes agregar más lógica para actualizar los datos del cliente
            messagebox.showinfo("Success", f"Client {id} updated successfully.")
            update_window.destroy()

        tk.Button(update_window, text="Update", command=update).grid(row=1, column=1)

    tk.Button(customer_window, text="Add Customer", command=add_customer).pack()
    tk.Button(customer_window, text="Verify Customer", command=verify_customer).pack()
    tk.Button(customer_window, text="Disable Customer", command=disable_customer).pack()
    tk.Button(customer_window, text="Update Customer Data", command=update_customer).pack()
    tk.Button(customer_window, text="Back", command=customer_window.destroy).pack()

def membership_management():
    membership_window = tk.Toplevel(root)
    membership_window.title("Membership Management")

    def update_membership():
        update_window = tk.Toplevel(membership_window)
        update_window.title("Update Membership")

        tk.Label(update_window, text="Client Document:").grid(row=0)
        client_id = tk.Entry(update_window)
        client_id.grid(row=0, column=1)

        def update():
            id = int(client_id.get())
            michael_gym.update_client_membership(id)
            messagebox.showinfo("Success", f"Membership for client {id} updated successfully.")
            update_window.destroy()

        tk.Button(update_window, text="Update", command=update).grid(row=1, column=1)

    def add_membership():
        add_window = tk.Toplevel(membership_window)
        add_window.title("Add Membership")

        def submit():
            michael_gym.create_membership()
            messagebox.showinfo("Success", "New membership added successfully.")
            add_window.destroy()

        tk.Button(add_window, text="Submit", command=submit).pack()

    def disable_membership():
        disable_window = tk.Toplevel(membership_window)
        disable_window.title("Disable Membership")

        tk.Label(disable_window, text="Client Document:").grid(row=0)
        client_id = tk.Entry(disable_window)
        client_id.grid(row=0, column=1)

        def disable():
            id = int(client_id.get())
            michael_gym.delete_client_membership(id)
            messagebox.showinfo("Success", f"Membership for client {id} disabled successfully.")
            disable_window.destroy()

        tk.Button(disable_window, text="Disable", command=disable).grid(row=1, column=1)

    tk.Button(membership_window, text="Update Membership", command=update_membership).pack()
    tk.Button(membership_window, text="Add Membership", command=add_membership).pack()
    tk.Button(membership_window, text="Disable Membership", command=disable_membership).pack()
    tk.Button(membership_window, text="Back", command=membership_window.destroy).pack()

def reports():
    report_window = tk.Toplevel(root)
    report_window.title("Reports")

    def daily_profit_report():
        report_date = simpledialog.askstring("Input", "Enter the desired date (YYYY-MM-DD):")
        if report_date:
            michael_gym.calculate_earning_peer_day(report_date)
            messagebox.showinfo("Success", f"Daily profit report for {report_date} created successfully.")

    def current_customers_report():
        michael_gym.generate_report_current_clients()
        messagebox.showinfo("Success", "Current customers report created successfully.")

    def new_customers_report():
        report_date = simpledialog.askstring("Input", "Enter the desired date (YYYY-MM-DD):")
        if report_date:
            michael_gym.generate_report_day(report_date)
            messagebox.showinfo("Success", f"New customers report for {report_date} created successfully.")

    tk.Button(report_window, text="Daily Profit Report", command=daily_profit_report).pack()
    tk.Button(report_window, text="Current Customers Report", command=current_customers_report).pack()
    tk.Button(report_window, text="New Customers Report", command=new_customers_report).pack()
    tk.Button(report_window, text="Back", command=report_window.destroy).pack()

def gym_access():
    access_window = tk.Toplevel(root)
    access_window.title("Gym Access")

    tk.Label(access_window, text="Client Document:").grid(row=0)
    client_id = tk.Entry(access_window)
    client_id.grid(row=0, column=1)

    def access():
        id = int(client_id.get())
        michael_gym.handle_change_client_training(id)
        messagebox.showinfo("Success", f"Client {id} access handled successfully.")
        access_window.destroy()

    tk.Button(access_window, text="Submit", command=access).grid(row=1, column=1)

tk.Button(root, text="Customer Management", command=customer_management, width=30, height=2).pack(pady=10)
tk.Button(root, text="Membership Management", command=membership_management, width=30, height=2).pack(pady=10)
tk.Button(root, text="Reports", command=reports, width=30, height=2).pack(pady=10)
tk.Button(root, text="Gym Access", command=gym_access, width=30, height=2).pack(pady=10)
tk.Button(root, text="Exit", command=root.quit, width=30, height=2).pack(pady=10)

# Iniciar el bucle principal de la interfaz
root.mainloop()
