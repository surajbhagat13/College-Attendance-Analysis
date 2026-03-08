import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
data = pd.read_csv("../dataset/student_data.csv")

# Show first 5 rows
print(data.head())

# Attendance vs Marks correlation
correlation = data["Attendance"].corr(data["Final_Marks"])
print("Correlation between Attendance and Marks:", correlation)

# Subject wise average marks
subject_avg = data.groupby("Subject")["Final_Marks"].mean()
print(subject_avg)

# Plot graph
plt.figure(figsize=(6,4))
subject_avg.plot(kind="bar")
plt.title("Average Marks by Subject")
plt.xlabel("Subject")
plt.ylabel("Marks")
plt.show()

# Risk prediction
data["Risk"] = data.apply(
    lambda x: "High Risk" if x["Attendance"] < 50 and x["Internal_Marks"] < 15 else "Normal",
    axis=1
)

print(data[["Name","Attendance","Internal_Marks","Risk"]])
