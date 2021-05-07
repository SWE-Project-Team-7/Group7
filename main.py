import time
import random
import tkinter
from tkinter import Frame, LabelFrame, ttk
from tkinter import Button, DISABLED, NORMAL, W, END, RIGHT
from tkinter import Toplevel
from tkinter import Tk
from tkinter import Label, Entry, Text, Checkbutton
from tkinter import StringVar, IntVar
from tkinter import messagebox


class MainWindow:
    def __init__(self, master):
        self.master = master

        # The title of the window
        self.master.title("Medicine Tracker")

        # The coordinates of the screen
        self.master.geometry("1350x750+0+0")

        # getting screen width and height of display
        width = self.master.winfo_screenwidth()
        height = self.master.winfo_screenheight()
        # setting tkinter window size
        self.master.geometry("%dx%d" % (width, height))

        # Building in an escape
        self.master.bind("<Escape>", lambda x: self.master.destroy())

        # Setting up the frame
        self.frame = Frame(self.master)
        self.frame.pack()

        # The username and password variables
        self.Username = StringVar()
        self.Password = StringVar()

        # ===================================================================================================================================

        # Creating the login page
        self.LabelTitle = Label(self.frame, text="Medicine Tracker", font=("Times New Roman", 40, "bold"), bd=20)
        self.LabelTitle.grid(row=0, column=0, columnspan=2, pady=20)

        self.LoginFrame = LabelFrame(self.frame, width=1010, height=300, bd=20)
        self.LoginFrame.grid(row=1, column=0)

        # ============================================MiddleFrameAndBottomFrame===============================================================

        # Creating the other frames
        # The middle
        self.MidFrame = Frame(self.frame, width=1000, height=100, bd=20, relief="ridge")
        self.MidFrame.grid(row=2, column=0)

        self.BottomFrame = Frame(self.frame, width=1000, height=200, bd=20, relief="ridge")
        self.BottomFrame.grid(row=3, column=0, pady=10)

        # ==========================================UserAndPassword=================================================================

        # Creating the username label and text box
        self.LabelUsername = Label(self.LoginFrame, text="Username:", font=("Times New Roman", 30, "bold"), bd=25)
        self.LabelUsername.grid(row=0, column=0)

        self.txtUsername = Entry(self.LoginFrame, textvariable=self.Username,
                                 font=("Times New Roman", 30, "bold"), bd=20)
        self.txtUsername.grid(row=0, column=1)

        # Creating the password label and text box
        self.LabelPassword = Label(self.LoginFrame, text="Password:", font=("Times New Roman", 30, "bold"), bd=25)
        self.LabelPassword.grid(row=1, column=0)

        self.txtPassword = Entry(self.LoginFrame, textvariable=self.Password, show="*",
                                 font=("Times New Roman", 30, "bold"), bd=20)
        self.txtPassword.grid(row=1, column=1)
        # ===================================================================================================================================

        # Button for logging in, resetting, and exiting
        btnLogin = Button(self.MidFrame, text="Login", width=15, font=("Times New Roman", 20),
                          command=self.logSystem)
        btnLogin.grid(row=0, column=0)

        btnReset = Button(self.MidFrame, text="Reset", width=15, font=("Times New Roman", 20),
                          command=self.Reset)
        btnReset.grid(row=0, column=1)

        btnExit = Button(self.MidFrame, text="Exit", width=15, font=("Times New Roman", 20),
                         command=self.Exit)
        btnExit.grid(row=0, column=2)

        # ===================================================================================================================================

        # Button for the other windows
        # The buttons state will be disabled until the login credentials is correct
        self.btnRegistration = Button(self.BottomFrame, text="Registration Management", font=("Times New Roman", 24),
                                      command=self.regWindow, state=DISABLED)
        self.btnRegistration.grid(row=0, column=0)

        self.btnMeds = Button(self.BottomFrame, text="Medication Management", font=("Times New Roman", 24),
                              command=self.medWindow, state=DISABLED)
        self.btnMeds.grid(row=0, column=1)

    # =============================================LoginFunction======================================================================

    # Function for the log-in system
    def logSystem(self):
        user = (self.Username.get())
        password = (self.Password.get())

        if (user == str(1234)) and (password == str(1234)):
            self.btnRegistration.config(state=NORMAL)
            self.btnMeds.configure(state=NORMAL)
        else:
            tkinter.messagebox.askyesno("Medicine Tracker", "Invalid Login. Try again?")
            self.btnRegistration.configure(state=DISABLED)
            self.btnMeds.config(state=DISABLED)
            self.Username.set("")
            self.Password.set("")
            self.txtUsername.focus()

    # Function to reset the window
    def Reset(self):
        self.btnRegistration.config(state=DISABLED)
        self.btnMeds.config(state=DISABLED)
        self.Username.set("")
        self.Password.set("")
        self.txtUsername.focus()

    # Function to exit the window
    def Exit(self):
        self.iExit = tkinter.messagebox.askyesno("Medicine Tracker", "Are you sure you want to exit?")
        if self.iExit > 0:
            self.master.destroy()
            return

    # Function for the Registration Window
    def regWindow(self):
        self.newWindow = Toplevel(self.master)
        self.app = PatientWindow(self.newWindow)

    # Function for the Medicine Window
    def medWindow(self):
        self.newWindow = Toplevel(self.master)
        self.app = MedicationWindow(self.newWindow)


# ================================================PatientWindow=========================================================

class PatientWindow:
    def __init__(self, master):
        self.master = master

        # The title of the window
        self.master.title("Patients Registration System")

        # getting screen width and height of display
        width = self.master.winfo_screenwidth()
        height = self.master.winfo_screenheight()
        # setting tkinter window size
        self.master.geometry("%dx%d" % (width, height))

        # Building in an escape
        self.master.bind("<Escape>", lambda x: self.master.destroy())

        # Setting up the frame
        self.frame = Frame(self.master)
        self.frame.pack()

        # ==========================================Functions===========================================================
        def iReset():
            # Resets the left box
            firstName.set("")
            lastName.set("")
            address.set("")
            zipCode.set("")
            phoneNumber.set("")
            reference.set("")
            proofOfId.set("")
            membershipType.set("")
            paymentMethod.set("")
            fee.set(0)
            self.cboProofOfID.current(0)
            self.cboPaymentMethod.current(0)
            self.cboMembershipType.current(0)
            self.txtReceipt.delete("1.0", END)
            return

        def iRecordReset():
            firstName.set("")
            lastName.set("")
            address.set("")
            zipCode.set("")
            phoneNumber.set("")
            reference.set("")
            proofOfId.set("")
            membershipType.set("")
            paymentMethod.set("")
            fee.set(0)
            self.cboProofOfID.current(0)
            self.cboPaymentMethod.current(0)
            self.cboMembershipType.current(0)
            return

        def iExit():
            iExit = tkinter.messagebox.askyesno("Registration Management", "Are you sure you want to exit?")
            if iExit > 0:
                self.master.destroy()
                return

        def ReferenceNumber():
            # A function to randomize the reference number for members
            number = random.randint(110644, 800000)
            randomReferenceNumber = str(number)
            reference.set(randomReferenceNumber)

        def Receipt():
            ReferenceNumber()
            self.txtReceipt.insert(END, "      " + reference.get() + "\t\t\t" + firstName.get() + "\t\t" + lastName.get()
                                   + "\t\t" + orderDate.get() + "\t" + phoneNumber.get() +
                                   "\t\t" + patientMembership.get() + "\n")

        def PatientFees():
            if fee.get() == 1:
                self.txtMembership.configure(state=NORMAL)
                amount1 = float(100)
                patientMembership.set("$" + str(amount1))
            elif fee.get() == 0:
                self.txtMembership.configure(state=DISABLED)
                patientMembership.set("0")

        # ==========================================Variables===========================================================

        # Order Variables
        orderDate = StringVar()
        orderDate.set(time.strftime("%m/%d/%y"))

        # Patient Information
        firstName = StringVar()
        lastName = StringVar()
        address = StringVar()
        zipCode = StringVar()
        phoneNumber = StringVar()
        reference = StringVar()
        proofOfId = StringVar()
        membershipType = StringVar()
        paymentMethod = StringVar()
        fee = IntVar()

        # Setting patient information
        patientMembership = StringVar()
        patientMembership.set("0")

        # ===============================================Frame==========================================================

        # The main frame
        MainFrame = Frame(self.frame)
        MainFrame.grid()

        # The title frame and title
        titleFrame = Frame(MainFrame, bd=20, width=1350, padx=20, relief="ridge")
        titleFrame.pack(side="top")

        self.labelTitle = Label(titleFrame, text="Patient Registration Management",
                                font=("Times New Roman", 40, "bold"),
                                padx=2)
        self.labelTitle.grid()

        # ============================================LeftAndRightFrames===============================================

        patientDetailsFrame = Frame(MainFrame, height=500, width=1350, bd=10, pady=5, relief="ridge")
        patientDetailsFrame.pack(side="bottom")

        # Left Frame formatting
        patientDetailsLeft = LabelFrame(patientDetailsFrame, height=500, width=1000, bd=10, relief="ridge")
        patientDetailsLeft.pack(side="left")

        patientNameFrame = LabelFrame(patientDetailsLeft, height=400, width=350, bd=10, text="Patient's Name",
                                      font=("Times New Roman", 12, "bold"), relief="ridge")
        patientNameFrame.grid(row=0, column=0)

        # Right Frame formatting
        patientDetailsRight = LabelFrame(patientDetailsFrame, height=425, width=1000, bd=10, relief="ridge")
        patientDetailsRight.pack(side="right")

        # =========================================LabelsAndTextboxesLeftFrame===================================================

        # Reference Number label and textbox
        self.labelReferenceNumber = Label(patientNameFrame, text="Reference Number: ",
                                          font=("Times New Roman", 18, "bold"), bd=8, padx=2)
        self.labelReferenceNumber.grid(row=0, column=0, sticky=W)
        self.txtReferenceNumber = Entry(patientNameFrame, font=("Times New Roman", 18, "bold"), textvariable=reference,
                                        state=DISABLED, bd=8, insertwidth=1)
        self.txtReferenceNumber.grid(row=0, column=1)

        # First Name label and textbox
        self.labelFirstName = Label(patientNameFrame, text="First Name: ",
                                    font=("Times New Roman", 18, "bold"), bd=8, padx=2)
        self.labelFirstName.grid(row=1, column=0, sticky=W)
        self.txtFirstName = Entry(patientNameFrame, textvariable=firstName, font=("Times New Roman", 18, "bold"), bd=8,
                                  insertwidth=1)
        self.txtFirstName.grid(row=1, column=1)

        # Last Name label and textbox
        self.labelFirstName = Label(patientNameFrame, text="Last Name: ",
                                    font=("Times New Roman", 18, "bold"), bd=8, padx=2)
        self.labelFirstName.grid(row=2, column=0, sticky=W)
        self.txtFirstName = Entry(patientNameFrame, textvariable=lastName, font=("Times New Roman", 18, "bold"), bd=8,
                                  insertwidth=1)
        self.txtFirstName.grid(row=2, column=1)

        # Address label and textbox
        self.labelAddress = Label(patientNameFrame, text="Address:",
                                  font=("Times New Roman", 18, "bold"), bd=8, padx=2)
        self.labelAddress.grid(row=3, column=0, sticky=W)
        self.txtAddress = Entry(patientNameFrame, textvariable=address, font=("Times New Roman", 18, "bold"), bd=8,
                                insertwidth=1)
        self.txtAddress.grid(row=3, column=1)

        # Zipcode label and textbox
        self.labelZipcode = Label(patientNameFrame, text="Zipcode:",
                                  font=("Times New Roman", 18, "bold"), bd=8, padx=2)
        self.labelZipcode.grid(row=4, column=0, sticky=W)
        self.txtZipcode = Entry(patientNameFrame, textvariable=zipCode, font=("Times New Roman", 18, "bold"), bd=8,
                                insertwidth=1)
        self.txtZipcode.grid(row=4, column=1)

        # Phone Number label and textbox
        self.labelPhoneNumber = Label(patientNameFrame, text="Phone Number: ",
                                      font=("Times New Roman", 18, "bold"), bd=8, padx=2)
        self.labelPhoneNumber.grid(row=5, column=0, sticky=W)
        self.txtPhoneNumber = Entry(patientNameFrame, textvariable=phoneNumber, font=("Times New Roman", 18, "bold"),
                                    bd=8, insertwidth=1)
        self.txtPhoneNumber.grid(row=5, column=1)

        # Date label and textbox
        self.labelDate = Label(patientNameFrame, text="Date: ", font=("Times New Roman", 18, "bold"), bd=8, padx=2)
        self.labelDate.grid(row=6, column=0, sticky=W)
        self.txtDate = Entry(patientNameFrame, textvariable=orderDate, font=("Times New Roman", 18, "bold"), bd=8,
                             insertwidth=1)
        self.txtDate.grid(row=6, column=1)

        # =============================================PatientInformation=======================================================

        # Creating the proof of ID label
        self.labelProofOfID = Label(patientNameFrame, text="Proof of ID:",
                                    font=("Times New Roman", 18, "bold"), padx=2, pady=2)
        self.labelProofOfID.grid(row=7, column=0, sticky=W)

        # Formatting the proof of ID combo box
        self.cboProofOfID = ttk.Combobox(patientNameFrame, textvariable=proofOfId, state="readonly",
                                         font=("Times New Roman", 18, "bold"), width=20)
        self.cboProofOfID["value"] = ("", "Driver's License", "Student ID", "Federal ID", "Passport")
        self.cboProofOfID.current(0)
        self.cboProofOfID.grid(row=7, column=1)

        # Creating the Membership Typeof the patient label
        self.labelMembershipType = Label(patientNameFrame, text="Membership Type:",
                                         font=("Times New Roman", 18, "bold"), padx=2, pady=2)
        self.labelMembershipType.grid(row=8, column=0, sticky=W)

        # Formatting the Membership Type of the patient combo box
        self.cboMembershipType = ttk.Combobox(patientNameFrame, textvariable=membershipType, state="readonly",
                                              font=("Times New Roman", 18, "bold"), width=20)
        self.cboMembershipType["value"] = ("", "Annual", "Quarterly", "Monthly", "One time")
        self.cboMembershipType.current(0)
        self.cboMembershipType.grid(row=8, column=1)

        # Creating the Payment Method label
        self.labelPaymentMethod = Label(patientNameFrame, text="Payment Method:",
                                        font=("Times New Roman", 18, "bold"), padx=2, pady=2)
        self.labelPaymentMethod.grid(row=9, column=0, sticky=W)

        # Formatting the Payment Method combo box
        self.cboPaymentMethod = ttk.Combobox(patientNameFrame, textvariable=paymentMethod, state="readonly",
                                             font=("Times New Roman", 18, "bold"), width=20)
        self.cboPaymentMethod["value"] = ("", "Master Card", "Visa", "Credit Card", "PayPal", "Apple Pay", "Google Pay",
                                          "Samsung Pay")
        self.cboPaymentMethod.current(0)
        self.cboPaymentMethod.grid(row=9, column=1)

        # Creating the fee checkbox for member payment
        self.chkMembership = Checkbutton(patientNameFrame, text="Membership Fee", variable=fee, offvalue=0, onvalue=1,
                                         command=PatientFees, font=("Times New Roman", 18, "bold"), padx=2, pady=2)
        self.chkMembership.grid(row=10, column=0, sticky=W)
        self.txtMembership = Entry(patientNameFrame, textvariable=patientMembership, state=DISABLED, justify=RIGHT,
                                   font=("Times New Roman", 18, "bold"), bd=8, insertwidth=1)
        self.txtMembership.grid(row=10, column=1)

        # ============================================ReceiptRightFrame=========================================================
        # Creating the Receipt label and textbox
        self.labelReceipt = Label(patientDetailsRight, font=("Times New Roman", 14, "bold"), padx=5, pady=5,
                                  text="Membership Number\tFirst Name\t Last Name\tDate\tPhone Number\tPayment Type")
        self.labelReceipt.grid(row=0, column=0, columnspan=4)

        self.txtReceipt = Text(patientDetailsRight, height=17, width=90, font=("Times New Roman", 14, "bold"), padx=5,
                               pady=5)
        self.txtReceipt.grid(row=1, column=0, columnspan=4)

        # =============================================ButtonFunction===========================================================
        self.btnReceipt = Button(patientDetailsRight, text="Receipt", width=15, padx=10, pady=10, bd=8,
                                 font=("Times New Roman", 14, "bold"), command=Receipt).grid(row=2, column=0)
        self.btnReset = Button(patientDetailsRight, text="Reset", width=15, padx=10, pady=10, bd=8,
                               font=("Times New Roman", 14, "bold"), command=iReset).grid(row=2, column=1)
        self.btnAdd = Button(patientDetailsRight, text="Add Member", width=15, padx=10, pady=10, bd=8,
                             font=("Times New Roman", 14, "bold"), command=iRecordReset).grid(row=2, column=2)
        self.btnExit = Button(patientDetailsRight, text="Exit", width=15, padx=10, pady=10, bd=8,
                              font=("Times New Roman", 14, "bold"), command=iExit).grid(row=2, column=3)


# ===================================================================================================================================

class MedicationWindow:
    def __init__(self, master):
        self.master = master

        # The title of the window
        self.master.title("Medication Management")

        # getting screen width and height of display
        width = self.master.winfo_screenwidth()
        height = self.master.winfo_screenheight()
        # setting tkinter window size
        self.master.geometry("%dx%d" % (width, height))

        # Building in an escape
        self.master.bind("<Escape>", lambda x: self.master.destroy())

        # Setting up the frame
        self.frame = Frame(self.master)
        self.frame.pack()

        # The variables for the application
        nameTablets = StringVar()
        dose = StringVar()
        tabletAmount = StringVar()
        issuedDate = StringVar()
        expiredDate = StringVar()
        dailyDosage = StringVar()
        sideEffects = StringVar()
        storage = StringVar()
        machineUsage = StringVar()
        instructions = StringVar()
        patientID = StringVar()
        patientName = StringVar()
        dob = StringVar()
        address = StringVar()

        # =============================================ButtonFunction======================================================

        def iPrescription():
            # Pressing the button will put it into the right frame
            self.txtPrescription.insert(END, "Name of Prescription: " + nameTablets.get() + "\n")
            self.txtPrescription.insert(END, "Dosage: " + dose.get() + "\n")
            self.txtPrescription.insert(END, "Number of Tablets: " + tabletAmount.get() + "\n")
            self.txtPrescription.insert(END, "Issued Date: " + issuedDate.get() + "\n")
            self.txtPrescription.insert(END, "Expiration Date: " + expiredDate.get() + "\n")
            self.txtPrescription.insert(END, "Daily Dosage: " + dailyDosage.get() + "\n")
            self.txtPrescription.insert(END, "Side Effects: " + sideEffects.get() + "\n")
            self.txtPrescription.insert(END, "Storage Advice: " + storage.get() + "\n")
            self.txtPrescription.insert(END, "Operating Machinery: " + machineUsage.get() + "\n")
            self.txtPrescription.insert(END, "Patient ID: " + patientID.get() + "\n")
            self.txtPrescription.insert(END, "Patient Name: " + patientName.get() + "\n")
            self.txtPrescription.insert(END, "Date of Birth: " + dob.get() + "\n")
            self.txtPrescription.insert(END, "Patient's Address: " + address.get() + "\n")

            return

        def iPrescriptionData():
            # Inserting the data into the lower frame to display the prescription
            self.txtframeDetails.insert(END, nameTablets.get() + "\t\t" + dose.get()
                                        + "          \t   " + tabletAmount.get() + "       \t\t      " + issuedDate.get() +
                                        "    \t\t       " + expiredDate.get() + "     \t\t     " + dailyDosage.get() +
                                        "   \t\t  " + storage.get() + "\t\t" + patientName.get() +
                                        "\t" + dob.get() + "\t" + "\n")

            return

        def iDelete():
            # Deletes all of the data
            self.cboTabletName.current(0)
            self.cboDosage.current(0)
            self.cboTabletAmount.current(0)
            issuedDate.set("")
            expiredDate.set("")
            dailyDosage.set("")
            sideEffects.set("")
            storage.set("")
            self.cboMachine.current(0)
            instructions.set("")
            patientID.set("")
            patientName.set("")
            dob.set("")
            address.set("")
            self.txtPrescription.delete("1.0", END)
            self.txtframeDetails.delete("1.0", END)
            return

        def iReset():
            # Resets the second box but leaves the lower frame
            self.cboTabletName.current(0)
            self.cboDosage.current(0)
            self.cboTabletAmount.current(0)
            issuedDate.set("")
            expiredDate.set("")
            dailyDosage.set("")
            sideEffects.set("")
            storage.set("")
            self.cboMachine.current(0)
            instructions.set("")
            patientID.set("")
            patientName.set("")
            dob.set("")
            address.set("")
            self.txtPrescription.delete("1.0", END)
            return

        def iExit():
            iExit = tkinter.messagebox.askyesno("Medication Management", "Are you sure you want to exit?")
            if iExit > 0:
                self.master.destroy()
                return

        # =============================================Frame======================================================
        # The main frame
        MainFrame = Frame(self.frame)
        MainFrame.grid()

        # The title frame and title
        titleFrame = Frame(MainFrame, bd=20, width=1350, padx=20, relief="ridge")
        titleFrame.pack(side="top")

        self.labelTitle = Label(titleFrame, text="Medication Management", width=40,
                                font=("Times New Roman", 40, "bold"), padx=2)
        self.labelTitle.grid()

        frameDetails = Frame(MainFrame, bd=20, width=1350, height=100, padx=20, relief="ridge")
        frameDetails.pack(side="bottom")

        # Creating the frame for the button
        buttonFrameDetails = Frame(MainFrame, bd=20, width=1350, height=50, padx=20, relief="ridge")
        buttonFrameDetails.pack(side="bottom")

        # Creating the frames for the data, left and right
        dataFrameDetails = Frame(MainFrame, bd=20, width=1350, height=400, padx=20, relief="ridge")
        dataFrameDetails.pack(side="bottom")

        # Left
        dataFrameDetailsLeft = LabelFrame(dataFrameDetails, bd=10, width=400, height=400, padx=20, relief="ridge",
                                          font=("Times New Roman", 16, "bold"), text="Patient's Information:", )
        dataFrameDetailsLeft.pack(side="left")

        # Right
        dataFrameDetailsRight = LabelFrame(dataFrameDetails, bd=10, width=400, height=400, padx=20, relief="ridge",
                                           font=("Times New Roman", 16, "bold"), text="Prescription:", )
        dataFrameDetailsRight.pack(side="right")

        # =============================================dataFrameDetailsLeft======================================================

        # Creating the name of the tablet label
        self.labelTabletName = Label(dataFrameDetailsLeft, text="Name of Prescription:",
                                     font=("Times New Roman", 16, "bold"), padx=2, pady=2)
        self.labelTabletName.grid(row=0, column=0, sticky=W)

        # Formatting the tablet combo box
        self.cboTabletName = ttk.Combobox(dataFrameDetailsLeft, textvariable=nameTablets, state="readonly",
                                          font=("Times New Roman", 16, "bold"), width=18)
        self.cboTabletName["value"] = (
            "", "Ibuprofen", "Acetaminophen", "Wellbutrin", "Cetirizine", "Zoloft", "Aspirin", "Benadryl")
        self.cboTabletName.current(0)
        self.cboTabletName.grid(row=0, column=1)

        # Instructions
        self.labelInfo = Label(dataFrameDetailsLeft, text="Instructions:", font=("Times New Roman", 16, "bold"), padx=2,
                               pady=2)
        self.labelInfo.grid(row=0, column=2, sticky=W)
        self.txtInfo = Entry(dataFrameDetailsLeft, font=("Times New Roman", 16, "bold"), textvariable=instructions)
        self.txtInfo.grid(row=0, column=3)

        # Creating the dosage label
        self.labelTabletName = Label(dataFrameDetailsLeft, text="Dosage(mg):",
                                     font=("Times New Roman", 16, "bold"), padx=2, pady=2)
        self.labelTabletName.grid(row=1, column=0, sticky=W)

        # Dosage
        self.cboDosage = ttk.Combobox(dataFrameDetailsLeft, textvariable=dose, state="readonly",
                                      font=("Times New Roman", 16, "bold"), width=18)
        self.cboDosage["value"] = ("", "50mg", "100mg", "150mg", "300mg", "450mg", "600mg", "800mg")
        self.cboDosage.current(0)
        self.cboDosage.grid(row=1, column=1)

        # Storage
        self.labelStorage = Label(dataFrameDetailsLeft, text="Storage Information:",
                                  font=("Times New Roman", 16, "bold"), padx=2, pady=2)
        self.labelStorage.grid(row=1, column=2, sticky=W)
        self.txtStorage = Entry(dataFrameDetailsLeft, font=("Times New Roman", 16, "bold"), textvariable=storage)
        self.txtStorage.grid(row=1, column=3)

        # Creating the tablet amount label
        self.labelTabletAmount = Label(dataFrameDetailsLeft, text="Number of Tablets:",
                                       font=("Times New Roman", 16, "bold"), padx=2, pady=2)
        self.labelTabletAmount.grid(row=3, column=0, sticky=W)

        # Tablet amount
        self.cboTabletAmount = ttk.Combobox(dataFrameDetailsLeft, textvariable=tabletAmount, state="readonly",
                                            font=("Times New Roman", 16, "bold"), width=18)
        self.cboTabletAmount["value"] = ("", "30 days", "60 days", "90 days")
        self.cboTabletAmount.current(0)
        self.cboTabletAmount.grid(row=3, column=1)

        # Creating the machinery label
        self.labelMachine = Label(dataFrameDetailsLeft, text="Operate Machinery:",
                                  font=("Times New Roman", 16, "bold"), padx=2, pady=2)
        self.labelMachine.grid(row=3, column=2, sticky=W)

        # Machinery
        self.cboMachine = ttk.Combobox(dataFrameDetailsLeft, textvariable=machineUsage, state="readonly",
                                       font=("Times New Roman", 16, "bold"), width=18)
        self.cboMachine["value"] = ("", "Yes", "No")
        self.cboMachine.current(0)
        self.cboMachine.grid(row=3, column=3)

        # Issued Date
        self.labelIssueDate = Label(dataFrameDetailsLeft, text="Issued Date:", font=("Times New Roman", 16, "bold"),
                                    padx=2, pady=2)
        self.labelIssueDate.grid(row=4, column=0, sticky=W)
        self.txtIssueDate = Entry(dataFrameDetailsLeft, font=("Times New Roman", 16, "bold"), textvariable=issuedDate)
        self.txtIssueDate.grid(row=4, column=1)

        # Patient ID
        self.labelPatInfo = Label(dataFrameDetailsLeft, text="Patient ID:", font=("Times New Roman", 16, "bold"),
                                  padx=2, pady=2)
        self.labelPatInfo.grid(row=4, column=2, sticky=W)
        self.txtPatInfo = Entry(dataFrameDetailsLeft, font=("Times New Roman", 16, "bold"), textvariable=patientID)
        self.txtPatInfo.grid(row=4, column=3)

        # Expiration Date
        self.labelExpDate = Label(dataFrameDetailsLeft, text="Expiration Date:", font=("Times New Roman", 16, "bold"),
                                  padx=2, pady=2)
        self.labelExpDate.grid(row=6, column=0, sticky=W)
        self.txtExpDate = Entry(dataFrameDetailsLeft, font=("Times New Roman", 16, "bold"), textvariable=expiredDate)
        self.txtExpDate.grid(row=6, column=1)

        # Patient Name
        self.labelPatName = Label(dataFrameDetailsLeft, text="Patient Name:", font=("Times New Roman", 16, "bold"),
                                  padx=2, pady=2)
        self.labelPatName.grid(row=6, column=2, sticky=W)
        self.txtPatName = Entry(dataFrameDetailsLeft, font=("Times New Roman", 16, "bold"), textvariable=patientName)
        self.txtPatName.grid(row=6, column=3)

        # Daily Dosage
        self.labelDayDose = Label(dataFrameDetailsLeft, text="Daily Dosage:", font=("Times New Roman", 16, "bold"),
                                  padx=2, pady=2)
        self.labelDayDose.grid(row=7, column=0, sticky=W)
        self.txtDayDose = Entry(dataFrameDetailsLeft, font=("Times New Roman", 16, "bold"), textvariable=dailyDosage)
        self.txtDayDose.grid(row=7, column=1)

        # DOB
        self.labelDOB = Label(dataFrameDetailsLeft, text="Date of Birth:", font=("Times New Roman", 16, "bold"),
                              padx=2, pady=2)
        self.labelDOB.grid(row=7, column=2, sticky=W)
        self.txtDOB = Entry(dataFrameDetailsLeft, font=("Times New Roman", 16, "bold"), textvariable=dob)
        self.txtDOB.grid(row=7, column=3)

        # Side Effects
        self.labelSideEff = Label(dataFrameDetailsLeft, text="Side Effects:", font=("Times New Roman", 16, "bold"),
                                  padx=2, pady=2)
        self.labelSideEff.grid(row=8, column=0, sticky=W)
        self.txtSideEff = Entry(dataFrameDetailsLeft, font=("Times New Roman", 16, "bold"), textvariable=sideEffects)
        self.txtSideEff.grid(row=8, column=1)

        # Patient Address
        self.labelPatAddy = Label(dataFrameDetailsLeft, text="Patient Address:", font=("Times New Roman", 16, "bold"),
                                  padx=2, pady=2)
        self.labelPatAddy.grid(row=8, column=2, sticky=W)
        self.txtPatAddy = Entry(dataFrameDetailsLeft, font=("Times New Roman", 16, "bold"), textvariable=address)
        self.txtPatAddy.grid(row=8, column=3)

        # =============================================dataFrameDetailsRight======================================================

        self.txtPrescription = Text(dataFrameDetailsRight, width=30, height=11,
                                    font=("Times New Roman", 16, "bold"),
                                    padx=4, pady=11)
        self.txtPrescription.grid(row=0, column=0)

        # =============================================buttonFrameDetails======================================================
        self.btnPrescription = Button(buttonFrameDetails, text="Prescription", font=("Times New Roman", 16, "bold"),
                                      width=21, bd=1, command=iPrescription)
        self.btnPrescription.grid(row=0, column=0)

        self.btnPrescriptionData = Button(buttonFrameDetails, text="Prescription Data",
                                          font=("Times New Roman", 16, "bold"),
                                          width=21, bd=1, command=iPrescriptionData)
        self.btnPrescriptionData.grid(row=0, column=1)

        self.btnDelete = Button(buttonFrameDetails, text="Delete", font=("Times New Roman", 16, "bold"),
                                width=21, bd=1, command=iDelete)
        self.btnDelete.grid(row=0, column=2)

        self.btnReset = Button(buttonFrameDetails, text="Reset", font=("Times New Roman", 16, "bold"),
                               width=21, bd=1, command=iReset)
        self.btnReset.grid(row=0, column=3)

        self.btnExit = Button(buttonFrameDetails, text="Exit", font=("Times New Roman", 16, "bold"),
                              width=21, bd=1, command=iExit)
        self.btnExit.grid(row=0, column=4)

        # =============================================frameDetails======================================================
        self.labelLabel = Label(frameDetails,
                                text="Name of Tablets\t\tDosage\t\tNumber of Tablets\t\tIssued Date\t\tExpiration Date\t\tDaily Dose\t\tStorage Information\t\tPatient Name\tDOB",
                                font=("Times New Roman", 10, "bold"), pady=2)
        self.labelLabel.grid(row=0, column=0)

        self.txtframeDetails = Text(frameDetails, width=117, height=4,
                                    font=("Times New Roman", 16, "bold"),
                                    padx=2, pady=2)
        self.txtframeDetails.grid(row=1, column=0)


# ===================================================================================================================================

def main():
    root = Tk()
    app = MainWindow(root)
    root.mainloop()


if __name__ == '__main__':
    main()
